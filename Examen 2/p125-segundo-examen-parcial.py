# p125-segundo-examen-parcial.py

"""
 Nombre del Alumno: Gustavo Daniel Rodriguez Vargas
 Matrícula: 37184888
 Materia: Computación Aplicada
 Examen: Segundo Parcial
 Objetivo: Se desea procesar el inventario de productos de una tienda de electrónicos ("TecnoTienda"). Para ello,
deberá solicitar al usuario los siguientes datos por cada producto:
    • nombre (del producto)
    • precio (valor numérico, ej. 1500.50)
    • categoria (ej. 'Laptops', 'Celulares', 'Audio')
    • proveedor (el nombre del distribuidor, ej. 'Sony', 'HP', 'Generico')
    • stock (cantidad en inventario, ej. 25)
 Los datos se deben almacenar en una lista, donde cada elemento de la lista sea un diccionario con los
datos de un producto.
 Nota: No olvides documentar las partes importantes del código, explicando que hace ese fragmento de
código en específico.
"""

# --- Inicialización de Contadores y Acumuladores ---
# Aquí se declaran todas las variables que necesitarás para guardar los datos

# --- Lista de Productos ---
# Almacenaremos cada producto como un diccionario dentro de esta lista
productos = []


print('\033[2J\033[H')
print("--- Sistema de TecnoTienda ---")

# --- Ciclo Principal para registro de Productos ---
# Usaremos un ciclo while para registrar productos hasta que el usuario decida parar.
continuar_venta = "s"
while continuar_venta == "s":

    print("\n--- Nuevo Producto ---")
    # --- 1. Solicitud de Datos ---
    # Pide nombre, precio, categoria, proveedor, stock.
    datos = {}
    datos['nombre'] = input("Introduce nombre del producto: ")
    datos['precio'] = float(input("Introduce el precio del producto: "))
    datos['categoria'] = input("Introduce la categoria del producto: ")
    datos['proveedor'] = input("Introduce el proveedor del producto: ")
    datos['stock'] = int(input("Introduce el stock del producto: "))
    productos.append(datos)
    
    
    # Pregunta al usuario si desea registrar otro producto.
    continuar_venta = input("\n¿Deseas registrar otro producto? (S/N): ").lower()

# --- FIN DEL CICLO ---


# --- 1. Datos Crudos ---
print(('\n--- Datos (Lista de Diccionarios) ---'))
print(productos)

# --- 2. Datos Tabular ---
print(('\n--- Tabla de Datos ---'))
print(' Nombre \t| Precio \t| Categoria \t| Stock | Proveedor ')
for producto in productos:
    print(f'{producto['nombre']} \t| {producto['precio']} \t| {producto['categoria']} \t| {producto['stock']} \t| {producto['proveedor']} ')
    
# --- 3. Resumen del Inventario ---
print('\n--- RESUMEN ---')
print(f'Productos Totales: {len(productos)}')
    

# --- 3.1. Contador de Categorias ---
# Contamos cuántos productos hay en cada categoría
categorias = {}
for producto in productos:
    categoria = producto['categoria']
    if categoria not in categorias:
        categorias[categoria] = {"nombre": categoria, "cantidad": 0}
    
    categorias[categoria]['cantidad'] += 1
    

print('\nCategorias: ')
# Iteramos sobre los valores del diccionario para acceder a cada categoría
for categoria in categorias.values():
    print(f'- {categoria['nombre']}: {categoria['cantidad']}')

# --- 3.2. Contador de Proveedores ---
# Contamos cuántos productos hay en cada proveedor
proveedores = {}
for producto in productos:
    proveedor = producto['proveedor']
    if proveedor not in proveedores:
        proveedores[proveedor] = {"nombre": proveedor, "cantidad": 0}
    
    proveedores[proveedor]['cantidad'] += 1
    

print('\nProveedores: ')
# Iteramos sobre los valores del diccionario para acceder a cada proveedor
for proveedor in proveedores.values():
    print(f'- {proveedor['nombre']}: {proveedor['cantidad']}')
    
suma_stock = sum(p['stock'] for p in productos)
promedio_stock = suma_stock / len(productos) if len(productos) > 0 else 0
print(f"\n- Stock -> Suma: {suma_stock}, Promedio: {promedio_stock:.1f}")

suma_precio = sum(p['precio'] for p in productos)
promedio_precio = suma_precio / len(productos) if len(productos) > 0 else 0
print(f"\n- Precio -> Suma: {suma_precio:,.2f}, Promedio: {promedio_precio:,.2f}")


producto_mas_caro = max(productos, key=lambda p: p['precio'])
producto_mas_barato = min(productos, key=lambda p: p['precio'])
print(f"\n- {producto_mas_caro['nombre']} de {producto_mas_caro['precio']:,.2f} es el más caro, {producto_mas_barato['nombre']} de {producto_mas_barato['precio']:,.2f} es el más barato.")