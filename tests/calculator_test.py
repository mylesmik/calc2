"""Testing the Calculator class"""
import pytest
from calc.calculator import Calculator
from calc.history.calculations import Calculations
from calc.csv_handling.csv_reading import CsvRead
from calc.csv_handling.log_file import LogWrite
from calc.csv_handling.csv_writing import CsvWrite
from calc.csv_handling.file_move import FileOperator


@pytest.fixture
def clear_history():
    """Clears the history of the calculator for each test"""
    Calculations.clear_history()


def row_to_tup(row):
    """Converts the values within a row into a tuple"""
    return row['value_a'], row['value_b'], row['value_c']


def test_adding(clear_history):
    """Tests the adding function of the calculator class"""
    # pylint: disable=redefined-outer-name, unused-argument, unused-variable
    test_file_name = 'adding.csv'
    csv_loc = CsvRead.search_csv(test_file_name)
    df_two = CsvRead.csv_to_df(csv_loc)
    for index, row in df_two.iterrows():
        tup = row_to_tup(row)
        test_value = Calculator.add_numbers(tup)
        LogWrite.add_to_log(test_file_name)
        assert test_value == row['result']
    FileOperator.move_to_destination(csv_loc)



def test_subtracting(clear_history):
    """Tests the subtracting function of the calculator class"""
    # pylint: disable=redefined-outer-name, unused-argument, unused-variable
    test_file_name = 'subtracting.csv'
    csv_loc = CsvRead.search_csv(test_file_name)
    df_two = CsvRead.csv_to_df(csv_loc)
    for index, row in df_two.iterrows():
        tup = row_to_tup(row)
        assert Calculator.subtract_numbers(tup) == row['result']
        LogWrite.add_to_log(test_file_name)
    FileOperator.move_to_destination(csv_loc)


def test_multiplying(clear_history):
    """Tests the multiplying function of the calculator class"""
    # pylint: disable=redefined-outer-name, unused-argument, unused-variable
    test_file_name = 'multiplying.csv'
    csv_loc = CsvRead.search_csv(test_file_name)
    df_two = CsvRead.csv_to_df(csv_loc)
    for index, row in df_two.iterrows():
        tup = row_to_tup(row)
        assert Calculator.multiply_numbers(tup) == row['result']
        LogWrite.add_to_log(test_file_name)
    FileOperator.move_to_destination(csv_loc)

def test_dividing(clear_history):
    """Tests the dividing function of the calculator class"""
    # pylint: disable=redefined-outer-name, unused-argument, unused-variable
    test_file_name = 'dividing.csv'
    csv_loc = CsvRead.search_csv(test_file_name)
    df_two = CsvRead.csv_to_df(csv_loc)
    for index, row in df_two.iterrows():
        tup = row_to_tup(row)
        if row['result'] == '#DIV/0!':
            assert Calculator.divide_numbers(tup) == ZeroDivisionError
            LogWrite.add_to_zero_log(test_file_name)
        else:
            assert Calculator.divide_numbers(tup) == float(row['result'])
            LogWrite.add_to_log(test_file_name)
    FileOperator.move_to_destination(csv_loc)


def test_complete_logs():
    """Commits the logs to csvs and resets the dataframes"""
    CsvWrite.set_directory()
    LogWrite.commit_log()
    LogWrite.commit_zero_log()
    LogWrite.reset_dfs()
