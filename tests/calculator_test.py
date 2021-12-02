"""Testing the Calculator"""
import pytest
from calc.calculator import Calculator
from calc.history.calculations import Calculations

@pytest.fixture
def clear_history_fixture():
    """define a function that will run each time you pass it to a test, it is called a fixture"""
    # pylint: disable=redefined-outer-name
    Calculations.clear_history()
#You have to add the fixture function as a parameter to the test that you want to use it with

def test_calculator_add_static(clear_history_fixture, addition_file_fixture):
    """testing that our calculator has a static method for addition"""
    #Arrange
    tuple_values = addition_file_fixture.value_1[5], addition_file_fixture.value_2[5]
    #Act
    Calculator.__add__(tuple_values)
    #Assert
    assert Calculations.get_last_calculation_object() == addition_file_fixture['result'][5] \
           and clear_history_fixture is True

def test_calculator_subtract_static(clear_history_fixture, subtraction_file_fixture):
    """Testing the subtract method of the calc"""
    #Arrange
    tuple_values = subtraction_file_fixture.value_1[5], subtraction_file_fixture.value_2[5]
    #Act
    Calculator.__sub__(tuple_values)
    #Assert
    assert Calculations.get_last_calculation_object() == subtraction_file_fixture['result'][5] \
           and clear_history_fixture is True

def test_calculator_multiply_static(clear_history_fixture, multiplication_file_fixture):
    """Testing the multiplication method of the calc"""
    #Arrange
    tuple_values = multiplication_file_fixture.value_1[5], multiplication_file_fixture.value_2[5]
    #Act
    Calculator.__mul__(tuple_values)
    #Assert
    assert Calculations.get_last_calculation_object() == multiplication_file_fixture['result'][5] \
           and clear_history_fixture is True

def test_calculator_divide_static(clear_history_fixture, division_file_fixture):
    """Testing the division method of the calc"""
    #Arrange
    tuple_values = division_file_fixture.value_1[5], division_file_fixture.value_2[5]
    #Act
    Calculator.__truediv__(tuple_values)
    #Assert
    assert Calculations.get_last_calculation_object() == division_file_fixture['result'][5].round(decimals=5) \
           and clear_history_fixture is True

def test_calculator_divide_exception_static(clear_history_fixture, division_file_fixture):
    """Testing the division method of the calc for the exception"""
    #Arrange
    tuple_values = division_file_fixture.value_1[2], division_file_fixture.value_2[0]
    #Act
    Calculator.__truediv__(tuple_values)
    #Assert
    with pytest.raises(ZeroDivisionError):
        assert Calculations.get_last_calculation_object() is True \
               and clear_history_fixture is True

