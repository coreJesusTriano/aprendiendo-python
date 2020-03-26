tupla = (1, 2, 3, 4, 5, 6)
lista = [10, 20, 30, 40]

resultado = zip(tupla, lista)
tupla_resultado = tuple(resultado)
lista_resultado = list(resultado)
tupla = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 200, 300, 400)
primero, segundo, *_, ultimo = tupla
print(primero, segundo, ultimo)

mensaje = "Este es el curso de Python"
nueva_lista = list(mensaje)
nueva_tupla = tuple(mensaje)
