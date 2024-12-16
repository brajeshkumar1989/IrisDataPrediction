import sys
from src.irisdataprediction import logger
from src.irisdataprediction.exception import IrisPredictionException
from src.irisdataprediction.pipeline.data_ingestion_pipeline import DataIngestionTraningPipeline
from src.irisdataprediction.pipeline.data_validation_pipeline import DataValidationTrainingPipeline
from src.irisdataprediction.pipeline.data_transformation_pipeline import DataTransformationPipeline
from src.irisdataprediction.pipeline.model_training_pipeline import ModelTrainerTrainingPipeline


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


# Data Transformation
STAGE_NAME="Data Transformation Stage"

try:
    logger.info(f"<<<<<< stage {STAGE_NAME} started. >>>>>>")
    data_tranformation=DataTransformationPipeline()
    data_tranformation.initiate_data_transformation()
    logger.info(f"<<<<<< stage {STAGE_NAME} completed >>>>>>")
except Exception as e:
    raise IrisPredictionException(e, sys)


# Model Training
STAGE_NAME="Model Training Stage"

try:
    logger.info(f"<<<<<< stage {STAGE_NAME} started. >>>>>>")
    model_trainer=ModelTrainerTrainingPipeline()
    model_trainer.initiate_model_training()
    logger.info(f"<<<<<< stage {STAGE_NAME} completed >>>>>>")
except Exception as e:
    raise IrisPredictionException(e, sys)

