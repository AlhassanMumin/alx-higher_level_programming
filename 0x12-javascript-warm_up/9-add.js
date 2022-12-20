#!/usr/bin/node
let argOne = process.argv[2], argTwo = process.argv[3];
function add(a, b)
{
	console.log(a + b);	
}
add(parseInt(argOne), parseInt(argTwo));
