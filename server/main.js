var express = require('express');
var axios = require('axios');
var app = express();
var server = require('http').Server(app);
var io = require('socket.io')(server);
server.listen(8088, function() {
    console.log('Servidor corriendo en http://localhost:8088');
});
var sendData = []

io.on('connection', (socket)=> {
    console.log('Un cliente se ha conectado');
    socket.on('messages', (data) => {
        sendData.push(data)
        if(sendData.length == 5){
            axios.post('http://api:8080/VeMecApi/historiales/varios_registros',sendData,{ headers: {'Access-Control-Allow-Origin': '*'} })
                .then(()=>{
                }).catch((e)=>{
                })
            sendData = []
        }
        io.emit('messages', data);
    });
});

