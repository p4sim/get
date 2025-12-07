# -*- coding: utf-8 -*-
"""
Created on Sun Dec  7 18:56:43 2025

@author: p4sim
"""

import adc_plot as plot
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

x_data = [0.66, 1.14, 1.64, 2.12]
y_data = [40,80,120,160]

plt.plot(x_data, y_data, marker='.', linestyle='-', label = "y=-13.9+82x")
plt.title('Калибровка: перевод напряжения АЦП в давление') # Заголовок графика [6]
plt.xlabel('Напряжение АЦП, В')
plt.ylabel('Артериальное давление, мм рт.ст.')
plt.legend ()
plt.grid()