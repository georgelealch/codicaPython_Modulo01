from TEMATICAS.hash_table import get_hash

class HashTable(list):
    """
    Subclase de lista para agregar el método .set() simulando el comportamiento del ejercicio.
    """
    def set(self, key, value):
        index = get_hash(key)
        if index >= len(self):
            self.extend([None] * (index - len(self) + 1))
        
        self[index] = (key, value)

def make_table():
    """
    Crea una HashTable inicializada con valores None.
    Para el ejemplo, un tamaño inicial de 10 es suficiente.
    """
    table = HashTable([None] * 10)
    return table

def get_or_default(hash_table, key, default):
    """
    Busca el valor asociado a una clave en la tabla hash.
    Si la clave no existe o el índice está vacío/tiene otra clave, devuelve default.
    """
    index = get_hash(key)
    
    if 0 <= index < len(hash_table):
        item = hash_table[index]
        if item is not None:
            stored_key, stored_value = item
            if stored_key == key:
                return stored_value
    
    return default

# --- Código de prueba del ejercicio ---

hash_table = make_table()
# El método set(clave, valor) guarda un valor asociado a una clave en el mapa
hash_table.set("g", "bar")
hash_table.set("e", "foo")

print(get_or_default(hash_table, "g", "python")) # Debería imprimir: bar
print(get_or_default(hash_table, "a", "python")) # Debería imprimir: python

# Verificación interna de la estructura
hash_table = make_table()
hash_table.set("e", "foo")
hash_table.set("f", "baz")
hash_table.set("g", "bar")

# Nota: El print puede mostrar más Nones de los que pide el ejercicio exacto 
# porque inicialicé la lista con tamaño fijo, pero la lógica de índices es la misma.
print(hash_table) 

# ==========================================
# EXPLICACIÓN PASO A PASO
# ==========================================
# 
# 1. La Función Hash (`get_hash`):
#    - Se importa del módulo `TEMATICAS.hash_table`.
#    - Esta función convierte la clave (string) en un número (índice) utilizando la suma de los valores ASCII
#      de sus caracteres, módulo 10, más 1.
#    - Por ejemplo, para la clave 'g', calcula el índice donde debe almacenarse.
#    - Esto nos permite saltar directamente a la posición probable del dato sin buscar en toda la lista.
#
# 2. La Estructura de Datos (`hash_table`):
#    - Es una lista que actúa como tabla hash.
#    - Cada posición puede contener `None` (vacío) o una tupla `(clave, valor)`.
#
# 3. La Función `get_or_default(hash_table, key, default)`:
#    
#    Paso A: Calcular el Índice
#    - Se llama a `get_hash(key)` para obtener el índice correspondiente a la clave buscada.
#    
#    Paso B: Verificar Límites
#    - Se comprueba si el índice calculado está dentro del rango válido de la lista `hash_table`.
#    - Si el índice está fuera de los límites, significa que la clave definitivamente no está, 
#      así que devolvemos el valor por defecto.
#
#    Paso C: Buscar en la Posición
#    - Si el índice es válido, miramos el contenido en `hash_table[index]`.
#    - Si encontramos `None`, la clave no está.
#    - Si encontramos un elemento (tupla), verificamos si la clave almacenada coincide con la clave buscada (`stored_key == key`).
#      - Si coincide, devolvemos el valor asociado (`stored_value`).
#      
#    Paso D: Retorno por Defecto
#    - Si no encontramos la clave en el paso C (ya sea porque la celda estaba vacía o porque contenía otra clave en caso de colisión),
#      la función devuelve el valor `default`.
#
# Resumen:
# La función utiliza el índice calculado matemáticamente para acceder directamente a la posible ubicación del elemento,
# verificando su existencia y coincidencia antes de devolver el valor o el default.