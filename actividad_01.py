# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 02:16:12 2021

@author: KEVIN
"""

import os
import statistics
import math 

arch_AS = []                               #Lista de archivos crudos
arch_o = []                                #Lista de archivos .o

coord_x = []                               #Lista de coordenadas x
coord_y = []                               #lista de coordenadas y
coord_z = []                               #lista de coordenadas z

cwd = os.getcwd()                            #Asignando espacio de trabajo "current working directory"                                   

ext = '.AS'                                  #Variable con extension .AS 
ext1 = '.o'                                  #Variable con extension .o

def listar(cwd):                                       #funcion para listar los archivos y guardarlos en la lista arch_AS
    for root, dirs, files in os.walk(cwd):             #Bucle para navegar en la carpeta de trabajo   
        for file in files:                             #Bucle para iterar en cada archivo
            if os.path.splitext(file)[1] == ext:       #Condicional para separar el nombre de la extension de cada archivo selecionarla y compararla con la variable ext
                arch_AS.append(file)                   #En caso de ser igual lo agrega a la lista de archivos AS
                
             
#listar(cwd)

def convert(arch_AS):                                                   #Funcion para convertir los archivos de la lista AS a archivos de observacion
    for file in arch_AS:                                                #Bucle para iterar en cada archivo de la lista AS 
        new_name = file.split('.')[0]+'.o'                              #variable en la que se separa el nombre de la extension del archivo, se selecciona el nombre y se le agrega la extension .o
        print(new_name)                                                 
        os.system('teqc -O.dec 30 +obs ' + new_name  + ' ' +  file)     #comando para utilizar el ejecutable del programa usando el archivo renombrado y el archivo AS

#convert(arch_AS)    

def extract(cwd):                                                    #Funcion para extraccion de coordenadas
    for root, dirs, files in os.walk(cwd):
        for file in files:                                           #bucle para iterar en sobre cada archivo
            if os.path.splitext(file)[1] == ext1:                    #Condicional para separar el nombre de la extension de cada archivo selecionarla y compararla con la variable ext1
                arch_o.append(file)                                  #En caso de ser igual lo agrega a la lista de archivos de observacion
                
    for file_o in arch_o:                                            #bucle para iterar sobre cada archivo de la lista de archivos de observacion
        with open(file_o) as f:                                      #comando para abrir el archivo renombrandolo como f
            lineas = f.readlines()[9:10]                             #variable para leer y asignar la linea de interes 
            for linea in lineas:                                     #bucle para iterar en cada linea del archivo
                new_line = linea.strip().split(' ', 4)[0:4]          #variable a la que se le asigna la linea seleccionada, se le quita los espacios arriba y abajo, 
                coord_x.append(float(new_line[0]))                             #se separa usando los espacios un maximo de 4 veces y se selecciona los primeros 4 elementos de la lista
                coord_y.append(float(new_line[1]))
                coord_z.append(float(new_line[3]))                   #Los tres comandos anteriores asignan cada coordenada a su respectiva lista y la convierte de cadenas a numeros 
    x = statistics.mean(coord_x)
    y = statistics.mean(coord_y)
    z = statistics.mean(coord_z)                                     #Los tres comandos anteriores calculan el promedio de cada coordenada segun los valores de cada lista
        
    a = 6378137                         #Parametros para elipsoide WGS84
    b = 6356752.314
    
    p = math.sqrt(x**2 + y**2)            #calculos de ecuasiones para el algoritmo de Bowring   

    te = math.atan((z*a)/(p*b))

    e2 = (a**2-b**2)/(a**2)

    e_2 = (a**2-b**2)/(b**2)
 
    lamd = math.atan(y/x)

    phi = math.atan((z + e_2*b*math.sin(te)**3)/(p - e2*a*math.cos(te)**3))

    n = a/math.sqrt(1 - e2*math.sin(phi)**2)

    h = (p/math.cos(phi))-n
    
    geo_x = math.degrees(lamd)            #conversion de radianes a grados deimales   
    geo_y = math.degrees(phi)
    print('geo_x =', geo_x)
    print('geo_y =', geo_y)    
    print('h = ', h)

    str_x = str(geo_x)                    #convertir floats a strings
    str_y = str(geo_y)
    str_z = str(h)
    coords =[str_x, str_y, str_z]         #unir strings a lista
    c =','.join(coords)                   #uniendo coordenadas en una sola cadena separada por comas
    
    with open('Coordenadas Geodesicas de Estacion de CURNO.csv', 'w') as archivo:  #creando archivo csv
        archivo.write('Coordenada X, Coordenada Y, Coordenada Z\n')
        archivo.write(c)
     
extract(cwd)



















    
    
    
    
    
    
    
    