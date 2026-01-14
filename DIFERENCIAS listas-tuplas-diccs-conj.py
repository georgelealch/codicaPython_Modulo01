Estructuras de datos en Python: Listas, Tuplas, Diccionarios y Conjuntos
Vamos a explorar cada estructura con ejemplos claros para entender sus diferencias y casos de uso.



📋 Listas (Lists)
Características:

Mutables: Puedes modificarlas después de crearlas

Ordenadas: Mantienen el orden de inserción

Permiten duplicados

Indexadas: Accedes a elementos por posición (0, 1, 2...)

python
# Creación
lista_frutas = ["manzana", "banana", "naranja"]
lista_numeros = [1, 2, 3, 4, 5]
lista_mixta = ["texto", 100, True, 3.14]

# Operaciones comunes
lista_frutas.append("uva")  # Añadir al final
lista_frutas.insert(1, "kiwi")  # Insertar en posición específica
lista_frutas.remove("banana")  # Eliminar elemento
ultimo = lista_frutas.pop()  # Eliminar y devolver último elemento

# Acceso
primer_elemento = lista_frutas[0]  # "manzana"
sublista = lista_frutas[1:3]  # ["kiwi", "naranja"]

# Modificación
lista_frutas[0] = "sandía"  # Cambiar un elemento

print(lista_frutas)  # ['sandía', 'kiwi', 'naranja']
📌 Casos de uso:

Cuando necesitas una colección ordenada que cambiará (añadir/eliminar elementos)

Para procesar secuencias de elementos uno por uno

Almacenar resultados que se van acumulando



🔒 Tuplas (Tuples)
Características:

Inmutables: No se pueden modificar después de crearlas

Ordenadas: Mantienen el orden de inserción

Permiten duplicados

Indexadas: Accedes a elementos por posición

Más eficientes que las listas en memoria

python
# Creación (paréntesis son opcionales pero recomendables)
coordenadas = (10, 20)
colores = "rojo", "verde", "azul"
punto_3d = (5.0, 3.5, 2.0)

# Acceso
x = coordenadas[0]  # 10
y = coordenadas[1]  # 20

# Desempaquetado
a, b = coordenadas  # a=10, b=20
r, g, b = colores  # r="rojo", g="verde", b="azul"

# Intento de modificación (ERROR)
# coordenadas[0] = 15  # TypeError: 'tuple' object does not support item assignment

# Tuplas de un elemento (¡necesita coma!)
tupla_unitaria = (5,)  # Correcto
no_tupla = (5)  # Esto es solo el entero 5

# Conversión
lista_a_tupla = tuple([1, 2, 3])  # (1, 2, 3)
tupla_a_lista = list((1, 2, 3))   # [1, 2, 3]
📌 Casos de uso:

Cuando quieres asegurar que los datos no cambien (coordenadas, configuraciones)

Para devolver múltiples valores desde una función

Como claves en diccionarios (las listas no pueden ser claves)

Para datos fijos que no deben modificarse



📖 Diccionarios (Dictionaries)
Características:

Mutables: Puedes modificarlos

No ordenados (hasta Python 3.7) / Ordenados de inserción (Python 3.7+)

Clave-Valor: Accedes por clave, no por índice

Claves únicas: No se permiten duplicados en las claves

Claves deben ser inmutables (strings, números, tuplas)

python
# Creación
estudiante = {
    "nombre": "Carlos",
    "edad": 22,
    "curso": "Python",
    "aprobado": True
}

# Otra forma de crear
calificaciones = dict(matematicas=9.5, historia=8.0, fisica=7.5)

# Acceso
nombre = estudiante["nombre"]  # "Carlos"
edad = estudiante.get("edad")  # 22 (método get, evita KeyError)

# Añadir o modificar
estudiante["ciudad"] = "Madrid"  # Añade nueva clave
estudiante["edad"] = 23  # Modifica valor existente

# Eliminar
valor_eliminado = estudiante.pop("curso")  # Elimina y devuelve valor
del estudiante["aprobado"]  # Elimina sin devolver

# Métodos útiles
claves = estudiante.keys()     # dict_keys(['nombre', 'edad', 'ciudad'])
valores = estudiante.values()  # dict_values(['Carlos', 23, 'Madrid'])
items = estudiante.items()     # dict_items([('nombre', 'Carlos'), ...])

# Recorrer
for clave, valor in estudiante.items():
    print(f"{clave}: {valor}")
📌 Casos de uso:

Cuando necesitas asociar claves con valores (como un diccionario real)

Para almacenar datos estructurados (como JSON)

Contadores o frecuencias

Configuraciones o parámetros con nombres descriptivos



🌀 Conjuntos (Sets)
Características:

Mutables (pero los elementos deben ser inmutables)

No ordenados (hasta Python 3.7) / Ordenados de inserción (Python 3.7+)

No permiten duplicados: Elementos únicos automáticamente

No indexados: No puedes acceder por posición

