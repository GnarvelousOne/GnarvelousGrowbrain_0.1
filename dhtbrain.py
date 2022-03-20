#!/usr/bin/python

import RPi.GPIO as GPIO
import time
import datetime
from dht import dhtRun
#from quickstart import dhtUpload

def main():
    # Main program block
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)       # Use BCM GPIO numbers

    # Get the temperature and humidity from dht
    #dhtRun()
    data = dhtRun()
    print(f'data from dhtbrain: {data}')
    
    # Upload the newest version to Google Drive
    #dhtUpload()
    
if __name__ == '__main__':

  try:
    main()
  except KeyboardInterrupt:
    pass
  finally:
    GPIO.cleanup()
