#!/usr/bin/python3

import io
from icalendar import Calendar, Event
from datetime import datetime

global TRENNER
global calTxtPath, calIcsPath
calTxtPath = "/home/koebi/scratch/termine.txt"
calIcsPath = "/home/koebi/scratch/termine.ics"
TRENNER= "=================="

def setUpCalendar(cal):
	parse

def parseTermine(cal):
	data = io.open(calTxtPath, 'rb').read().decode('utf-8')
	t = data.split('\n')

	newdays = []
	termine = []
	current = ""

	for i in range(len(t)):
		if t[i] == TRENNER:
			newdays += [i-1]

	for i in range(len(newdays)):
		current = t[newdays[i]]
		if i == len(newdays)-1:
			termine = t[newdays[i]+2:]
		else:
			termine = t[newdays[i]+2:newdays[i+1]]
		calendarAdd(current, termine, cal)

	f = open(calIcsPath, 'wb')
	f.write(cal.to_ical())
	f.close()

def calendarAdd(cur, term, cal):
	wd, mm, yy = cur.split("/")
	wd, dd = wd.split()

	dd, mm, yy = int(dd), int(mm), int(yy)

	time = ''
	ev = ''
	begin, end = '', ''

	for i in term:
		bh, bm, eh, em = '0', '0', '0', '0'
		event = Event()
		if i == '':
			continue
		else:
			time, ev = i.split(' ', 1)

		if '-' in time:
			begin, end = time.split('-')
			if ":" in begin:
				bh, bm = begin.split(":")
			else:
				bh = begin
			if ":" in end:
				eh, em = end.split(":")
			else:
				eh = end
		else:
			if ":" in time:
				bh, bm = time.split(":")
			else:
				bh = time

		if bh == '!!!':
			begin = datetime(yy, mm, dd)
		else:
			bh, bm, eh, em = int(bh), int(bm), int(eh), int(em)
			begin = datetime(yy, mm, dd, bh, bm)

		event.add("summary", ev)
		event.add("dtstart", begin)
		if eh != "0":
			end = datetime(yy, mm, dd, eh, em)
			event.add("dtend", end)
		cal.add_component(event)

if __name__ == "__main__":
	cal = Calendar()
	parseTermine(cal)
