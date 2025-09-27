#ciclo while "infinito"

  
# Listas con datos
mililitros = [250, 350, 500, 1000]
precios = [15, 18, 20, 30]  # precios en pesos
stock = [5, 3, 4, 2]        # unidades disponibles

# Mostrar todas las presentaciones
print("=== Presentaciones de Coca-Cola ===")
for i in range(len(mililitros)):
    print(f"{mililitros[i]} ml - ${precios[i]} - Stock: {stock[i]} unidades")

# Consultar si hay una presentación específica
consulta = int(input("\n¿Qué presentación (ml) quieres buscar? "))

if consulta in mililitros:
    indice = mililitros.index(consulta)
    if stock[indice] > 0:
        print(f"Sí hay Coca-Cola de {consulta} ml.")
        print(f"Precio: ${precios[indice]} - Stock: {stock[indice]} unidades")
    else:
        print(f"No hay stock disponible de {consulta} ml.")
else:
    print("Esa presentación no está disponible.")
while True:
      control= imput("quieres salir?")
    if control = imput "si":
        break