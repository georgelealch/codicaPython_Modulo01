def build_definition_list(definitions):
    """
    Genera una lista de definiciones HTML a partir de una lista de listas.
    """
    # Si la lista de definiciones está vacía, retornamos una cadena vacía
    if not definitions:
        return ""
    
    # Iniciamos la cadena con la etiqueta de apertura de la lista de definición
    html_output = "<dl>"
    
    # Recorremos cada elemento de la lista definitions
    for item in definitions:
        # Extraemos el término y la descripción
        term = item[0]
        description = item[1]
        
        # Concatenamos las etiquetas correspondientes al resultado
        html_output += f"<dt>{term}</dt><dd>{description}</dd>"
    
    # Cerramos la lista de definición
    html_output += "</dl>"
    
    return html_output

# Ejemplo de uso
definitions = [
  ['Chévere', 'Algo muy bueno o genial, típico del habla en Venezuela y Colombia'],
  ['Ceviche', 'Plato tradicional de pescado crudo marinado en limón, típico de la costa del Perú'],
]

print(build_definition_list(definitions))

"""
EXPLICACIÓN PARA EL ESTUDIANTE:

1. **Definición de la función**:
   - Creamos una función llamada `build_definition_list` que recibe un parámetro `definitions`.

2. **Manejo de lista vacía**:
   - `if not definitions:` verifica si la lista está vacía. En Python, una lista vacía se evalúa como `False`. Si es así, retornamos `""` inmediatamente.

3. **Construcción del string**:
   - Inicializamos la variable `html_output` con la etiqueta de apertura `<dl>`.

4. **Bucle `for`**:
   - `for item in definitions:` recorre cada sub-lista (par término-descripción) dentro de la lista principal.
   - `term = item[0]` y `description = item[1]` extraen los valores individuales. También se podría usar "desempaquetado" así: `for term, description in definitions:`.

5. **Concatenación (f-strings)**:
   - `html_output += ...` va agregando al final de nuestra cadena las etiquetas `<dt>` para el término y `<dd>` para la descripción.
   - Usamos `f-strings` (f"...") para insertar las variables directamente dentro del texto, lo cual es más legible.

6. **Cierre y Retorno**:
   - Finalmente agregamos la etiqueta de cierre `</dl>` y devolvemos el resultado completo.
"""
