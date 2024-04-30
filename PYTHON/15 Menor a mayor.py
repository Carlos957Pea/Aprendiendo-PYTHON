'''
Ejercicio 15
Ordena una lista de números 
de menor a mayor
'''
# Utilizando .sort()
lis_num = [6,8,7,1,3,9]
lis_num.sort()

print("Lista ordenada: ", lis_num)

# De mayor a menor
lis_ord = sorted(lis_num, reverse=True)
print("Lista ordenada de mayor a menor: ", lis_ord)