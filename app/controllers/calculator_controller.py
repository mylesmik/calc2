from app.controllers.controller import ControllerBase
from calc.calculator import Calculator
from calc.history.calculations import Calculations
from flask import render_template, request, flash


class CalculatorController(ControllerBase):
    @staticmethod
    def post():
        if request.form['value1'] == '' or request.form['value2'] == '' or request.form['value3']=='':
            error = 'You MUST enter a numeric value for value 1 and or value 2 and or value 3'
        else:
            flash('Calculation done successfully')
            flash('View your results below')

            # get the values out of the form
            value1 = request.form['value1']
            value2 = request.form['value2']
            value3 = request.form['value3']
            operation = request.form['operation']
            # make the tuple
            my_tuple = (value1, value2, value3)
            # this will call the correct operation
            getattr(Calculator, operation)(my_tuple)
            result = str(Calculations.get_last_calculation_result_value())
            return render_template('result.html', value1=value1, value2=value2, value3=value3, operation=operation, result=result)
        return render_template('calculator.html', error=error)
    @staticmethod
    def get():
        return render_template('calculator.html')





