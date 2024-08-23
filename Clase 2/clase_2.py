#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 13:05:26 2024

@author: Estudiante
"""

''' ARCHIVOS '''

datame = 'datame.txt'

def abrir1 ():
    archivo = open(datame, 'rt') # rt = read text
    data = archivo.read()
    archivo.close()
    print(data)

def abrir2 ():
    with open(datame, 'rt') as file:
        data = file.read()
    print(data)
    
''' ^ Las dos formas son equivalentes, en la segunda el archivo se cierra solo! '''


def abrirline ():
    with open(datame, 'rt') as file:
        for line in file:
           print (line)
        
''' ^ Para leer un archivo linea por linea '''

def nuevoarchivo1 ():
    with open(datame,'rt') as file:
        data = file.read()
        
    data_nuevo = '2024 seguimos con DATAME \n\n' + data
    data_nuevo = data_nuevo + '\nDirección de Carrera LCD'
    
    datame_2024 = open(datame, 'w') # w = write
    datame_2024.write(data_nuevo)
    datame_2024.close()
    
''' ^ Nuevo archivo '''

cronograma = 'cronograma_sugerido.csv'

def csv1 ():
    with open(cronograma,'rt') as file:
        for line in file:
            datos_linea = line.split(',')
            print(datos_linea[1])
            
''' ^ Abro el csv como un archivo de texto '''

import csv

def csv2 ():
    file = open(cronograma)
    filas = csv.reader(file)
    for fila in filas:
        print(fila)
    file.close()
    
''' ^ Lector de archivos csv '''
    
def csv3 ():
    file = open(cronograma)
    filas = csv.reader(file) 
    encabezado = next(filas) # un paso del iterador
    for fila in filas: # empieza desde la segunda fila
        print(fila)
    file.close()
    
''' ^ Separa el encabezado antes de printear el csv'''

import pandas as pd

def dataframe1 ():
    dicc = {'nombre': ['tiago', 'mati', 'eli'], 
            'apellido': ['scalise', 'garibaldi', 'carriedo'], 
            'lu': ['374/23', '1053/23', '392/23']}
    
    df = pd.DataFrame(data = dicc)
    df.set_index('lu', inplace = True)
    
    return df

''' ^ Dataframe desde un diccionario '''

# PRACTICA 2







    



