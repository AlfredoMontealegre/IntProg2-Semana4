# . Todos los lunes, miércoles y viernes, una persona corre la misma ruta y cronometra
# los tiempos obtenidos. Determinar el tiempo promedio que la persona tarda en recorrer
# la ruta en una semana cualquiera

tiempo_lun = float(input("Ingrese el tiempo del lunes (minutos): "))
tiempo_mie= float(input("Ingrese el tiempo del miercoles (minutos): "))
tiempo_vie = float(input("Ingrese el tiempo del viernes (minutos): "))

tiempo_prom = (tiempo_lun + tiempo_mie + tiempo_vie) / 3

print(f"El tiempo promedio es: {tiempo_prom:.2f} ")