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
# Devolver un listado con los nombres de los departamentos que no tienen
# ningún caso asociado.

consultaSQL = """
                SELECT DISTINCT descripcion as departamento,
                FROM departamento
                LEFT OUTER JOIN casos
                ON departamento.id = casos.id_depto
                WHERE id_depto IS NULL ;
              """    

AAAresultado = sql^ consultaSQL

#%% EJERCICIO Cb ==============================================================
# Devolver un listado con los tipos de evento que no tienen ningún caso
# asociado.

consultaSQL = """
                SELECT DISTINCT descripcion as evento
                FROM tipoevento
                LEFT OUTER JOIN casos
                ON tipoevento.id = casos.id_tipoevento
                WHERE id_tipoevento IS NULL ;
              """

AAAresultado = sql^ consultaSQL

#%% ===========================================================================

 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# #                              EJERCICIO D                              # #
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

#%% EJERCICIO Da ==============================================================
# Calcular la cantidad total de casos que hay en la tabla casos.

consultaSQL = """
                SELECT SUM(cantidad)
                FROM casos ;
              """

AAAresultado = sql^ consultaSQL

#%% EJERCICIO Db ==============================================================
# Calcular la cantidad total de casos que hay en la tabla casos para cada año y
# cada tipo de caso. Presentar la información de la siguiente manera:
# descripción del tipo de caso, año y cantidad. Ordenarlo por tipo de caso
# (ascendente) y año (ascendente).

consultaSQL = """
                SELECT DISTINCT descripcion as evento, anio, SUM(cantidad) as cantidad
                FROM casos
                JOIN tipoevento
                ON tipoevento.id = casos.id_tipoevento
                GROUP BY anio, evento
                ORDER BY evento ASC, anio DESC ;
              """

AAAresultado = sql^ consultaSQL

#%% EJERCICIO Dc ==============================================================
# Misma consulta que el ítem anterior, pero sólo para el año 2019.

consultaSQL = """
                SELECT DISTINCT descripcion as evento, anio, SUM(cantidad) as cantidad
                FROM casos
                JOIN tipoevento
                ON tipoevento.id = casos.id_tipoevento
                GROUP BY anio, evento
                HAVING anio = 2019
                ORDER BY evento ASC, anio DESC ;
              """

AAAresultado = sql^ consultaSQL

#%% EJERCICIO Dd ==============================================================
# Calcular la cantidad total de departamentos que hay por provincia. Presentar
# la información ordenada por código de provincia

consultaSQL = """
                SELECT DISTINCT id_provincia as id, 
                                provincia.descripcion, 
                                COUNT(id_provincia) as num_deptos
                FROM departamento
                JOIN provincia
                ON departamento.id_provincia = provincia.id
                GROUP BY id_provincia, provincia.descripcion
                ORDER BY id_provincia
              """

AAAresultado = sql^ consultaSQL

#%% EJERCICIO De ==============================================================
# Listar los departamentos con menos cantidad de casos en el año 2019.

consultaSQL = """
                SELECT DISTINCT d.id,
                                d.descripcion as departamento,
                                SUM(c.cantidad) as num_casos
                FROM departamento AS d
                JOIN casos AS c ON d.id = c.id_depto
                GROUP BY d.id, d.descripcion, c.anio
                HAVING c.anio = 2019
                ORDER BY num_casos
              """
              
casos_deptos = sql^ consultaSQL

consultaSQL = """
                SELECT MIN(num_casos) as min
                FROM casos_deptos
              """
              
min_casos = sql^ consultaSQL

consultaSQL = """
                SELECT DISTINCT cd.id,
                                cd.departamento,
                                cd.num_casos
                FROM casos_deptos AS cd
                JOIN min_casos ON num_casos = min
              """
              
AAAresultado = sql^ consultaSQL
del casos_deptos
del min_casos

#%% EJERCICIO Df ==============================================================
# Listar los departamentos con más cantidad de casos en el año 2020.

consultaSQL = """
                SELECT DISTINCT d.id,
                                d.descripcion as departamento,
                                SUM(c.cantidad) as num_casos
                FROM departamento AS d
                JOIN casos AS c ON d.id = c.id_depto
                GROUP BY d.id, d.descripcion, c.anio
                HAVING c.anio = 2020
                ORDER BY num_casos
              """
              
casos_deptos = sql^ consultaSQL

consultaSQL = """
                SELECT MAX(num_casos) as max
                FROM casos_deptos
              """
              
