# lista con valores de un mismo tipo de datos
numbers = [2,4,6,8,10]

# Calcula la longitud de la lista
len(numbers)

# lista con diferentes tipos de datos
objects = ['Hola', 3, 4, 5, True, False, 0.5]

# Acceder a los valores de una lista
objects[0] # Result: 'Hola'

objects[2] # Result: 4

# Agregar un elemento a la lista
objects.append(0.6)

# Agregar varios elementos
objects.extend(['34', '56', '66'])

# Agrega un elemento en el indice indicado
# array.insert(index, value)
objects.insert(1, "World")

# Eliminar un elemento a la lista según su posición
objects.pop(3)

# Elimina el ultimo de la lista
objects.pop()

# Elimina segun su valor
objects.remove(5)

# Eliminar todos los valores de la lista
objects.clear()

# Recorrer una lista
for element in objects:
	print(element)

# Puedo usar los Slices
new_object = objects[::-1]

# Unir listas
a = [1,3, True]
b = [4, 5, False]
c = a + b # Result: [1, 3, True, 4, 5, False]
print(c)

# Puedo unir listas sumandolos entre si
numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]
numbers = numbers1 + numbers2
# Result: [1, 2, 3, 4, 5, 6]

# Tambien puede multiplicarlo a la N
numbers1 * 3
# Result:[1, 2, 3, 1, 2, 3, 1, 2, 3]