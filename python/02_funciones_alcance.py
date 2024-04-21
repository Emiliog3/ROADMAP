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