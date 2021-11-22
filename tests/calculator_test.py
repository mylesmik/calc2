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

def test_calculator_add_static(clear_history_fixture):
    """testing that our calculator has a static method for addition"""
    # pylint: disable=unused-argument,redefined-outer-name
    my_tuple = (1.0,2.0,5.0)
    Calculator.add_numbers(my_tuple)
    assert Calculator.get_last_result_value() == 8.0
    my_tuple = (10.0, 58.0, 50.0)
    Calculator.add_numbers(my_tuple)
    assert Calculator.get_last_result_value() == 118.0

def test_calculator_subtract_static(clear_history_fixture):
    """Testing the subtract method of the calc"""
    # pylint: disable=unused-argument,redefined-outer-name
    my_tuple = (1.0,2.0,3.0)
    Calculator.subtract_numbers(my_tuple)
    assert Calculator.get_last_result_value() == -4.0
    my_tuple = (100.0, 25.0, 35.0)
    Calculator.subtract_numbers(my_tuple)
    assert Calculator.get_last_result_value() == 40.0

def test_calculator_multiply_static(clear_history_fixture):
    """Testing the multiply method of the calc"""
    # pylint: disable=unused-argument,redefined-outer-name
    my_tuple = (1.0,2.0,3.0)
    Calculator.multiply_numbers(my_tuple)
    assert Calculator.get_last_result_value() == 6.0
    my_tuple = (11.0, 20.0, 30.0)
    Calculator.multiply_numbers(my_tuple)
    assert Calculator.get_last_result_value() == 6600.0

def test_calculator_divide_static(clear_history_fixture):
    """Testing the divide method of the calc"""
    # pylint: disable=unused-argument,redefined-outer-name
    my_tuple = (1.0,2.0,2.0)
    Calculator.divide_numbers(my_tuple)
    assert Calculator.get_last_result_value() == 0.25
    my_tuple = (100.0, 2.0, 5.0)
    Calculator.divide_numbers(my_tuple)
    assert Calculator.get_last_result_value() == 10.0

def test_calculator_division_exception_static(clear_history_fixture):
    """Testing the divide method with exception of the calc"""
    # pylint: disable=unused-argument,redefined-outer-name
    my_tuple = (1.0,0.0,2.0)
    Calculator.divide_numbers(my_tuple)
    with pytest.raises(ZeroDivisionError):
        assert Calculator.get_last_result_value() is True
