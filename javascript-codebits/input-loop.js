// Loop till input is > 100
// Revisit to see if null check can be simplified
let num = 0;
while(num < 100){
    let txt = prompt('Num > 100?'); 
    num = +txt;
    if(txt == 0 || txt == null) break;
    if(num <= 100) alert('Not greater than 100');
}
