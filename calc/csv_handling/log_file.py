"""Writes log csv files utilizing pandas"""
import time
from random import randint
import pandas as pd
from calc.csv_handling.csv_writing import CsvWrite
from calc.history.calculations import Calculations


class WriteLog:
    """method to prepare a log"""
    df = pd.DataFrame(columns=['id', 'time', 'operation', 'result', 'filename'])
    zero_df = pd.DataFrame(columns=['id', 'time', 'operation', 'result', 'filename'])
    save_path = 'calc2/tests/results'

    @staticmethod
    def get_id():
        """Returns id of a calculation"""
        record = WriteLog.df.shape[0]
        return record

    @staticmethod
    def get_time():
        """Returns unix time of calculation"""
        curr_time = time.time()
        return curr_time

    @staticmethod
    def get_operation():
        """Returns class of obj to get operation"""
        op = type(Calculations.get_last_calculation_object())
        return op

    @staticmethod
    def get_operation_result():
        """Returns the result of a calculation"""
        curr_result = Calculations.get_last_calculation_result_value()
        return curr_result

    @staticmethod
    def get_filename(test_file_name):
        """Returns the file name of the csv that is used for a test"""
        return test_file_name

    @staticmethod
    def add_to_log(test_file_name):
        """method to gather info to create dataframe"""
        WriteLog.df.loc[WriteLog.df.shape[0]] = [WriteLog.get_id(),
                                                 WriteLog.get_time(),
                                                 WriteLog.get_operation(),
                                                 WriteLog.get_operation_result(),
                                                 WriteLog.get_filename(test_file_name)]
        return True

    @staticmethod
    def add_to_zero_log(test_file_name):
        """Adding entry in exception log"""
        WriteLog.zero_df.loc[WriteLog.zero_df.shape[0]] = [WriteLog.get_id(),
                                                           WriteLog.get_time(),
                                                           WriteLog.get_operation(),
                                                           WriteLog.get_operation_result(),
                                                           WriteLog.get_filename(test_file_name)]
        return True

    @staticmethod
    def log_filename():
        """Generating name for log file"""
        log_name = 'log_' + str(randint(0, 50))
        return log_name

    @staticmethod
    def zero_log_filename():
        """Generating name for exception log file"""
        log_name = 'exception_log_' + str(randint(0, 50))
        return log_name

    @staticmethod
    def reset_dfs():
        """Removing data from panda dataframe"""
        WriteLog.df = pd.DataFrame(columns=['id', 'time', 'operation', 'result', 'filename'])
        WriteLog.zero_df = pd.DataFrame(columns=['id', 'time', 'operation', 'result', 'filename'])
        return True

    @staticmethod
    def commit_log():
        """Committing log into a csv"""
        CsvWrite.df_to_csv(WriteLog.df, file_name=WriteLog.log_filename())
        return True

    @staticmethod
    def commit_zero_log():
        """Committing exceptions log into a csv"""
        CsvWrite.df_to_csv(WriteLog.zero_df, file_name=WriteLog.zero_log_filename())
        return True
