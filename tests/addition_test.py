"""Testing Addition"""
from calc.calculations.addition import Addition

def test_calculation_addition(addition_file_fixture):
    """testing that our calculator has a static method for addition"""
    #Arrange
    for index, row in addition_file_fixture.iterrows():
        values = (row.value_1, row.value_2)
    # Act
    addition = Addition.create(values)
    #Assert
    assert addition.get_result() == row.result
