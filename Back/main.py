# coding=utf-8
import json as json_y

from sanic import Sanic
from sanic.response import json

app = Sanic("SFPanel_Back")

@app.route("/")
async def test(request):
    return json({"hello": "world"})

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=9090)