def make_user(name, age):
    user = {
        'name': name,
        'age': age
    }
    return user


def format_user(user):
    return f"{user['name']}, {user['age']}"

print(format_user(make_user('John', 30)))

"""
Explicación paso a paso:

1.  **Función `make_user(name, age)`**:
    -   Esta función recibe dos argumentos: `name` (nombre) y `age` (edad).
    -   Dentro de la función, creamos un diccionario llamado `user`.
    -   Asignamos las claves `'name'` y `'age'` con los valores que recibimos en los argumentos.
    -   Finalmente, retornamos ese diccionario recién creado.

2.  **Función `format_user(user)`**:
    -   Esta función recibe un argumento `user`, que esperamos que sea el diccionario que creó `make_user`.
    -   Para obtener el resultado deseado ('Nombre, Edad'), accedemos directamente a los valores dentro del diccionario usando sus claves: `user['name']` y `user['age']`.
    -   Usamos una "f-string" (indicada por la `f` antes de las comillas) para combinar estos valores en una sola cadena de texto, separados por una coma y un espacio.

3.  **Ejecución**:
    -   Llamamos a `format_user(make_user('John', 30))`. Primero se ejecuta `make_user`, creando el diccionario para John. Luego ese diccionario se pasa a `format_user`, que devuelve la cadena "John, 30".
"""