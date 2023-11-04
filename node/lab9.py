## In sep terminal, start server with 'node api' then run python file with 'python lab9.py' in another terminal for output.

import json #imports json module, provides methods to work with JSON data
import requests #imports requests module, makes HTTP requests to work w/ web services and APIs


try: #start of exception handling
	response = requests.get("http://localhost:3000") #sends HTTP get request
	response.raise_for_status() #checks if HTTP request returns an error status code and raises exception

	widget_data = response.json() #goes through response as jSON and loads into variable widget_data

	for i, widget in enumerate(widget_data, start=1): #starts for loop, goes through widget_data which holds JSON data and i keeps track of index starting at 1 while widget is linked to each object
		name = widget.get("name", "Widget{}".format(i)) #gets name data or default value if not present
		color = widget.get("color", "Unknown") #gets color data or default value if not present
		print("Widget{} is {}.".format(i, color)) #prints name and color using the .format for string formatting and combines them into readable format

except requests.exceptions.RequestException as err: #starts exception handling block for exceptions raised during the http requests, err dislays error messages
	print("Error: {}".format(err)) #line executes if there is an exception in HTTP requests and prints error message

except json.JSONDecodeError as err: #starts exception handling for exceptions raised during JSON decoding, JSON error will show if there is an exception
	print("Error parsing JSON: {}".format(err)) #line executes if JSON Decode error is present and prints error message

