socket.on('message', function() {
	$('#log').empty();
	$('#log').append( "<tr id=\"head\"><td class=\"level table-header\">Level</td><td class=\"timestamp table-header\">Timestamp</td><td class=\"message table-header\">Message</td><tr>" );
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
			//$('#log').append( "<p class=\"" + notification_type + "\" id=" + data[i].uuid + ">" + data[i].level + " | " + data[i].timestamp + " | <b>" + data[i].body + "</b></p>" );
			//$('#log').append( "<tr class=\"" + notification_type + "\" id=" + data[i].uuid + "><td>" + data[i].level + "</td><td>" + data[i].timestamp + "</td><td>" + data[i].body + "</td><tr>" );
			//$('#log').append( "<tr id=" + data[i].uuid + " class=\"tr-message\"><td class=\"" + notification_type + "-text level\">" + data[i].level + "</td><td class=\"timestamp\">" + data[i].timestamp + "</td><td class=\"message\">" + data[i].body + "</td><tr>" );
			$( "<tr id=" + data[i].uuid + " class=\"tr-message\"><td class=\"" + notification_type + "-text level\">" + data[i].level + "</td><td class=\"timestamp\">" + data[i].timestamp + "</td><td class=\"message\">" + data[i].body + "</td><tr>" ).insertAfter('#head');
		}
	});
});