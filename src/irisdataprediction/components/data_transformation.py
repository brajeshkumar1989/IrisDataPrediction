import os

from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OrdinalEncoder
from sklearn.compose import make_column_selector, make_column_transformer
from sklearn.pipeline import make_pipeline
import pandas as pd
import numpy as np
from src.irisdataprediction import logger
from src.irisdataprediction.entity.config_entity import (DataTransformationConfig)


class DataTransformation:
    def __init__(self, config: DataTransformationConfig, threshold=0):
        self.config=config
        self.threshold=threshold
        self.dataset=pd.read_csv(self.config.data_path)
        self.dataset_columns=self.dataset.columns
        self.transformed_dataset=None


    
    def data_standardization(self):
        num_pipeline=make_pipeline(SimpleImputer(strategy='median'),StandardScaler())
        cat_pipeline=make_pipeline(SimpleImputer(strategy='most_frequent'), OrdinalEncoder(handle_unknown='use_encoded_value', unknown_value=np.nan))
        preprocessing= make_column_transformer((num_pipeline, make_column_selector(dtype_include=np.number)),(cat_pipeline, make_column_selector(dtype_include=object)))

        self.dataset= preprocessing.fit_transform(self.dataset)
        self.transformed_dataset=pd.DataFrame(data=self.dataset,columns=self.dataset_columns, index=None)

    def remove_correlated_columns(self):

        col_corr=set() #set of the names of correlated columns
        #corr_matrix=self.transformed_dataset.select_dtypes(include=[np.number]).corr()
        corr_matrix=self.transformed_dataset.iloc[:,:-1].corr()
        logger.info(f"<<<<<< Data Transformation: correlation between different columns >>>>>>")
        #logger.info(self.transformed_dataset.select_dtypes(include=[np.number]).corr())
        logger.info(self.transformed_dataset.iloc[:,:-1].corr())
        logger.info(f"<<<<<< =========================== >>>>>>")
        for i in range(len(corr_matrix.columns)):
            for j in range(i):
                if abs(corr_matrix.iloc[i,j])> self.threshold: #absolute is to compare +ve and -ve correlated columns both with threshold.
                    colname= corr_matrix.columns[i] #getting the name of the column
                    col_corr.add(colname)

        print(col_corr)            
        self.transformed_dataset.drop(col_corr, axis=1,inplace=True)

    def train_test_spliting(self):
        train, test=train_test_split(self.transformed_dataset)
        train.to_csv(os.path.join(self.config.root_dir,"train.csv"), index=False)
        test.to_csv(os.path.join(self.config.root_dir,"test.csv"), index=False)

        logger.info("Splitted data into training and test sets")




