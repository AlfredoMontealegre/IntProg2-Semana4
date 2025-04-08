# En un hospital existen 3 áreas: Urgencias, Pediatría y Traumatología. El presupuesto
# anual del hospital se reparte de la siguiente manera

presupuesto = int(input("Ingrese el presupuesto: "))
urgencias = presupuesto * 0.37
pediatria = presupuesto * 0.42
trauma = presupuesto * 0.21

presupuesto_t = urgencias + pediatria + trauma

print(f"Urgencias (37%): ", urgencias)
print(f"Pediatria (42%): ", pediatria)
print(f"Traumatologia (21%): ", trauma)
print(f"Presupuesto Total Ingresado: ", presupuesto_t)