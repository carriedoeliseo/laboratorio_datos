# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 21:29:28 2024

@author: carri
"""

from inline_sql import sql, sql_val
import pandas as pd

#%% Data sets =================================================================

carpeta = './clase6/guiaPracticaSQL/'

casos = pd.read_csv(carpeta + 'casos.csv')
departamento = pd.read_csv(carpeta + 'departamento.csv')
gropoetario = pd.read_csv(carpeta + 'grupoetario.csv')
provincia = pd.read_csv(carpeta + 'provincia.csv')
tipoevento = pd.read_csv(carpeta + 'tipoevento.csv')

#%% ===========================================================================

 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# #                              EJERCICIO A                              # #
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

#%% EJERCICIO Aa ==============================================================
# Listar sólo los nombres de todos los departamentos que hay en la tabla 
# departamento (dejando los registros repetidos).

consultaSQL = """
                SELECT descripcion
                FROM departamento ;
              """

AAAresultado = sql^ consultaSQL

#%% EJERCICIO Ab ==============================================================
# Listar sólo los nombres de todos los departamentos que hay en la tabla
# departamento (eliminando los registros repetidos).

consultaSQL = """
                SELECT DISTINCT descripcion
                FROM departamento ;
              """
              
AAAresultado = sql^ consultaSQL

#%% EJERCICIO Ac ==============================================================
# Listar sólo los códigos de departamento y sus nombres, de todos los
# departamentos que hay en la tabla departamento.

consultaSQL = """
                SELECT id, descripcion
                FROM departamento ;
              """
              
AAAresultado = sql^ consultaSQL

#%% EJERCICIO Ad ==============================================================
# Listar todas las columnas de la tabla departamento.

consultaSQL = """
                SELECT *
                FROM departamento ;
              """
              
AAAresultado = sql^ consultaSQL

#%% EJERCICIO Ae ==============================================================
# Listar los códigos de departamento y nombres de todos los departamentos
# que hay en la tabla departamento. Utilizar los siguientes alias para las
# columnas: codigo_depto y nombre_depto, respectivamente.


consultaSQL = """
                SELECT id as codigo_depto, descripcion as nombre_depto
                FROM departamento ;
              """
              
AAAresultado = sql^ consultaSQL

#%% EJERCICIO Af ==============================================================
# Listar los registros de la tabla departamento cuyo código de provincia es
# igual a 54.

consultaSQL = """
                SELECT *
                FROM departamento
                WHERE id_provincia = 54 ;
              """
              
AAAresultado = sql^ consultaSQL

#%% EJERCICIO Af ==============================================================
# Listar los registros de la tabla departamento cuyo código de provincia es
# igual a 22, 78 u 86.

consultaSQL = """
                SELECT *
                FROM departamento
                WHERE id_provincia = 54 OR
                      id_provincia = 78 OR 
                      id_provincia = 86 ;
              """
             
AAAresultado = sql^ consultaSQL

#%% EJERCICIO Af ==============================================================
# Listar los registros de la tabla departamento cuyos códigos de provincia se
# encuentren entre el 50 y el 59 (ambos valores inclusive).

consultaSQL = """
                SELECT *
                FROM departamento
                WHERE id_provincia > 53 AND id_provincia < 60 ;
              """
             
AAAresultado = sql^ consultaSQL

#%% ===========================================================================

 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# #                              EJERCICIO B                              # #
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

#%% EJERCICIO Ba ==============================================================
# Devolver una lista con los código y nombres de departamentos, asociados al
# nombre de la provincia al que pertenecen

consultaSQL = """
                SELECT departamento.id,
                       departamento.descripcion as departamento, 
                       provincia.descripcion as provincia
                FROM departamento
                JOIN provincia
                ON departamento.id_provincia = provincia.id ;
              """
             
AAAresultado = sql^ consultaSQL

#%% EJERCICIO Bb ==============================================================
# Devolver una lista con los código y nombres de departamentos, asociados al
# nombre de la provincia al que pertenecen

consultaSQL = """
                SELECT departamento.id,
                       departamento.descripcion as departamento, 
                       provincia.descripcion as provincia
                FROM departamento
                JOIN provincia
                ON departamento.id_provincia = provincia.id ;
              """
             
AAAresultado = sql^ consultaSQL

#%% EJERCICIO Bc ==============================================================
# Devolver los casos registrados en la provincia de “Chaco”.


consultaSQL = """
                SELECT departamento.id as departamento_id
                FROM departamento
                JOIN provincia
                ON departamento.id_provincia = provincia.id
                WHERE provincia.descripcion = 'Chaco' ;
              """

departamentosChaco = sql^ consultaSQL
                      
consultaSQL = """
                SELECT *
                FROM casos
                JOIN departamentosChaco
                ON id_depto = departamento_id ;
              """               

AAAresultado = sql^ consultaSQL
del departamentosChaco

#%% EJERCICIO Bd ==============================================================
# Devolver aquellos casos de la provincia de “Buenos Aires” cuyo campo
# cantidad supere los 10 casos.

consultaSQL = """
                SELECT departamento.id as departamento_id
                FROM departamento
                JOIN provincia
                ON departamento.id_provincia = provincia.id
                WHERE provincia.descripcion = 'Buenos Aires' ;
              """

departamentosBsAs = sql^ consultaSQL

consultaSQL = """
                SELECT *
                FROM casos
                JOIN departamentosBsAs
                ON id_depto = departamento_id
                WHERE cantidad >= 10 ;
              """    

AAAresultado = sql^ consultaSQL
del departamentosBsAs

#%% ===========================================================================

 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# #                              EJERCICIO C                              # #
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

#%% EJERCICIO Ca ==============================================================
