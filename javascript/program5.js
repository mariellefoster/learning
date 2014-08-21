// program.js

function countWords(inputWords){
  return inputWords.reduce(function(wordNum, currVal){
    if (!wordNum[currVal]){
      wordNum[currVal] = 1;
    } else {
      wordNum[currVal] = wordNum[currVal] + 1;
    }
    return wordNum;
  },{});
}


//elegant
function countWords(inputWords) {
	//console.log(inputWords);
	return inputWords.reduce(function(count, word){
		count[word] = ++count[word] || 1;
		return count;
	}, {});
}

module.exports = countWords;