import os, globales, random
os.system("cls")

def ventas_aleatorios():
    valor = globales.leer_archivo_json('valores.json')
    nombre = globales.leer_archivo_json('nombres.json')
    

    id_ventas = ventas[-1:][0]['id_venta']

    for i in range(15):
        producto = random.choice(producto)

        id_ventas += 1
        id_producto = ['id_producto']
        valor = random.randint(2000, 10000)
        iva = total_iva * 0.15

        nuevo_producto = {
            "id_producto":,
            "nombre_producto": ,
            "iva_producto"
        }

    ventas.append(nueva_venta)

globales.guardar_archivo_json('ventas.json', ventas)