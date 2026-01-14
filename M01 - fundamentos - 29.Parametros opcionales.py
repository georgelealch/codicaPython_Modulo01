################# PARAMETROS OPCIONALES ####################

def get_hidden_card(card_number, shorter=4): #SE LE TIENE QUE DAR UN VALOR AL PARAMETRO OPCIONAL, QUE SIEMPRE DEBE SER EL SEGUNDO (O DE AHI PARA ALLÁ)
    asteriscos = '*' * shorter
    mensaje = f'{asteriscos}{card_number[12:]}'

    return mensaje

print(get_hidden_card("1234567812345678"))