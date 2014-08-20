// program.js

//note to self: RETURN EVERYTHING EVERY TIME

function checkUsersValid(goodUsers) {
	return function(submittedUsers) {
		return submittedUsers.every(function(user) {
			return goodUsers.some(function(official_user) {				
				return user.id == official_user.id;
			});
		});
	};
}

module.exports = checkUsersValid;