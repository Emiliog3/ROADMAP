# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-


"""
Operadores

"""

# Operadores aritméticos
# Suma
# Suma dos números. Ejemplo 01:  2 + 3 = 5. Ejemplo 02: 2 + 4 = 6
print(2 + 3)
print(2 + 4)

# Resta
# Resta dos números. Ejemplo 01: 2 - 3 = -1. Ejemplo 02: 2 - 5 = -3
print(2 - 3)
print(2 - 5)

# Multiplicación
# Multiplica dos números. Ejemplo 01: 2 * 3 = 6. Ejemplo 02: 2 * 5 = 10
print(2 * 3)
print(2 * 5)

# División
# Divide dos números. Ejemplo 1: 2 / 3 = 0.6666666666666666. Ejemplo 2: 2 / 4 = 0.5
print(2 / 3)
print(2 / 4)

# División entera
# Devuelve la parte entera de la división. Ejemplo 1: 2 // 3 = 0. Ejemplo 2: 2 // 4 = 0
print(2 // 3)
print(2 // 4)

# Módulo
# Devuelve el residuo de la división. Ejemplo 1: 2 % 3 = 2. Ejemplo 2: 2 % 5 = 2
print(2 % 3)
print(2 % 5)

# Potencia
# Eleva un número a la potencia de otro. Ejemplo 1: 2 ** 3 = 8. Ejemplo 2: 2 ** 5 = 32
print(2 ** 3)
print(2 ** 5)

# Operadores de comparación

# Igualdad
# Comparan dos valores y devuelven un valor booleano. Ejemplo 1: 2 == 3 = False. Ejemplo 2: 2 == 2 = True
print(2 == 3)
print(2 == 2)

# Diferencia
# Comprueba si dos valores son diferentes. Ejemplo 1: 2 != 3 = True. Ejemplo 2: 2 != 5 = True
print(2 != 3)
print(2 != 5)

# Mayor que
# Comprueba si un valor es mayor que otro. Ejemplo 1: 2 > 3 = False. Ejemplo 2: 2 > 1 = True
print(2 > 3)
print(2 > 1)

# Menor que
# Comprueba si un valor es menor que otro. Ejemplo 1: 2 < 3 = True. Ejemplo 2: 2 < 1 = False
print(2 < 3)
print(2 < 1)

# Mayor o igual que
# Comprueba si un valor es mayor o igual que otro. Ejemplo 1: 2 >= 3 = False. Ejemplo 2: 2 >= 2 = True
print(2 >= 3)
print(2 >= 2)

# Menor o igual que
# Comprueba si un valor es menor o igual que otro. Ejemplo 1: 2 <= 3 = True. Ejemplo 2: 2 <= 2 = True
print(2 <= 3)
print(2 <= 2)

# Operadores lógicos
# and
# Devuelve True si ambos valores son True. Ejemplo 1: True and False = False. Ejemplo 2: True and True = True
print(True and False)
print(True and True)

# or
# Devuelve True si al menos uno de los valores es True. Ejemplo 1: True or False = True. Ejemplo 2: True or True = True
print(True or False)
print(True or True)

# not
# Devuelve el valor contrario. Ejemplo 1: not True = False. Ejemplo 2: not False = True
print(not True)
print(not False)

# Operadores de asignación

# Asignación
# Asigna un valor a una variable. Ejemplo 1: a = 2. Ejemplo 2: b = 3
a = 2
b = 3
print(a)
print(b)

# Suma y asignación
# Suma un valor a una variable y lo asigna. Ejemplo 1: a += 3. Ejemplo 2: a += 5
a += 3
print(a)

# Resta y asignación
# Resta un valor a una variable y lo asigna. Ejemplo 1: a -= 3. Ejemplo 2: a -= 5
a -= 3
print(a)
a -= 5
print(a)

# Multiplicación y asignación
# Multiplica un valor a una variable y lo asigna. Ejemplo 1: a *= 3. Ejemplo 2: a *= 5
a *= 3
print(a)
a *= 5
print(a)

# División y asignación
# Divide un valor a una variable y lo asigna. Ejemplo 1: a /= 3. Ejemplo 2: a /= 5
a /= 3
print(a)
a /= 5
print(a)

# División entera y asignación
# Divide entero un valor a una variable y lo asigna. Ejemplo 1: a //= 3. Ejemplo 2: a //= 5
a //= 3
print(a)
a //= 5
print(a)

# Módulo y asignación
# Calcula el módulo de un valor a una variable y lo asigna. Ejemplo 1: a %= 3. Ejemplo 2: a %= 5
a %= 3
print(a)
a %= 5
print(a)

# Potencia y asignación
# Eleva un valor a una potencia y lo asigna. Ejemplo 1: a **= 3. Ejemplo 2: a **= 5
a **= 3
print(a)
a **= 5
print(a)

# Operadores de identidad

# is
# Comprueba si dos variables son el mismo objeto. Ejemplo 1: a is b = False. Ejemplo 2: a is a = True
a = 5
b = 2
print(a is b)
print(a is a)

# is not
# Comprueba si dos variables no son el mismo objeto. Ejemplo 1: a is not b = True. Ejemplo 2: a is not a = False
print(a is not b)
print(a is not a)

# Operadores de membresía
# in
# Comprueba si un valor está en una lista. Ejemplo 1: 1 in my_list = True. Ejemplo 2: 4 in my_list = False
my_list = [1, 2, 3]
print(1 in my_list)
print(4 in my_list)

# not in
# Comprueba si un valor no está en una lista. Ejemplo 1: 1 not in my_list = False. Ejemplo 2: 4 not in my_list = True
print(1 not in my_list)
print(4 not in my_list)

# Operador de concatenación

# +
# Concatena dos strings. Ejemplo 1: "Hola" + " " + "mundo" = "Hola mundo". Ejemplo 2: "Hola" + " " + "Pablo" = "Hola Pablo"
print("Hola" + " " + "mundo")
print("Hola" + " " + "Pablo")

# Operador de repetición
# *
# Repite un string. Ejemplo 1: "Hola" * 3 = "HolaHolaHola". Ejemplo 2: "Hola" * 5 = "HolaHolaHolaHolaHola"
print("Hola" * 3)
print("Hola" * 5)

# Operador de indexación
# []
# Devuelve un elemento de una lista. Ejemplo 1: my_list[0] = 1. Ejemplo 2: my_list[2] = 3
my_list = [1, 2, 3]
print(my_list[0])
print(my_list[2])

# Operador de slicing
# [:]
# Devuelve una sublista. Ejemplo 1: my_list[0:2] = [1, 2]. Ejemplo 2: my_list[1:3] = [2, 3]
print(my_list[0:2])
print(my_list[1:3])

# Operador de longitud
# len()
# Devuelve la longitud de una lista. Ejemplo 1: len(my_list) = 3. Ejemplo 2: len(my_other_list) = 5
my_list = [1, 2, 3]
my_other_list = [1, 2, 3, 4, 5]
print(len(my_list))
print(len(my_other_list))

# Operador de pertenencia
# in
# Comprueba si un valor está en una lista. Ejemplo 1: 1 in my_list = True. Ejemplo 2: 4 in my_list = False
my_list = [1, 2, 3]
print(1 in my_list)
print(4 in my_list)

# Operador de identidad
# is
# Comprueba si dos variables son el mismo objeto. Ejemplo 1: a is b = False. Ejemplo 2: a is a = True
a is b
a is a
print(a is b)
print(a is a)

# Operador de asignación
# =
# Asigna un valor a una variable. Ejemplo 1: a = 2. Ejemplo 2: b = 3
a = 2
b = 3
print(a)
print(b)



# Ejemplos de Operadores aritméticos

print(f"Suma: 10 + 3 = {10 + 3}") # Este es un concepto de interpolación de cadenas. Esto siginfica que se puede insertar una variable en una cadena de texto.
print(f"Resta: 10 - 3 = {10 - 3}")
print(f"Multiplicación: 10 * 3 = {10 * 3}")
print(f"División: 10 / 3 = {10 / 3}")
print(f"División entera: 10 // 3 = {10 // 3}")
print(f"Módulo: 10 % 3 = {10 % 3}")
print(f"Potencia: 10 ** 3 = {10 ** 3}")
print(f"Exponente: 10 ** 3 = {10 ** 3}")

# Ejemplos de Operadores de comparación

print(f"Igualdad: 10 == 3 = {10 == 3}")
print(f"Diferencia: 10 != 3 = {10 != 3}")
print(f"Mayor que: 10 > 3 = {10 > 3}")
print(f"Menor que: 10 < 3 = {10 < 3}")
print(f"Mayor o igual que: 10 >= 3 = {10 >= 3}")
print(f"Menor o igual que: 10 <= 3 = {10 <= 3}")


# Ejemplos de Operadores lógicos

print(f"AND: True and False = {True and False}")
print(f"AND: 10 + 3 == 13 AND 5 - 1 == 4 = {10 + 3 == 13 and 5 - 1 == 4}")
print(f"OR: True or False = {True or False}")
print(f"OR: 10 + 3 == 13 OR 5 - 1 == 4 = {10 + 3 == 13 or 5 - 1 == 4}")
print(f"not: not True = {not True}")
print(f"NOT: not 10 + 3 == 13 = {not 10 + 3 == 13}")
print(f"NOT: not 10 + 3 == 14 = {not 10 + 3 == 14}")

# Ejemplos de Operadores de asignación
# Asignación
my_number = 10
print(my_number)

# Suma y asignación
my_number += 3
print(my_number)

# Resta y asignación
my_number -= 5
print(my_number)

# Multiplicación y asignación
my_number *= 2
print(my_number)

# División y asignación
my_number /= 4

# División entera y asignación
my_number //= 2
print(my_number)

# Módulo y asignación
my_number %= 3
print(my_number)

# Potencia y asignación
my_number **= 2
print(my_number)

# Ejemplos de Operadores de identidad
# Sirve para comparar si dos variables son el mismo objeto
my_new_number = 10
print(my_number is my_new_number)

my_new_number = my_number
print(my_number is my_new_number)
print(my_number is not my_new_number)

# Ejemplos de Operadores de membresía o pertenencia
# Sirve para saber si un valor está en una lista o pertenece a una lista
my_list = [1, 2, 3, 4, 5]
print(1 in my_list)
print(6 in my_list)
print(f" 'u' in 'moure = {'u' in 'moure'}")
print(f" 'u' not in 'moure = {'u' not in 'moure'}")
print(f" 'b' in 'moure = {'b' in 'moure'}")
print(f" 'b' not in 'moure = {'b' not in 'moure'}")


# Ejemplos de operadores de bits
# Sirve para hacer operaciones con bits. Es decir, con números en binario.
# & (AND)
# | (OR)
# ^ (XOR)
# ~ (NOT)
# << (Desplazamiento a la izquierda)
# >> (Desplazamiento a la derecha)

# Número binarios del 0 al 20
"""
0 = 0000
1 = 0001
2 = 0010
3 = 0011
4 = 0100
5 = 0101
6 = 0110
7 = 0111
8 = 1000
9 = 1001
10 = 1010
11 = 1011
12 = 1100
13 = 1101
14 = 1110
15 = 1111
16 = 10000
17 = 10001
18 = 10010
19 = 10011
20 = 10100

"""

a = 10 # 1010
b = 3 # 0011
print(f"AND: {a} & {b} = {a & b}") # 1010 & 0011 = 0010 porque 1 & 1 = 1, 0 & 0 = 0, 1 & 0 = 0, 0 & 1 = 0. 0010 = 2
print(f"OR: {a} | {b} = {a | b}") # 1010 | 0011 = 1011 porque 1 | 1 = 1, 0 | 0 = 0, 1 | 0 = 1, 0 | 1 = 1. 1011 = 11
print(f"AND: 10 & 3 = {10 & 3}") # 1010 & 0011 = 0010 porque 1 & 1 = 1, 0 & 0 = 0, 1 & 0 = 0, 0 & 1 = 0. 0010 = 2
print(f"OR: 10 | 3 = {10 | 3}") # 1010 | 0011 = 1011 porque 1 | 1 = 1, 0 | 0 = 0, 1 | 0 = 1, 0 | 1 = 1. 1011 = 11
print(f"XOR: 10 ^ 3 = {10 ^ 3}") # 1010 ^ 0011 = 1001 porque 1 ^ 1 = 0, 0 ^ 0 = 0, 1 ^ 0 = 1, 0 ^ 1 = 1. 1010 = 10 y 1001 = 9
print(f"NOT: ~10 = {~10}") # ~1010 = -11 porque ~1010 = -11 y -11 = -11
print(f"Desplazamiento a la izquierda: 10 << 1 = {10 << 1}") # 1010 << 1 = 10100 porque 1010 << 1 = 10100 y 10100 = 20
print(f"Desplazamiento a la derecha: 10 >> 1 = {10 >> 1}") # 1010 >> 1 = 101 porque 1010 >> 1 = 101 y 101 = 5

# Estructuras de control


# Condicionales
# Sirve para tomar decisiones en un programa si se cumple una condición
my_string = "Braise"
if my_string == "Mouredev":
    print("Mi string es igual a Mouredev")
elif my_string == "Braise":
    print("Mi string es igual a Braise")
else:
    print("Mi string no es igual a Mouredev, ni braise")


# Iteraciones
# Sirve para repetir un bloque de código varias veces

for i in range(11):
    print(f"Valor de i: {i}")

for i in range(5):
    print(i)

i = 0

while i <= 10:
    print(f"Valor de i: {i}")
    i += 1


# Manejo de excepciones
# Sirve para manejar errores en un programa
# try sirve para intentar ejecutar un bloque de código y que nuestro programa no se detenga si hay un error

try:
    print (10 / 0)
except:
    print("Ha ocurrido un error")

finally:
    print("Ha finalizado el manejo de excepciones")


try:
    print (10 / 1)
except:
    print("Ha ocurrido un error")

finally:
    print("Ha finalizado el manejo de excepciones")


# Ejercicio de operadores

i = 0

while i <= 55:
    print(f"Valor de i: {i}")
    i += 1

for number in range (10, 56):
    print (number)


# Ejercicio con impares
for number in range (10, 56):
    if number % 2 != 0:
        print (number)

# Ejercicio con pares
for number in range (10, 56):
    if number % 2 == 0:
        print (number)

# Ejercicio con pares y una exclusión
for number in range (10, 56):
    if number % 2 == 0 and number != 16:
        print (number)

# Ejercicio con pares y varias exclusiones
for number in range (10, 56):
    if number % 2 == 0 and number != 16 and number != 20 and number != 30:
        print (number)


# Ejercicio con pares y varias exclusiones
for number in range (10, 56):
    if number % 2 == 0 and number != 16 and number != 20 and number != 30 and number %3 != 0:
        print (number)


# Ejercicio con pares y varias exclusiones

for number in range(10, 56):
    if number % 2 == 0 and number not in [16, 24, 28]:
        print(number)




