'''
Ejercico 38
Determina sin un numero es 
divisible entre 5 y 7
'''

num = int(input("Dame un número: "))

if num % 5 == 0 and num % 7 == 0:
    print("Es divisible entre 5 y 7")
else:
    print("\nERROR: \nNo es divisible entre 5 Y 7")