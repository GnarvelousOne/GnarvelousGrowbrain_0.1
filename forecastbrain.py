#!/usr/bin/python

# Credit for the LCD interfacing goes to :
#
#  lcd_16x2.py
#  16x2 LCD Test Script
#
# Author : Matt Hawkins
# Date   : 06/04/2015
#
# http://www.raspberrypi-spy.co.uk/
#
# Copyright 2015 Matt Hawkins
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#--------------------------------------

# The wiring for the LCD is as follows:
# 1 : GND
# 2 : 5V
# 3 : Contrast (0-5V)*
# 4 : RS (Register Select)
# 5 : R/W (Read Write)       - GROUND THIS PIN
# 6 : Enable or Strobe
# 7 : Data Bit 0             - NOT USED
# 8 : Data Bit 1             - NOT USED
# 9 : Data Bit 2             - NOT USED
# 10: Data Bit 3             - NOT USED
# 11: Data Bit 4
# 12: Data Bit 5
# 13: Data Bit 6
# 14: Data Bit 7
# 15: LCD Backlight +5V**
# 16: LCD Backlight GND


import RPi.GPIO as GPIO
import time
import requests
import json
import datetime
from dht import dhtRun
import dht
api_key = "3b0d6b5cb7b4d578ecbadefd15973c44"

#these are Louisville, KY coordinates
lat = "38.091349"
lon = "-85.583982"

#url contains Thixton, KY coordinates
url = "https://api.openweathermap.org/data/2.5/onecall?" \
      "lat=38.0996&lon=-85.5631&units=imperial&" \
      "exclude=current,hourly,minutely&" \
      "appid=3b0d6b5cb7b4d578ecbadefd15973c44"


response = requests.get(url)
data = json.loads(response.text)

daily = data["daily"]

timeNow = datetime.datetime.now()
#print(timeNow)

dayTemp = ""
minTemp = ""
maxTemp = ""
nightTemp = ""
eveTemp = ""
mornTemp = ""
dailyHum = ""
dailyWindspeed = ""


# Define GPIO to LCD mapping
LCD_RS = 7
LCD_E  = 8
LCD_D4 = 25
LCD_D5 = 24
LCD_D6 = 23
LCD_D7 = 18


# Define some device constants
LCD_WIDTH = 16    # Maximum characters per line
LCD_CHR = True
LCD_CMD = False

LCD_LINE_1 = 0x80 # LCD RAM address for the 1st line
LCD_LINE_2 = 0xC0 # LCD RAM address for the 2nd line

# Timing constants
E_PULSE = 0.0005
E_DELAY = 0.0005

