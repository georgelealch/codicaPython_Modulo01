
def string_or_not(mensaje):
    if isinstance(mensaje, str):
        return 'yes'
    else:
        return 'no'
    
print(string_or_not("no sé"))




def analizar_mensaje(texto):
    ultimo = texto[-1]
    if ultimo == '?':
        return 'Es una pregunta'
    elif ultimo == '!':
        return 'Es una exclamación'
    else:
        return 'No es una pregunta'

print(analizar_mensaje('¿Vienes?'))



hora = 17
saludo = "Buenos días" if hora < 18 else "Buenas noches"
print(saludo)


edad = 23
mensaje = "Bebé" if edad < 2 else "Niño pequeño" if edad < 5 else "Niño" if edad < 12 else "Adolescente" if edad < 18 else "Joven" if edad < 30 else "Adulto" if edad < 60 else "Mayor"
print(mensaje)


################# EJERCICIO ############
def normalize_url(url_dir):
    if url_dir[:7] != "http://" and url_dir[:8] != "https://":
        return f'https://{url_dir}'
    elif url_dir[:7] == "http://":
        return f'https://{url_dir[7:]}'
    elif url_dir[:8] == "https://":
        return url_dir


print(normalize_url('https://google.com'))