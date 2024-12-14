from src.irisdataprediction.entity.config_entity import (DataIngestionConfig)
from src.irisdataprediction import logger
import pandas as pd





class DataIngestion:
    def __init__(self, config:DataIngestionConfig):
        self.config=config

    def convert_to_csv_and_save_to_disk(self):
        logger.info(f"<<<<<< data ingestion: read data and convert to csv initiated >>>>>>")
        raw_data=pd.read_csv(self.config.local_data_file)
        raw_data.columns=self.config.columns_info
        save_path= self.config.unzip_dir+'/'+'iris.csv'
        raw_data.to_csv(save_path, index=False)
        logger.info(f"<<<<<< data ingestion: data converted to csv and stored in data ingestion  >>>>>>")