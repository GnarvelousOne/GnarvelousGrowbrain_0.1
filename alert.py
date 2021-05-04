#!/usr/bin/python3

import ezgmail
import time
import datetime
from dht import dhtRun
from quickstart import dhtUpload

def alert_high_temp_send():
	
	timeNow = datetime.datetime.now()
	recipientList = ['stephenmparvin@gmail.com']
	
	print("Sending High Temp Alert!!!")
	
	for i in recipientList:
		ezgmail.send(i,'HIGH TEMP ALERT','ALERT:  On ' + 
		str(timeNow.strftime('%A %m/%d %H:%M %p')) + 
		', the ambient temperature in the JM Nursery is ABOVE the safe level.  '+
		'\n\n'+'This email was sent automatically by The Gnarvelous Growbrain')


def alert_low_temp_send():
	
	timeNow = datetime.datetime.now()
	recipientList = ['stephenmparvin@gmail.com']
	
	print("Sending Low Temp Alert!!!")
	
	for i in recipientList:
		ezgmail.send(i,'LOW TEMP ALERT','ALERT:  On ' + 
		str(timeNow.strftime('%A %m/%d %H:%M %p')) + 
		', the ambient temperature in the JM Nursery is BELOW the safe level.  '+
		'\n\n'+'This email was sent automatically by The Gnarvelous Growbrain')

def alert_high_hum_send():
	
	timeNow = datetime.datetime.now()
	recipientList = ['stephenmparvin@gmail.com']
	
	print("Sending High Humidity Alert!!!")
	
	for i in recipientList:
		ezgmail.send(i,'HIGH HUMIDITY ALERT','ALERT:  On ' + 
		str(timeNow.strftime('%A %m/%d %H:%M %p')) + 
		', the relative humidity in the JM Nursery is ABOVE the safe level.  '+
		'\n\n'+'This email was sent automatically by The Gnarvelous Growbrain')

# uncomment to test code:
#alert_high_temp_send()
