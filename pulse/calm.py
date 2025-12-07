# -*- coding: utf-8 -*-
"""
Created on Sun Dec  7 19:09:30 2025

@author: p4sim
"""

import adc_plot as plot
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('calm2.csv')



x_data = df['Время [c]']
y_data = df['Напряжение[B]'] 

pressure = [0]*len(y_data)
for i in range (len(y_data)):
    pressure[i] =82*y_data[i]

plt.figure(figsize=(30, 20)) # Опционально: задаем размер графика



sys = [115]*len(y_data)
dia = [72]*len(y_data)

plt.plot(x_data, pressure, marker=' ', linestyle='-', label='давление') 
plt.plot(x_data, sys, marker=' ', linestyle='-', color='r', label='систола')
plt.plot(x_data, dia, marker=' ', linestyle='-', color='g', label='диастола')
# Или plt.scatter(x_data, y_data, color='red') # Точечный график

plt.title('Измерение артериального давления при помощи тонометра') # Заголовок графика [6]
plt.xlabel('Время')
plt.ylabel('Давление, мм рт.ст.')
plt.legend()
plt.grid(True) 

plt.show() # Показываем график