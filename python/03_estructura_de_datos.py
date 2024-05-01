# Estructura de Datos

# Listas
my_list = ["Brais", 25, 1.75, 3, 25, 500, True]
print(my_list)

my_list.append("A Coruña") # Añadir un elemento al final de la lista
print(my_list)

my_list.remove(25) # Eliminar un elemento de la lista
print(my_list)
print(my_list[1]) # Acceder a un elemento de la lista
# Acceder a varios elementos de la list
print(my_list[0:2]) # Brais, 1.75
print(my_list[:2]) # Brais, 1.75
print(my_list[2:]) # 1.75, True, A Coruña
my_list[0] = "Brais García" # Modificar un elemento de la lista
print(my_list)
my_list.sort(key=str) # Ordenar la lista
print(my_list)


# Tuplas
# Una tupla es una colección de elementos ordenada e inmutable, es decir no se pueden modificar
my_tuple = ("Brais", 25, 1.75, 3, 25, 500, True)
print(my_tuple)
print(type(my_tuple))

