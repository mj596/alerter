$('#log').empty();
$.get( "getData", function( data ) {
	for (i = 0; i < data.length; i++) {
		var message_type = data[i].level;
		var notification_type;
		if(message_type == "ERROR") {
			notification_type = "error";
		} else if(message_type == "WARNING") {
			notification_type = "warning";
		} else if(message_type == "INFO") {
			notification_type = "info";
		} else {
			notification_type = "message";
		}
		$('#log').append( "<p class=\"" + notification_type + "\" id=" + data[i].uuid + ">" + data[i].level + " | " + data[i].timestamp + " | <b>" + data[i].body + "</b></p>" );
	}
});