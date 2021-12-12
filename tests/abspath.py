"""This is a function which returns the absolute path of a csv file for pylint"""
from pathlib import Path

def absolutepath(filepath):
    """relativepath calls the path object and then returns the absolute path"""
    relativepath = Path(filepath)
    return relativepath.absolute()
