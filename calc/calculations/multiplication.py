"""Multiplication Class"""
from calc.calculations.calculation import Calculation

class Multiplication(Calculation):
    """multiplication calculation object"""
    def get_result(self):
        """get the multiplication results"""
        multiplied_value = 0.0
        for index, value in enumerate(self.values):
            if index == 0:
                multiplied_value = value
            else:
                multiplied_value = multiplied_value * value
        return multiplied_value
