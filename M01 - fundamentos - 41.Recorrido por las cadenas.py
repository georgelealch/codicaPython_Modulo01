############ EJERCICIO LECCIÓN ##########

def my_substr(text, long):
    index_text = 0                                               # 1. Empezamos en 0
    resultado_text = ''
    
    while index_text < long and index_text < len(text):          # 2. Mientras el índice sea menor que la longitud deseada - AUNQUE SE PUEDE DEJAR SOLO CON < len()
        resultado_text = resultado_text + text[index_text]       # Y TAMBIÉN menor que la longitud del texto (para evitar errores si piden más de lo que hay)
        index_text += 1

    return resultado_text

print(my_substr('If I look back I am lost', 9))







########## EJEMPLO 1 #################

def print_name_by_symbol(name):
    i = 0
    while i < len(name):  # Recorremos desde el primer hasta el último carácter. Nótese que se usa < y no <=, pues el conteo de las letras empiezan en 0
        print(name[i])    # Mostramos cada letra
        i += 1            # Pasamos a la siguiente

print_name_by_symbol('Arya')


########## EJEMPLO 2 #############

def reverse_string(text):
    index = len(text) - 1   # Empezamos desde el último carácter
    reversed_text = ''      # Cadena nueva, vacía

    while index >= 0:
        reversed_text = reversed_text + text[index]  # Agregamos letra por letra
        index -= 1                                   # Retrocedemos

    return reversed_text

print(reverse_string('Bran'))    # 'narB'
print(reverse_string('Códica'))  # 'acidoC'

"""
EXPLICACIÓN DETALLADA DEL EJEMPLO 2:

La función `reverse_string` tiene como objetivo invertir el orden de los caracteres de un texto.
1. Inicialización (`index = len(text) - 1`): Se comienza apuntando al último carácter de la cadena. Recordemos que los índices en Python empiezan en 0, por lo que el último es la longitud menos 1.
2. Acumulador (`reversed_text = ''`): Se crea una cadena vacía que servirá para ir guardando las letras en el nuevo orden.
3. Bucle (`while index >= 0`): Mientras queden letras por procesar (desde la última hasta la primera, índice 0), el ciclo continúa.
4. Concatenación (`reversed_text + text[index]`): En cada iteración, se toma la letra de la posición actual (`index`) y se añade al final de la cadena acumuladora.
5. Decremento (`index -= 1`): Se resta 1 al índice para "retroceder" una posición en la cadena original, moviéndose hacia el principio.

Al terminar el bucle, se retorna la cadena `reversed_text` que ya contiene el texto completamente invertido.
"""

################ EJEMPLO 3 ##################

def upper_codica(name):
    name = 'Códica'
    result = ''
    i = 0
    while (i < len(name)):
        result = result + name[i].upper()
        i += 1
    return result

print(upper_codica('Códica'))



"""
EXPLICACIÓN DETALLADA DEL EJEMPLO 3:

La función `upper_codica` tiene como objetivo convertir una cadena específica a mayúsculas, carácter por carácter.
1. Sobrescritura (`name = 'Códica'`): Aunque la función recibe un argumento `name`, en la primera línea lo sobrescribe forzosamente con el valor fijo 'Códica'. 
    Esto significa que no importa qué le pases a la función, siempre trabajará con 'Códica'.
2. Acumulador (`result = ''`): Se inicia una cadena vacía para ir construyendo el resultado en mayúsculas.
3. Bucle (`while i < len(name)`): Se recorre la cadena desde el índice 0 hasta el final.
4. Conversión (`name[i].upper()`): En cada vuelta, se toma el carácter actual, se convierte a mayúscula usando el método `.upper()` y se concatena al acumulador `result`.
5. Retorno: Al finalizar, se devuelve la nueva cadena construida ('CÓDICA').
"""


#palabra = "Python"
#print(palabra[0])

"""
¿Qué error común puede ocurrir al trabajar con índices en una cadena?

Intentar acceder al índice len(cadena)

Concatenar con números

No usar print() para mostrar la cadena

Olvidar usar comillas dobles


La respuesta correcta es: Intentar acceder al índice len(cadena).

Aquí tienes la explicación detallada de por qué ocurre esto y por qué las otras opciones no son la respuesta correcta en este contexto:

¿Por qué es un error acceder a len(cadena)?
En Python, los índices siempre empiezan a contar desde 0.

Si tienes una cadena como texto = "Hola", su longitud (len(texto)) es 4.
Sus índices son: 0 (H), 1 (o), 2 (l), y 3 (a).
Si intentas acceder a texto[4] (que es igual a len(texto)), Python buscará una posición que no existe, ya que la última posición válida es la 3. Esto provoca el famoso error IndexError: string index out of range.

Análisis de las otras opciones:
Concatenar con números: Esto da un error (TypeError), pero no tiene que ver con el manejo de índices, sino con operaciones entre tipos de datos incompatibles.
No usar print(): Esto no es un error de programación; el código funcionará, simplemente no verás nada en la consola.
Olvidar usar comillas dobles: Esto es un error de sintaxis (SyntaxError) al escribir la cadena, no un error lógico al usar sus índices.
"""


"""
PREGUNTA: Completa la línea para acceder al último carácter de una cadena llamada texto.
ultimo = ?
RESPUESTA: ultimo = texto[-1]
EXPLICACIÓN:
En Python, los índices negativos permiten acceder a los elementos desde el final de la cadena.
- El índice -1 siempre corresponde al último carácter.
- El índice -2 al penúltimo, y así sucesivamente.
Alternativa: También es posible usar `texto[len(texto) - 1]`, pero usar `texto[-1]` es más directo y "Pythonico".
"""



########### EXPLICACION EJERCICIO DE LA LECCIÓN ##########################
"""
¡Hola! Analizando tu código, puedo deducir tu intención y señalarte los errores.

¿Qué intentas hacer?
Parece que estás intentando crear tu propia función para extraer una subcadena (un pedazo de texto) desde el principio de la frase. Específicamente, 
quieres tomar los primeros long caracteres del text.

En tu ejemplo: my_substr('If I look back I am lost', 9), esperas obtener los primeros 9 caracteres: 'If I look'.

¿Qué está mal?
Tienes tres errores principales que impiden que funcione:

1. El punto de partida (index_text):

Tienes: index_text = len(text)
El problema: Estás iniciando el índice en la longitud total del texto (el final).
Corrección: Deberías empezar desde el principio, es decir, index_text = 0.

2. La condición del bucle (while):

Tienes: while index_text <= long:
El problema: Como iniciaste index_text con la longitud total (que es 24 en tu ejemplo) y long es 9, la condición 24 <= 9 es Falsa inmediatamente, 
por lo que el bucle nunca se ejecuta y devuelve una cadena vacía.
Corrección: Si empiezas en 0, la condición debería ser while index_text < long: (menor estricto) para obtener exactamente esa cantidad de caracteres.

3. Error de índice (IndexError):

Si por alguna razón el bucle entrara con tu código actual, text[index_text] daría un error porque len(text) no es una posición válida (los índices en Python van de 0 a longitud - 1).
Código Corregido
Aquí tienes la versión corregida de tu lógica:
"""
