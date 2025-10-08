import RPi.GPIO as gpio
import time


class R2R_DAC:
    def __init__(self,gpio_bits,dynamic_range, verbose = False):
        self.gpio_bits = gpio_bits
        self.dynamic_range = dynamic_range
        self.verbose = verbose

        gpio.setmode (gpio.BCM)
        gpio.setup(self.gpio_bits, gpio.OUT, initial = 0)

    def deinit(self):
        gpio.output(self.gpio_bits, 0)
        gpio.cleanup()

    def set_number(self,number):
        return [int(element)for element in bin(number)[2:].zfill(8)]

    def set_voltage(self,voltage):
        return int (voltage/self.dynamic_range * 255)


if __name__ == "__main__":
    try:
        dac = R2R_DAC ([16,20,21,25,26,17,27,22],3.13, True)

        while True:
            try:
                voltage = float(input("Введите напряжение в Вольтах:"))
                number = dac.set_voltage(voltage)
                print ("Число на вход ЦАП: ", number, ", биты: ", dac.set_number(number))
                gpio.output (dac.gpio_bits, dac.set_number(number))

            except ValueError:
                print ("Вы ввели не число. Попробуйте ещё раз\n")

    finally:
        dac.deinit()
