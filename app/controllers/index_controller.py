from app.controllers.controller import ControllerBase
from flask import render_template

class IndexController(ControllerBase):
    # pylint: disable-all
    @staticmethod
    def get():
        return render_template('index.html')
