from datetime import datetime
import time

print("Hello. Would you like to know the time? (y/n)")

answer = input

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
