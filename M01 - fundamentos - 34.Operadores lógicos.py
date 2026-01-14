########### EJEMPLO con and ########################

def es_contrasena_valida(password):
    largo = len(password)
    return largo > 8 and largo < 20

print(es_contrasena_valida("123"))            # False — muy corta
print(es_contrasena_valida("qwerty12345"))    # True  — está bien
print(es_contrasena_valida("contraseñademasiadolarga"))  # False — muy larga


########### EJEMPLO con or ########################

def tiene_descuento(monto, cupon):
    return monto > 10000 or cupon == "BIENVENIDO"

print(tiene_descuento(5000, "BIENVENIDO"))   # True — tiene cupón
print(tiene_descuento(15000, ""))            # True — el monto es alto
print(tiene_descuento(3000, ""))             # False — no cumple nada


########### EJEMPLO con not ########################
def puede_acceder(esta_bloqueado):
    return not esta_bloqueado

print(puede_acceder(False))  # True — cuenta activa
print(puede_acceder(True))   # False — está bloqueada




def funciona(mensaje):
    if not mensaje == "esta bien":
        return True
    else:
        return False

print(funciona("esta bien"))


########### EJEMPLO con and & not ########################

def es_castillo_adecuado(habitaciones, nombre):
    return habitaciones >= 100 or (habitaciones >= 80 and nombre != "Invernalia")

print(es_castillo_adecuado(90, "Roca Casterly"))     # True
print(es_castillo_adecuado(78, "Invernalia"))        # False
print(es_castillo_adecuado(80, "Invernalia"))        # False
print(es_castillo_adecuado(80, "Altojardín"))        # True
print(es_castillo_adecuado(120, "Invernalia"))       # True


########### EJERCICIO ####################
def is_leap_year(year):
    year_div_4 = year / 4
    year_div_100 = year / 100
    year_div_400 = year / 400

    if year_div_4.is_integer() and not year_div_100.is_integer() or year_div_400.is_integer():
        return True
    else:
        return False

print(is_leap_year(2017))