Optimizados para operaciones de pertenencia (ver si algo está en el conjunto)

python
# Creación
vocales = {"a", "e", "i", "o", "u"}
numeros = {1, 2, 3, 4, 5}

# Con duplicados (se eliminan automáticamente)
con_duplicados = {1, 2, 2, 3, 3, 3}  # {1, 2, 3}

# Añadir elementos
vocales.add("y")  # {'a', 'e', 'i', 'o', 'u', 'y'}

# Eliminar elementos
vocales.remove("y")  # Elimina, error si no existe
vocales.discard("z")  # Elimina si existe, sin error si no

# Operaciones de conjuntos
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

union = A | B  # {1, 2, 3, 4, 5, 6}  (también A.union(B))
interseccion = A & B  # {3, 4}  (también A.intersection(B))
diferencia = A - B  # {1, 2}  (también A.difference(B))
diferencia_simetrica = A ^ B  # {1, 2, 5, 6}

# Verificar pertenencia
print(3 in A)  # True
print(7 in A)  # False

# Conjunto inmutable (frozenset)
inmutable = frozenset([1, 2, 3])
# inmutable.add(4)  # ERROR: los frozenset son inmutables
📌 Casos de uso:

Eliminar duplicados de una lista: list(set(mi_lista))

Operaciones matemáticas de conjuntos (unión, intersección, etc.)

Verificar pertenencia de forma eficiente

Para manejar colecciones de elementos únicos (etiquetas, categorías)



📊 Resumen Comparativo
Característica	Lista	Tupla	Diccionario	Conjunto
Mutabilidad	✅ Sí	❌ No	✅ Sí	✅ Sí (elementos inmutables)
Orden	✅ Sí	✅ Sí	✅ Sí (3.7+)	✅ Sí (3.7+)
Indexación	✅ Por posición	✅ Por posición	❌ Por clave	❌ No
Duplicados	✅ Permitidos	✅ Permitidos	❌ Claves únicas	❌ No permitidos
Sintaxis	[]	()	{k:v}	{} (con elementos)
Velocidad búsqueda	Lenta (O(n))	Lenta (O(n))	Muy rápida (O(1))	Muy rápida (O(1))
Uso memoria	Moderado	Bajo	Moderado/Alto	Moderado



🎯 Ejemplo Práctico Integrado
python
# SIMULACIÓN DE UN SISTEMA DE ESTUDIANTES

# TUPLA: Datos fijos de configuración
CURSOS_DISPONIBLES = ("Matemáticas", "Historia", "Programación", "Inglés")

# LISTA: Colección ordenada que cambia (estudiantes matriculados)
estudiantes_matriculados = ["Ana", "Luis", "María"]

# DICCIONARIO: Datos estructurados de cada estudiante
calificaciones = {
    "Ana": {"Matemáticas": 9.0, "Programación": 8.5},
    "Luis": {"Historia": 7.0, "Inglés": 6.5},
    "María": {"Matemáticas": 8.0, "Historia": 9.5}
}

# CONJUNTO: Materias únicas que se están cursando
materias_activas = {"Matemáticas", "Historia", "Programación", "Inglés"}

# OPERACIONES DEL SISTEMA
print(f"Cursos disponibles (fijos): {CURSOS_DISPONIBLES}")

# Añadir nuevo estudiante (lista)
estudiantes_matriculados.append("Carlos")
print(f"Estudiantes: {estudiantes_matriculados}")

# Registrar calificaciones (diccionario)
calificaciones["Carlos"] = {"Programación": 7.5, "Inglés": 8.0}
print(f"Calificaciones de Carlos: {calificaciones['Carlos']}")

# Añadir nueva materia (conjunto)
materias_activas.add("Física")
print(f"Materias activas: {materias_activas}")

# Verificar si una materia existe (conjunto es eficiente para esto)
if "Programación" in materias_activas:
    print("Programación es una materia activa")

# Obtener primer estudiante (lista mantiene orden)
print(f"Primer estudiante matriculado: {estudiantes_matriculados[0]}")

# Intentar modificar tupla (esto daría error)
# CURSOS_DISPONIBLES[0] = "Álgebra"  # TypeError



💡 Consejos para elegir
Usa lista cuando:

El orden importa

Necesitas modificar (añadir/eliminar) elementos

Quieres elementos duplicados

Usa tupla cuando:

Los datos no deben cambiar

Necesitas usar la colección como clave en un diccionario

Quieres garantizar la integridad de los datos

Usa diccionario cuando:

Necesitas asociar claves con valores

El acceso rápido por clave es importante

Los datos tienen estructura de "atributo-valor"

Usa conjunto cuando:

Necesitas eliminar duplicados automáticamente

Las operaciones de conjuntos (unión, intersección) son útiles

La verificación de pertenencia es frecuente y debe ser rápida

Esta guía debería ayudarte a decidir qué estructura usar en cada situación. ¡La práctica es clave para interiorizarlo!

