$(document).ready(function(){
	$("#log").delegate("p", "click", function(){
		//var identifier = event.target.id;
		var identifier = $(this).attr( "id" );
		$(this).hide();
		socket.emit('delete', { "uuid": identifier } );
		socket.emit('message');
	});
});		