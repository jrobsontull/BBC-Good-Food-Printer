from __future__ import print_function
from Adafruit_Thermal import *
from datetime import datetime

printer = Adafruit_Thermal("/dev/serial0", 19200, timeout=5)

def wrap_print(toPrint):
	if (len(toPrint) > 32):
		wrappedText = []
		temp = ""
		for word in toPrint.split():
			if (len(temp + word) >= 32):
				wrappedText.append(temp)
				temp = (word + " ")
			else:
				temp = (temp + word + " ")

		wrappedText.append(temp)

		for line in wrappedText:
			printer.print(line + "\n")
	else:
		printer.print(toPrint)

def print_header():
	printer.boldOn()
	printer.setSize('S')
	printer.inverseOn()
	printer.justify('C')

	currentDay = datetime.now()
	currentDayFormatted = currentDay.strftime('%A %d %B %Y')
	while len(currentDayFormatted) < 32:
		currentDayFormatted = " " + currentDayFormatted
		if (len(currentDayFormatted) != 32):
			currentDayFormatted = currentDayFormatted + " "
	printer.print(currentDayFormatted + "\n")

	printer.print("      Printed at: " + currentDay.strftime('%I:%M %p      '))

	printer.feed(2)