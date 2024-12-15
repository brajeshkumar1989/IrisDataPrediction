import os
import sys
import yaml
from src.irisdataprediction import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
from box.exceptions import BoxValueError
from src.irisdataprediction.exception import IrisPredictionException
import matplotlib.pyplot as plt

@ensure_annotations

def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    reads yaml file and returns
    
    Args:
        path_to_yaml(str): path like input
        
    Raises:
        ValueError: if yaml file is empty
        e: empty file
        
    Returns:
        ConfigBox: ConfigBox type
        
    
    """

    try:
        with open(path_to_yaml) as yaml_file:
            content= yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise IrisPredictionException(e, sys)

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """
    Create list of directories

    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created.
        Defaults to False.
    """

    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory at: {path}")


@ensure_annotations
def save_json(path: Path, data: dict):
    """
    save json data

    Args:
        path (Path): path to json file
        data (dict): data to be saved in json file
    """

    with open(path, "w") as f:
        json.dump(data, f, indent=4)

    logger.info(f"json file saved at: {path}")


@ensure_annotations
def load_json(path:Path)->ConfigBox:
    """load json file"""
    with open(path) as f:
        content=json.load(f)
    
    logger.info(f"json file loaded successfully from:{path}")
    return ConfigBox(content)


@ensure_annotations
def save_bin(data: Any, path: Path):
    """Save binary file
    """

    joblib.dump(value=data, filename=path)
    logger.info(f"binary file saved at: {path}")


@ensure_annotations
def load_bin(path: Path) -> Any:
    """load binary data"""
    data=joblib.load(path)
    logger.info(f"binary file loaded from:{path}")
    return data


# @ensure_annotations
def save_figure(fig_id: str,image_path: Path, tight_layout :bool, fig_extension: str, resolution: int):
    plt.rc('font', size=14)
    plt.rc('axes', labelsize=14, titlesize=14)
    plt.rc('legend', fontsize=14)
    plt.rc('xtick',labelsize=10)
    plt.rc('ytick',labelsize=10)
    # path=image_path/ f"{fig_id}.{fig_extension}"
    path=os.path.join(image_path,f"{fig_id}.{fig_extension}")
    if tight_layout:
        plt.tight_layout()
    plt.savefig(path, format=fig_extension, dpi=resolution)
    logger.info(f"Created directory at: {image_path}")
    