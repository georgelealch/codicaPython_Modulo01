
def tiene_mayusculas(mensaje):

    if any (c.isupper() for c in mensaje):
        return True
    else:
        return False

print(tiene_mayusculas('mensAje'))