const express = require('express');
const http = require('http');

const port = 3000;

const app = express();
app.use('/', express.static(__dirname));
const server = http.createServer(app);

server.listen(port, () => console.log(`Server started on port localhost:${port}`));

const spawner = require('child_process').spawn;

// string 
const data_to_pass_in ='Send this to python script.';

console.log('Data sent to python script:', data_to_pass_in);

const python_process = spawner('python', ['./did.py', data_to_pass_in]); 
python_process.stdout.on('data', (data) => { 
    console.log('Data received from python script:', data.toString());
});