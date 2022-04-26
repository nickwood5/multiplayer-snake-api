from flask import Flask, jsonify
import flask, websockets
from waitress import serve


async def get_user_id():
    async with websockets.connect("ws://127.0.0.1:8765") as websocket:
        user_id = await websocket.recv()
        return user_id

app = Flask(__name__)

@app.route('/')
async def aaaa():
    user_id = await get_user_id()
    resp = flask.make_response(jsonify({"Nick API": "HELLO"}))
    return resp

if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=8080)