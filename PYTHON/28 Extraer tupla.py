'''
Ejercicio 28
Extraer un elemento especifico
de una tupla
'''

tupla = (10,20,30)
elemento = tupla[2] #extraemos el segundo elemento de la tupla

print("Primer elemento extraido =",elemento)

#Si queremos extraer otro elemento podemos hacer lo siguiente:
nuev_elem = 1
elemento = tupla[nuev_elem]
print("Nuevo elemento por extraer (contamo0s desde cero) =", nuev_elem , "\nEl valor del nuevo elemento  es =",elemento)