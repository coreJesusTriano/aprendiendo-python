texto = "curso de Python 3"

txt1 = texto.capitalize() # Curso de python 3
txt2 = texto.swapcase() # CURSO DE pYTHON 3
txt3 = texto.upper() # CURSO DE PYTHON 3
txt4 = texto.lower() # curso de python 3
txt5 = texto.title() # Curso De Python 3

texto = "curso de Python 3, Python básico"
txt6 = texto.replace("Python", "Java", 1) # curso de Java 3, Python básico
# .replace(texto_reemplazado, reemplazo, num_reemplazos_opcional)

minusculas = txt4.islower()
mayusculas = txt3.isupper()

texto = "    curso de Python 3, Python básico   "

txt7 = texto.strip() # "curso de Python 3, Python básico" sin espacios en los extremos

