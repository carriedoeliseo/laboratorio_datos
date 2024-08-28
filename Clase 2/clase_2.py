#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 13:17:10 2024

@author: Estudiante
"""
#%% Importar data

import pandas as pd

arbolado_par = pd.read_csv('Clase 2/arbolado-en-espacios-verdes.csv')
arbolado_ver = pd.read_csv('./Clase 2/arbolado-publico-lineal-2017-2018.csv')
arbolado_ver = arbolado_ver[['nombre_cientifico', 
                             'ancho_acera', 
                             'diametro_altura_pecho',
                             'altura_arbol']]

#%% Ejercicio Clase

nombres_com = sorted(arbolado_par['nombre_com'].unique())

# Jacarandás
niveles_jacarandas = arbolado_par['nombre_com'].isin(['Jacarandá'])
jacarandas = arbolado_par[niveles_jacarandas]
num_jacarandas = len(jacarandas.index)

max_alt_jacarandas = max(jacarandas['altura_tot'])
min_alt_jacarandas = min(jacarandas['altura_tot'])
prom_alt_jacarandas = sum(jacarandas['altura_tot'])/num_jacarandas

max_diam_jacarandas = max(jacarandas['diametro'])
min_diam_jacarandas = min(jacarandas['diametro'])
prom_diam_jacarandas = sum(jacarandas['diametro'])/num_jacarandas


# Palos borrachos
niveles_palosborrachos = arbolado_par['nombre_com'].isin(['Palo borracho',
                                                      'Palo borracho rosado',
                                                      'Palo borracho blanco'])
palosborrachos = arbolado_par[niveles_palosborrachos]
num_palosborrachos = len(palosborrachos.index)

max_alt_palosborrachos = max(palosborrachos['altura_tot'])
min_alt_palosborrachos = min(palosborrachos['altura_tot'])
prom_alt_palosborrachos = sum(palosborrachos['altura_tot'])/num_palosborrachos

max_diam_palosborrachos = max(palosborrachos['diametro'])
min_diam_palosborrachos = min(palosborrachos['diametro'])
prom_diam_palosborrachos = sum(palosborrachos['diametro'])/num_palosborrachos

def cantidad_arboles (parque):
    arbolado = pd.read_csv('./Clase 2/arbolado-en-espacios-verdes.csv')
    parque_dframe = arbolado[arbolado['espacio_ve'].isin([parque])]
    return len(parque_dframe.index)

def cantidad_nativos (parque):
    arbolado = pd.read_csv('./Clase 2/arbolado-en-espacios-verdes.csv')
    parque_dframe = arbolado[arbolado['espacio_ve'].isin([parque]) & 
                            arbolado['origen'].isin(['Nativo/Autóctono'])]
    return len(parque_dframe.index)
    
#%% Practica 2 - 1

def leer_parque (nombre_archivo, parque):
    dframe = pd.read_csv(nombre_archivo)
    parque_dframe = dframe[dframe['espacio_ve'].isin([parque])]
    sol = []
    for i in range (len(parque_dframe.index)):
        sol.append(parque_dframe.iloc[i].to_dict())
    return sol

#%% Practica 2 - 2

def especies (lista_arboles):
    sol = []
    for arbol in lista_arboles:
        sol.append(arbol['nombre_com'])
    return sol

#%% Practica 2 - 3

def contar_ejemplares (lista_arboles):
    sol = {}
    for especie in especies(lista_arboles):
        if especie in sol.keys():
            sol[especie] += 1
        else:
            sol[especie] = 1
    return sol

#%% Practica 2 - 4

def obtener_alturas (lista_arboles, especie):
    sol = []
    for arbol in lista_arboles:
        if arbol['nombre_com'] == especie:
            sol.append(float(arbol['altura_tot']))
    return sol

# General Paz
gral_paz = leer_parque(arbolado_par, 'GENERAL PAZ')
alturas_gralpaz = obtener_alturas(gral_paz, 'Jacarandá')
max_altura_gralpaz = max(alturas_gralpaz)
prom_altura_gralpaz = sum(alturas_gralpaz)/contar_ejemplares(gral_paz)['Jacarandá']

# Parque los Andes
losandes = leer_parque(arbolado_par, 'ANDES, LOS')
alturas_losandes = obtener_alturas(losandes, 'Jacarandá')
max_altura_losandes = max(alturas_losandes)
prom_altura_losandes = sum(alturas_losandes)/contar_ejemplares(losandes)['Jacarandá']

# Centenario
centenario = leer_parque(arbolado_par, 'CENTENARIO')
alturas_centenario = obtener_alturas(centenario, 'Jacarandá')
max_altura_centenario = max(alturas_centenario)
prom_altura_centenario = sum(alturas_centenario)/contar_ejemplares(centenario)['Jacarandá']
        
#%% Practica 2 - 5

def obtener_inclinaciones (lista_arboles, especie):
    sol = []
    for arbol in lista_arboles:
        if arbol['nombre_com'] == especie:
            sol.append(float(arbol['inclinacio']))
    return sol

#%% Practica 2 - 6

def especimen_mas_inclinado (lista_arboles):
    especies_unique = pd.Series(especies(lista_arboles)).unique()
    actual = 0
    sol = ''
    for especie in especies_unique:
        inclinaciones = obtener_inclinaciones(lista_arboles, especie)
        if max(inclinaciones) >= actual:
            actual = max(inclinaciones)
            sol = especie
    return sol, actual
            
#%% Practica 2 - 7

def especie_promedio_mas_inclinada (lista_arboles):
    especies_unique = pd.Series(especies(lista_arboles)).unique()
    actual = 0
    sol = ''
    for especie in especies_unique:
        inclinaciones = obtener_inclinaciones(lista_arboles, especie)
        prom_inclinaciones = sum(inclinaciones)/len(inclinaciones)
        if prom_inclinaciones >= actual:
            actual = prom_inclinaciones
            sol = especie
    return sol, actual

#%% Practica 2 - 8

tipa_arbolado_par = arbolado_par.copy()
tipa_arbolado_par = tipa_arbolado_par[tipa_arbolado_par['nombre_cie'] == 'Tipuana Tipu']
tipa_arbolado_par = tipa_arbolado_par[['nombre_cie', 'altura_tot', 'diametro']]

tipa_arbolado_ver = arbolado_ver.copy()
tipa_arbolado_ver = tipa_arbolado_ver[tipa_arbolado_ver['nombre_cientifico'] == 'Tipuana tipu']
tipa_arbolado_ver = tipa_arbolado_ver[['nombre_cientifico', 'diametro_altura_pecho', 'altura_arbol']]
tipa_arbolado_ver.columns = tipa_arbolado_par.columns
tipa_arbolado_ver.nombre_cie = tipa_arbolado_par.nombre_cie.iloc[0]

#%% Practica 2 - 9

tipa_arbolado_par['ambiente'] = 'parque'
tipa_arbolado_ver['ambiente'] = 'vereda'

#%% Practica 2 - 10

tipa_arbolado = pd.concat([tipa_arbolado_par, tipa_arbolado_ver])

#%% Practica 2 - 11

tipa_altura_sort = tipa_arbolado.sort_values(by = 'altura_tot', ascending=False).reset_index(drop=True)
print(tipa_altura_sort[tipa_altura_sort['ambiente'] == 'parque'].head())
# Las tipas son más altas en las veredas.
# Tipa de parque más alta tiene posicion #6090/13361 en el df

tipa_diametro_sort = tipa_arbolado.sort_values(by = 'diametro', ascending=False).reset_index(drop=True)
print(tipa_diametro_sort[tipa_diametro_sort['ambiente'] == 'vereda'].head())
# Las tipas son más anchas en los parques.
# Tipa de vereda más ancha tiene posicion #2989/13361 en el df


        
        



    
