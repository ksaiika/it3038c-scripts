from datetime import datetime

currentTime = datetime.now()
currentTimeA = currentTime.strftime("%H:%M"
 
print('Hello, would you like to know the time? (y/n)')

answer = input()

if answer == 'Y' or 'y':
	print('The current time is '+ currentTimeA)
else:
	time.sleep(3)
	print("Okay, goodbye!")