def main():
    # Main program block
    

    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)       # Use BCM GPIO numbers
    GPIO.setup(LCD_E, GPIO.OUT)  # E
    GPIO.setup(LCD_RS, GPIO.OUT) # RS
    GPIO.setup(LCD_D4, GPIO.OUT) # DB4
    GPIO.setup(LCD_D5, GPIO.OUT) # DB5
    GPIO.setup(LCD_D6, GPIO.OUT) # DB6
    GPIO.setup(LCD_D7, GPIO.OUT) # DB7
    GPIO.setup(14, GPIO.OUT)     # for the relay
    GPIO.output(14, False)       # starts relay in off mode


    # Initialise display
    #lcd_init()

    with open('ForecastLog.txt', 'a') as forecastLog:
        forecastLog.write("\n"+"Forecast taken on "+str(timeNow.strftime('%b %d at %H:%M'))+":")
        forecastLog.close()
        
    print("")
    print("Forecast taken on "+str(timeNow.strftime('%b %d at %H:%M'))+":")
    print("")
    
    for i in range(len(daily)):
        print(
            datetime.datetime.fromtimestamp(
                int(daily[i]['dt'])
            ).strftime('%A %m/%d')
        )
        print("Min temp: " + str(daily[i]['temp']['min']))
        with open('ForecastLog.txt', 'a') as forecastLog:
            forecastLog.write(datetime.datetime.fromtimestamp(int(daily[i]['dt'])).strftime('%A %m/%d') +
                              ": Min temp: " + str(daily[i]['temp']['min']) + "\n")
        print("Max temp: " + str(daily[i]['temp']['max']))
        with open('ForecastLog.txt', 'a') as forecastLog:
            forecastLog.write(datetime.datetime.fromtimestamp(int(daily[i]['dt'])).strftime('%A %m/%d') +
                              ": Max temp: " + str(daily[i]['temp']['max']) + "\n")
        print("Morning temp: " + str(daily[i]['temp']['morn']))
        with open('ForecastLog.txt', 'a') as forecastLog:
            forecastLog.write(datetime.datetime.fromtimestamp(int(daily[i]['dt'])).strftime('%A %m/%d') +
                              ": Morning temp: " + str(daily[i]['temp']['morn']) + "\n")        
        print("Day temp: " + str(daily[i]['temp']['day']))
        with open('ForecastLog.txt', 'a') as forecastLog:
            forecastLog.write(datetime.datetime.fromtimestamp(int(daily[i]['dt'])).strftime('%A %m/%d') +
                              ": Day temp: " + str(daily[i]['temp']['day']) + "\n")
        print("Evening temp: " + str(daily[i]['temp']['eve']))
        with open('ForecastLog.txt', 'a') as forecastLog:
            forecastLog.write(datetime.datetime.fromtimestamp(int(daily[i]['dt'])).strftime('%A %m/%d') +
                              ": Evening temp: " + str(daily[i]['temp']['eve']) + "\n")
        print("Night temp: " + str(daily[i]['temp']['night']))
        with open('ForecastLog.txt', 'a') as forecastLog:
            forecastLog.write(datetime.datetime.fromtimestamp(int(daily[i]['dt'])).strftime('%A %m/%d') +
                              ": Night temp: " + str(daily[i]['temp']['night']) + "\n")
        print("Humidity: " + str(daily[i]['humidity']))
        with open('ForecastLog.txt', 'a') as forecastLog:
            forecastLog.write(datetime.datetime.fromtimestamp(int(daily[i]['dt'])).strftime('%A %m/%d') + ": Humidity: " + str(daily[i]['humidity']) + "\n")
        print("Windspeed: " + str(daily[i]['wind_speed']))
        with open('ForecastLog.txt', 'a') as forecastLog:
            forecastLog.write(datetime.datetime.fromtimestamp(int(daily[i]['dt'])).strftime('%A %m/%d') + ": Windspeed: " + str(daily[i]['wind_speed']) + "\n")
        with open('ForecastLog.txt', 'a') as forecastLog:
            forecastLog.write("\n")

        #print("Conditions: " + str(daily[i]['weather'][0:1][1:2]) + ", " + str(daily[i]['weather'][1:2]))
        print("")

    for i in range(len(daily)):
        if daily[i]['temp']['min'] < 45:
            print("--- LOW TEMP ALERT --- " + str(datetime.datetime.fromtimestamp(int(daily[i]['dt'])).strftime('%A %m/%d'))
                  + " --- " + str(daily[i]['temp']['min']) + " deg F")
            with open('ForecastLog.txt', 'a') as forecastLog:
                forecastLog.write(datetime.datetime.fromtimestamp(int(daily[i]['dt'])).strftime('%A %m/%d')
                                  + "--- LOW TEMP ALERT ---" + str(daily[i]['temp']['min']) + "\n")
                
        if daily[i]['temp']['max'] > 82:
            print("--- HIGH TEMP ALERT --- " + str(datetime.datetime.fromtimestamp(int(daily[i]['dt'])).strftime('%A %m/%d'))
                  + " --- " + str(daily[i]['temp']['max']) + " deg F")
            with open('ForecastLog.txt', 'a') as forecastLog:
                forecastLog.write(datetime.datetime.fromtimestamp(int(daily[i]['dt'])).strftime('%A %m/%d')
                                  + "--- HIGH TEMP ALERT ---" + str(daily[i]['temp']['max']) + "\n")
                
        if daily[i]['humidity'] > 60:
            print("--- HUMIDITY ALERT --- " + str(datetime.datetime.fromtimestamp(int(daily[i]['dt'])).strftime('%A %m/%d'))
                  + " --- " + str(daily[i]['humidity']) + " % rH")
            with open('ForecastLog.txt', 'a') as forecastLog:
                forecastLog.write(datetime.datetime.fromtimestamp(int(daily[i]['dt'])).strftime('%A %m/%d')
                                  + "--- HUMIDITY ALERT ---" + str(daily[i]['humidity']) + "\n")

        
    
    with open('ForecastLog.txt', 'a') as forecastLog:
        forecastLog.write("\n")
        forecastLog.write("\n")
    print("")
    
    #while datetime.datetime.now().minute not in {0,15,30,45}:
     #   time.sleep(1)
        
    #def task():
    #dhtRun()
    
    #task()
    
    #while True:
     #   time.sleep(60*15)
      #  task()
