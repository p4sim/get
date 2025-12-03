import mcp3021_driver as adc
import time
import adc_plot as plot
import numpy as np

adc = adc.MCP3021 (5.19, True)
voltage_values = []
time_values = []
duration = 60.0


start = time.time()

while (time.time() - start < duration):             
    delta = time.time() - start
    time_values.append (delta)
    voltage_values.append (adc.get_voltage ())

plot.plot_voltage_vs_time (time_values, voltage_values, 3.3)
data = np.column_stack((time_values, voltage_values))
np.savetxt('load2.csv',
data,
delimiter = ',',
fmt='%.4f',
header = 'Время [c],Напряжение[B]',
comments='',
encoding='utf-8')
                    #print (voltage_values)
                #plot.plot_voltage_vs_time (time_values, voltage_values, 3.3)
                #plot.plot_sampling_period_hist (time_values)



