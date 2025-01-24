'''
Hour Tone

Make a sound on the hour

JD Linares
2025 01 22
2025 01 24

Add to crontab: 
# Note TIMEZONE
# m h  dom mon dow   command
  0 7-22  *  *    *     /bin/python /home/diego/projects/Productivity/01_hourTone/hour_tone.py

'''

import  datetime
from gpiozero import PWMOutputDevice
import time


my_tz = datetime.timezone(datetime.timedelta(hours=-5))
my_time = datetime.datetime.now(my_tz)
#print(str(my_time))
my_hour = my_time.hour%12      # convert to 12 hour time

my_ten = my_hour // 10          # 10's place
my_one = my_hour % 10           #  1's place

hour_tone = PWMOutputDevice(pin=12)

if my_ten:
    hour_tone.on()
    time.sleep(4)
    hour_tone.off()
    time.sleep(1)
else:
    hour_tone.on()
    time.sleep(.1)
    hour_tone.off()
    time.sleep(.05)
    hour_tone.on()
    time.sleep(.1)
    hour_tone.off()
    time.sleep(.05)
    hour_tone.on()
    time.sleep(.1)
    hour_tone.off()
    time.sleep(.05)
    hour_tone.on()
    time.sleep(.1)
    hour_tone.off()
    time.sleep(1)


for i in range(my_one):
    hour_tone.on()
    time.sleep(1)
    hour_tone.off()
    time.sleep(1)



