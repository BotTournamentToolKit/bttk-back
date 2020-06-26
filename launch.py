import asyncio
import platform

from sanic import Sanic
from sanic.response import json
from sanic.request import Request
from config import WEB_SERVER_PORT

app = Sanic(name="BTTK")


@app.route("/")
async def test(request: Request):
    return json({"hello": "world"})


def correct_loop():
    if platform.system() == "Windows":
        loop = asyncio.ProactorEventLoop()
    else:
        loop = asyncio.get_event_loop()
    return loop


if __name__ == "__main__":
    asyncio.set_event_loop(correct_loop())
    app.run(host="0.0.0.0", port=WEB_SERVER_PORT)
