const express = require("express"); //imports express library, used for building web apps in node JS. Used link geeksforgeeks.org/steps-to-create-an-express-js-application/
const fs = require("fs"); //imports the file system module which allows us to work with the file system.

<<<<<<< HEAD
const app = express();
const portNum = 3000;

const logFile = "/home/cechuser/it3038c-scripts/project2/log.log";
=======
const app = express(); //creates instance of express app and stores in app variable
const port = 3000; //sets variable port to 3000, specifying which port web server will listen for incoming requests

const logFilePath = "/home/cechuser/it3038c-scripts/project2/log.log"; //sets the path to the log file I will be using (I pulled kernal logs for 11/1 and 10/30, as there was too much data to pull all of it)
>>>>>>> 50c97b80e2a4f1687bb561c95a92fc863ae8b25e

app.get("/", (req, res) => { //sets up a route listening for HTTP GET requests to the root URL, when the request is received the callback function is initiated. Used link geeksforgeeks.org/express-js-app-get-request-function/

<<<<<<< HEAD
	fs.readFile(logFile, "utf8", (err, data) => {
		if (err) {
			res.status(500).send("Error");
=======
	fs.readFile(logFilePath, "utf8", (err, data) => { //Reads contents of file listed above and if there are any errors, it is caught in err and data will hold the content. Used link geeksforgeeks.org/node-js-fs-readfile-method/
		if (err) { // checks err and if yes, executes script following that sending an http response w status code 500 and plaintext, in this case error.
			res.status(500).send("Error"); // used link geeksforgeeks.org/express-js-res-status-function/
>>>>>>> 50c97b80e2a4f1687bb561c95a92fc863ae8b25e
		}	else {
			const logHTML = `<html><head><title>Log File Viewer</title></head><body><pre>${data}</pre></body></html>`; // creates html page pulling in data and assigning to variable logHTML
			res.send(logHTML); //Send an HTTP response containing the html page via the variable. Used link geeksforgeeks.org/express-js-res-send-function/
		}
	});
});

<<<<<<< HEAD
app.listen(portNum, () => {
	console.log(`Log file view running on http://localhost:${portNum}`);
=======
app.listen(port, () => { //Starts the express app and listens for incoming HTTP requests on whichever port we specified, when the server is started the function initiates. Used link geeksforgeeks.org/express-js-app-listen-function/
	console.log(`Log file view running on http://localhost:${port}`); //logs a message to the consolde indicating the server has started 
>>>>>>> 50c97b80e2a4f1687bb561c95a92fc863ae8b25e
});
