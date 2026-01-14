
from symbols import is_vowel


def count_vowels(palabra):
    i = 0
    palabra = palabra.lower()
    count = 0

    while i < len(palabra):
        if is_vowel(palabra[i]):
            count += 1
        i += 1
    return count


print(count_vowels("London is the capital of Great Britain"))
