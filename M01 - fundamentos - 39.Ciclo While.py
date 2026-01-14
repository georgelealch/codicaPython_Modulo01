
############# EJERCICIO #############

def print_numbers(number):

    while number > 0:
        print(number)
        number -= 1
    print("finished!")

print_numbers(4)


# 1. La Condición: Usamos > 0 para detenernos antes de imprimir el 0.
# 2. La Acción: Imprimimos antes de restar para mostrar el número actual.
# 3. El Decremento: Restamos 1 para acercarnos a la condición de salida y evitar un bucle infinito.
# 4. El Final: Se ejecuta una sola vez al terminar el ciclo.