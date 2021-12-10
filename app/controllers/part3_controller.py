from app.controllers.controller import ControllerBase
from flask import render_template

class Part3Controller(ControllerBase):
    # pylint: disable-all
    @staticmethod
    def get():
        return render_template('part3.html')