# coding=utf-8
import asyncio
from Log import Log as print
import json as json_y

from sanic import Sanic
from sanic.response import json

app = Sanic("SFPanel_Back")
print = print('Back')

@app.route("/ping")
async def test(request):
    print.INFO('* -> ping')
    return json({"hello": "world"})

async def Start():
    print.INFO('后端启动成功')

app.add_task(Start())

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=9000)
