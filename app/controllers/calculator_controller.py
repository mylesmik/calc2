from app.controllers.controller import ControllerBase
from calc.calculator import Calculator
from calc.history.calculations import Calculations
from flask import render_template, request, flash
from tests.csv_read import Read
from calc.csv_handling.csv_writing import CsvWrite

class CalculatorController(ControllerBase):
    # pylint: disable-all
    @staticmethod
    def post():
        if request.form['value1'] == '' or request.form['value2'] == '' or request.form['value3']=='':
            error = 'You MUST enter a numeric value for value 1 and or value 2 and or value 3'
        else:
            flash('Calculation done successfully')
            flash('View your results below')

            value1 = request.form['value1']
            value2 = request.form['value2']
            value3 = request.form['value3']
            operation = request.form['operation']

            my_tuple = (value1, value2, value3)

            getattr(Calculator, operation)(my_tuple)
            result =str(Calculations.get_last_calculation_result_value())
            CsvWrite.create_dataframe_to_write(value1, value2,value3, result, operation)
            df = Read.csvreader()
            return render_template('result_table.html', value1=value1, value2=value2, value3=value3, operation=operation, result=result,
                                   tables=[df.to_html(classes='data')], titles=df.columns.values,
                                   row_data=list(df.values.tolist()), zip=zip)
        return render_template('calculator.html', error=error)

    @staticmethod
    def get():
        return render_template('calculator.html')