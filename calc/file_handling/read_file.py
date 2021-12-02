"""Using pandas to extract data from external file for testing all operations"""

import os
import pandas as pd

class PandasParseData:
    # pylint: disable=too-few-public-methods
    """Class to create dataframes for our external data"""
    def __init__(self, file_name):
        self._file_name = file_name

    @property
    def file_name(self):
        return self._file_name

    @staticmethod
    def read_file(file_name):
        """Method to read the file type"""
        if ".csv" in file_name:
            function_handler = PandasParseData._parse_csv_file
        elif ".xlsx" in file_name:
            function_handler = PandasParseData._parse_xlsx_file
        else:
            raise ValueError("Could not recognize file type")
        return function_handler(file_name)

    @staticmethod
    def _parse_xlsx_file(file_name):
        """Method to convert data from xlsx to df"""
        root_dir = os.path.dirname(os.path.realpath(__file__))
        file_path = os.path.join(root_dir, "test_data", file_name)
        df_data = pd.read_excel(io=file_path, index_col=None,
                                names=["value_a", "value_b", "result"], dtype='float')
        return df_data


    @staticmethod
    def _parse_csv_file(file_name):
        # pylint: disable=unnecessary-pass
        """Method to process data from csv file to df"""
        root_dir = os.path.dirname(os.path.realpath(__file__))
        file_path = os.path.join(root_dir, "test_data", file_name)
        df_data = pd.read_csv(file_path, header=None)
        return df_data