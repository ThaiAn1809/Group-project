// process.stdin.setEncoding('utf8');
// process.stdin.on('data', function(input) {
//     const nums = input.trim().split('\n');
//     let x = parseInt(nums[0]);
//     let y = parseInt(nums[1]);
//     console.log(x+y);
//     console.log(x-y);
// });


process.stdin.setEncoding('utf8');
process.stdin.on('data', function(input) {
   var mile = parseInt(input)
   var km = mile * 1.60;
   console.log(km);
});