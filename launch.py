from sanic import Sanic
from sanic.response import json
from sanic.request import Request
from config import WEB_SERVER_PORT

app = Sanic(name="BTTK")


@app.route("/")
async def test(request: Request):
    return json({"hello": "world"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=WEB_SERVER_PORT)
