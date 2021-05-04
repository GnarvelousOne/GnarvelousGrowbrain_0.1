#! /usr/bin/python

displaytemp_f = 0

def dhtRun():
    import config
    import I2C_LCD_driver
    import openpyxl
    import time
    import datetime
    import board
    import adafruit_dht
    import RPi.GPIO as GPIO
    from alert import alert_high_temp_send, alert_low_temp_send, alert_high_hum_send

    timeNow = datetime.datetime.now()
    
    
    # Initial the dht device, with data pin connected to:

    dhtDevice = adafruit_dht.DHT11(board.D4)

    # you can pass DHT22 use_pulseio=False if you wouldn't like to use pulseio.
    # This may be necessary on a Linux single board computer like the Raspberry Pi,
    # but it will not work in CircuitPython.
    # dhtDevice = adafruit_dht.DHT22(board.D18, use_pulseio=False)


    # take the average of 3 readings, adjust for any errors.  It takes 2 seconds between readings for the sensor to update
    tempClist = []
    tempFlist = []
    humlist = []  


    try:
        temperature_c = dhtDevice.temperature
        tempClist.append(temperature_c)
    except:
        pass
    try:
        temperature_c = dhtDevice.temperature
        temperature_f = temperature_c * (9 / 5) + 32
        tempFlist.append(temperature_f)
    except:
        pass
    try:
        humidity = dhtDevice.humidity
        humlist.append(humidity)
    except:
        pass

    time.sleep(2)

    try:
        temperature_c = dhtDevice.temperature
        tempClist.append(temperature_c)
    except:
        pass
    try:
        temperature_c = dhtDevice.temperature
        temperature_f = temperature_c * (9 / 5) + 32
        tempFlist.append(temperature_f)
    except:
        pass
    try:
        humidity = dhtDevice.humidity
        humlist.append(humidity)
    except:
        pass

    time.sleep(2)

    try:
        temperature_c = dhtDevice.temperature
        tempClist.append(temperature_c)
    except:
        pass
    try:
        temperature_c = dhtDevice.temperature
        temperature_f = temperature_c * (9 / 5) + 32
        tempFlist.append(temperature_f)
    except:
        pass
    try:
        humidity = dhtDevice.humidity
        humlist.append(humidity)
    except:
        pass

    time.sleep(2)

    print(tempFlist)
    print(tempClist)
    print(humlist)

    j = 0
    for i in tempClist:
        try:
            j += i
        except:
            pass

    k = 0
    for i in tempFlist:
        try:
            k += i
        except:
            pass

    l = 0
    for i in humlist:
        try:
            l += i
        except:
            pass

    try:
        displaytemp_c = (j/len(tempClist))
    except:
        displaytemp_c = 0

    try:
        displaytemp_f = (k/len(tempFlist))
    except:
        displaytemp_f = 0

    try:
        if l < humidity*3:
            displayhum = humlist[-1]
        else:
            displayhum = (l/len(humlist))
    except:
        displayhum = humlist[-1]

    # Uncomment to check the math
    #print(k)
    #print(j)
    #print(l)

    if type(displaytemp_f) == int or type(displaytemp_f) == float:
        displaytemp_f = round(displaytemp_f)
    if type(displaytemp_c) == int or type(displaytemp_c) == float:
        displaytemp_c = round(displaytemp_c)
    if type(displayhum) == int or type(displayhum) == float:
        displayhum = round(displayhum)
        
    # set the high and low temp and hum alerts to trigger sending an email alert:
    hightemp = 73
    lowtemp = 45
    highhum = 75
    
    if displaytemp_f == hightemp or displaytemp_f > hightemp:
        alert_high_temp_send()
    if displaytemp_f == lowtemp or displaytemp_f < lowtemp:
        alert_low_temp_send()
    if displayhum == highhum or displayhum > highhum:
        alert_high_hum_send()

    print(
        "DHT reading on " + str(timeNow.strftime('%A %m/%d %H:%M %p')) + ": "+"Temp: {:.1f} F / {:.1f} C    Humidity: {}% ".format(
            displaytemp_f, displaytemp_c, displayhum)
    )

    with open('ForecastLog.txt', 'a') as forecastLog:
                forecastLog.write("DHT reading on " + str(timeNow.strftime('%A %m/%d %H:%M %p')) + ": " + "Temp: {:.1f} F / {:.1f} C    Humidity: {}% ".format(
            displaytemp_f, displaytemp_c, displayhum)+"\n")
                    
    wb = openpyxl.load_workbook('dhtdata.xlsx')
    ws = wb.active

    row = [[str(timeNow.strftime('%m/%d %H:%M')), displaytemp_f, displayhum]]

    for data in row:
        if displaytemp_f == 0:
            pass
        else:
            ws.append(data)


    wb.save('dhtdata.xlsx')
    '''
    # Use this if you have a 2004 LCD for display:
    mylcd = I2C_LCD_driver.lcd()
    mylcd.lcd_display_string(str(timeNow.strftime('%b %d at %H:%M')), 1)
    mylcd.lcd_display_string("{:.1f} F / {}% rH".format(
            displaytemp_f, displayhum), 2)
    mylcd.lcd_display_string("Script: /dhtbrain.py", 3)
    mylcd.lcd_display_string("Data: dhtdata.xlsx", 4)
    '''

    time.sleep(2.0)
    dhtDevice.exit()
    
    # this checks if all 3 measurements failed. If so, the module runs again, up to 5 times.
    # if it screws up more than 5 times in such a short period of time consider replacing sensor
    trycounter = 0
    if type(displayhum) == int or type(displayhum) == float:
        pass
    else:
        trycounter += 1
        if trycounter < 5:
            dhtRun()
        else:
            pass
        
def gettemp():
    blob = 0
    blob == dhtRun.displaytemp_f
    return blob
    
    '''    
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


    lcd_byte(0x01, LCD_CMD)
    '''
    '''
    lcd_string(str(timeNow.strftime('%b %d at %H:%M')),LCD_LINE_1)
    lcd_string("{:.1f} F / {}% rH".format(
            displaytemp_f, displayhum),LCD_LINE_2)'''

        
