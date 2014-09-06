#!/usr/bin/python3

import io
import datetime

global TRENNER
global calTxtPath
calTxtPath = "/home/koebi/scratch/termine.txt"
TRENNER = "================="


def updateCalendar():
	data = io.open(calTxtPath, 'wrb').read().decode('utf-8')
	t = data.split('\n')

	newdays = []

	# Ersetze jede Zeile mit = vorne durch TRENNER
	for i in range(len(t)):
		if t[i][0] == "=":
			if t[i] != TRENNER:
				t[i] = TRENNER

	for i in range(len(t)):
		if t[i] == TRENNER:
			newdays += [i]

	first = t[0]
	firstwd, firstmm, firstyy = first.split("/")
	firstwd, firstdd = firstwd.split()
	firstdd, firstmm, firstyy = int(firstdd), int(firstmm), int(firstyy)
	first = datetime.date(firstyy, firstmm, firstdd)

	today = datetime.date.today()

	if first != today:
		

	
