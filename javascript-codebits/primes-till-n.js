// Output all primes up to given n
let n = +prompt('Integer > 2?');
let outputText = '';

outer: for(let i = 2; i <= n; i++){
	for(let j = 2; j < i; j++){
		if(i % j == 0){
			continue outer;
		}
	}
	outputText += `,${i}`;
}

alert(outputText.substring(1));
