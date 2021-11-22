"""Division Class"""
from calc.calculations.calculation import Calculation

class Division(Calculation):
    """division calculation object"""
    def get_result(self):
        """get the division results"""
        divided_value = 0.0
        for index, value in enumerate(self.values):
            if index == 0:
                divided_value = value
            else:
                divided_value = divided_value / value
        return divided_value
