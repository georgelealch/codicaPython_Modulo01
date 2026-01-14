def is_palindrome(nombre):
    name1 = nombre
    name2 = nombre[::-1]

    if name1 == name2:
        return True
    else:
        return False


print(is_palindrome('radar'))
print(is_palindrome('abs'))
print(is_palindrome(''))


def is_palindrome2(word):
    return word == word[::-1]

print(is_palindrome2('radar'))
print(is_palindrome2('abs'))
print(is_palindrome2(''))