'''
  # Send some test
  lcd_string("Seconds ON: ",LCD_LINE_1)
  x = input(' ')
  lcd_string("Seconds OFF: ",LCD_LINE_2)
  y = input(' ')
  time.sleep(1) # 3 second delay

  # Send some text
  lcd_string("ON: " +str(x), "OFF: " +str(y),LCD_LINE_1)
  lcd_string("Ctrl-C to exit",LCD_LINE_2)
  time.sleep(y)

  while True:   
    GPIO.output(14, True)
    time.sleep(x)
    GPIO.output(14, False)
    time.sleep(y)
'''

def lcd_init():
  # Initialise display
  lcd_byte(0x33,LCD_CMD) # 110011 Initialise
  lcd_byte(0x32,LCD_CMD) # 110010 Initialise
  lcd_byte(0x06,LCD_CMD) # 000110 Cursor move direction
  lcd_byte(0x0C,LCD_CMD) # 001100 Display On,Cursor Off, Blink Off
  lcd_byte(0x28,LCD_CMD) # 101000 Data length, number of lines, font size
  lcd_byte(0x01,LCD_CMD) # 000001 Clear display
  time.sleep(E_DELAY)

def lcd_byte(bits, mode):
  # Send byte to data pins
  # bits = data
  # mode = True  for character
  #        False for command

  GPIO.setmode(GPIO.BCM)
  GPIO.setup(LCD_E, GPIO.OUT)  # E
  GPIO.setup(LCD_RS, GPIO.OUT) # RS
  GPIO.setup(LCD_D4, GPIO.OUT) # DB4
  GPIO.setup(LCD_D5, GPIO.OUT) # DB5
  GPIO.setup(LCD_D6, GPIO.OUT) # DB6
  GPIO.setup(LCD_D7, GPIO.OUT) # DB7
  GPIO.setup(14, GPIO.OUT)     # for the relay
  GPIO.output(14, False)       # starts relay in off mode
  GPIO.output(LCD_RS, mode) # RS
  # High bits
  GPIO.output(LCD_D4, False)
  GPIO.output(LCD_D5, False)
  GPIO.output(LCD_D6, False)
  GPIO.output(LCD_D7, False)
  if bits&0x10==0x10:
    GPIO.output(LCD_D4, True)
  if bits&0x20==0x20:
    GPIO.output(LCD_D5, True)
  if bits&0x40==0x40:
    GPIO.output(LCD_D6, True)
  if bits&0x80==0x80:
    GPIO.output(LCD_D7, True)

  # Toggle 'Enable' pin
  lcd_toggle_enable()

  # Low bits
  GPIO.output(LCD_D4, False)
  GPIO.output(LCD_D5, False)
  GPIO.output(LCD_D6, False)
  GPIO.output(LCD_D7, False)
  if bits&0x01==0x01:
    GPIO.output(LCD_D4, True)
  if bits&0x02==0x02:
    GPIO.output(LCD_D5, True)
  if bits&0x04==0x04:
    GPIO.output(LCD_D6, True)
  if bits&0x08==0x08:
    GPIO.output(LCD_D7, True)

  # Toggle 'Enable' pin
  lcd_toggle_enable()

def lcd_toggle_enable():
  # Toggle enable
  time.sleep(E_DELAY)
  GPIO.output(LCD_E, True)
  time.sleep(E_PULSE)
  GPIO.output(LCD_E, False)
  time.sleep(E_DELAY)

def lcd_string(message,line):
  # Send string to display




  message = message.ljust(LCD_WIDTH," ")

  lcd_byte(line, LCD_CMD)

  for i in range(LCD_WIDTH):
    lcd_byte(ord(message[i]),LCD_CHR)



if __name__ == '__main__':

  try:
    main()
  except KeyboardInterrupt:
    pass
  finally:
    #lcd_byte(0x01, LCD_CMD)
    #lcd_string("",LCD_LINE_1)
    #lcd_string("",LCD_LINE_2)
    GPIO.cleanup()
