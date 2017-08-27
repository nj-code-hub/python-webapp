#!usr/bin/env python3
# -*- coding utf-8 -*-

__author__ = "NJ"

import orm
from models import User, Blog, Comment
import asyncio, time

async def newUser(loop):
    await orm.create_pool(loop=loop, user='www-data', password='www-data', db='awesome')

    u = User(name='Test5', email='test5@example.com', password='123456789', image='about:black')
    
    await u.save()


loop = asyncio.get_event_loop()
loop.run_until_complete(newUser(loop))
loop.close()
    