'''
Hour Tone

Make a sound on the hour

JD Linares
2025 01 22
'''

from gpiozero import PWMOutputDevice
import time

hour_tone = PWMOutputDevice(pin=12)
hour_tone.on()
time.sleep(4)
hour_tone.off()

'''
# m h  dom mon dow   command
  0 7-22  *  *    *     /bin/python /home/diego/projects/Productivity/01_hourTone/hour_tone.py
'''




'''
c = 261
d = 293
e = 329
f = 349
g = 392

hour_tone.frequency = c
hour_tone.on()
time.sleep(1)
hour_tone.off()
hour_tone.frequency = d
hour_tone.on()
time.sleep(1)
hour_tone.off()
hour_tone.frequency = e
hour_tone.on()
time.sleep(1)
hour_tone.off()
hour_tone.frequency = c
hour_tone.on()
time.sleep(1)
hour_tone.off()




'''


