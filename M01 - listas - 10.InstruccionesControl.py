

def get_total_amount(money, type=str): #Divide la lista en dos listas
    money_split = []
    
    for i in range(len(money)):
        money_split.append(money[i].split())

    money_usd = []
    money_eur = []
    money_cop = []

    for i in range(len(money_split)):
        if money_split[i][0] == 'usd':
            money_usd.append(money_split[i])
        elif money_split[i][0] == 'eur':
            money_eur.append(money_split[i])
        elif money_split[i][0] == 'cop':
            money_cop.append(money_split[i])

    sum_usd = 0
    sum_eur = 0
    sum_cop = 0

    for i in range(len(money_usd)):
        sum_usd += int(money_usd[i][1])

    for i in range(len(money_eur)):
        sum_eur += int(money_eur[i][1])

    for i in range(len(money_cop)):
        sum_cop += int(money_cop[i][1])

    if type == 'usd':
        return sum_usd
    elif type == 'eur':
        return sum_eur
    elif type == 'cop':
        return sum_cop
    else:
        return sum_usd, sum_eur, sum_cop


money = [
  'eur 10', 'usd 1', 'usd 10', 'cop 50', 'usd 5',
]

print(get_total_amount(money, 'usd'))


def get_total_amount_v2(money, type=str):
    # Inicializamos un diccionario con los totales en 0
    totals = {'usd': 0, 'eur': 0, 'cop': 0}

    for item in money:
        # Dividimos el texto una sola vez y asignamos a variables claras
        currency, amount = item.split()
        
        # Si la moneda existe en nuestro diccionario, sumamos el valor
        if currency in totals:
            totals[currency] += int(amount)

    # Si el tipo solicitado está en el diccionario, lo devolvemos
    if type in totals:
        return totals[type]
    
    # Si no, devolvemos todos los valores (comportamiento por defecto)
    return totals['usd'], totals['eur'], totals['cop']

# Probando la nueva función con el mismo caso de prueba
print(get_total_amount_v2(money, 'usd'))

"""
Explicación de los cambios para el estudiante:

1. Uso de Diccionario (`totals`):
   En lugar de tener variables sueltas (`sum_usd`, `sum_eur`...) y listas separadas, usamos un diccionario. Imagínalo como una caja con compartimentos etiquetados. Esto nos permite guardar y sumar los valores de forma mucho más ordenada y escalable.

2. Eficiencia (Un solo ciclo `for`):
   La función original recorría la lista múltiples veces (para dividir, clasificar y sumar). La versión v2 recorre la lista de datos una única vez. En ese mismo momento "entiende" qué moneda es y la suma. Hacemos más trabajo en menos pasos.

3. Legibilidad (Desempaquetado):
   La línea `currency, amount = item.split()` asigna nombres claros a los datos inmediatamente. En lugar de intentar entender qué es `money_split[i][1]`, ahora leemos `amount` (cantidad), lo cual hace que la lógica sea mucho más fácil de seguir para cualquier programador.
"""