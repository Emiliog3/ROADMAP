# Funciones y Alcance
# Una función es un bloque de código que solo se ejecuta cuando se llama y se puede reutilizar en cualquier parte del programa cada vez que se llame.

# Funciones definidas por el usuario
# En Python, una función se define utilizando la palabra clave def.
# def nombre_funcion(parametros):

def greet():
    print("Hello, World!")

# Llamar a la función
greet()

# Con retonro

def retonr_greet():
    return "Hello, Pablo!" 

print(retonr_greet())

# Con un argumento

def greet_name(name):
    return "Hello, " + name

print(greet_name("Pablo Emilio"))

def arg_greet(name):
    print(f"Hello, {name}") 
arg_greet("Pablo Emilio Gómez")


def arg_greet(name, age):
    print(f"Hello, {name} you are {age} years old")

arg_greet("Pablo Emilio Gómez", 25)


def default_greet(name = "Pablo Emilio Gómez"):
    print(f"Hello, {name}")

default_greet("Python")
default_greet()


# Con arguentos

def return_args_greet(greet, name):
    return f"{greet}, {name} !"

print(return_args_greet("Hello", "Pablo Emilio Gómez"))



def return_args_greet(greet, name):
    return f"{greet}, {name}!"



print(return_args_greet("Hello", "Pablo Emilio Gómez"))

# Con retonro de varios valores

def multiple_return_greet():
    return "Hello", "Pablo Emilio Gómez Gómez"

greet, name = multiple_return_greet()
print(greet)
print(name)

# Con un número variable de argumentos

def variable_arg_greet(*names):
    for name in names:
        print(f"Hello, {name}")

variable_arg_greet("Pablo", "Emilio", "Gómez", "Comunidad")      


# Con un número variable de argumentos con palabras clave

# Con un número variable de argumentos con palabras clave

def variable_key_arg_greet(**names):
    for param, name in names.items():  # Corrección aquí
        print(f"Hello, {name} ({param})!")

variable_key_arg_greet(
    lenguaje="Python",
    name="Pablo Emilio Gómez",
    comunidad="Comunidad",
    age=25    
)


# Funciones dentro de funciones

def outer_function():
    def inner_function():
        print("Hello, World!")
    inner_function()

outer_function()


# Funciones del lenguaje o building functions

# print len sirve para contar la cantidad de caracteres de una cadena           
print(len("Hello, World!"))
# print type sirve para saber el tipo de dato de una variable
print(type("Hello, World!"))
# print id sirve para saber la dirección de memoria de una variable
print(id("Hello, World!"))
# print abs sirve para saber el valor absoluto de un número
print(abs(-1))
print(abs(1))
print(abs(-1.0))
print(abs(1.0))
# print round sirve para redondear un número
print(round(1.5))
print(round(1.4))
print(round(1.6))
print(round(1.6, 1)) # redondear a un decimal. Por ejemplo, 1.6 redondeado a 1 decimal es 1.6
print(round(1.6, 0)) # redondear a un entero. Por ejemplo, 1.6 redondeado a 0 decimales es 2
print(round(1.666666, 1)) # redondear a un decimal. Por ejemplo, 1.666666 redondeado a 1 decimal es 1.7
print(round(1.666666, 2)) # redondear a dos decimales. Por ejemplo, 1.666666 redondeado a 2 decimales es 1.67
print(round(1.666666, 3)) # redondear a tres decimales. Por ejemplo, 1.666666 redondeado a 3 decimales es 1.667
print(round(1.666666, 4)) # redondear a cuatro decimales. Por ejemplo, 1.666666 redondeado a 4 decimales es 1.6667
print("Hello, World!".upper()) # convertir a mayúsculas
print("Hello, World!".lower()) # convertir a minúsculas
print("Hello, World!".capitalize()) # convertir la primera letra a mayúscula
print("Hello, World!".title()) # convertir la primera letra de cada palabra a mayúscula
print("Hello, World!".swapcase()) # convertir mayúsculas en minúsculas y viceversa
print("Hello, World!".replace("Hello", "Hi")) # reemplazar una cadena por otra
print("Hello, World!".split(",")) # dividir una cadena en una lista de cadenas
print("Hello, World!".split(" ")) # dividir una cadena en una lista de cadenas
print("Hello, World!".split()) # dividir una cadena en una lista de cadenas
print("   Hello, World!".strip()) # eliminar espacios en blanco al principio y al final
print("Hello  , World!  ".lstrip()) # eliminar espacios en blanco al principio
print("Hello, World!".rstrip()) # eliminar espacios en blanco al final
print("Hello, World!".center(20)) # centrar una cadena
print("Hello, World!".ljust(20)) # alinear a la izquierda una cadena
print("Hello, World!".rjust(20)) # alinear a la derecha una cadena
print("Hello, World!".zfill(20)) # rellenar con ceros a la izquierda una cadena
print("Hello, World!".find("World")) # encontrar la posición de una subcadena
print("Hello, World!".index("World")) # encontrar la posición de una subcadena
print("Hello, World!".count("o")) # contar la cantidad de veces que aparece una subcadena
print("Hello, World!".startswith("Hello")) # verificar si una cadena comienza con una subcadena
