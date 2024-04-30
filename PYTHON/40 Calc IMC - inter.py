'''
Ejercicio 40
Calcular el IMC e interpretarlo
'''


peso = 60
altura = 1.64

imc = peso / altura ** 2
print ("Tu indice de masa corporal",  imc)



# INTERPRETACION
'''
IMC             CLASIFICACION
<18,5            Bajo peso
18,5-24,9        Normal
25-29,9          Sobrepeso
30-34,9          Obesidad de grado 1
35-39,9          Obesidad de grado 2
>=40             Obesidad de grado 3
'''

if imc < 18.5:
    print("Bajo peso")
elif imc < 25:
    print("Peso normal")
elif imc  < 30:
    print("Sobrepeso")
elif imc < 35:
    print("Obesidad de grado 1")
elif imc < 40:
    print("Obesidad de grado  2")
else:
        print("Obesidad grado 3")