#!/usr/bin/node
let len = process.argv.length - 2;
if (len === 0)
{
	console.log('Missing number of occurrences');
}
else if (len > 0 && process.argv[2] > 0)
{
	let size = process.argv[2];
	while (size--)
	{
		console.log('C is fun');
	}
}
