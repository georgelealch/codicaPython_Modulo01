
#TODO ES SOBRE USAR 'RETURN' EN LAS FUNCIONES, PARA USARLAS MAS ADELANTE

#EJEMPLO:
def obtener_descuento():
    return 20  # porcentaje

precio = 100 # guardamos el precio original.
descuento = obtener_descuento() # usamos una función que devuelve el % de descuento.
precio_final = precio - (precio * descuento / 100) # calculamos el precio con descuento.

print(precio_final)  # Muestra: 80.0
#########################################################

#EJEMPLO 2:
def mostrar_y_entregar():
    print("Calculando...")  # Solo muestra un mensaje
    return 42               # Devuelve un valor que puedes usar

resultado = mostrar_y_entregar()  # Muestra: Calculando...
print(resultado)                  # Muestra: 42
#############################################################

def cualquiera(dato1, dato2): #MI PRIMERA FUNCION :)
    datos = dato1 + dato2

    return(datos)
    
print(cualquiera(40, 50) * 2) #AQUI SI FUNCIONA

###########################################################

def personaje_favorito():
    return 'Arya Stak'

print(personaje_favorito())

#################################################
#rol = "estudiante"
#rol = "mentor"
#rol = "admin"
rol = "docente"

if rol == "estudiante":
    print("Bienvenido_Estudiante")
elif rol == "mentor":
    print("Bienvenido_Mentor")
elif rol == "admin":
    print("Acceso_concedido")
else:
    print("quien coño eres?")

################################################
def say_hurray_three_times():
    mesaje = 'hurray! hurray! hurray!'
    return mesaje

result = say_hurray_three_times()
print(result)
