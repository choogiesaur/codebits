function firstFactorial(num) { 

  let ans = 1;  
  for(let i = num; i >= 1; i--){
    ans *= i;
  }
  return ans; 

}

console.log(firstFactorial(5));
// 120
