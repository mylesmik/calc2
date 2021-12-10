from app.controllers.controller import ControllerBase
from flask import render_template

class Video2Controller(ControllerBase):
    # pylint: disable-all
    @staticmethod
    def get():
        return render_template('video2.html')