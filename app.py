from importlib.resources import Resource
from flask import Flask, jsonify
import flask
from waitress import serve
from flask_restful import Api

app = Flask(__name__)
api = Api(app)

connected_ids = []

@app.route('/remove/<int:id>/')
def remove(id):
    print("REMOVE CALLED")
    if id in connected_ids:
        connected_ids.remove(id)
        resp = flask.make_response(jsonify({"API": "success"}))
    else:
        resp = flask.make_response(jsonify({"API": "id_does_not_exist"}))
    print("Connected ids is now {}".format(connected_ids))
    return resp

@app.route('/')
def hello():
    resp = flask.make_response(jsonify({"API": "HI"}))
    return resp

@app.route('/get/')
def get(id):
    print("GET CALLED")
    id = 0
    while id in connected_ids:
        id += 1
    connected_ids.append(id)
    resp = flask.make_response(jsonify({"id": id}))
    return resp

if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=8080)