def is_palindrome(word):
    """
    Determina si una palabra es un palíndromo.
    
    Args:
        word (str): La palabra a verificar.
        
    Returns:
        bool: True si es palíndromo, False en caso contrario.
    """
    # Convertimos a minúsculas para asegurar que la comparación no sea sensible a mayúsculas
    # Aunque el ejercicio no lo especifica explícitamente, 'radar' vs 'Radar' suele considerarse igual.
    # Sin embargo, los ejemplos son todos minúsculas o vacíos.
    # El ejemplo 'radar' es palíndromo.
    # Si la entrada fuera 'Radar', word[::-1] sería 'radaR', que no es igual a 'Radar'.
    # Dado que el usuario no pidió insensibilidad a mayúsculas explícitamente, 
    # pero es buena práctica, lo haré exacto como pide el ejemplo primero.
    # Los ejemplos son estrictos: 'radar' == 'radar'.
    
    return word == word[::-1]

# Pruebas
if __name__ == "__main__":
    print(f"is_palindrome(''): {is_palindrome('')}")          # True
    print(f"is_palindrome('radar'): {is_palindrome('radar')}") # True
    print(f"is_palindrome('a'): {is_palindrome('a')}")        # True
    print(f"is_palindrome('abs'): {is_palindrome('abs')}")    # False
    print(f"is_palindrome('aibofobia'): {is_palindrome('aibofobia')}") # True
