def get_super_series_winner(scores):
    # Inicializamos los contadores de victorias para cada equipo
    wins_south_america = 0
    wins_europe = 0

    # Recorremos la lista de resultados partido por partido
    for match in scores:
        # match es una lista como [3, 1]
        # match[0] son los goles de Sudamérica
        # match[1] son los goles de Europa
        
        if match[0] > match[1]:
            wins_south_america += 1
        elif match[1] > match[0]:
            wins_europe += 1
        # Si empatan (else), no sumamos victoria a ninguno
            
    # Al final del ciclo, comparamos quién ganó más partidos
    if wins_south_america > wins_europe:
        return 'sudamerica'
    elif wins_europe > wins_south_america:
        return 'europa'
    else:
        return None

scores = [
  [3, 1], # Primer partido
  [2, 2], # Segundo partido
  [1, 3],
  [4, 2],
  [0, 2],
  [1, 1],
  [3, 3],
  [2, 0],
]

print(get_super_series_winner(scores))

"""
Explicación de los cambios:

1. Contadores (wins_south_america, wins_europe):
   En lugar de una sola variable `result` que cambiaba en cada vuelta del bucle (lo que hacía que solo importara el último partido), creamos dos variables para contar cuántos partidos ganó cada equipo acumulativamente.

2. Bucle For:
   Recorremos cada partido en la lista `scores`. En cada iteración, comparamos los goles de ese partido específico.

3. Condicionales (if/elif):
   - Si Sudamérica tiene más goles (`match[0] > match[1]`), sumamos 1 a su contador.
   - Si Europa tiene más goles (`match[1] > match[0]`), sumamos 1 al suyo.
   - Si hay empate, no hacemos nada (no entra en los if), lo cual es correcto porque buscamos al ganador de la serie por partidos ganados.

4. Resultado Final:
   Fuera del bucle (cuando ya revisamos todos los partidos), comparamos los contadores totales para decidir quién devuelve la función ('sudamerica', 'europa' o None).
"""
