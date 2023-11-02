const express = require("express");
const fs = require("fs");

const app = express();
const port = 3000;

const logFilePath = "/home/cechuser/it3038c-scripts/project2/log.log";

app.get("/", (req, res) => {

	fs.readFile(logFilePath, "utf8", (err, data) => {
		if (err) {
			res.status(500).send("Error");
		}	else {
			const logHTML = `<html><head><title>Log File Viewer</title></head><body><pre>${data}</pre></body></html>`;
			res.send(logHTML);
		}
	});
});

app.listen(port, () => {
	console.log(`Log file view running on http://localhost:${port}`);
});
