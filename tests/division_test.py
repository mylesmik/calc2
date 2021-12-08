"""Testing Division"""
from calc.calculations.division import Division

def test_calculation_division():
    """testing that our calculator has a static method for division"""
    #Arrange
    mynumbers = (1.0,2.0)
    # Act
    division = Division(mynumbers)
    #Assert
    assert division.get_result() == 0.5
