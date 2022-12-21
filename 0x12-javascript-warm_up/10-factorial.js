#!/usr/bin/node
const val = process.argv[2];
function factoria(val)
{
	if (val === 1 || isNaN(val))
		return 1;
	return (val * factoria(val-1));
}
console.log(factoria(val));
