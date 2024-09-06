# -*- coding: utf-8 -*-
"""
Materia: Laboratorio de datos - FCEyN - UBA
Clase  : Clase SQL. Script clase.
Autor  : Pablo Turjanski
Fecha  : 2024-03-25
"""

# Importamos bibliotecas
import pandas as pd
from inline_sql import sql, sql_val


#%%===========================================================================
# Importamos los datasets que vamos a utilizar en este programa
#=============================================================================

carpeta = "./clase7/archivosSQL/"

# Ejercicios AR-PROJECT, SELECT, RENAME
empleado       = pd.read_csv(carpeta+"empleado.csv")
# Ejercicios AR-UNION, INTERSECTION, MINUS
alumnosBD      = pd.read_csv(carpeta+"alumnosBD.csv")
alumnosTLeng   = pd.read_csv(carpeta+"alumnosTLeng.csv")
# Ejercicios AR-CROSSJOIN
persona        = pd.read_csv(carpeta+"persona.csv")
nacionalidades = pd.read_csv(carpeta+"nacionalidades.csv")
# Ejercicios ¿Mismos Nombres?
se_inscribe_en=pd.read_csv(carpeta+"se_inscribe_en.csv")
materia       =pd.read_csv(carpeta+"materia.csv")
# Ejercicio JOIN múltiples tablas
vuelo      = pd.read_csv(carpeta+"vuelo.csv")    
aeropuerto = pd.read_csv(carpeta+"aeropuerto.csv")    
pasajero   = pd.read_csv(carpeta+"pasajero.csv")    
reserva    = pd.read_csv(carpeta+"reserva.csv")    
# Ejercicio JOIN tuplas espúreas
empleadoRol= pd.read_csv(carpeta+"empleadoRol.csv")    
rolProyecto= pd.read_csv(carpeta+"rolProyecto.csv")    
# Ejercicios funciones de agregación, LIKE, Elección, Subqueries 
# y variables de Python
examen     = pd.read_csv(carpeta+"examen.csv")
# Ejercicios de manejo de valores NULL
examen03 = pd.read_csv(carpeta+"examen03.csv")



#%%===========================================================================
# Ejemplo inicial
#=============================================================================

print(empleado)

consultaSQL = """
               SELECT DISTINCT DNI, Salario
               FROM empleado;
              """

dataframeResultado = sql^ consultaSQL

print(dataframeResultado)


#%%===========================================================================
# Ejercicios AR-PROJECT <-> SELECT
#=============================================================================
# a.- Listar DNI y Salario de empleados 
consultaSQL = """
                
              """

dataframeResultado = sql^ consultaSQL

#%%-----------
# b.- Listar Sexo de empleados 
consultaSQL = """

              """

dataframeResultado = sql^ consultaSQL

#%%-----------
#c.- Listar Sexo de empleados (sin DISTINCT)
consultaSQL = """

              """

dataframeResultado = sql^ consultaSQL

#%%===========================================================================
# Ejercicios AR-SELECT <-> WHERE
#=============================================================================
# a.- Listar de EMPLEADO sólo aquellos cuyo sexo es femenino
consultaSQL = """

              """

dataframeResultado = sql^ consultaSQL

#%% -----------
#b.- Listar de EMPLEADO aquellos cuyo sexo es femenino y su salario es mayor a $15.000
consultaSQL = """

              """

dataframeResultado = sql^ consultaSQL

#%%===========================================================================
# Ejercicios AR-RENAME <-> AS
#=============================================================================
#a.- Listar DNI y Salario de EMPLEADO, y renombrarlos como id e Ingreso
consultaSQL = """

              """

dataframeResultado = sql^ consultaSQL


#%% # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
 # #                                                                     # #
# #    INICIO -->           EJERCICIO Nro. 01                             # #
 # #                                                                     # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# IMPORTANTE: Recordar que se utilizaran los datos de vuelo, aeropuerto, pasajero y reserva

#%%===========================================================================
# EJERCICIOS PARA REALIZAR DE MANERA INDIVIDUAL --> EJERCICIO Nro. 01
#=============================================================================
# Ejercicio 01.1.- Retornar Codigo y Nombre de los aeropuertos de Londres
consultaSQL = """
                SELECT DISTINCT Codigo, Nombre
                FROM aeropuerto
                WHERE Ciudad = 'Londres'
              """

