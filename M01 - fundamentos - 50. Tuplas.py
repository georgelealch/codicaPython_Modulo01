
########### EJEM 01 ###############################
def calcular_total(precio, iva):
    total = precio + (precio * iva / 100)
    return precio, total  # ← devolvemos una tupla

base, final = calcular_total(1800, 19)

print("Precio sin IVA:", base)
print("Precio con IVA:", final)


########## EJEM 02 ################################

def mostrar_persona(persona):
    nombre, edad = persona
    print(f"{nombre} tiene {edad} años")

datos = ("Ana", 30)
mostrar_persona(datos)  # → Ana tiene 30 años


############# EJERCICIO ######################

def sort_pair(nums):
    a, b = nums
    if a < b:
        return a, b
    else:                   #debe ser un 'else', pues con el 'elif' no se ejecuta, returna None si la tupla es (5, 5)
        return b, a
    
numeros = (70, 4)
print(sort_pair(numeros))
print(sort_pair((5, 5)))
print(sort_pair((10, 20)))
