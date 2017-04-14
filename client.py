#!/usr/bin/env python
# coding: utf-8

from socketIO_client import SocketIO, BaseNamespace, LoggingNamespace
import json

#def registrationResponse(*args):
#    print('raspberry_registration', args)

data = {	
		"raspberry":"gaston_berger"
	}

json_data_registration = json.dumps(data)

socketIO = SocketIO('localhost', 8080)
socketIO.emit('raspberry_registration',json_data_registration)
#socketIO.emit('message', 'emit_data')
#socketIO.on('raspberry_registration',json_data_registration)
#socketIO.wait()
#socketIO.on('raspberry_registration',json_data_registration)
socketIO.wait()