dataframeResultado = sql^ consultaSQL

#%% -----------
# Ejercicio 01.2.- ¿Qué retorna 
#                       SELECT DISTINCT Ciudad AS City 
#                       FROM aeropuerto 
#                       WHERE Codigo='ORY' OR Codigo='CDG'; ?
consultaSQL = """
                SELECT DISTINCT Ciudad AS City 
                FROM aeropuerto 
                WHERE Codigo='ORY' OR Codigo='CDG'
              """

dataframeResultado = sql^ consultaSQL

#%% -----------
# Ejercicio 01.3.- Obtener los números de vuelo que van desde CDG hacia LHR
consultaSQL = """
                SELECT DISTINCT Numero
                FROM vuelo
                WHERE Origen = 'CDG' AND Destino = 'LHR'
              """

dataframeResultado = sql^ consultaSQL

#%% -----------
# Ejercicio 01.4.- Obtener los números de vuelo que van desde CDG hacia LHR o viceversa
consultaSQL = """
                SELECT DISTINCT Numero
                FROM vuelo
                WHERE (Origen = 'CDG' AND Destino = 'LHR') OR (Origen = 'LHR' AND Destino = 'CDG') 
              """

dataframeResultado = sql^ consultaSQL

#%% -----------
# Ejercicio 01.5.- Devolver las fechas de reservas cuyos precios son mayores a $200
consultaSQL = """
                SELECT DISTINCT Fecha
                FROM reserva
                WHERE precio > 200
              """

dataframeResultado = sql^ consultaSQL


#%% # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
 # #                                                                     # #
# #    FIN -->              EJERCICIO Nro. 01                             # #
 # #                                                                     # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    
#=============================================================================
# Ejercicios AR-UNION, INTERSECTION, MINUS <-> UNION, INTERSECTION, EXCEPT
#=============================================================================
# a1.- Listar a los alumnos que cursan BDs o TLENG

consultaSQL = """
                SELECT DISTINCT *
                FROM alumnosBD
                UNION
                SELECT DISTINCT *
                FROM alumnosTLeng
              """

dataframeResultado = sql^ consultaSQL


#%% -----------
# a2.- Listar a los alumnos que cursan BDs o TLENG (usando UNION ALL)

consultaSQL = """
                SELECT DISTINCT *
                FROM alumnosBD
                UNION ALL
                SELECT DISTINCT *
                FROM alumnosTLeng
              """

dataframeResultado = sql^ consultaSQL

#%% -----------
# b.- Listar a los alumnos que cursan simultáneamente BDs y TLENG

consultaSQL = """
                SELECT DISTINCT *
                FROM alumnosBD
                INTERSECT
                SELECT DISTINCT *
                FROM alumnosTLeng
              """

dataframeResultado = sql^ consultaSQL

#%% -----------
# c.- Listar a los alumnos que cursan BDs y no cursan TLENG 

consultaSQL = """
                SELECT DISTINCT *
                FROM alumnosBD
                EXCEPT
                SELECT DISTINCT *
                FROM alumnosTLeng
              """

dataframeResultado = sql^ consultaSQL

#%% # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
 # #                                                                     # #
# #    INICIO -->           EJERCICIO Nro. 02                             # #
 # #                                                                     # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# IMPORTANTE: Recordar que se utilizaran los datos de vuelo, aeropuerto, pasajero y reserva

#=============================================================================
#  EJERCICIOS PARA REALIZAR DE MANERA INDIVIDUAL --> EJERCICIO Nro. 02
#=============================================================================
# Ejercicio 02.1.- Devolver los números de vuelo que tienen reservas generadas (utilizar intersección)
consultaSQL = """
                SELECT DISTINCT Numero
                FROM vuelo
                INTERSECT
                SELECT DISTINCT NroVuelo
                FROM reserva
              """

dataframeResultado = sql^ consultaSQL

#%%-----------
# Ejercicio 02.2.- Devolver los números de vuelo que aún no tienen reservas
consultaSQL = """
                SELECT DISTINCT Numero
                FROM vuelo
                EXCEPT
                SELECT DISTINCT NroVuelo
                FROM reserva
              """

dataframeResultado = sql^ consultaSQL

