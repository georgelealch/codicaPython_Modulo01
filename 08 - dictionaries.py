def count_all(elementos):

    dictionary = {}

    for elemento in elementos: 
        if elemento in dictionary:
            dictionary[elemento] += 1
        else:
            dictionary[elemento] = 1
    
    return dictionary


def count_all_get(elementos):
    dictionary = {}
    for elemento in elementos:
        dictionary[elemento] = dictionary.get(elemento, 0) + 1
    return dictionary


lista = [1, 2, 2, 4, 5, 7, 7, 7, 9, 10]
lista2 = ["cat", "dog", "cat"]
string = "hola" 

print(count_all(lista))
print(count_all_get(lista))


"""
Explicación paso a paso de por qué funciona count_all():

1. dictionary = {}: Se crea un diccionario vacío. Los diccionarios funcionan asignando valores a claves únicas,
lo que es ideal para contar frecuencias.

2. for elemento in elementos: El bucle 'for' recorre cada ítem de la lista de entrada uno por uno.

3. if elemento in dictionary: Esta es la parte clave.
   - Python verifica si el 'elemento' actual ya existe como clave dentro del diccionario.
   - Es una búsqueda muy eficiente.

4. dictionary[elemento] += 1 (Si ya existe):
   - Si la condición del 'if' es verdadera, significa que ya hemos visto este elemento antes.
   - Accedemos a su valor actual (la cuenta que llevamos) y le sumamos 1.

5. dictionary[elemento] = 1 (Si no existe - else):
   - ¡Aquí empieza la cuenta! Si el 'if' fue falso, es la PRIMERA vez que vemos este elemento.
   - No podemos sumar 1 todavía porque no existe en el diccionario.
   - Así que lo creamos y le asignamos el valor 1 (porque lo hemos visto 1 vez).

6. return dictionary: Al finalizar el bucle, se devuelve el diccionario que ahora contiene cada elemento único como clave 
y el número de veces que apareció como valor.

---------------------------------------------------------
Explicación de la NUEVA función count_all_get() con .get():

1. dictionary.get(elemento, 0): Esta es la magia que reemplaza al if/else.
   - Le dice a Python: "Busca 'elemento' en el diccionario".
   - "Si lo encuentras, dame su valor actual".
   - "Si NO lo encuentras, dame un 0" (este es el valor por defecto que pusimos).

2. ... + 1:
   - Al valor que obtuvimos (ya sea el conteo actual o 0 si es nuevo), le sumamos 1.

3. dictionary[elemento] = ...:
   - Guardamos ese nuevo resultado en el diccionario.
   - Si era nuevo, guardará 0 + 1 = 1.
   - Si ya existía (ej. 2), guardará 2 + 1 = 3.

Es una forma más "Pythonica" y concisa de hacer exactamente lo mismo.

---------------------------------------------------------
Respondiendo a tu duda: "¿Cómo sabe el diccionario qué es clave y qué es valor?"

No es que el diccionario "lo sepa" mágicamente, ¡TÚ se lo estás diciendo explícitamente con la sintaxis!

La sintaxis en Python es:  DICCIONARIO[ CLAVE ] = VALOR

1. Lo que pones DENTRO de los corchetes [] siempre será la CLAVE (Key).
   - En `dictionary[elemento]`, le estás diciendo: "Usa 'elemento' como la ETIQUETA o CLAVE".

2. Lo que pones DESPUÉS del signo igual = siempre será el VALOR (Value).
   - En `... = 1`, le dices: "El contenido de esa caja será 1".
   - En `... = dictionary.get(...) + 1`, le dices: "El contenido será el resultado de esta suma".

Es como etiquetar una caja:
- `dictionary["Manzana"] = 5`
  - Etiqueta de la caja (Clave): "Manzana"
  - Contenido de la caja (Valor): 5

Python no decide nada, solo obedece donde pones cada cosa: a la izquierda del '=' va la CLAVE (entre corchetes), 
y a la derecha del '=' va el VALOR.
"""