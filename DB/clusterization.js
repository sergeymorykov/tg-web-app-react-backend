const kmeans = require('ml-kmeans');

const fs = require('fs');
const data = JSON.parse(fs.readFileSync('data.json', 'utf8'));

let clusters = kmeans.kmeans(data, 2);


console.log(clusters);
