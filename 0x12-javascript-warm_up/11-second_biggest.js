#!/usr/bin/node
const arr = new Array();
let size = process.argv.length, tmp;
if (size === 3 || isNaN(process.argv[2]))
{
	console.log(0);
	return;
}
for(let i = 2; i < process.argv.length; ++i) 
{
	tmp = parseInt(process.argv[i]);
	arr.push(tmp);
}
arr.sort();
console.log(arr);
console.log(arr[size - 4]);
