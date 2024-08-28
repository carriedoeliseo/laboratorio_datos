#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 09:20:52 2024

@author: Estudiante
"""
#%% Data

import pandas as pd
import matplotlib.pyplot as plt

wifis = pd.read_csv('Clase-03-Actividad-01-Datos.csv')
movilidad = pd.read_csv('Encuesta de Movilidad - Respuestas de formulario 1.csv')
movilidad = movilidad.iloc[:50]

resultados = movilidad['Tipo de transporte utilizado']

#%% Grafico
dic = {}
for resultado in resultados:
    if resultado in dic.keys():
        dic[resultado] +=1
    else:
        dic[resultado] = 0

plt.style.use('_mpl-gallery')
fig, ax = plt.subplots(figsize=(7, 5))
ax.stem(dic.keys(), dic.values())
plt.show()

#%% Otra forma de conteo
conteo = resultados.value_counts()
