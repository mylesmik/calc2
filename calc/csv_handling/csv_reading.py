"""Reads csv files """

import pandas as pd
from calc.csv_handling.abs_path import abs_path_to_csv


class CsvRead:
    """Class is built to read csv files"""
    @staticmethod
    def csv_to_df(csv_to_convert):
        """Converts a csv file into a dataframe"""
        pathway = abs_path_to_csv(csv_to_convert)
        return pd.read_csv(pathway)

    @staticmethod
    def search_csv(name_of_csv):
        """Searches for a particular csv in an input folder and returns location"""
        absolute_location = "tests/csvs/input_csv/" + name_of_csv
        return absolute_location
