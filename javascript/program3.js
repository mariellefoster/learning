// program.js

//initial
function getShortMessages(messages) {
	var messy = messages.filter(function(mess) {
		if (mess.message.length < 50) {
			return mess.message;
		}
	});
	return messy.map(function(mess) {
		return mess.message;
	});
}

//more elegant

function getShortMessages(messages) {
	return messages.filter(function(mess) {
		 return mess.message.length < 50
	}).map(function(mess) {
		return mess.message;
	});
}

module.exports = getShortMessages;