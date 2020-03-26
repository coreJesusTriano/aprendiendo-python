var_uno = 10
var_dos = 18
# Comparadores posibles los siguientes 6:
mayor = var_uno > var_dos # False
menor = var_uno < var_dos # True
mayor_igual = var_uno >= var_dos # False
menor_igual = var_uno <= var_dos # True
igual = var_uno == var_dos # False
distinto = var_uno != var_dos # True
# Devuelven un valor booleano 'bool'
print(mayor)
print(menor)
print(mayor_igual)
print(menor_igual)
print(igual)
print(distinto)
# Operadores lógicos
verdadero = True and True
print("verdadero = True and True => ",verdadero)
verdadero = True or False
print("verdadero = True or False => ",verdadero)
falso = not verdadero
print("falso = not verdadero => ",verdadero)
# Para comparar si dos valores enteros son iguales podemos 
# utilizar la palabra reservada 'is' como un comparador
print(23 is 23)
