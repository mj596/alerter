$(document).ready(function(){
	$("#log").delegate("tr", "click", function(){
		//var identifier = event.target.id;
		var identifier = $(this).attr( "id" );
		if( identifier == "head") {
		} else {
			$(this).hide();
			socket.emit('delete', { "uuid": identifier } );
			socket.emit('message');
		}
	});
});		