#!/usr/bin/python3

import io
import datetime

global TRENNER
global calTxtPath
calTxtPath = "/home/koebi/scratch/termine.txt"
TRENNER = "================="


def updateCalendar():
	f = io.open(calTxtPath, 'wrb')
	data = f.read().decode('utf-8')
	t = data.split('\n')

	newdays = []

	# Ersetze jede Zeile mit = vorne durch TRENNER
	for i in range(len(t)):
		if t[i][0] == "=":
			if t[i] != TRENNER:
				t[i] = TRENNER

	# Finde alle Indizes von Tagen
	for i in range(len(t)):
		if t[i] == TRENNER:
			newdays += [i-1]

	today = datetime.date.today()

	for i in newdays:
		first = t[0]
		firstwd, firstmm, firstyy = first.split("/")
		firstwd, firstdd = firstwd.split()
		firstdd, firstmm, firstyy = int(firstdd), int(firstmm), int(firstyy)
		first = datetime.date(firstyy, firstmm, firstdd)
		if first == today:
			first = i
			break

	old = t[:i]
	t = t[i:]

	deldays = 0
	for i in old:
		if i[0] == "=":
			deldays += 1

	for i in range(deldays):
		newday = today + datetime+timedelta(i+1)
		wd = dayToString(newday.weekday())
		dd = str(newday.day) if len(str(newday.day)) == 2 else '0' + str(newday.day)
		mm = str(newday.month) if len(str(newday.month)) == 2 else '0' + str(newday.month)
		yy = str(newday.year)
		newline1 = wd + " " + dd + "/" + mm + "/" + yy
		newline2 = TRENNER
		newline3 = ""
		t += [newline1, newline2, newline3]

	newdata = ""
	for i in t:
		newdata = newdata + i + "\n"

	newdata = newdata[:-2]

	f.write(newdata)
	f.close

def dayToString(wd):
	days = ["Mo", "Di", "Mi", "Do", "Fr", "Sa", "So"]
	return days[wd]
