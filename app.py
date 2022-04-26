from importlib.resources import Resource
from flask import Flask, jsonify
import flask
from waitress import serve
from flask_restful import Api

app = Flask(__name__)
api = Api(app)

connected_ids = []

class addId(Resource):
    def get(self, id):
        if id not in connected_ids:
            connected_ids.append(id)
            resp = flask.make_response(jsonify({"API": "success"}))
        else:
            resp = flask.make_response(jsonify({"API": "id_already_exists"}))
        
        print("Connected ids is now {}".format(connected_ids))
        return resp

class removeId(Resource):
    def get(self, id):
        if id in connected_ids:
            connected_ids.remove(id)
            resp = flask.make_response(jsonify({"API": "success"}))
        else:
            resp = flask.make_response(jsonify({"API": "id_does_not_exist"}))
        print("Connected ids is now {}".format(connected_ids))
        return resp

api.add_resource(addId, "/add/<int:id>")
api.add_resource(removeId, "/remove/<int:id>")

if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=8080)