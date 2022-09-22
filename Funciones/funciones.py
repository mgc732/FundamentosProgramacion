# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 03:04:15 2022

@author: Max
"""

'''





4. Diseñe e implemente una función en Python que multiplique una cantidad 
variable de números ingresados por el usuario y devuelva el resultado.

5. La serie de Fibonacci se calcula de la forma siguiente:
    1 + 1 + 2 + 3 + 5 + 8 + 13 +... Donde cada término i se calcula 
    sumando los 2 anteriores: ti=ti-1+ti-2, y los 2 términos iniciales 
    valen 1. Escriba una función para calcular los primeros n números de 
    la serie de Fibonacci y luego escriba un programa cliente que la utilice. 

6. Un grupo de investigación analiza el comportamiento de 65 pacientes 
hospitalizados y afectados por COVID19. Para ello se ingresan el número de 
paciente y luego los valores de presión de oxígeno en sangre registrados 
para ese paciente durante 7 días (una medición por día).

a) Almacene la información ingresada en una lista.

b) Calcule mediante una función  cuántos pacientes tuvieron hipoxemia 
    (presión de oxígeno inferior a 72) durante 2 o más días. Escriba el 
    programa en Python que calcule e informe los resultados.

7. Se ingresan el año (int) y luego 12 temperaturas máximas (float) de cada 
mes registradas en un año en una localidad.  Los 10 años analizados van 
entre 1990 y 1999. Organice la información en una estructura de datos,  
determine e informe:

a) El año de mayor temperatura máxima en febrero. Crear una función.

b) Qué % disminuyó la temperatura máxima  entre el valor de Enero y 
    el de Julio de 1995. Crear una función.

c) El promedio de las seis temperaturas máximas en todo el año 1991.

8. Construya el módulo operaciones_naturales.py, este debe contener las 
funciones: es_par(numero), divisores(numero), es_primo(numero) y 
factorial(numero), diseñadas e implementadas en los ejercicios previos y ejemplos.

Diseñe e implemente un programa en Python donde el usuario ingrese 
un número natural y se muestre: si es par o no, si es primo o no, sus 
divisores y su factorial. Nota: importe y utilice el módulo operaciones_naturales.py.

9. Una empresa distribuidora de equipos médicos vende 10 artículos distintos 
y exporta a otros países. Posee 8 sucursales y desea analizar el desempeño
de las mismas en el 2020. Para ello se ingresan 4 datos por cada operación 
de venta realizada en  ese año: mes (1..12), sucursal(1..8), 
moneda (‘U’ o ‘P’), monto. El dato moneda indica si el monto de la operación 
es en dólares (‘U’) o en pesos (‘P’).  Puede haber varias ventas en un 
mismo mes y para una misma sucursal.

a) Organice la información ingresada acumulando por separado los montos 
    vendidos en pesos y en dólares.

b) Determine la recaudación anual en USD  y en pesos de la sucursal 7.

c) En el mes de mayo, cuál fue la mayor recaudación en dólares de una 
    sucursal? Y qué sucursal lo logró?

Use funciones para los puntos b y c.

10. Para determinar la condición final de los alumnos de un curso de la 
asignatura Química se ingresa el nombre del alumno, las dos notas de los 
parciales y la cantidad de trabajos prácticos aprobados. Escriba una 
función que determine la condición de cada alumno sabiendo que para 
regularizar la materia debe tener promedio de los parciales mayor a 60 y 5 
o más trabajos prácticos aprobados, sino cumple con alguno de estos 
requisitos estará en condición de libre. Informe un listado con los nombres
 de los alumnos y su condición final (regular o libre).

 
'''
#%%
'''
1. Diseñe e implemente una función que reciba como parámetro un número natural
 e indique todos sus divisores.
'''

def divisores(numero):
    '''
    La funcion devuelve una lista con todos los divisores del numero entero
    que es pasado como parametro
    '''
    divisores = []
    for i in range(1,numero):
        if numero % i == 0:
            divisores.append(i)
        
    return divisores

numeroNatural = int(input("Ingrese un numero natural:"))
print(divisores(numeroNatural))

#%%
'''
2. Diseñe e implemente una función que reciba como parámetro un número natural
 e indique: True si es un número primo y False si no lo es. 
 Compruebe su correcto funcionamiento con dos valores ingresados por el usuario.
'''
def esPrimo(numero):
    primo = False
    divisores = []
    for i in range(1,numero+1):
        if numero % i == 0:
            divisores.append(i)
            
    if len(divisores) == 2 and  divisores[0] == 1 and divisores[1] == numero:
        primo = True
    else:
        primo = False
    return primo

numeroNatural = int(input("Ingrese un numero natural:"))
print(f'El numero: {numeroNatural} es Primo: {esPrimo(numeroNatural)}')

#%%
'''
3. Escriba una función para calcular el mínimo común múltiplo (m.c.m.) de dos
 números enteros dados.
'''

def calcularMCM(primerValor, segundoValor):
    bandera = True
    mcm = 0
    contador = 1
    listaMultiplos = [primerValor*indice for indice in range(1,10000+1)]
    while bandera:
        if segundoValor*contador in listaMultiplos:
            mcm = segundoValor*contador
            bandera = False
        else:
            contador = contador + 1
    return mcm
calcularMCM(201, 57)