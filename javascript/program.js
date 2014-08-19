// program.js

function repeat(operation, num) {
	if (num > 0) {
		operation();
		repeat(operation, num-1);
	}
	return;
}

module.exports = repeat;