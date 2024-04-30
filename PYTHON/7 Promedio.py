'''
Ejercicio 7
Calcula el promedio de 
una lista de números
'''

numeros = [2,6,9,30]
resultado = sum(numeros) / len(numeros)

print("El promedio es: ", resultado)



#OTRA FORMA  DE HACERLO CON LIST COMPREHENSIONS Y FUNCIONES ANONIMAS

# lista =  [2,4,6,8,10]
# def calculo_promedio(lst):
#     return sum(lst)/len(lst)
# print("El promedio es: ",calculo_promedio(numeros))