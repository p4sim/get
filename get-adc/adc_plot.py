import matplotlib.pyplot as plt

def plot_voltage_vs_time (time, voltage, max_voltage):
    plt.figure(figsize = (10,6))
    plt.plot(time,voltage)
    plt.title("ADC Voltage from Time")
    plt.xlim(right = 10)
    plt.ylim(bottom = 0,top = max_voltage)
    plt.grid()
    plt.show()

def plot_sampling_period_hist (time):
    plt.figure(figsize = (10,6))
    plt.plot(time,voltage)
    plt.title("ADC Voltage from Time")
 
    plt.grid()
    plt.show()
