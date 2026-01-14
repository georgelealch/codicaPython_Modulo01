
#############################################################

def cualquiera(dato1, dato2): #MI PRIMERA FUNCION :)
    datos = dato1 + dato2

    return(datos)
    
print(cualquiera(40, 50) * 2) 

###########################################################

def saludar(nombre):
    return f"Hola, {nombre}. Bienvenido"

print(saludar("Alexander"))

#######################################################
#EJEM:
def sum(a, b):
    return (a + b)

a = int(input('Enter 1st number: '))
b = int(input('Enter 2nd number: '))

print(f'Sum of {a} and {b} is {sum(a, b)}')

##########################################################
#EJERCICIO LECCIÓN:

def truncate(text, length):
    mensaje = text[:length] + "..."

    return mensaje

print(truncate("Códica", 2))


