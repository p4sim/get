import RPi.GPIO as gpio
import r2r_dac as r2r
import signal_generator as sg
import time

amplitude = 3.13
signal_frequency = 10
sampling_frequency = 10

if __name__ == "__main__":
    try:
        dac = r2r.R2R_DAC ([16,20,21,25,26,17,27,22],3.13, True)
        while True:
            try:
                sg.wait_for_sampling_period(sampling_frequency)
                voltage = (sg.get_triangle_wave_amplitude(signal_frequency, time.time())* amplitude)
                number = dac.set_voltage(voltage)
                print ("Число на вход ЦАП: ", number, ", биты: ", dac.set_number(number))
                gpio.output (dac.gpio_bits, dac.set_number(number))

            except ValueError:
                print ("Вы ввели не число. Попробуйте ещё раз\n")

    finally:
        dac.deinit()
