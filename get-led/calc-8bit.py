import RPi.GPIO as gpio
import time
gpio.setmode (gpio.BCM)
leds = [16,12,25,17,27,23,22,24]
gpio.setup(leds, gpio.OUT)
gpio.output(leds, 0)

up = 9
down = 10
enter = 13
gpio.setup (up, gpio.IN)
gpio.setup (down, gpio.IN)
gpio.setup (enter, gpio.IN)
num = 0

def dec2bin(value):
    return [int(element)for element in bin(value)[2:].zfill(8)]

sleep_time = 0.2
sum = 0
i = 0

while True:

    if gpio.input(up):
        num +=1
        print (num,dec2bin(num))
        time.sleep(sleep_time)

    if gpio.input(down):
        num -=1
        if num < 0:
            num = 255
        print (num,dec2bin(num))
        time.sleep(sleep_time)

    if gpio.input(up) and gpio.input(down):
        num = 255
        print (num,dec2bin(num))
        time.sleep(sleep_time)

    if num > 255:
        num = 0

    gpio.output (leds, dec2bin(num))

    if gpio.input (enter):
        sum+=num
        i+=1
        num = 0
    
    if i==2:
        gpio.output (leds, dec2bin(sum))

   