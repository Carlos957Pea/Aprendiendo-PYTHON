'''
Ejercico 21
Multiplica una cadena 
por un número entero
'''
 
cad1 = "Hello "
oper = 9
resultado = cad1 * oper 

print(resultado)



# Otra  forma de hacerlo:
cad2 = "Hola "
oper2 = 10

multi = cad2 * oper2

print(multi)


# Codigo para dejar la cantidad de espacio que queremos entre cada palabra
def multiplicar_cadena(cadena, numero):
    return cadena + ("-" * (numero - 1)) + cadena

print(multiplicar_cadena(" Mundo ", 100))