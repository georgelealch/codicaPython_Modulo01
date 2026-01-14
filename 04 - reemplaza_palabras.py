def make_censored(sentence, censored_words):

    separator = ' '
    words = sentence.split(separator)
    new_words = []
    
    for word in words:
        if word in censored_words:
            word = '$#%!'
        new_words.append(word)

    return separator.join(new_words)


sentence = 'Cuando juegas el juego de los tronos, ganas o mueres'
censored_words = ['mueres', 'juegas']
result = make_censored(sentence, censored_words)
print(result)


"""
Explicación paso a paso para estudiantes:

1. separator = ' ':
   Definimos qué carácter usaremos para separar las palabras. Aquí es un espacio vacío.

2. words = sentence.split(separator):
   El método .split() toma la oración completa y la "corta" cada vez que encuentra el separador.
   Esto convierte el texto en una LISTA de palabras sueltas.
   Por ejemplo: "Hola mundo" se convierte en ["Hola", "mundo"].

3. new_words = []:
   Preparamos una lista vacía nueva. Aquí iremos poniendo las palabras una vez que hayamos decidido si se censuran o no.

4. Bucle for word in words:
   Vamos a revisar palabra por palabra de la lista original.
   
   - if word in censored_words:
     Preguntamos: "¿Esta palabra actual aparece en la lista de palabras prohibidas?".
     Si la respuesta es SÍ, reemplazamos la variable 'word' por los símbolos '$#%!'.
   
   - new_words.append(word):
     Agregamos la palabra a nuestra lista nueva. Si fue censurada, se agrega la versión con símbolos.
     Si no, se agrega la original.

5. return separator.join(new_words):
   Al final, tomamos la lista nueva y usamos .join().
   Esto hace lo contrario al .split(): une todos los elementos de la lista en un solo texto (string),
   poniendo un espacio (separator) entre cada uno.
"""


    
