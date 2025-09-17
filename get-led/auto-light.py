import RPi.GPIO as gpio
gpio.setmode (gpio.BCM)
photo = 6
led = 26
gpio.setup(photo, gpio.IN)
gpio.setup(led, gpio.OUT)
while True:
    gpio.output(led, not gpio.input(photo))