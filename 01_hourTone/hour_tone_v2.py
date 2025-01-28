'''
Hour Tone v2

Make a sound on the hour

JD Linares
2025 01 22
2025 01 28

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

hour_tone = PWMOutputDevice(pin=12)

def play_fives(fives_val):
    for i in range(fives_val):
        hour_tone.on()
        time.sleep(1)
        hour_tone.off()
        time.sleep(1)

def play_ones(ones_val):
    for i in range(ones_val):
        hour_tone.on()
        time.sleep(.1)
        hour_tone.off()
        time.sleep(.1)

my_hour = my_time.hour%12      # convert to 12 hour time

my_fives = my_hour // 5          # 5's place
my_ones = my_hour % 5           #  1's place


for i in range(2):
    play_fives(my_fives)
    play_ones(my_ones)
    time.sleep(2)

