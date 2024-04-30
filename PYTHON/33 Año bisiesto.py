'''
Ejercico 34
Determina si un año es bisiesto
    Regla del ejercicio
    - Divisible por 4
    - No divisible  por 100
    - Divisible por 400
'''

anio = 20024

if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
    print("El año", anio, "es bisiesto")
else:
    print("El año", anio, "no es bisiesto")