
$(document).ready(function(){
//    var socket = io.connect('http://' + document.domain + ':' + location.port + '/update');
    var socket = io.connect('http://localhost:5000/update');    
//    var numbers_received = [];
//    socket.on('newnumber', function(msg) {
//        console.log("Received number" + msg.number);
//        //maintain a list of ten numbers
//        if (numbers_received.length >= 10){
//            numbers_received.shift()
//        }            
//        numbers_received.push(msg.number);
//        numbers_string = '';
//        for (var i = 0; i < numbers_received.length; i++){
//            numbers_string = numbers_string + '<p>' + numbers_received[i].toString() + '</p>';
//        }
//        $('#log').html(numbers_string);
//    });
//
});
