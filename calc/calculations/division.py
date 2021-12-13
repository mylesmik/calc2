"""Division Class"""
from calc.calculations.calculation import Calculation

class Division(Calculation):
    """division calculation object"""
    def get_result(self):
        """get the division results"""
        divided_value = self.values[0]
        for index, value in enumerate(self.values):
            if index > 0:
                try:
                    divided_value /= value
                except ZeroDivisionError:
                    return 'Zero Division Error'

        return round(divided_value,2)
