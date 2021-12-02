""" This is the increment function"""
from calc.calculations.addition import Addition
from calc.calculations.subtraction import Subtraction
from calc.calculations.multiplication import Multiplication
from calc.history.calculations import Calculations
from calc.calculations.division import Division

#the calculator class just contains the methods to calculate
class Calculator:
    """ This is the Calculator class"""
    #the calculator class just calls methods on Calculations class
    @staticmethod
    def get_last_result_value():
        """ This is the gets the result of the calculation"""
        # I made this method so that I don't have more than one action per function
        return Calculations.get_last_calculation_result_value()

    @staticmethod
    def __add__(values: tuple):
        """ adds list of numbers"""
        Calculations.append_calculation_to_history(Addition.create(values))
        return True

    @staticmethod
    def __sub__(values: tuple):
        """ subtract a list of numbers from result"""
        Calculations.append_calculation_to_history(Subtraction.create(values))
        return True

    @staticmethod
    def __mul__(values: tuple):
        """ multiplication number from result"""
        Calculations.append_calculation_to_history(Multiplication.create(values))
        return True

    @staticmethod
    def __truediv__(values: tuple):
        """ Division number from result"""
        Calculations.append_calculation_to_history(Division.create(values))
        return True
