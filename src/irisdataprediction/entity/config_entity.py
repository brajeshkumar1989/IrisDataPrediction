from dataclasses import dataclass
from pathlib import Path


@dataclass
class DataIngestionConfig:
    root_dir: Path
    local_data_file: Path
    unzip_dir: Path
    columns_info: list

@dataclass
class DataValidationConfig:
    root_dir: Path
    STATUS_FILE: str
    unzip_data_dir: Path
    all_schema: dict  #this is to hold data from schema.yaml
    image_path: Path

@dataclass
class DataTransformationConfig():
    root_dir: Path
    data_path: Path