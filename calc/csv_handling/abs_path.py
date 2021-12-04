"""function to returns the absolute path of a csv file"""
from pathlib import Path


def abs_path_to_csv(filepath):
    """Converting a relative path to an absolute path"""
    return (Path(filepath)).absolute()
