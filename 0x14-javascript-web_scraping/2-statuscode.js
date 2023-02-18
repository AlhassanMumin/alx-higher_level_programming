#!/usr/bin/node
const request = require('request');
const args = process.argv.slice(2);
request(args[0], (error, response, body) => {
	if (error) {
    console.error(error);
    return;
  }
	console.log(`code: ${response.statusCode}`);
});
