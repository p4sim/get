# -*- coding: utf-8 -*-
"""
Created on Sun Dec  7 18:40:00 2025

@author: p4sim
"""

import adc_plot as plot
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('data40.csv')

x_data = df['Время [c]']
y_data = df['Напряжение[B]'] 

plt.figure(figsize=(15, 10)) # Опционально: задаем размер графика
plt.ylim(0.5,0.8)
plt.plot(x_data, y_data, marker=' ', linestyle='-') # Линейный график с точками
# Или plt.scatter(x_data, y_data, color='red') # Точечный график

plt.title('Калибровка: напряжение АЦП при давлении 40 мм рт ст') # Заголовок графика [6]
plt.xlabel('Время')
plt.ylabel('Напряжение АЦП, В')
plt.grid(True) # Добавляем сетку (опционально)

plt.show() # Показываем график




