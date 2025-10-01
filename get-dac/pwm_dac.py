import RPi.GPIO as gpio
import time

class PWM_DAC:
    def __init__(self, gpio_pin, pwm_frequency, dynamic_range, verbose = False):
        self.gpio_pin = gpio_pin
        self.pwm_frequency = pwm_frequency
        self.dynamic_range = dynamic_range
        self.verbose = verbose

        gpio.setmode (gpio.BCM)
        gpio.setup(self.gpio_pin, gpio.OUT, initial = 0)
        self.pwm = gpio.PWM (self.gpio_pin, self.pwm_frequency)
        self.pwm.start (0)

    def deinit(self):
        gpio.output(self.gpio_pin, 0)
        gpio.cleanup()


    def set_voltage(self,voltage):
        if not (0.0<=voltage<=self.dynamic_range):
            print(f"Напряжение выходит за динамический диапазон ЦАП (0.00 - {self.dynamic_range:.2f} В)")
            print ("Устанавливаем 0.0 В")
            return 0
        self.pwm.ChangeDutyCycle(voltage/self.dynamic_range*100)

if __name__ == "__main__":
    try:
        dac = PWM_DAC(12, 500, 3.14, True)

        while True:
            try:
                voltage = float(input("Введите напряжение в Вольтах:"))
                dac.set_voltage(voltage)
            

            except ValueError:
                print ("Вы ввели не число. Попробуйте ещё раз\n")

    finally:
        dac.deinit()