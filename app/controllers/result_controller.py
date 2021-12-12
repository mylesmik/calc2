from app.controllers.controller import ControllerBase
from tests.csv_read import Read
from flask import render_template

class ResultController(ControllerBase):
    # pylint: disable-all
    @staticmethod
    def get():
        df = Read.csvreader()
        return render_template('result_table.html', titles=df.columns.values, row_data=list(df.values.tolist()), zip=zip)
