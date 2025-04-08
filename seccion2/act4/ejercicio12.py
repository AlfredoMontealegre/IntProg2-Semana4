# El dueño de una tienda compra un artículo a un precio determinado. Obtener el precio
# en que lo debe vender para obtener una ganancia del 30%.

articulo = int(input("Ingrese el valor del articulo comprado: "))
venta = articulo * 0.30
new_precio = articulo + venta

print(f"Para sacar provecho, el producto debe revenderse a: ", new_precio)
