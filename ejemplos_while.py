"""
Ejemplos educativos del ciclo 'while' en Python.
Este archivo muestra diferentes formas de usar 'while' para repetir acciones.
"""

import time

def separador(titulo):
    print("\n" + "="*40)
    print(f" {titulo}")
    print("="*40)

# ---------------------------------------------------------
# EJEMPLO 1: Contador simple
# ---------------------------------------------------------
# Este es el uso más básico: repetir algo un número fijo de veces.
separador("EJEMPLO 1: Contador del 1 al 5")

contador = 1
while contador <= 5:
    print(f"Contando: {contador}")
    contador += 1  # ¡Importante! Aumentar el contador para no crear un bucle infinito.
    time.sleep(0.5) # Pausa pequeña para ver el efecto

print("¡Terminó el conteo!")


# ---------------------------------------------------------
# EJEMPLO 2: Validación de entrada (Simulada)
# ---------------------------------------------------------
# Muy útil para pedir datos al usuario hasta que ingrese lo correcto.
separador("EJEMPLO 2: Adivina el número secreto (es 7)")

numero_secreto = 7
intento = 0

# Simulamos entradas del usuario para este ejemplo automático
# En un programa real usarías: intento = int(input("Adivina: "))
entradas_simuladas = [1, 3, 10, 7] 
indice = 0

while intento != numero_secreto:
    if indice < len(entradas_simuladas):
        intento = entradas_simuladas[indice]
        print(f"Usuario ingresa: {intento}")
        indice += 1
        
        if intento != numero_secreto:
            print("Incorrecto, intenta de nuevo...")
        else:
            print("¡Correcto! Adivinaste el número.")
    else:
        break # Seguridad por si se acaban las entradas simuladas


# ---------------------------------------------------------
# EJEMPLO 3: Uso de 'break' (Romper el ciclo)
# ---------------------------------------------------------
# 'break' permite salir del ciclo inmediatamente, sin esperar a la condición.
separador("EJEMPLO 3: Detener un bucle infinito con 'break'")

numero = 0
while True: # 'True' crea un bucle que nunca terminaría por sí solo
    print(f"El número es {numero}")
    if numero == 3:
        print("¡Se encontró el 3! Rompiendo el ciclo con 'break'.")
        break # Salimos del while aquí mismo
    numero += 1


# ---------------------------------------------------------
# EJEMPLO 4: Uso de 'continue' (Saltar iteración)
# ---------------------------------------------------------
# 'continue' salta el resto del código en esa vuelta y vuelve al inicio del while.
separador("EJEMPLO 4: Imprimir solo números impares (saltando pares)")

n = 0
while n < 6:
    n += 1
    if n % 2 == 0: # Si el número es par
        print(f"Saltando el número par {n} con 'continue'")
        continue # Vuelve arriba a la condición 'while', ignorando el print de abajo
    
    print(f"-> Número impar procesado: {n}")

print("\nFin de los ejemplos.")
