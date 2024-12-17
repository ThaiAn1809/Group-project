process.stdin.setEncoding('utf8');

process.stdin.on('data', function(input) {
    const nums = input.split('\n');
    const testCases = nums[0];
    
    for(let i = 1 ; i <= 2 * testCases; i += 2) {
        console.log(nums[i],nums[i+1])
    }
});