from flask import Flask, jsonify
from flask_cors import CORS
import flask

app = Flask(__name__)
CORS(app)

@app.route('/ping', methods=['GET', 'POST'])
def aaaa():
    resp = flask.make_response(jsonify({"Nick API": "ONLINE"}))
    return resp

app.run()