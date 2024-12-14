from src.irisdataprediction.config.configuration import ConfigurationManager
from src.irisdataprediction.components.data_ingestion import DataIngestion
from src.irisdataprediction import logger




class DataIngestionTraningPipeline:
    def __init__(self):
        pass

    def initiate_data_ingestion(self):
        config=ConfigurationManager()
        data_ingestion_config=config.get_data_ingestion_config()
        data_ingestion=DataIngestion(config=data_ingestion_config)
        data_ingestion.convert_to_csv_and_save_to_disk()
