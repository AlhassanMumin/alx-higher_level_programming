#!/usr/bin/node
let size = process.argv[2];
let arr = [];
if (isNaN(process.argv[2]) || process.argv.length - 2 === 0)
{
	console.log('Missing size');
}
else if (size > 0)
{
	while (size--)
	{
		arr.push('x');
	}
	let str = arr.join('');
	for (let i = 0; i < process.argv[2]; i++)
	{
		console.log(str);
	}
}
