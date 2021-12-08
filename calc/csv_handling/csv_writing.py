"""calculator test to write a log file"""
import os
import pandas as pd


class CsvWrite:
    """Will turn a pandas dataframe into a csv log file"""
    @staticmethod
    def df_to_csv(df_to_convert: pd.DataFrame, file_name):
        """Converts a dataframe into a csv file"""
        df_to_convert.to_csv(file_name + ".csv", index=False)
        return True

    @staticmethod
    def set_directory():
        """Changes the directory to 'results' in order to commit the logs"""
        os.chdir('tests/results')
        return True
