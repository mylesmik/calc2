"""A simple flask web app"""
from flask import Flask
from app.controllers.index_controller import IndexController
from app.controllers.calculator_controller import CalculatorController
from app.controllers.video2_controller import Video2Controller
from app.controllers.part3_controller import Part3Controller
from werkzeug.debug import DebuggedApplication

#pylint: disable-all
app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.wsgi_app = DebuggedApplication(app.wsgi_app, True)

@app.route("/", methods=['GET'])
def index_get():
    return IndexController.get()

@app.route("/video2", methods=['GET'])
def video2_get():
    return Video2Controller.get()

@app.route("/part3", methods=['GET'])
def part3_get():
    return Part3Controller.get()

@app.route("/calculator", methods=['GET'])
def calculator_get():
    return CalculatorController.get()

@app.route("/calculator", methods=['POST'])
def calculator_post():
    return CalculatorController.post()