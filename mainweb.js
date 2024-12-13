function outerFunction(x) {
    function innerFunction(y) {
        return x * y;
    }
    var result = innerFunction(x);
    return result;
}

var output = outerFunction(5);
console.log(output);
