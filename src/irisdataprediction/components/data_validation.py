from src.irisdataprediction.entity.config_entity import (DataValidationConfig)
from src.irisdataprediction import logger
from src.irisdataprediction.exception import IrisPredictionException
from src.irisdataprediction.utils.common import save_figure
import pandas as pd
import sys
import matplotlib.pyplot as plt
import seaborn as sns




class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config= config
        self.dataset=pd.read_csv(self.config.unzip_data_dir)

    def validate_all_columns(self)->bool:
        try:
            validation_status= None
            dataset=self.dataset

            # data= pd.read_csv(self.config.unzip_data_dir)
            all_cols= list(dataset.columns)
            all_schema=self.config.all_schema.keys()

            for col in all_cols:
                if col not in all_schema:
                    validation_status=False
                    with open(self.config.STATUS_FILE,'w') as f:
                        f.write(f"Validation status: {validation_status}")
                else:
                    validation_status= True
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation status: {validation_status}")
            return validation_status

        except Exception as e:
            raise IrisPredictionException(e, sys)

    def eda(self):

        dataset=self.dataset
        ## A histogram is a plot that shows the frequeny distribution of a set of continuous variable, it helps to see outliers, normal distribution (if feature follows), and skewness etc.       
        dataset.hist(bins=50,figsize=(12,8))
        save_figure("attribute_histogram_plots",self.config.image_path,tight_layout=True, fig_extension="png", resolution=300)
        # plt.show()
        
        ## check dataset embalance
        plt.figure(figsize=(4, 4))
        dataset['name'].value_counts().plot(kind='bar')
        plt.title("class distribution - if imbalance?")
        plt.xlabel("class")
        plt.ylabel('Count')
        save_figure("class_count_check_data_imbalance",self.config.image_path,tight_layout=True, fig_extension="png", resolution=300)
        # plt.show()

        ## check for outliers
        #check of outliers
        #set the figure size
        fig, axes = plt.subplots(nrows=1, ncols=4, figsize=(20, 8))
        i=0
        for ax, column in zip(axes.flat, dataset.columns):

            if type(dataset[column].iloc[i]) !=str:
                sns.boxplot(dataset[column],ax=ax)
                ax.set_title(column)
            i +=1
        
        save_figure("check_for_outliers",self.config.image_path,tight_layout=True, fig_extension="png", resolution=300)
        # plt.show()

        ## comparing distributions among given features
        plt.figure(figsize=(8, 8))
        sns.pairplot(dataset[dataset.columns], size=2)
        fig.tight_layout()
        save_figure("compare_features",self.config.image_path,tight_layout=True, fig_extension="png", resolution=300)
        # plt.show()

        ## comparing distributions among given features
        plt.figure(figsize=(4, 4))
        sns.heatmap(dataset.iloc[:,:-1].corr(), annot=True)
        fig.tight_layout()
        save_figure("features_correlation",self.config.image_path,tight_layout=True, fig_extension="png", resolution=300)
        # plt.show()



    def validate_null_value(self):
        try:
            validation_status= None
            dataset=self.dataset

            for i in range(len(dataset.columns)):
                if(int(dataset[dataset.columns[i]].isnull().sum())==0):
                    validation_status= True

                else:
                    validation_status= False
                    
                break
            if(validation_status):
                    with open (self.config.STATUS_FILE,'w') as f:
                        f.write(f"Validation status: {validation_status}")

        except Exception as e:
            raise IrisPredictionException(e, sys)
            