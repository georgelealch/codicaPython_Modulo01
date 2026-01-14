
def print_name_by_symbol(name):
    for letra in name:               # Cada vuelta trae una letra directamente
        print(letra)                 # La mostramos sin usar índices

print_name_by_symbol("12345")


def filter_string(text, char):
    char_to_remove = char.lower()
    new_text = ''

    for letra in text:
        if letra.lower() != char_to_remove:
            new_text += letra
    
    return new_text.strip()

print(filter_string("I look back if you are lost", "o"))



def is_palindrome(nombre):
    name1 = nombre
    name2 = nombre[::-1]

    if name1 == name2:
        print(True)
    else:
        print(False)


is_palindrome('alita')

