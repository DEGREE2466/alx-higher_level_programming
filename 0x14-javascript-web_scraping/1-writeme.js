#!/usr/bin/node
// A  script to write to file

const fs = require('fs');
const filePath = process.argv[2];
const contentToWrite = process.argv[3];

fs.writeFile(filePath, contentToWrite, 'utf-8', (error) => {
  if (error) {
    console.log(error);
  }
});
