# Solicita el nombre, precio de un producto y un porcentaje de descuento. 
# Muestra el nombre del producto y precio final luego de aplicar el descuento.

nombre = str(input("Ingresa el nombre de tu producto: "))
precio = int(input("Ingresa el precio de tu producto: "))
descuento = int(input("Hoy hace un buen dia, que tal si ingresas un descuento?: "))

precio_fin = precio - ((precio * descuento) / 100)

print(f"Producto: ", nombre)
print(f"Precio Final: ", precio_fin)