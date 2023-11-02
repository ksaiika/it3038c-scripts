My project uses NodeJS to take the output of a log file and show it on a web page.

Here is how to run it:
1) Boot up your linux VM
2) Right-click > Open Terminal
3) Save the logoutput.js and log.log files to your folder where you will be calling the functions from
4) Make sure NodeJS is initialized(run 'npm init -y' in the folder where your files are) and the files are in the same folder as the two previous files (you will see them listed in this project file as well)
5) Install express app (run 'npm install express')
6) Start the server by running 'node logoutput.js', you should see 'Log file view running on http://localhost:3000' indicating it has started
7) Open an html browser and navigate to 'http://localhost:3000' and you should see the results of the log.log file which should be two lines from 11/1 and 10/30 regarding system kernal information
8) You can stop the server by running ctrl + c in the terminal
9) Ta-Da!
