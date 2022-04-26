from flask import Flask, jsonify
import flask
from waitress import serve

app = Flask(__name__)

@app.route('/')
def aaaa():
    resp = flask.make_response(jsonify({"Nick API": "ONLINE"}))
    return resp

if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=8080)