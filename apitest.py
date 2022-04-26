import asyncio
import websockets

async def hello():
    async with websockets.connect("ws://127.0.0.1:8765") as websocket:
        a = await websocket.recv()
        print(a)

asyncio.run(hello())