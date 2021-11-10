"""Testing Addition"""
from calc.calculations.addition import Addition

def test_calculation_addition():
    """testing that our calculator has a static method for addition"""
    #Arrange
    mynumbers = (1.0,2.0)
    # Act
    addition = Addition(mynumbers)
    #Assert
    assert addition.get_result() == 3.0
