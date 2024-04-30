'''
Ejercicio 19
Cuentas las concurrencias de un 
cáracter especifico en una cadena
'''

cad = "Programación AAAA en Python"
# Tener en cuenta  que el carácter a buscar, solo se buscara y contara ya sea miniscula o mayusculas
caracter = "a"
concurrencia = cad.count(caracter)
print("El carácter", caracter, "aparece", concurrencia, "veces")

concurrencia1 = cad.lower().count(caracter.lower()) # Para tener la misma condición para todas las letras
print("Y si consideramos que son iguales Mayúsculas y Minúsculas")

print(concurrencia1)
