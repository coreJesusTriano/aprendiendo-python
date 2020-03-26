lista = [8.17, 90, 8.17, 1, 5, 44, 1.32]

lista.sort() # ordena la lista en orden ascendente
lista.sort(reverse=True) # ordena la lista orden decreciente
# Ahora la lista esta ordenada decrecientemente
mayor = lista[0] # el primero elemento ahora es el mayor
lista.sort()
menor = lista[0] # ahora el primero es el menor
maximo = max(lista) # devuelve el valor mayor
minimo = min(lista) # devuelve el valor menor
longitud = len(lista) # devuelvel el tamaño de la lista
resultado = 8 in lista # booleano True si '8' está en la lista o False en caso contrario
# Para hallar el indice de un elemento, el cual debe existir
indice = lista.index(8.17) # devuelve el indice primera ocurrencia
contador = lista.count(8.17) # devuelve el número de ocurrencias del elemento dado.
existe = lista.count("No se existe este elemento") # devuelve 0 si el elemento no existe en la lista.
# otras funciones/métodos con listas
lista.append(6.34) # inserta elemento al final
lista.insert(1, 6.12) # inserta en el indice dato el elemento del segundo parametro.
lista.remove(6.34) # elimina el elemento dado
lista.clear() # vacia la lista
