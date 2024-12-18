import sys
from src.irisdataprediction.config.configuration import ConfigurationManager

from src.irisdataprediction.components.data_transformation import DataTransformation

from src.irisdataprediction import logger

from src.irisdataprediction.exception import IrisPredictionException

from pathlib import Path





class DataTransformationPipeline:
    def __init__(self):
        pass

    def initiate_data_transformation(self):
        try:
            with open(Path("artifacts/data_validation/status.txt"), 'r') as f:
                status= f.read().split(" ")[-1]

                if(status=="True"):
                    config=ConfigurationManager()
                    data_transformation_config=config.get_data_transformation_config()
                    data_transformation=DataTransformation(config=data_transformation_config,threshold=0.87)
                    data_transformation.data_standardization()
                    #data_transformation.remove_correlated_columns()
                    data_transformation.train_test_spliting()
                else:
                    logger.info("Transformation pipleline: Validation pipeline has issue , correct the same to proceed further!!!")
                    raise Exception("Validation pipeline has issue , correct the same to proceed further!!!")
                    
        except Exception as e:
            logger.info(f"Transformation pipleline: {e} ")
            raise IrisPredictionException(e, sys)