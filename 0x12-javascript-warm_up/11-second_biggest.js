#!/usr/bin/node
let arr = [];
let size = process.argv;
if (size === 3 || isNaN(process.argv[2]))
{
	console.log(0);
	return;
}

for (let i = 2; i < size; i++)
{
	arr.push(parseInt(process.argv[i]));
}
arr.sort();
console.log(arr[1]);
