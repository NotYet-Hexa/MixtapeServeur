#!/usr/bin/env python
# coding: utf-8

from socketIO_client import SocketIO, BaseNamespace, LoggingNamespace
import json

def registrationResponse(*args):
    print('raspberry_registration', args)

data = {	
		"raspberry":"gaston_berger"
	}

json_data_registration = json.dumps(data)

def on_res(*args):
    print('on_reponse', args)


#socketIO = SocketIO('localhost', 8080)
#socketIO.on('raspberry_registration',json_data_registration)
#socketIO.wait()

with SocketIO('localhost', 8000, LoggingNamespace) as socketIO:
    socketIO.emit('raspberry_registration', {'ack': 'ok'}, on_res)
    socketIO.wait_for_callbacks(seconds=1)