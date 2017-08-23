#!/usr/bin/env python
# -*- coding utf-8 -*-

__author__="NJ"

import logging; logging.basicConfig(level=logging.INFO)

import asyncio, os, json, time
from datetime import datetime

from aiohttp import web

def index(request):
	return web.Response(body='<h1>hello python3</h1>')


#async 
@asyncio.coroutine
def init(loop):
	app = web.Application(loop)
	app.router.add_route('GET','/','index')
	#srv = await loop.create_server(app.make_handler(), '127.0.0.1', 9000)
	srv = yield from loop.create_server(app.make_handler(), '127.0.0.1', 9000)
	logging.info('server started at http://127.0.0.1:9000...')
	return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()