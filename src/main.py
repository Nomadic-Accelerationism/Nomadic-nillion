from flask import Flask, jsonify, request
import requests 
import json
from nada_dsl import *
app = Flask(__name__)


@app.route("/")
def helloworld():
    return 'N/ACC'
    


@app.route('/compare', methods=['GET'])
def compare():
    interestFrom = request.args.get('interestFrom')
    interinterestToest2 = request.args.get('interestTo')
    party1 = Party(name="interestFrom")
    party2 = Party(name="interestTo")
    a = SecretInteger(Input(name="A", party=party1))
    b = SecretInteger(Input(name="B", party=party2))

    resultFrom = a > 1
    resultTo = b > 1
    result = resultFrom + resultTo

    return [Output(result, "my_output", party3)]


