
############ PRUEBA RANDOM ###############################
def get_age_difference(valor1, valor2):
    resta = abs(valor2 - valor1)
    return f'The age difference is {resta}'

print(get_age_difference(2000, 3000))

########## REPASO DE FUNCIONES ########################

def verificar_stock(producto, cantidad_disponible, cantidad_solicitada):
    
    if cantidad_disponible >= cantidad_solicitada:
        return True
    elif cantidad_disponible <= cantidad_solicitada:
        return False
    
#print(verificar_stock("medias", 0, 3))

def calcular_total(precio_unitario: int, cantidad: int) -> int:
    return(precio_unitario * cantidad)

#print(calcular_total(1200, 3))

def mostrar_ticket(nombre_cliente, producto, precio_unitario, cantidad_solicitada):
    hay_producto = verificar_stock('medias', 2, 3)
    total = precio_unitario * cantidad_solicitada

    if hay_producto == True:
        return(f'Señor {nombre_cliente}, usted ha comprado {cantidad_solicitada} pares de {producto}; cada una con un valor de {precio_unitario}, para un valor total de {total}')
    else:
        return(f'lo sentimos, señor {nombre_cliente}, no hay suficiente stock en bodega')
        

print(mostrar_ticket('Jorge', 'Medias', 1200, 3))

####################################################################
#EJERCICIOS:

def mostrar(nombre, mensaje="Hola"):
    print(mensaje, nombre)

mostrar("Arya", mensaje="¡Hey!")


def cuadrado(n):
    return n * n

print(cuadrado(4))


def enviar_mensaje(mensaje):
    print(mensaje)

enviar_mensaje("¡Dracarys!")