#!/usr/bin/node

const fs = require('fs');
const args = process.argv.slice(2);
fs.writeFile(args[0], args[1], { encoding: 'utf8' }, (err) => {
  if (err) {
    console.log(err);
    return;
  }
});
