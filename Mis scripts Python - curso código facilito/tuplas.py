# Las tuplas son como las listas pero son inmutables
mi_tupla = ('Eduardo', 2, 4.5, True)
# Las tuplas son más rápidas que las listas, pero no se puede añadir ni eliminar elementos
tupla = (1,2,3,4,5,6,7,8,9,0)

elemento = tupla[4]
impares = tupla[:9:2]
pares = tupla[1:10:2]
# si intentamos modificar un elemento de una tupla
# tupla[0] = 10
# provocará un error en tiempo ejecución.

otra_tupla = (1,2,3,4)
# uno, dos, tres, cuatro = otra_tupla[0], otra_tupla[1], otra_tupla[2], otra_tupla[3]
# la linea anterior se puede simplificar así:
uno, dos, tres, cuatro = otra_tupla
# para que no de error debo asignar a variables cada elemento de la tupla (o subtupla)
tupla_mayor = (1,2,3,4,5,6)
uno, dos, tres, cuatro, *resto = tupla_mayor
# podemos usar la notación * para que el resto se guarde en dicha variable como una lista
print(resto)
resto[0] = 10
print(resto)
uno, dos, *lista, seis = tupla_mayor
print(uno, dos, lista, seis) # 1 2 [3, 4, 5] 6