#%%-----------
# Ejercicio 02.3.- Retornar los códigos de aeropuerto de los que parten o arriban los vuelos
consultaSQL = """
                SELECT DISTINCT Destino as Codigos
                FROM vuelo
                UNION
                SELECT DISTINCT Origen
                FROM vuelo
              """
              
dataframeResultado = sql^ consultaSQL



#%% # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
 # #                                                                     # #
# #    FIN -->              EJERCICIO Nro. 02                             # #
 # #                                                                     # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

#=============================================================================
# Ejercicios AR-... JOIN <-> ... JOIN
#=============================================================================
# a1.- Listar el producto cartesiano entre las tablas persona y nacionalidades

consultaSQL = """

              """

dataframeResultado = sql^ consultaSQL


#%%-----------
# a2.- Listar el producto cartesiano entre las tablas persona y nacionalidades (sin usar CROSS JOIN)

consultaSQL = """

              """

dataframeResultado = sql^ consultaSQL


#%% --------------------------------------------------------------------------------------------
# Carga los nuevos datos del dataframe persona para los ejercicios de AR-INNER y LEFT OUTER JOIN
# ----------------------------------------------------------------------------------------------
persona        = pd.read_csv(carpeta+"persona_ejemplosJoin.csv")
# ----------------------------------------------------------------------------------------------
# b1.- Vincular las tablas persona y nacionalidades a través de un INNER JOIN

consultaSQL = """

              """

dataframeResultado = sql^ consultaSQL

#%%-----------
# b2.- Vincular las tablas persona y nacionalidades (sin usar INNER JOIN)

consultaSQL = """

              """

dataframeResultado = sql^ consultaSQL

#%%-----------
# c.- Vincular las tablas persona y nacionalidades a través de un LEFT OUTER JOIN

consultaSQL = """

              """

dataframeResultado = sql^ consultaSQL

#%%===========================================================================
# Ejercicios SQL - ¿Mismos Nombres?
#=============================================================================
# a.- Vincular las tablas Se_inscribe_en y Materia. Mostrar sólo LU y Nombre de materia

consultaSQL = """

              """

dataframeResultado = sql^ consultaSQL

    
#%% # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
 # #                                                                     # #
# #    INICIO -->           EJERCICIO Nro. 03                             # #
 # #                                                                     # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# IMPORTANTE: Recordar que se utilizaran los datos de vuelo, aeropuerto, pasajero y reserva

#%%===========================================================================
# EJERCICIOS PARA REALIZAR DE MANERA INDIVIDUAL --> EJERCICIO Nro. 03
#=============================================================================
# Ejercicio 03.1.- Devolver el nombre de la ciudad de partida del vuelo número 165

consultaSQL = """
                SELECT DISTINCT Ciudad
                FROM vuelo
                JOIN aeropuerto
                ON Origen = Codigo
                WHERE Numero = 165 ;
              """

dataframeResultado = sql^ consultaSQL
print(dataframeResultado)

#%%-----------
# Ejercicio 03.2.- Retornar el nombre de las personas que realizaron reservas a un valor menor a $200

consultaSQL = """
                SELECT DISTINCT Nombre
                FROM pasajero
                NATURAL JOIN reserva
                WHERE Precio < 200 ;
              """

dataframeResultado = sql^ consultaSQL
print(dataframeResultado)

#%%-----------
# Ejercicio 03.3.- Obtener Nombre, Fecha y Destino del Viaje de todos los pasajeros que vuelan desde Madrid

vuelosAMadrid = sql^"""
                    SELECT DISTINCT *
                    FROM vuelo
                    WHERE Origen = 'MAD'
              """

dniPersonasDesdeMadrid = sql^"""
                    SELECT DISTINCT *
                    FROM vuelosAMadrid
                    JOIN reserva
                    ON Numero = NroVuelo
              """

consultaSQL = """
                SELECT DISTINCT Nombre, Fecha, Destino
                FROM dniPersonasDesdeMadrid
                NATURAL JOIN pasajero
              """

dataframeResultado = sql^ consultaSQL
print(dataframeResultado)

#%% # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
 # #                                                                     # #
# #    FIN -->              EJERCICIO Nro. 03                             # #
 # #                                                                     # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    
