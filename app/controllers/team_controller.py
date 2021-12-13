from app.controllers.controller import ControllerBase
from flask import render_template

class TeamController(ControllerBase):
    # pylint: disable-all
    @staticmethod
    def get():
        return render_template('team.html')