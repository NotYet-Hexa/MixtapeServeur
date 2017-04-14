#!/usr/bin/env python
# coding: utf-8

from socketIO_client import SocketIO, BaseNamespace

socketIO = SocketIO('localhost', 8080)
socketIO.emit('message', 'emit_data')
socketIO.wait()