#%%===========================================================================
# Ejercicios SQL - Join de varias tablas en simultáneo
#=============================================================================
# a.- Vincular las tablas Reserva, Pasajero y Vuelo. Mostrar sólo Fecha de reserva, hora de salida del vuelo y nombre de pasajero.
    
consultaSQL = """

              """

dataframeResultado = sql^ consultaSQL

    
#%%===========================================================================
# Ejercicios SQL - Tuplas espúreas
#=============================================================================
# a.- Vincular (JOIN)  EmpleadoRol y RolProyecto para obtener la tabla original EmpleadoRolProyecto
    
consultaSQL = """

              """

dataframeResultado = sql^ consultaSQL

#%%===========================================================================
# Ejercicios SQL - Funciones de agregación
#=============================================================================
# a.- Usando sólo SELECT contar cuántos exámenes fueron rendidos (en total)
    
consultaSQL = """

              """

dataframeResultado = sql^ consultaSQL


#%%-----------
# b1.- Usando sólo SELECT contar cuántos exámenes fueron rendidos en cada Instancia
    
consultaSQL = """

              """

dataframeResultado = sql^ consultaSQL


#%%-----------
# b2.- Usando sólo SELECT contar cuántos exámenes fueron rendidos en cada Instancia (ordenado por instancia)
    
consultaSQL = """

              """

dataframeResultado = sql^ consultaSQL


#%%-----------
# b3.- Ídem ejercicio anterior, pero mostrar sólo las instancias a las que asistieron menos de 4 Estudiantes
    
consultaSQL = """

              """

dataframeResultado = sql^ consultaSQL

#%%-----------
# c.- Mostrar el promedio de edad de los estudiantes en cada instancia de examen
    
consultaSQL = """

              """

dataframeResultado = sql^ consultaSQL


#%%===========================================================================
# Ejercicios SQL - LIKE")
#=============================================================================
# a1.- Mostrar cuál fue el promedio de notas en cada instancia de examen, sólo para instancias de parcial.
    
consultaSQL = """

              """

dataframeResultado = sql^ consultaSQL

#%%-----------
# a2.- Mostrar cuál fue el promedio de notas en cada instancia de examen, sólo para instancias de parcial. Esta vez usando LIKE.
    
consultaSQL = """

              """

dataframeResultado = sql^ consultaSQL


#%%===========================================================================
# Ejercicios SQL - Eligiendo
#=============================================================================
# a1.- Listar a cada alumno que rindió el Parcial-01 y decir si aprobó o no (se aprueba con nota >=4).
    
consultaSQL = """
                SELECT Nombre, Nota,
                CASE WHEN Nota >= 4
                    THEN 'Aprobó'
                    ELSE 'No Aprobó'
                END AS Estado
                FROM examen
                WHERE Instancia = 'Parcial-01'
                ORDER BY Nombre ;
              """

dataframeResultado = sql^ consultaSQL
print(dataframeResultado)

#%%-----------
# a2.- Modificar la consulta anterior para que informe cuántos estudiantes aprobaron/reprobaron en cada instancia.
    
consultaSQL = """
                SELECT Instancia,
                CASE WHEN Nota >= 4
                    THEN 'Aprobó'
                    ELSE 'No Aprobó'
                END AS Estado,
                COUNT(*) AS Cantidad
                FROM examen
                GROUP BY Instancia, Estado
                ORDER BY Instancia, Estado
              """

dataframeResultado = sql^ consultaSQL
print(dataframeResultado)

#%%===========================================================================
# Ejercicios SQL - Subqueries
#=============================================================================
#a.- Listar los alumnos que en cada instancia obtuvieron una nota mayor al promedio de dicha instancia

consultaSQL = """
                SELECT e1.Nombre, e1.Instancia, e1.Nota
                FROM examen AS e1
                WHERE e1.Nota > (
                    SELECT AVG(e2.Nota)
                    FROM examen AS e2
                    WHERE e2.Instancia = e1.Instancia)
                ORDER BY Instancia ASC, Nota DESC
              """


dataframeResultado = sql^ consultaSQL
print(dataframeResultado)

#%%-----------
# b.- Listar los alumnos que en cada instancia obtuvieron la mayor nota de dicha instancia

