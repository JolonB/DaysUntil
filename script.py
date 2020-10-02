import serial
import time
import datetime

BAUD = 115200
PORT = "/dev/ttyS7"

ser = serial.Serial('/dev/ttyS7', 115200)

future_date = datetime.date(2020, 10, 16)

n = 0
while True:
    today = datetime.date.today()
    diff = (future_date - today).days
    print(diff)
    ser.write('{}'.format(diff).encode())
    time.sleep(10)
