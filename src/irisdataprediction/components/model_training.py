import sys,os
import pandas as pd
from src.irisdataprediction import logger
from src.irisdataprediction.exception import IrisPredictionException
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import (
    AdaBoostClassifier, GradientBoostingClassifier, RandomForestClassifier
)

from src.irisdataprediction.config.configuration import ModelTrainerConfig

from src.irisdataprediction.utils.ml_utils.metric.classification_metric import get_classification_score

from sklearn.metrics import r2_score
import joblib
import mlflow
import dagshub
dagshub.init(repo_owner="brajeshkumar1989", repo_name="IrisDataPrediction", mlflow=True)

class ModelTrainer:
    def __init__(self, config:ModelTrainerConfig):
        self.config= config
        self.report_train={}
        #self.report_test={}

    def track_mlflow(self,best_model, classificationmetric):
        with mlflow.start_run():
            f1_score=classificationmetric.f1_score
            precision_score=classificationmetric.precision_score
            recall_score=classificationmetric.recall_score

            mlflow.log_metric("f1_score", f1_score)
            mlflow.log_metric("precision", precision_score)
            mlflow.log_metric("recall_score", recall_score)
            mlflow.sklearn.log_model(best_model, "model")

    
    
    def evaluate_models(self,train_X, train_y,models,param):
        try:
            

            for i in range(len(list(models))):
                model=list(models.values())[i]
                para=param[list(models.keys())[i]]

                gs= GridSearchCV(model, para, cv=3)
                gs.fit(train_X, train_y)
                model.set_params(**gs.best_params_)
                model.fit(train_X, train_y)

                y_train_pred= model.predict(train_X)
                #y_test_pred=model.predict(test_X)

                train_model_score=r2_score(train_y, y_train_pred)
                #test_model_score=r2_score(test_y,y_test_pred)

                self.report_train[list(models.keys())[i]]=train_model_score
                #self.report_test[list(models.keys())[i]]=test_model_score
            
        except Exception as e:
            raise IrisPredictionException(e, sys)




    def train_model(self,train_X, train_y,test_X, test_y):
        models={
            "Random Forest": RandomForestClassifier(verbose=1),
            "Decision Tree": DecisionTreeClassifier(),
            "Gradient Boosting": GradientBoostingClassifier(verbose=1),
            "Logistic Regression": LogisticRegression(verbose=1),
            "AdaBoost": AdaBoostClassifier(), 
        }

        params={
            "Decision Tree":{
                'criterion':['gini','entropy','log_loss'],

                'splitter':['best' ,'random'],
                
            },

            "Random Forest":{
                'criterion':['gini','entropy','log_loss'],
                'n_estimators':[8,16,32,64,128,256]
            },
            "Gradient Boosting": {
                'learning_rate':[.1,.01,.05,.001],
                'subsample':[0.6,0.7,0.75,0.8,0.85,0.9],
                'criterion':['squared_error', 'friedman_mse'],
                'max_features':['auto','sqrt','log2'],
                'n_estimators':[8,16,32,64,128,256]
            },
            "Logistic Regression":{},
            "AdaBoost":{
                'learning_rate':[.1,.01,.5,.001],
                'n_estimators':[8,16,32,64,128,256]
            }

        }

        model_report:dict=self.evaluate_models(train_X=train_X, train_y=train_y, models=models, param=params)


        #to get the best model score from dict
        best_model_score_train=max(sorted(self.report_train.values()))
        #best_model_score_test=max(sorted(self.report_test.values()))

        #to get the best model name from dict (using test result)
        # to find the key of best_model_core_test
        best_model_name= list(self.report_train.keys())[
            list(self.report_train.values()).index(best_model_score_train)
        ]

        #get the best model 
        best_model= models[best_model_name]

        y_train_pred= best_model.predict(train_X)

        classification_train_metric=get_classification_score(y_true=train_y, y_pred=y_train_pred)

        ## track the experiment with mlflow
        self.track_mlflow(best_model, classification_train_metric)

        ## test data
        y_test_pred=best_model.predict(test_X)
        classification_test_metric= get_classification_score(y_true=test_y, y_pred=y_test_pred)

        self.track_mlflow(best_model, classification_test_metric)

        #save model
        joblib.dump(best_model, os.path.join(self.config.root_dir,self.config.model_name))       


    
    
    def initiate_model_trainer(self):
        train_data= pd.read_csv(self.config.train_data_path)
        test_data=pd.read_csv(self.config.test_data_path)

        train_X= train_data.drop([self.config.target_column], axis=1)
        test_X= test_data.drop([self.config.target_column], axis=1)
        train_y=train_data[[self.config.target_column]]
        test_y=test_data[[self.config.target_column]]

        model_trainer_artifacts=self.train_model(train_X, train_y, test_X, test_y)

        return model_trainer_artifacts