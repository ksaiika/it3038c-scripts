from datetime import datetime
import time

print("Hello. Would you like to know the time? (y/n)")

answer = input()

"""Used this website to find the time modules and conversion: https://www.freecodecamp.org/news/how-to-get-the-current-time-in-python-with-datetime/#:~:text=To%20get%20the%20current%20time%20in%20particular%2C%20you%20can%20use,hours%2C%20minutes%2C%20and%20seconds"""

currently = datetime.now()
currentH = currently.strftime("%H")
currentM = currently.strftime("%M")

if answer == "Y" or answer == "y" and int(currentH) < 13:
	print("It is currently " + currentH + ":" + currentM)
elif answer == "Y" or answer == "y" and int(currentH) > 13:
	print("It is currently " + str(int(currentH) - 12) + ":" + currentM)
else:
	print("Okay, goodbye!")
	time.sleep(1)
