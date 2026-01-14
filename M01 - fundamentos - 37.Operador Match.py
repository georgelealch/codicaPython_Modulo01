
def get_number_explanation(special_number):
    match special_number:
        case 666:
            return "Número del diablo."
        case 42:
            return "La respuesta a la pregunta definitiva sobre la vida."
        case 7:
            return "Número de la suerte."
        case _:
            return "Solo un número más."

print(get_number_explanation(666))

# --- Ejemplos Adicionales ---

# 1. Coincidencia de Patrones en Secuencias (Listas/Tuplas)
def procesar_comando(comando):
    match comando:
        case ["salir"]:
            print("Saliendo del programa...")
        case ["cargar", archivo]:
            print(f"Cargando archivo: {archivo}")
        case ["guardar", archivo]:
            print(f"Guardando en: {archivo}")
        case ["mover", x, y]:
            print(f"Moviendo a coordenadas ({x}, {y})")
        case _:
            print("Comando no reconocido")

print("\n--- Secuencias ---")
procesar_comando(["mover", 10, 20])

# 2. Coincidencia con OR (|) y Guardas (if)
def clasificar_edad(edad):
    match edad:
        case n if n < 0:
            print("Error: La edad no puede ser negativa")
        case 0 | 1 | 2:
            print("Es un bebé")
        case n if n < 18:
            print(f"Es un menor de edad ({n} años)")
        case _:
            print("Es un adulto")

print("\n--- Guardas y OR ---")
clasificar_edad(15)
clasificar_edad(1)

# 3. Coincidencia de Diccionarios
def procesar_usuario(usuario):
    match usuario:
        case {"rol": "admin", "nombre": nombre}:
            print(f"Bienvenido Administrador {nombre}")
        case {"rol": "editor", "nombre": nombre}:
            print(f"Hola Editor {nombre}")
        case {"nombre": nombre}:
            print(f"Hola usuario {nombre}")
        case _:
            print("Usuario desconocido")

print("\n--- Diccionarios ---")
procesar_usuario({"rol": "admin", "nombre": "Ana", "id": 123})

# 4. Coincidencia de Clases (Objetos)
class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def ubicar_punto(punto):
    match punto:
        case Punto(x=0, y=0):
            print("Origen")
        case Punto(x=0, y=y):
            print(f"Eje Y (y={y})")
        case Punto(x=x, y=0):
            print(f"Eje X (x={x})")
        case Punto(x=x, y=y) if x == y:
            print(f"En la diagonal (x={x}, y={y})")
        case Punto():
            print("Punto en otro lugar")
        case _:
            print("No es un punto")

print("\n--- Clases ---")
ubicar_punto(Punto(0, 5))
ubicar_punto(Punto(4, 4))