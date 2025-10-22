import r2r_adc as adc
import time
import adc_plot as plot

if __name__ == "__main__":
    try:
        adconv = adc.R2R_ADC (3.3, 0.01, True)
        voltage_values = []
        time_values = []
        duration = 10.0

        while True:
            try:
                start = time.time()
                while (time.time() - start < duration):
                    delta = time.time() - start
                    time_values.append (delta)
                    voltage_values.append (adconv.get_sc_voltage ())
                    #print (voltage_values)
                plot.plot_voltage_vs_time (time_values, voltage_values, 3.3)



            except ValueError:
                print ("Вы ввели не число. Попробуйте ещё раз\n")

    finally:
        adconv.deinit()