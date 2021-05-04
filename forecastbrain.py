#!/usr/bin/python

import ezgmail
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
recipientList = ['stephenmparvin@gmail.com']
timeNow = datetime.datetime.now()

def emailtext():
  emailstring = ""
  for i in range(len(daily)):
    emailstring = emailstring+(datetime.datetime.fromtimestamp(int(daily[i]['dt'])).strftime('%A %m/%d')+"\n")
    emailstring = emailstring+("Max temp: " + str(daily[i]['temp']['max'])+"\n")
    emailstring = emailstring+("Min temp: " + str(daily[i]['temp']['min'])+"\n")
    emailstring = emailstring+("Morning temp: " + str(daily[i]['temp']['morn'])+"\n")
    emailstring = emailstring+("Day temp: " + str(daily[i]['temp']['day'])+"\n")
    emailstring = emailstring+("Evening temp: " + str(daily[i]['temp']['eve'])+"\n")
    emailstring = emailstring+("Night temp: " + str(daily[i]['temp']['night'])+"\n")
    emailstring = emailstring+("Humidity: " + str(daily[i]['humidity'])+"\n")
    emailstring = emailstring+("Windspeed: " + str(daily[i]['wind_speed'])+"\n\n")
  return emailstring

def main():
    # Main program block
    
    timeNow = datetime.datetime.now()
    
    with open('ForecastLog.txt', 'a') as forecastLog:
        forecastLog.write("\n"+"Forecast taken on "+str(timeNow.strftime('%b %d at %H:%M'))+":"+"\n\n")
        forecastLog.close()
        
    print("")
    print("Forecast taken on "+str(timeNow.strftime('%b %d at %H:%M'))+":")
    print("")
    
    for i in range(len(daily)):
        print(datetime.datetime.fromtimestamp(int(daily[i]['dt'])).strftime('%A %m/%d'))
        with open('ForecastLog.txt', 'a') as forecastLog:
            forecastLog.write(datetime.datetime.fromtimestamp(int(daily[i]['dt'])).strftime('%A %m/%d')+"\n")
        print("Max temp: " + str(daily[i]['temp']['max']))
        with open('ForecastLog.txt', 'a') as forecastLog:
            forecastLog.write("Max temp: " + str(daily[i]['temp']['max']) + "\n")
        print("Min temp: " + str(daily[i]['temp']['min']))
        with open('ForecastLog.txt', 'a') as forecastLog:
            forecastLog.write("Min temp: " + str(daily[i]['temp']['min']) + "\n")
        print("Morning temp: " + str(daily[i]['temp']['morn']))
        with open('ForecastLog.txt', 'a') as forecastLog:
            forecastLog.write("Morning temp: " + str(daily[i]['temp']['morn']) + "\n")        
        print("Day temp: " + str(daily[i]['temp']['day']))
        with open('ForecastLog.txt', 'a') as forecastLog:
            forecastLog.write("Day temp: " + str(daily[i]['temp']['day']) + "\n")
        print("Evening temp: " + str(daily[i]['temp']['eve']))
        with open('ForecastLog.txt', 'a') as forecastLog:
            forecastLog.write("Evening temp: " + str(daily[i]['temp']['eve']) + "\n")
        print("Night temp: " + str(daily[i]['temp']['night']))
        with open('ForecastLog.txt', 'a') as forecastLog:
            forecastLog.write("Night temp: " + str(daily[i]['temp']['night']) + "\n")
        print("Humidity: " + str(daily[i]['humidity']))
        with open('ForecastLog.txt', 'a') as forecastLog:
            forecastLog.write("Humidity: " + str(daily[i]['humidity']) + "\n")
        print("Windspeed: " + str(daily[i]['wind_speed']))
        with open('ForecastLog.txt', 'a') as forecastLog:
            forecastLog.write("Windspeed: " + str(daily[i]['wind_speed']) + "\n")
        with open('ForecastLog.txt', 'a') as forecastLog:
            forecastLog.write("\n")
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
	
    recipientList = ['stephenmparvin@gmail.com']
	
    for j in recipientList:
      ezgmail.send(j,'Forecast Thixton, KY', emailtext())
      

if __name__ == '__main__':

  try:
    main()
  except KeyboardInterrupt:
    pass
