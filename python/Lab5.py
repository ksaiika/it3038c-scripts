#script to take a birthday date input and calculate how many seconds old the user is 

from datetime import datetime
import time

startTime = time.time()
scriptAge = int(time.time()-startTime)

#Prints the question to the user for their birthday in mm/dd/yyyy format
print('Hi, when is your birthday?? (Please answer in this format: mm/dd/yyyy)')

#receives the user's input
bday=input()

#try will check if the user's input is able to be formatted as mm/dd/yyyy
try:
#strptime will parse a string that has a date/time and converts it to a datettime object which we can then use for our operation below
  formattedBirthday = datetime.strptime(bday, '%m/%d/%Y')
#except will handle an exception where a user is inputting an incorrect date/value when asked for their birthday
except Exception as incorrectFormat:
  print('Invalid date format. Use mm/dd/yyyy')
#else means the try was successful and moves us forward with the code
else:
#datetime.now will pull the datetime object which is the current date/time based on the local time zone
  today=datetime.now()
 
#subtracts two datetime objects
  difference = today - formattedBirthday

#.total_seconds is part of timedelta objects which represents a duration of time and total_seconds allows us to get a total duration in seconds
  seconds=difference.total_seconds()


  print('Wow, you are ' + str(int(seconds)) + ' seconds old! I am only ' + str(scriptAge) + ' seconds old.')
