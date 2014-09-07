#!/usr/bin/python3

import io
import datetime

global TRENNER
global calTxtPath
calTxtPath = "/home/koebi/scratch/termine.txt"
TRENNER = "================="


def updateTermine():
	with open(calTxtPath, 'rb') as f:
		data = f.read().decode('utf-8')
	t = data.split('\n')

	newdays = []

	# Ersetze jede Zeile mit = vorne durch TRENNER
	for i in range(len(t)):
		if t[i] != "":
			if t[i][0] == "=":
				if t[i] != TRENNER:
					t[i] = TRENNER

	# Finde alle Indizes von Tagen
	for i in range(len(t)):
		if t[i] == TRENNER:
			newdays += [i-1]

	today = datetime.date.today()
	latest = t[newdays[-1]]

	for i in newdays:
		first = t[i]
		firstwd, firstmm, firstyy = first.split("/")
		firstwd, firstdd = firstwd.split()
		firstdd, firstmm, firstyy = int(firstdd), int(firstmm), int(firstyy)
		first = datetime.date(firstyy, firstmm, firstdd)
		if first == today:
			first = i
			break

	old = t[:first]
	t = t[first:]

	deldays = 0
	for i in old:
		if i != "":
			if i[0] == "=":
				deldays += 1

	latestwd, latestmm, latestyy = latest.split("/")
	latestwd, latestdd = latestwd.split()
	latestdd, latestmm, latestyy = int(latestdd), int(latestmm), int(latestyy)
	latest = datetime.date(latestyy, latestmm, latestdd)

	for i in range(deldays):
		newday = latest + datetime.timedelta(i+1)
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

	f = open(calTxtPath, "wt")
	f.write(newdata)
	f.close

def dayToString(wd):
	days = ["Mo", "Di", "Mi", "Do", "Fr", "Sa", "So"]
	return days[wd]

if __name__ == "__main__":
	updateTermine()
