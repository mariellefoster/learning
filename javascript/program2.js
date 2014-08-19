// program.js

//final
function doubleAll(numbers) {
	return numbers.map(function(num){
		return num*2;
	});
}

module.exports = doubleAll;

//initial solution, less elegant
function doubleAll(numbers) {
	var doubled = numbers.map(function(num){
		return num*2;
	});
	return doubled;
}

module.exports = doubleAll;