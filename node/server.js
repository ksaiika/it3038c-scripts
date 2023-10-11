var http = require("http");
var fs = require("fs");
var os = require("os");
var ip = require('ip');

http.createServer(function(req, res){

	if (req.url === "/") {
		fs.readFile("./Public/index.html", "UTF-8", function(err, body){
		res.writeHead(200, {"Content-Type": "text/html"});
		res.end(body);
	});
}
	else if(req.url.match("/sysinfo")) {
		myHostName=os.hostname();
		sUptime = os.uptime();
		sUptimeD = Math.floor(sUptime / (3600 * 24));
		sUptimeH = Math.floor((sUptime % (3600 *24)));
		sUptimeM = Math.floor((sUptime % 3600) / 60);
		sUptimeS = Math.floor((sUptime % 60));
		totalMem = (os.totalmem() / 1024 / 1024).toFixed(2);
		freeMem = (os.freemem() / 1024 / 1024).toFixed(2);
		cpus = os.cpus().length
		html=`
		<!DOCTYPE html>
		<html>
			<head>
				<title>Node JS Response</title>
			</head>
			<body>
				<p>Hostname: ${myHostName}</p>
				<p>IP: ${ip.address()}</p>
				<p>Server Uptime: Days: ${sUptimeD}, Hours: ${sUptimeH}, Minutes: ${sUptimeM}, Seconds: ${sUptimeS}</p>
				<p>Total Memory: ${totalMem} MB</p>
				<p>Free Memory: ${freeMem} MB</p>
				<p>Number of CPUs: ${cpus}</p>
			</body>
		</html>`
		res.writeHead(200, {"Content-Type": "text/html"});
		res.end(html);
	}
	else {
		res.writeHead(404, {"Content-Type": "text/plain"});
		res.end(`404 File Not Found at ${req.url}`);
	}
}).listen(3000);

console.log("Server listening on port 3000");
