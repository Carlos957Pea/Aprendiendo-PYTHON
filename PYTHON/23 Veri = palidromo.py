'''
Ejercicio 23
Verificar si una
palbra es un  palíndromo
'''

palabra = "AradarA"
es_palin = palabra == palabra[::-1]

print("¿La palabraes palíndromo?", es_palin)