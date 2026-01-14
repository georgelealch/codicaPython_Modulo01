
######### EJEMPLO ################

def saludar(nombre, edad):
    return f"Hola, {nombre}. Tienes {edad} años."

print(saludar("Ana", 25))  # Hola, Ana. Tienes 25 años. #ESTOS SON ARGUMENTOS POSICIONALES, QUE DEBEN NOMBRARSE EN EL MISMO ORDEN DE LOS PARAMENTROS DE ENTRADA

print(saludar(edad=25, nombre="Ana"))  # Hola, Ana. Tienes 25 años. ESTOS SON 'NOMBRAADOS', QUE, INDEPENDIENTEMENTE DE LA POSICIÓN, IMPRIME BIEN EL RESULTADO

#Puedes usar los dos tipos en una llamada, pero los posicionales siempre deben ir primero:
#crear_usuario("Marta", False, edad=25)  # Correcto
#crear_usuario(nombre="Marta", False, edad=25)  # Error

#############################################

def trim_and_repeat(text, offset=0, repetitions=1):
    mensaje = f"{text[offset:]}" * repetitions


    return mensaje

print(trim_and_repeat("Holassss!", 2, 6))

#############################################

#EJERCICIOS:
def saludar_2(nombre: str) -> str:
    return "Hola, " + nombre

print(saludar_2("Luisito"))


################################################
def letter_multiply(text: str, letra: str, numero: int) -> str:
    text_r = text.replace(letra, letra * numero)
    return f'{text_r}'

print(letter_multiply('python', 'p', 10))