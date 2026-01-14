# Ejemplo simple para entender enumerate()

lista_frutas = ["manzana", "banana", "uvas"]

print("--- Sin enumerate (solo elementos) ---")
for fruta in lista_frutas:
    print(fruta)

print("\n--- Con enumerate (indice y elemento) ---")
# enumerate() toma la lista y nos devuelve pares: (0, "manzana"), (1, "banana"), ...
for indice, fruta in enumerate(lista_frutas):
    print(f"La fruta en el índice {indice} es {fruta}")

print("\n--- Como se ve enumerate() internamente ---")
print(list(enumerate(lista_frutas)))
