const names = ['Chris', 'Li Kang', 'Anne', 'Francesca', 'Mustafa', 'Tina', 'Bert', 'Jada']

function random(lower, upper) {
    let diff = upper - lower;
    return (lower + Math.floor(Math.random() * diff));
}

function chooseName() {
    i = random(3,8);
    console.log(names[i]);
}

chooseName();
