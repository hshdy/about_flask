#! /usr/bin/env python
#-*- coding:utf-8 -*-
#Author: hsh
# 19-3-17  下午2:25

from eventlet import wsgi
import eventlet

def hello_world(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return ['Hello, World!\r\n']

wsgi.server(eventlet.listen(('192.168.222.132', 8090)), hello_world)

