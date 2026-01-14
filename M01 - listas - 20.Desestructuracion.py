import math

def get_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def get_the_nearest_location(locations, current_point):
    if not locations:
        return None

    nearest_location = None
    min_distance = float('inf')

    for location in locations:
        # Destructuring: Desempaquetamos la lista 'location' en nombre y coordenadas
        name, point = location
        
        distance = get_distance(point, current_point)
        
        if distance < min_distance:
            min_distance = distance
            nearest_location = location

    return nearest_location

if __name__ == "__main__":
    locations = [
      ['Park', [10, 5]],
      ['Sea', [1, 3]],
      ['Museum', [8, 4]],
    ]
    current_point = [5, 5]

    print(get_the_nearest_location([], current_point)) # None
    print(get_the_nearest_location(locations, current_point)) # ['Museum', [8, 4]]

# -------------------------------------------------------------------------------------
# Explicación paso a paso para el estudiante:
#
# 1. Función get_distance(point1, point2):
#    - Recibe dos puntos, cada uno es una lista con dos coordenadas [x, y].
#    - Usamos desestructuración 'x1, y1 = point1' para sacar los valores de la lista
#      sin usar índices como point1[0]. Esto hace el código más limpio.

#    - Calculamos la distancia euclidiana usando la fórmula matemática estándar.
#      Explicación de la línea: return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
#      1. (x1 - x2) y (y1 - y2): Calculamos la diferencia entre las coordenadas x e y de los dos puntos.
#         Esto nos dice qué tan lejos están en cada eje (como los lados de un triángulo).
#      2. **2: Elevamos esas diferencias al cuadrado. Esto es necesario porque si la diferencia es negativa,
#         al multiplicarla por sí misma se vuelve positiva (ej: -3 * -3 = 9). También es parte del teorema de Pitágoras.
#      3. +: Sumamos los cuadrados de las diferencias. Esto equivale a a^2 + b^2 en el teorema de Pitágoras.
#      4. math.sqrt(...): Finalmente, sacamos la raíz cuadrada de esa suma para obtener la distancia directa
#         (la hipotenusa del triángulo imaginario que forman los puntos).

# 2. Función get_the_nearest_location(locations, current_point):
#    - Primero verificamos si la lista 'locations' está vacía. Si es así, devolvemos None.
#    - Inicializamos 'min_distance' con infinito (float('inf')) para asegurarnos de que
#      cualquier distancia real que encontremos sea menor que la inicial.
#    - Iteramos sobre cada 'location' en la lista 'locations'.
#
# 3. La Desestructuración (El punto clave):
#    - Dentro del bucle, tenemos 'location', que es una lista como ['Park', [10, 5]].
#    - En lugar de hacer 'name = location[0]' y 'point = location[1]', hacemos:
#      'name, point = location'
#    - Python automáticamente asigna el primer elemento a 'name' y el segundo a 'point'.
#      Esto es lo que llamamos desestructuración o unpacking.
#
# 4. Comparación:
#    - Calculamos la distancia entre el punto actual y el del lugar.
#    - Si encontramos una distancia menor a la mínima registrada hasta ahora, actualizamos
#      nuestra 'min_distance' y guardamos ese lugar como 'nearest_location'.
#
# Al final, devolvemos el lugar que tuvo la menor distancia.
# -------------------------------------------------------------------------------------