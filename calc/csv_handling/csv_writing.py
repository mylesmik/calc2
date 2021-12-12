"""calculator test to write a log file"""
import os
import pandas as pd
from tests.csv_write import csvwriter

class CsvWrite:
    # pylint: disable-all
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

    @staticmethod
    def create_dataframe_to_write(val1, val2, val3, result, operation):
        """appends values and operation to history"""
        df_to_write = pd.DataFrame(columns=['value_1', 'value_2', 'value_3', 'result', 'operation performed'])
        df_to_write = df_to_write.append({'value_1': val1,
                                          'value_2': val2,
                                          'value_3': val3,
                                          'result': result,
                                          'operation performed': operation},
                                         ignore_index=True)
        return csvwriter(df_to_write)
