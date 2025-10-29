import matplotlib.pyplot as plt

def plot_voltage_vs_time (time, voltage, max_voltage):
    plt.figure(figsize = (10,6))
    plt.plot(time,voltage)
    plt.title("ADC Voltage from Time")
    plt.xlim(right = 10)
    plt.ylim(bottom = 0,top = 5.5)
    plt.grid()
    plt.show()

def plot_sampling_period_hist (time):
    sampling_periods = []

    for i in range(1, len(time)):
        period = time[i] - time [i-1]
        sampling_periods.append(period)
    plt.figure(figsize = (10,6))
    plt.hist (sampling_periods)
    plt.title("ADC Time Histogram")
    plt.xlim(0,0.6)
 
    plt.grid()
    plt.show()
