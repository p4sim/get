import time
import numpy as np

def get_sin_wave_amplitude(freq, time):
    return ((np.sin(2*np.pi*freq*time)+1)/2)

def wait_for_sampling_period(sampling_frequency):
    time.sleep (float(1/sampling_frequency))

def get_triangle_wave_amplitude (freq, time):
    return ((2*abs(2*freq*time-np.floor(2*freq*time+0.5))))