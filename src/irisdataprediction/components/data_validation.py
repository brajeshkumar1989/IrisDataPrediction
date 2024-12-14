from src.irisdataprediction.entity.config_entity import (DataValidationConfig)
from src.irisdataprediction import logger
from src.irisdataprediction.exception import IrisPredictionException
import pandas as pd
import sys




class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config= config

    def validate_all_columns(self)->bool:
        logger.info(f"<<<<<< data validation: columns type validation started >>>>>>")
        try:
            validation_status= None

            data= pd.read_csv(self.config.unzip_data_dir)
            all_cols= list(data.columns)
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
            logger.info(f"<<<<<< data validation: columns type validation completed >>>>>>")
            return validation_status

        except Exception as e:
            logger.info(f"<<<<<< data validation: Exception occurred while validating column types >>>>>>")
            raise IrisPredictionException(e, sys)
        

    def validate_null_value(self):
        logger.info(f"<<<<<< data validation: Null value checks initiated >>>>>>")
        try:
            validation_status= None
            data= pd.read_csv(self.config.unzip_data_dir)
            for i in range(len(data.columns)):
                if(int(data[data.columns[i]].isnull().sum())==0):
                    validation_status= True

                else:
                    validation_status= False
                    
                break
            if(validation_status):
                    with open (self.config.STATUS_FILE,'w') as f:
                        f.write(f"Validation status: {validation_status}")
            logger.info(f"<<<<<< data validation: Null value validation completed >>>>>>")
        except Exception as e:
            logger.info(f"<<<<<< data validation: Exception occurred while validating null values checks >>>>>>")
            raise IrisPredictionException(e, sys)
            