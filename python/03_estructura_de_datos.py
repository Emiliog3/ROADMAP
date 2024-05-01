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
# Lo unico que puedo hacer es obtener los elementos de la tupla

my_tuple = ("Brais", 25, 1.75, 3, 25, 500, True)
print(my_tuple)
print(type(my_tuple))
print(my_tuple[0])
print(my_tuple[0:2])
print(my_tuple[:2])
print(my_tuple[2:])
# print(my_tuple[8])
# my_tuple[0] = "Brais García" # Error
# my_tuple.append("A Coruña") # Error
# my_tuple.remove(25) # Error
# my_tuple.sort() # Error
# sorted_tuple = sorted(my_tuple) # Ordenar la tupla.
# print(sorted_tuple)
sorted_tuple = sorted(my_tuple, key=lambda x: str(x) if isinstance(x, (int, float)) else x)
print(sorted_tuple) # Este código lo que hace es ordenar la tupla, pero si hay un elemento que no es un número lo ordena alfabéticamente


# Sets
# Un set es una colección de elementos desordenada y mutable, es decir, se pueden modificar
# Los sets no permiten elementos duplicados
my_set = {"Brais", 25, 1.75, 3, 25, 500, True}
my_set.add("A Coruña") # Añadir un elemento al set
print(my_set)
my_set.add("Brais") # No se añade porque ya existe
my_set.add(26) # Se añade
print(my_set)
my_set.add("pgomezg3@gmail.com") # Se añade
my_set.add("pgomezg3@eafit.edu,co") # Se añade
print(my_set)
my_set.remove(3) # Eliminar un elemento del set
print(my_set)
my_set.pop() # Eliminar un elemento aleatorio del set
print(my_set)
my_set.update([26, 5, 65, 89])  # Se añaden
print(my_set)


# Diccionarios
# Un diccionario es una colección de elementos desordenada, mutable e indexada
# Los diccionarios se componen de claves y valores
my_dict = {
    "name": "Brais",
    "age": 25,
    "height": 1.75,
    "weight": 75,
    "email": "pgomezg3@gmail.com",
}
print(my_dict)

# Incertar un dato
my_dict["city"] = "A Coruña"
print(my_dict)

# Eliminar un dato
my_dict.pop("weight")
print(my_dict)
del my_dict["email"]
print(my_dict)

# Acceder a un dato
print(my_dict["name"])
print(my_dict.get("name"))

# Modificar un dato
my_dict["name"] = "Brais García"
print(my_dict)

# Recorrer un diccionario
for key in my_dict:
    print(key, my_dict[key])

for key, value in my_dict.items():
    print(key, value)

# Agregara datos a un diccionario
my_dict.update({"weight": 75, "email": "pgomezg3@gmail.com"})
print(my_dict)

# Copiar un diccionario
my_dict_copy = my_dict.copy()
print(my_dict_copy)

# Limpiar un diccionario
my_dict_copy.clear()
print(my_dict_copy)


# Los diccionarios no se pueden ordenar directamente, ya que son estructuras de datos desordenadas.
# Si necesitas un orden específico, puedes ordenar las claves y luego acceder a los valores en ese orden.
sorted_keys = sorted(my_dict.keys())
sorted_dict = {key: my_dict[key] for key in sorted_keys}
print(sorted_dict)