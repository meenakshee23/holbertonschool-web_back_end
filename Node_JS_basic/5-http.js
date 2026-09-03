const http = require('http');
const countStudents = require('./3-read_file_async');

const database = process.argv[2];

const app = http.createServer((req, res) =>{

});

app.listen(1245);

module.exports = app;
