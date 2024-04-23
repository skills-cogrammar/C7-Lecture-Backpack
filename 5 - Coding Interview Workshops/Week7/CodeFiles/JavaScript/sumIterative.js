function sum (n) {
    let total = 0;
    
    while (n > 0) {
        total += n;
        n -= 1;
    }

    return total
}

console.log(sum(1000))