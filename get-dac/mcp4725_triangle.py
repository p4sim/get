import RPi.GPIO as gpio
import mcp4725_driver as mcp
import signal_generator as sg
import time

amplitude = 5.20
signal_frequency = 10
sampling_frequency = 1000

if __name__ == "__main__":
    try:
        dac = mcp.MCP4725 (5.20, 0x61, True)
        while True:
            try:
                sg.wait_for_sampling_period(sampling_frequency)
                voltage = (sg.get_triangle_wave_amplitude(signal_frequency, time.time())* amplitude)
                dac.set_voltage(voltage)

            except ValueError:
                print ("Вы ввели не число. Попробуйте ещё раз\n")

    finally:
        dac.deinit()