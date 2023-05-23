#!/usr/bin/node
const fs = require('fs');

const filepath = process.argv[2];
const data = process.argv[3];

fs.writeFile(filepath, data, 'utf-8', function (error) {
  if (error) console.log(error);
});
