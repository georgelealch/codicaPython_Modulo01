
def tipo_entrega(nombre, direccion_confirmada, monto_pedido, es_cliente_vip):
    nombre_limpio = nombre.strip().upper()
    cumple = direccion_confirmada and es_cliente_vip and monto_pedido > 8000
    match cumple:
        case True:
            return f'Hola {nombre_limpio}, tu pedido será enviado a domicilio'
        case False:
            return f'Hola {nombre_limpio}, tu pedido esta listo para retirar en tienda'


print(tipo_entrega('Facundo', True, 7000, True))

