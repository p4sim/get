import mcp3021_driver as adc
import time
import adc_plot as plot

if __name__ == "__main__":
    try:
        adc = adc.MCP3021 (5.19, True)
        voltage_values = []
        time_values = []
        duration = 10.0

        while True:
            try:
                start = time.time()
                while (time.time() - start < duration):
                    delta = time.time() - start
                    time_values.append (delta)
                    voltage_values.append (adc.get_voltage ())
                    #print (voltage_values)
                plot.plot_voltage_vs_time (time_values, voltage_values, 3.3)
                #plot.plot_sampling_period_hist (time_values)



            except ValueError:
                print ("Вы ввели не число. Попробуйте ещё раз\n")

    finally:
        adc.deinit()