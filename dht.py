#! /usr/bin/python

# Variable will be used later to check for errors.
global try_counter
try_counter = 0

def dhtRun():
    #import ezgmail
    #import I2C_LCD_driver
    #import openpyxl
    import time
    import datetime
    import board
    import adafruit_dht
    import RPi.GPIO as GPIO
    import sqlite3

    # get the current time
    timeNow = datetime.datetime.now()

    # set the high and low temp and hum alerts
    # to trigger sending an email alert:
    hightemp = 78
    lowtemp = 45
    highhum = 70
    
    # email addresses to send alert warnings
    recipientList = ['youremailaddress@email.com']
    
    # Initial the dht device, with data pin connected to:
    dhtDevice = adafruit_dht.DHT11(board.D4)

    # you can pass DHT22 use_pulseio=False if you wouldn't like to use pulseio.
    # This may be necessary on a Linux single board computer like the Raspberry Pi,
    # but it will not work in CircuitPython.
    # dhtDevice = adafruit_dht.DHT22(board.D18, use_pulseio=False)

    # make the lists to hold the readings
    temp_C_list = []
    temp_F_list = []
    humidity_list = []  

    # Now take the average of 3 DHT readings, and adjust for any errors.
    # Add each reading to its list.  
    # Sleep for 2.5 seconds inbetween readings because it takes 2 seconds
    # for the sensor to take a new reading.
    # The DHT measures two things: temp in celsius and relative humidity,
    # so we will convert C to F mathematically
    for i in range(3):
        try:
            temperature_c = dhtDevice.temperature
            temp_C_list.append(temperature_c)
        except:
            pass
            
        try:
            temperature_f = temperature_c * (9 / 5) + 32
            temp_F_list.append(temperature_f)
        except:
            pass
            
        try:
            humidity = dhtDevice.humidity
            humidity_list.append(humidity)
        except:
            pass

        time.sleep(2.5)

    # Add together the 3 readings so we can take the average.
    temp_C_sum = 0
    for i in temp_C_list:
        try:
            temp_C_sum += i
        except:
            pass

    temp_F_sum = 0
    for i in temp_F_list:
        try:
            temp_F_sum += i
        except:
            pass

    humidity_sum = 0
    for i in humidity_list:
        try:
            humidity_sum += i
        except:
            pass

    # Take average, unless we have non-integer readings due to an error.
    # In that case, return zero.
    try:
        displaytemp_c = (temp_C_sum/len(temp_C_list))
    except:
        displaytemp_c = 0

    try:
        displaytemp_f = (temp_F_sum/len(temp_F_list))
    except:
        displaytemp_f = 0
        
    # If there is an error, the DHT returns a Nonetype for humidity, so 
    # work it different than the temp reading.
    try:
        if humidity_sum < humidity*3:
            displayhum = humidity_list[-1]
        else:
            displayhum = (humidity_sum/len(humidity_list))
    except:
        displayhum = humidity_list[-1]
        
    # Sometimes the averaging results in repeating decimals, so round off.
    if type(displaytemp_f) == int or type(displaytemp_f) == float:
        displaytemp_f = round(displaytemp_f)
    if type(displaytemp_c) == int or type(displaytemp_c) == float:
        displaytemp_c = round(displaytemp_c)
    if type(displayhum) == int or type(displayhum) == float:
        displayhum = round(displayhum)
    
    # Prepare results to be returned in a list.
    results = []
    results.append(displaytemp_c)
    results.append(displaytemp_f)
    results.append(displayhum)

    # Display the results.
    print(
        "DHT reading on " + str(timeNow.strftime('%A %m/%d %H:%M %p')) +
         ": "+"Temp: {:.1f} F / {:.1f} C    Humidity: {}% ".format(
            displaytemp_f, displaytemp_c, displayhum)
    )

    # Write the results to a .txt file.
    with open('ForecastLog.txt', 'a') as forecastLog:
                forecastLog.write("DHT reading on " +
                 str(timeNow.strftime('%A %m/%d %H:%M %p')) +": " +
                  "Temp: {:.1f} F / {:.1f} C    Humidity: {}% ".format(
            displaytemp_f, displaytemp_c, displayhum)+"\n")
                    
                    
    # Write the results to the SQL database.
    conn = sqlite3.connect("dht.db")
    
    c = conn.cursor()
    
    # Only run this the first time to create the table.
    '''c.execute("""CREATE TABLE dht (
                day_of_week text,
                date text,
                time text,
                celsius int,
                fahrenheit int,
                humidity int
                )""")'''
                
    c.execute("INSERT INTO dht VALUES (?,?,?,?,?,?)",
                (timeNow.strftime('%A'),
                timeNow.strftime('%m/%d'),
                timeNow.strftime('%H:%M %p'),
                 results[0], results[1], results[2]))
    
    conn.commit()
    conn.close()
    
    # Write the results to a .xlsx file.  This takes several seconds.
    '''print('writing to xlsx file')
    wb = openpyxl.load_workbook('dhtdata.xlsx')
    ws = wb.active

    row = [[str(timeNow.strftime('%m/%d %H:%M')), displaytemp_f, displayhum]]

    for data in row:
        if displaytemp_f == 0:
            pass
        else:
            ws.append(data)

    wb.save('dhtdata.xlsx')'''
    # close out the DHT properly. If you get an error that interrupts
    # the program before this gets to run, you may need to restart power
    # to the sensor for it to work properly.
    dhtDevice.exit()
    
    # Check if all 3 measurements failed. If so, the module runs again,
    # up to 5 times. If you get multiple failed readings, replace sensor.
    # Finally, return the results.    
    if type(displayhum) == int or type(displayhum) == float:
        return results
    else:
        trycounter += 1
        print(f'Reading failed, attempt {trycounter} initiated.')
        if trycounter < 5:
            dhtRun()
        else:
            return results
    
