"""Fixtures to be used globally under the tests directory"""

import pytest
from calc.calculations.addition import Addition
from calc.calculations.subtraction import Subtraction
from calc.calculations.multiplication import Multiplication
from calc.calculations.division import Division
from calc.history.calculations import Calculations
from calc.file_handling.read_file import PandasParseData

@pytest.fixture(name="clear_history_fixture")
def clear_history_fixture_test():
    """define a function that will run each time you pass it to a test, it is called a fixture"""
    return Calculations.clear_history()

@pytest.fixture(name="setup_history_test_fixture")
def setup_addition_calculation_fixture_test():
    """define a function that will run each time you pass it to a test, it is called a fixture"""
    #Arrange
    # import pdb;pdb.set_trace()
    file_name = "addition_15values.xlsx"
    df_values = PandasParseData(file_name).read_file()

    numbers_tuple1 = df_values.value_1[0], df_values.value_2[0]
    numbers_tuple2 = df_values.value_1[1], df_values.value_2[2]
    numbers_tuple3 = df_values.value_1[2], df_values.value_2[2]
    numbers_tuple4 = df_values.value_1[3], df_values.value_2[3]

    #Act
    Calculations.append_calculation_to_history(Addition.create(numbers_tuple1))
    Calculations.append_calculation_to_history(Subtraction.create(numbers_tuple2))
    Calculations.append_calculation_to_history(Multiplication.create(numbers_tuple3))
    Calculations.append_calculation_to_history(Division.create(numbers_tuple4))
    return True

@pytest.fixture(name="addition_file_fixture", scope="module")
def read_addition_file():
    """Method to read the file type"""
    file_name = "addition_1000values.xlsx"
    return  PandasParseData(file_name).read_file()

@pytest.fixture(name="subtraction_file_fixture", scope="module")
def read_subtraction_file():
    """Method to read the file type"""
    file_name = "subtraction_1000values.xlsx"
    return  PandasParseData(file_name).read_file()

@pytest.fixture(name="multiplication_file_fixture", scope="module")
def read_multiplication_file():
    """Method to read the file type"""
    file_name = "multiplication_1000values.xlsx"
    return  PandasParseData(file_name).read_file()

@pytest.fixture(name="division_file_fixture", scope="module")
def read_division_file():
    """Method to read the file type"""
    file_name = "division_1000values.xlsx"
    return  PandasParseData(file_name).read_file()

@pytest.fixture(name="subtraction_test_file_fixture", scope="module")
def read_subtraction_test_file():
    """Method to read the file type"""
    file_name = "subtraction_15values.xlsx"
    return  PandasParseData(file_name).read_file()
