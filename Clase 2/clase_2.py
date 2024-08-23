#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 13:17:10 2024

@author: Estudiante
"""
#%% Importar data

import pandas as pd

arbolado = pd.read_csv('./Clase 2/arbolado-en-espacios-verdes.csv')

#%% Ejercicio Clase

nombres_com = sorted(arbolado['nombre_com'].unique())

# Jacarandás
niveles_jacarandas = arbolado['nombre_com'].isin(['Jacarandá'])
jacarandas = arbolado[niveles_jacarandas]
num_jacarandas = len(jacarandas.index)
max_alt_jacarandas = max(jacarandas['altura_tot'])
min_alt_jacarandas = min(jacarandas['altura_tot'])
prom_alt_jacarandas = sum(jacarandas['altura_tot'])/num_jacarandas


# Palos borrachos
niveles_palosborrachos = arbolado['nombre_com'].isin(['Palo borracho',
                                                      'Palo borracho rosado',
                                                      'Palo borracho blanco'])
palosborrachos = arbolado[niveles_palosborrachos]
num_palosborrachos = len(palosborrachos.index)
max_alt_palosborrachos = max(palosborrachos['altura_tot'])
min_alt_palosborrachos = min(palosborrachos['altura_tot'])
prom_alt_palosborrachos = sum(palosborrachos['altura_tot'])/num_palosborrachos

