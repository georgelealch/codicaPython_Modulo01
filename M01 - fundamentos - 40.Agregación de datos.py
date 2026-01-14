########## EJEMPLO 1 ########## 
def sum_numbers_from_range(start, end):
    i = start
    total = 0
    while i <= end:
        total += i
        i += 1
    return total

print(sum_numbers_from_range(5, 7))

############ EJEMPLO 2 ############
def repeat(text, times):
    result = ''
    i = 1
    while i <= times:
        result = result + text
        i = i + 1
    return result

print(repeat('hola', 3))


############ EJEMPLO 3 ############
def multiply_numbers_from_range(start, finish):
    i = start
    multiply = 1
    while i <= finish:
        multiply *= i
        i += 1
    return multiply

print(multiply_numbers_from_range(5, 7))

"""
EXPLICACIÓN DE LOS CASOS:

EJEMPLO 1: Suma acumulativa
En este caso, la variable 'total' actúa como un acumulador numérico. Se inicializa en 0 y, en cada iteración del ciclo, se le suma el valor actual de 'i'. 
Al final, contiene la suma total de todos los números del rango.

EJEMPLO 2: Concatenación de cadenas
Aquí, la variable 'result' es un acumulador de texto. Se inicializa vacía y, en cada vuelta del ciclo, se le "pega" (concatena) el texto recibido. 
Es una agregación de caracteres para formar una cadena más larga.

EJEMPLO 3: Producto acumulativo
Similar al primer ejemplo, pero la operación es multiplicación. La variable 'multiply' se inicializa en 1 (neutro multiplicativo) para no afectar el resultado. 
En cada paso, se actualiza multiplicando su valor anterior por el nuevo número, resultando en el producto de todos los elementos.
"""


def join_numbers_from_range(start, finish):
    result = ''
    i = start # i debe ser igual a start para que funcione
    while i <= finish:
        result = result + str(i)
        i += 1
    return result

print(join_numbers_from_range(5, 10))




