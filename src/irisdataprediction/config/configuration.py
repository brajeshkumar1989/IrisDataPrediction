from src.irisdataprediction.entity.config_entity import (DataIngestionConfig,DataValidationConfig,DataTransformationConfig,ModelTrainerConfig)
from src.irisdataprediction.constants import *
from src.irisdataprediction.utils.common import read_yaml, create_directories

from src.irisdataprediction import logger




class ConfigurationManager:
    def __init__(self, config_filepath=CONFIG_FILE_PATH, params_filepath=PARAMS_FILE_PATH, schema_filepath=SCHEMA_FILE_PATH):
        logger.info(f"<<<<<< Setting up path, params, schema configurations >>>>>>")
        self.config=read_yaml(config_filepath)
        self.params=read_yaml(params_filepath)
        self.schema=read_yaml(schema_filepath)

        create_directories([self.config.artifacts_root])
        logger.info(f"<<<<<< Configuration detail scan completed followed by parent directory artifacts creation >>>>>>")

    def get_data_ingestion_config(self)->DataIngestionConfig:
        config=self.config.data_ingestion
        schema_independent=self.schema.COLUMNS
        schema_dependent=self.schema.TARGET_FEATURE

        #create directories
        create_directories([config.root_dir])
        logger.info(f"<<<<<< root directory created for artifacts Ingestion >>>>>>")

        #return created directories for file read, write and content manipulation
        data_ingestion_config=DataIngestionConfig(
            root_dir=config.root_dir,
            local_data_file= config.local_data_file,
            unzip_dir=config.unzip_dir,
            columns_info= [*schema_independent.keys(), *schema_dependent.keys()]

        )
       
        return data_ingestion_config
    
    def get_data_validation_config(self)->DataValidationConfig:
        config=self.config.data_validation
        schema= self.schema.COLUMNS

        create_directories([config.root_dir])
        create_directories([config.image_path])

        data_validation_config=DataValidationConfig(
            root_dir= config.root_dir,
            STATUS_FILE=config.STATUS_FILE,
            unzip_data_dir=config.unzip_data_dir,
            all_schema=schema,
            image_path=config.image_path
        )

        return data_validation_config
    

    def get_data_transformation_config(self)->DataTransformationConfig:
        config= self.config.data_transformation
        create_directories([config.root_dir])

        data_transformation_config= DataTransformationConfig(root_dir=config.root_dir, data_path=config.data_path)

        return data_transformation_config
    
    def get_model_trainer_config(self) -> ModelTrainerConfig:
        config= self.config.model_trainer
        params= self.params.ElasticNet
        schema=self.schema.TARGET_COLUMN

        create_directories([config.root_dir])

        model_trainer_config= ModelTrainerConfig(
            root_dir= config.root_dir,
            train_data_path=config.train_data_path,
            test_data_path=config.test_data_path,
            model_name=config.model_name,
            alpha=params.alpha,
            l1_ratio=params.l1_ratio,
            target_column=schema.name
        )

        return model_trainer_config