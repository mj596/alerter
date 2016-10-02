function discard() {
	if (confirm('Are you sure you want to discard these messages?')) {
		var selector = $('.tr-message:visible');
		selector.each( function( ) {
		var identifier = $(this).attr( "id" );
		socket.emit('delete', { "uuid": identifier } );
		$(this).hide();
	});
	socket.emit('message');
	} else {}
}