var http = require('http');
var fs = require('fs');

// Chargement du fichier index.html affiché au client
var server = http.createServer(function(req, res) {
    fs.readFile('./index.html', 'utf-8', function(error, content) {
        res.writeHead(200, {"Content-Type": "text/html"});
        res.end(content);
    });
});

// Chargement de socket.io
var io = require('socket.io').listen(server);

// Quand un client se connecte, on le note dans la console

io.sockets.on('connection', function (socket) {
	console.log('Connexion Raspberry Ouverte');

	socket.on('informations', function (message) {
		console.log('Infomrations : ' + message);
	});	

	socket.on('raspberry_registration', function (registrationMessage) {
		console.log('Receive Response');
		jsonObject = JSON.parse(registrationMessage);
		console.log(jsonObject.raspberry);
		console.log('Send Response');
		socket.emit('raspberry_registration', 'Registration Successfull');
	});	

});


server.listen(8080);
