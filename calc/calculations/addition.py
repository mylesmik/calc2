"""Addition Class"""
from calc.calculations.calculation import Calculation

class Addition(Calculation):
    """ calculation addition class"""
    def get_result(self):
        """get the addition results"""
        return sum(self.values)
