# toggle spreadsheet 10 and 11
# import serial
print "here1"
import gspread
print "here2"
import time
print "here3"
from oauth2client.service_account import ServiceAccountCredentials
print "here4"
scope = ['https://spreadsheets.google.com/feeds']
print "here5"
credentials = ServiceAccountCredentials.from_json_keyfile_name('Smart Kennel gspread-ac720d1668b1.json', scope)
print "here6"
gc = gspread.authorize(credentials)
print "here7"
ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=3)

# Open a worksheet from spreadsheet with one shot
wks = gc.open("Smart Kennel").sheet1
print "Ready"
b2_value = wks.acell('B2').value
b2_value = int(b2_value)
if (b2_value == 10):
	wks.update_acell('B2', "11")
	print 10
else:
	wks.update_acell('B2', "10")
	print 11