consultaSQL = """
                SELECT e1.Nombre, e1.Instancia, e1.Nota
                FROM examen AS e1
                WHERE e1.Nota = (
                    SELECT MAX(e2.Nota)
                    FROM examen AS e2
                    WHERE e2.Instancia = e1.Instancia)
                ORDER BY Nombre, Instancia, Nota ;
              """
              
# OTRA OPCION:
# SELECT e1.Nombre, e1.Instancia, e1.Nota
# FROM examen AS e1
# WHERE e1.Nota >= ALL (
#     SELECT e2.Nota
#     FROM examen AS e2
#     WHERE e2.Instancia = e1.Instancia)
# ORDER BY Nombre, Instancia, Nota ;

dataframeResultado = sql^ consultaSQL
print(dataframeResultado)

#%%-----------
# c.- Listar el nombre, instancia y nota sólo de los estudiantes que no rindieron ningún Recuperatorio

consultaSQL = """
                SELECT e1.Nombre, e1.Instancia, e1.Nota
                FROM examen AS e1
                WHERE NOT EXISTS (
                    SELECT e2.Nombre, e2.Instancia
                    FROM examen AS e2
                    WHERE e1.Nombre = e2.Nombre AND
                        e2.Instancia LIKE 'Recuperatorio%')
                ORDER BY Nombre, Instancia, Nota
              """

dataframeResultado = sql^ consultaSQL
print(dataframeResultado)

#%%===========================================================================
# Ejercicios SQL - Integrando variables de Python
#=============================================================================
# a.- Mostrar Nombre, Instancia y Nota de los alumnos cuya Nota supera el umbral indicado en la variable de Python umbralNota

umbralNota = 7

consultaSQL = """

              """

dataframeResultado = sql^ consultaSQL


#%%===========================================================================
# Ejercicios SQL - Manejo de NULLs
#=============================================================================
# a.- Listar todas las tuplas de Examen03 cuyas Notas son menores a 9

consultaSQL = """

              """

dataframeResultado = sql^ consultaSQL

#%%-----------
# b.- Listar todas las tuplas de Examen03 cuyas Notas son mayores o iguales a 9

consultaSQL = """

              """


dataframeResultado = sql^ consultaSQL


#%%-----------
# c.- Listar el UNION de todas las tuplas de Examen03 cuyas Notas son menores a 9 y las que son mayores o iguales a 9

consultaSQL = """

              """


dataframeResultado = sql^ consultaSQL


#%%-----------
# d1.- Obtener el promedio de notas

consultaSQL = """

              """


dataframeResultado = sql^ consultaSQL


#%%-----------
# d2.- Obtener el promedio de notas (tomando a NULL==0)

consultaSQL = """

              """


dataframeResultado = sql^ consultaSQL

#%%===========================================================================
# Ejercicios SQL - Mayúsculas/Minúsculas
#=============================================================================
# a.- Consigna: Transformar todos los caracteres de las descripciones de los roles a mayúscula

consultaSQL = """

              """

dataframeResultado = sql^ consultaSQL

#%%-----------
# b.- Consigna: Transformar todos los caracteres de las descripciones de los roles a minúscula

consultaSQL = """

              """

dataframeResultado = sql^ consultaSQL




#%%===========================================================================
# Ejercicios SQL - Reemplazos
#=============================================================================
# a.- Consigna: En la descripción de los roles de los empleados reemplazar las ñ por ni

consultaSQL = """

              """

dataframeResultado = sql^ consultaSQL


#%%===========================================================================
# Ejercicios SQL - Desafío
#=============================================================================
# a.- Mostrar para cada estudiante las siguientes columnas con sus datos: Nombre, Sexo, Edad, Nota-Parcial-01, Nota-Parcial-02, Recuperatorio-01 y , Recuperatorio-02

# ... Paso 1: Obtenemos los datos de los estudiantes
consultaSQL = """

              """


desafio_01 = consultaSQL



#%% -----------
# b.- Agregar al ejercicio anterior la columna Estado, que informa si el alumno aprobó la cursada (APROBÓ/NO APROBÓ). Se aprueba con 4.

consultaSQL = """
                 
              """

desafio_02 = sql^ consultaSQL



#%% -----------
# c.- Generar la tabla Examen a partir de la tabla obtenida en el desafío anterior.

consultaSQL = """

              """

desafio_03 = sql^ consultaSQL
