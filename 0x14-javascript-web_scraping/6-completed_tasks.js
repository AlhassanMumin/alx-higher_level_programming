#!/usr/bin/node
const request = require('request');
const apiURL = process.argv[2];
request(apiURL, (error, response, body) => {
  if (error) console.error(error);
const todos = JSON.parse(body);
const completedTasksByUserId = new Map();
for (const todo of todos) {
    if (todo.completed) {
      const userId = todo.userId;
      const count = completedTasksByUserId.get(userId) || 0;
      completedTasksByUserId.set(userId, count + 1);
    }
  }

const myDictionary = new Object();
  for (const [userId, count] of completedTasksByUserId.entries()) {
    myDictionary[userId] = count;	  
  }
	console.log(myDictionary);
});
