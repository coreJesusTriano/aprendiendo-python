lenguajes = "Python; Java; Ruby; PHP; Swift; JavaScript; C#; C; C++"
resultado = lenguajes.split("; ") # split recibe el separador, de no recibir nada usará el espacio como separador
"""
cadena.split(separador) devuelve una list y se aplica sobre una cadena, cada elemento de la lista serán sub-string del comienzo al separador, de este al siguiente separador, y así hasta el final.
"""

separador = ", "
nuevo_string = separador.join(resultado) 
"""
cadena.join() devuelve un str y recibe una list
el string retornado será:
cadena+list[0]+cadena+list[1]+ ... +cadena+list[-1]
"""

texto = """Este es un texto
con saltos
de línea"""
result = texto.splitlines() # devuelve una lista cuyos elementos son las líneas

