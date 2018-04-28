#!/usr/bin/env python

from aiohttp import web
import linyi

async def handle(request):
    name = request.match_info.get('name', "Anonymous")
    if name == "linyi":
        return web.Response(text = linyi.render())

    else:
        return web.Response(text=text)




app = web.Application()
app.add_routes([web.get('/', handle),
                web.get('/{name}', handle)])

web.run_app(app,host='0.0.0.0', port=8080)
