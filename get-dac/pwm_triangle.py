import RPi.GPIO as gpio
import pwm_dac as pwm
import signal_generator as sg
import time

amplitude = 3.13
signal_frequency = 10
sampling_frequency = 10

if __name__ == "__main__":
    try:
        dac = pwm.PWM_DAC (12, 500, 3.14, True)
        while True:
            try:
                sg.wait_for_sampling_period(sampling_frequency)
                voltage = (sg.get_triangle_wave_amplitude(signal_frequency, time.time())* amplitude)
                dac.set_voltage(voltage)

            except ValueError:
                print ("Вы ввели не число. Попробуйте ещё раз\n")

    finally:
        dac.deinit()