max_casos = sql^ consultaSQL

consultaSQL = """
                SELECT DISTINCT cd.id,
                                cd.departamento,
                                cd.num_casos
                FROM casos_deptos AS cd
                JOIN max_casos ON num_casos = max
              """
              
AAAresultado = sql^ consultaSQL
del casos_deptos
del max_casos

#%% EJERCICIO Dg ==============================================================
# Listar el promedio de cantidad de casos por provincia y año.

consultaSQL = """
                SELECT DISTINCT d.id_provincia,
                                p.descripcion,
                                c.anio,
                                AVG(c.cantidad) as promedio
                FROM casos as c
                JOIN departamento as d ON c.id_depto = d.id
                JOIN provincia as p ON d.id_provincia = p.id
                GROUP BY d.id_provincia, p.descripcion, c.anio
                ORDER BY c.anio DESC, d.id_provincia ASC
              """
              
AAAresultado = sql^ consultaSQL

#%% EJERCICIO Dh ==============================================================
# Listar, para cada provincia y año, cuáles fueron los departamentos que más
# cantidad de casos tuvieron.

consultaSQL = """
                SELECT p.id,
                       p.descripcion as provincia,
                       c.id_depto,
                       c.anio,
                       SUM(c.cantidad) as casos_depto
                FROM casos AS c
                JOIN departamento AS d ON c.id_depto = d.id
                JOIN provincia AS p ON d.id_provincia = p.id
                GROUP BY p.id, p.descripcion, c.id_depto, c.anio
                ORDER BY c.anio DESC, p.id ASC, c.id_depto ASC
              """

casos_deptos_prov = sql^ consultaSQL

consultaSQL = """
                SELECT cdp.id AS id, 
                       cdp.anio AS anio, 
                       MAX(cdp.casos_depto) AS max
                FROM casos_deptos_prov as cdp
                GROUP BY cdp.id, cdp.anio
              """
              
max_casos_cdp = sql^ consultaSQL

consultaSQL = """
                SELECT DISTINCT cdp.id,
                                cdp.provincia,
                                cdp.anio,
                                casos_depto as max_casos_depto
                FROM casos_deptos_prov as cdp
                JOIN max_casos_cdp as maxcdp ON cdp.id = maxcdp.id AND
                                                cdp.casos_depto = maxcdp.max AND
                                                cdp.anio = maxcdp.anio
                ORDER BY cdp.anio DESC, cdp.id ASC
              """
              
AAAresultado = sql^ consultaSQL
del casos_deptos_prov
del max_casos_cdp

#%% EJERCICIO Di ==============================================================
# Mostrar la cantidad de casos total, máxima, mínima y promedio que tuvo la
# provincia de Buenos Aires en el año 2019.

consultaSQL = """
               SELECT p.id,
                      p.descripcion AS provincia,
                      c.anio,
                      c.cantidad as casos
               FROM casos AS c
               JOIN departamento AS d ON c.id_depto = d.id
               JOIN provincia AS p ON d.id_provincia = p.id
               WHERE p.descripcion = 'Buenos Aires' AND c.anio = 2019
               ORDER BY c.cantidad
              """
              
casos_bsas = sql^ consultaSQL

consultaSQL = """
               SELECT DISTINCT cba.id,
                               cba.provincia,
                               SUM(cba.casos) AS total,
                               MAX(cba.casos) AS maximo,
                               MIN(cba.casos) AS minimo,
                               AVG(cba.casos) AS promedio
               FROM casos_bsas as cba
               GROUP BY cba.id, cba.provincia
              """
              
AAAresultado = sql^ consultaSQL
del casos_bsas

#%% EJERCICIO Dj ==============================================================
# Misma consulta que el ítem anterior, pero sólo para aquellos casos en que la
# cantidad total es mayor a 1000 casos.

consultaSQL = """
               SELECT p.id,
                      p.descripcion AS provincia,
                      c.anio,
                      c.cantidad as casos
               FROM casos AS c
               JOIN departamento AS d ON c.id_depto = d.id
               JOIN provincia AS p ON d.id_provincia = p.id
               WHERE c.anio = 2019
               ORDER BY p.descripcion
              """
              
casos_prov = sql^ consultaSQL

consultaSQL = """
               SELECT DISTINCT cp.id,
                               cp.provincia,
                               SUM(cp.casos) AS total,
                               MAX(cp.casos) AS maximo,
                               MIN(cp.casos) AS minimo,
                               AVG(cp.casos) AS promedio
               FROM casos_prov as cp
               GROUP BY cp.id, cp.provincia
               HAVING total >= 1000
              """
              
