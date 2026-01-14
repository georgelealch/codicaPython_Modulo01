
##############################################

# USO DE f PARA UNIR CADENAS DE TEXTO
mensaje = f"hola como estas, "
mensaje += f"espero que muy bien, "
mensaje += f"no te olvides de mi"

print(mensaje)

###############################################

# EJEMPLO DE CÓDIGO:
nombre = " ana "
producto = "Curso de Python"
precio = 35
moneda = "usd"

mensaje3 = f"Hola, {nombre.strip().capitalize()}!\n"
mensaje3 += f"Te interesa: {producto.upper()}\n"
mensaje3 += f"Precio: {round(precio, 2)} {moneda.upper()}"

print(mensaje3)


###############################################


#EJERCICIO NO OBLIGATORIO
nombre_cliente = " jorge "
producto = "curso python"
precio_unitario = 1432000
cantidad = 1
moneda = "pesos"

mensaje2 = f"Hola, {nombre_cliente.strip().capitalize() }. "
mensaje2 += f"Nos alegra saber que estas interesado en el {producto.upper()}, "
mensaje2 += f"el cual tiene un valor de: {precio_unitario} {moneda.upper()}. "
mensaje2 += f"Por esta compra tienes el envío totalmente incluido."

print(mensaje2)

##################################################

help(len) #SIRVE PARA BUSCAR INFORMACIÓN EN LA DOCUMENTACION DE FUNCIONES, EN ESTE CASO SOBRE LA FUNCION LEN()

nombre = "enano"
nombre_completo = len(nombre) * 2
print(nombre_completo)