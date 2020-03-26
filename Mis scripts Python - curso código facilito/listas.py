cursos = ["python", "django", "flask", "c", "c++", "c#", "java", "php"]

sub = cursos[2]
ultimo = cursos[-1] # Las listas se pueden recorrer también en direccion inversa
sub2 = cursos[3:6] # Indice del primer elemento de la sub-lista, Indice hasta el que llega excluido éste.
sub3 = cursos[:3] # Si omito primer parametro es desde el comienzo
sub4 = cursos[6:] # si omito segundo hasta el final
sub5 = cursos[1:7:2] # tercer parametro es el salto
copia = cursos[:]
inversa = cursos[::-1] # obtenemos la lista invertida
