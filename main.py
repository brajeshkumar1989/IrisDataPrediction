import sys
from src.irisdataprediction import logger
from src.irisdataprediction.exception import IrisPredictionException
from src.irisdataprediction.pipeline.data_ingestion_pipeline import DataIngestionTraningPipeline
from src.irisdataprediction.pipeline.data_validation_pipeline import DataValidationTrainingPipeline



# Data Ingestion
STAGE_NAME="Data Ingestion Stage"

try:
    logger.info(f"<<<<<< stage {STAGE_NAME} started. >>>>>>")
    data_ingestion=DataIngestionTraningPipeline()
    data_ingestion.initiate_data_ingestion()
    logger.info(f"<<<<<< stage {STAGE_NAME} completed >>>>>>")

except Exception as e:
    
    raise IrisPredictionException(e,sys)


# Data Validation
STAGE_NAME="Data validation Stage"

try:
    logger.info(f"<<<<<< stage {STAGE_NAME} started. >>>>>>")
    data_validation=DataValidationTrainingPipeline()
    data_validation.initiate_data_validation()
    logger.info(f"<<<<<< stage {STAGE_NAME} completed >>>>>>")
except Exception as e:
    raise IrisPredictionException(e, sys)
