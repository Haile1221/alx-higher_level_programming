#!/usr/bin/node

const fs = require('fs'); // Import the 'fs' module
const file = process.argv[2]; // Get the file path from the command line argument

// Read the file with utf-8 encoding
fs.readFile(file, 'utf-8', function (err, data) {
  if (err) {
    // If there's an error, print the error object
    console.log(err);
  } else {
    // Otherwise, print the content of the file
    console.log(data);
  }
});
