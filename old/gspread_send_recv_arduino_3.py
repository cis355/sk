import serial
import gspread
import time
from oauth2client.service_account import ServiceAccountCredentials


scope = ['https://spreadsheets.google.com/feeds']

credentials = ServiceAccountCredentials.from_json_keyfile_name('Smart Kennel gspread-ac720d1668b1.json', scope)

gc = gspread.authorize(credentials)

ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=3)
# Open a worksheet from spreadsheet with one shot
wks = gc.open("Smart Kennel").sheet1
print "Ready"
data = 10
led1 = 10
led2 = 20
led3 = 30
while 1:
    data = ser.readline()[:-2]
    if data:
        dataRead = int(data)
        if dataRead == 10:
            led1 = 10
            wks.update_acell('B2', "10")
        if dataRead == 11:
            led1 = 11
            wks.update_acell('B2', "11")
        if dataRead == 20:
            led2 = 10
            wks.update_acell('B3', "20")
        if dataRead == 21:
            led2 = 21
            wks.update_acell('B3', "21")
        if dataRead == 30:
            led3 = 30
            wks.update_acell('B4', "30")
        if dataRead == 31:
            led3 = 31
            wks.update_acell('B4', "31")
    b2_value = wks.acell('B2').value
    b2_value = int(b2_value)
    b3_value = wks.acell('B3').value
    b3_value = int(b3_value)
    b4_value = wks.acell('B4').value
    b4_value = int(b4_value)
    if b2_value != led1:
        if b2_value == 11:
            ser.write(b'11')
        else:
            ser.write(b'10')
    if b3_value != led2:
        if b3_value == 21:
            ser.write(b'21')
        else:
            ser.write(b'20')
    if b4_value != led3:
        if b4_value == 31:
            ser.write(b'31')
        else:
            ser.write(b'30')
   # if b2_value != data:

    
# Fetch a cell range
# cell_list = wks.range('A1:B7')
