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

def return_greet():
    return "Hello, Pablo!" 

print(return_greet())

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
        print(f"Hello, {name}!")

variable_arg_greet("Pablo", "Emilio", "Gómez", "Comunidad")      


# Con un número variable de argumentos con palabras clave

def variable_key_arg_greet(**names):
    for param, name in names.items():  
        print(f"Hello, {name} ({param})!")

variable_key_arg_greet(
    language="Python",
    name="Pablo Emilio Gómez",
    community="Comunidad",
    age=32 
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
print(round(1.6, 1)) 
print(round(1.6, 0)) 
print(round(1.666666, 1)) 
print(round(1.666666, 2)) 
print(round(1.666666, 3)) 
print(round(1.666666, 4)) 
print("Hello, World!".upper()) 
print("Hello, World!".lower()) 
print("Hello, World!".capitalize()) 
print("Hello, World!".title()) 
print("Hello, World!".swapcase()) 
print("Hello, World!".replace("Hello", "Hi")) 
print("Hello, World!".split(",")) 
print("Hello, World!".split(" ")) 
print("Hello, World!".split()) 
print("   Hello, World!".strip()) 
print("Hello  , World!  ".lstrip()) 
print("Hello, World!".rstrip()) 
print("Hello, World!".center(20)) 
print("Hello, World!".ljust(20)) 
print("Hello, World!".rjust(20)) 
print("Hello, World!".zfill(20)) 
print("Hello, World!".find("World")) 
print("Hello, World!".index("World")) 
print("Hello, World!".count("o")) 
print("Hello, World!".startswith("Hello"))

# Variables locales y globales

global_var = "Python01"

print(global_var)

def hello_python():
    local_var = "Hola01"
    print(f"Hello, {global_var}!")

hello_python()

# Crea una función que reciba dos parametros de tipo cadena de texto y retonre un número entero


def print_numbers(text1, text2) -> int:
    count = 0
    for number in range(1, 51):
        if number % 3 == 0 and number % 5 == 0: 
            print(text1 + " " + text2)
        elif number % 3 == 0: 
            print(text1)
        elif number % 5 == 0: 
            print(text2)
        else:
            print(number) 
            count += 1 
    return count 

print_numbers("Texto100", "Texto200") 
print_numbers("Fizz", "Buzz") 
print(print_numbers("Texto100", "Texto200")) 
print(print_numbers("Fizz", "Buzz")) 