AAAresultado = sql^ consultaSQL
del casos_prov

#%% EJERCICIO Dk ==============================================================
# Listar los nombres de departamento (y nombre de provincia) que tienen
# mediciones tanto para el año 2019 como para el año 2020. Para cada uno de
# ellos devolver la cantidad de casos promedio. Ordenar por nombre de
# provincia (ascendente) y luego por nombre de departamento (ascendente).

consultaSQL = """
               SELECT DISTINCT p.descripcion AS provincia,
                               c.id_depto,
                               d.descripcion AS departamento               
               FROM casos AS c
               JOIN departamento AS d ON c.id_depto = d.id
               JOIN provincia AS p ON d.id_provincia = p.id
               WHERE c.anio = 2019
                   INTERSECT
               SELECT DISTINCT p.descripcion AS provincia,
                               c.id_depto,
                               d.descripcion AS departamento               
               FROM casos AS c
               JOIN departamento AS d ON c.id_depto = d.id
               JOIN provincia AS p ON d.id_provincia = p.id
               WHERE c.anio = 2020
              """
              
deptos1920 = sql^ consultaSQL

consultaSQL = """
                SELECT DISTINCT c.id_depto,
                                d.descripcion AS departamento,
                                AVG(c.cantidad) AS promedio
                FROM casos AS c
                JOIN departamento AS d ON c.id_depto = d.id
                GROUP BY c.id_depto, d.descripcion
              """
              
prom_deptos = sql^ consultaSQL

consultaSQL = """
                SELECT DISTINCT d1920.provincia,
                                d1920.departamento,
                                pd.promedio
                FROM deptos1920 AS d1920
                NATURAL JOIN prom_deptos AS PD
                ORDER BY d1920.provincia ASC, d1920.departamento ASC
              """
              
AAAresultado = sql^ consultaSQL
del deptos1920
del prom_deptos

#%% EJERCICIO Dk ==============================================================
# Devolver una tabla que tenga los siguientes campos: descripción de tipo de
# evento, id_depto, nombre de departamento, id_provincia, nombre de
# provincia, total de casos 2019, total de casos 2020.

consultaSQL = """
                SELECT c.id_tipoevento,
                       c.id_depto,
                       SUM(c.cantidad) AS casos_2019,
                FROM casos AS c
                JOIN departamento AS d ON c.id_depto = d.id
                JOIN provincia AS p ON d.id_provincia = p.id
                JOIN tipoevento AS e ON c.id_tipoevento = e.id
                GROUP BY c.id_tipoevento,
                         c.anio, 
                         c.id_depto,
                         d.id_provincia,
                HAVING c.anio = 2019
                ORDER BY c.id_tipoevento ASC, c.id_depto ASC
              """

casos_2019 =  sql^ consultaSQL

consultaSQL = """
                SELECT c.id_tipoevento,
                       c.id_depto,
                       SUM(c.cantidad) AS casos_2020,
                FROM casos AS c
                JOIN departamento AS d ON c.id_depto = d.id
                JOIN provincia AS p ON d.id_provincia = p.id
                JOIN tipoevento AS e ON c.id_tipoevento = e.id
                GROUP BY c.id_tipoevento,
                         c.anio, 
                         c.id_depto,
                         d.id_provincia,
                HAVING c.anio = 2020
                ORDER BY c.id_tipoevento ASC, c.id_depto ASC
              """
              
casos_2020 =  sql^ consultaSQL

consultaSQL = """
                SELECT e.descripcion AS tipoevento,
                       d.id AS id_depto,
                       d.descripcion AS departamento,
                       d.id_provincia,
                       p.descripcion AS provincia,
                       c19.casos_2019,
                       c20.casos_2020,
                FROM departamento AS d
                LEFT OUTER JOIN casos_2019 AS c19 ON d.id = c19.id_depto
                LEFT OUTER JOIN casos_2020 AS c20 ON d.id = c20.id_depto
                JOIN provincia AS p ON d.id_provincia = p.id
                JOIN tipoevento AS e ON c19.id_tipoevento = e.id OR
                                        c20.id_tipoevento = e.id
                ORDER BY e.descripcion ASC, d.id_provincia ASC, d.id ASC
              """

AAAresultado =  sql^ consultaSQL
del casos_2019
del casos_2020


