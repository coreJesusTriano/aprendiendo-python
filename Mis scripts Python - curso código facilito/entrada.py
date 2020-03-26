print("¿Cúal es tu nombre?")
nombre = input()
print("¿Cúal es tu edad?")
edad = int(input())
""" 
podemos eliminar la línea del print incorporando la pregunta
dentro del input() como a continuación, para provocar el salto
de línea incorporamos al final '\n'
"""
# print("¿Cúal es tu peso?")
peso = float(input("¿Cúal es tu peso?\n"))
autorizado = input("¿Estás autorizado?(si/no)\n") == "si"

print("Hola", nombre)
print("Edad", edad)
print("Peso", peso)
print("Autorizado", autorizado)