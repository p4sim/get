# -*- coding: utf-8 -*-
"""
Created on Sun Dec  7 19:32:50 2025

@author: p4sim
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Dec  7 19:09:30 2025

@author: p4sim
"""

import adc_plot as plot
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('load2.csv')



x_data = df['Время [c]']
y_data = df['Напряжение[B]'] 

pressure = [0]*len(y_data)
for i in range (len(y_data)):
    pressure[i] =82*y_data[i]

plt.figure(figsize=(20, 15)) # Опционально: задаем размер графика
plt.xlim(20,30)
plt.ylim(80,128)



plt.plot(x_data, pressure, marker=' ', linestyle='-', label='число ударов за 10 секунд: 16, пульс: ~96 уд/мин') 


plt.title('Измерение пульса при помощи тонометра') # Заголовок графика [6]
plt.xlabel('Время')
plt.ylabel('Давление, мм рт.ст.')
plt.legend()
plt.grid(True) 

plt.show() # Показываем график