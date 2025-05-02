import numpy as np

# Función para calcular la distancia de taxi
def distancia_taxi(x, y):
    x, y = np.array(x), np.array(y)
    return np.sum(np.abs(x - y))

# Función para calcular la distancia euclidiana
def distancia_euclidea(x, y):  
    x, y = np.array(x), np.array(y)
    return np.sqrt(np.sum((x - y) ** 2))

# Función para calcular la distancia máxima
def distancia_maximo(x, y):
    x, y = np.array(x), np.array(y) 
    return np.max(np.abs(x - y))

# Solicitar al usuario el tipo de distancia
distancia = input("¿Qué distancia quieres calcular? (t/e/m): ")

# Solicitar al usuario la unidad de medida
medida = input("¿Qué unidad de medida quieres usar? (k/a/m): ")

# Validar la entrada y calcular la distancia
if distancia in ["t", "e", "m"]:
    # Solicitar las coordenadas de los puntos 
    while True:
        puntos = []
    print("Introduce las coordenadas de los puntos (escribe 'fin' para terminar):")
        while True:
            try:
                entrada = input("Introduce las coordenadas (x, y) separadas por coma: ")
            if entrada.lower() == "fin":
            if len(puntos) < 2:
                    print("Debes introducir al menos dos puntos.")
                    continue
                break
            x, y = map(float, entrada.split(","))
            puntos.append([x, y])
        except ValueError:
            print("Por favor, introduce valores válidos (ejemplo: 1.0, 2.0).")
    if medida == "a":
        # Convertir a millas
        punto1 = [x * 0.621371 for x in punto1]
        punto2 = [x * 0.621371 for x in punto2]
    elif medida == "m":
        # Convertir a metros
        punto1 = [x * 1000 for x in punto1]
        punto2 = [x * 1000 for x in punto2]
    
    # Calcular la distancia según la opción seleccionada
    if distancia == "t":
        resultado = distancia_taxi(punto1, punto2)
        tipo_distancia = "distancia de taxi"
    elif distancia == "e":
        resultado = distancia_euclidea(punto1, punto2)
        tipo_distancia = "distancia euclidiana"
    elif distancia == "m":
        resultado = distancia_maximo(punto1, punto2)
        tipo_distancia = "distancia máxima"
    
    # Mostrar el resultado
    if medida in ["k", "a", "m"]:
        unidad = {"k": "Kilómetros", "a": "Millas", "m": "Metros"}[medida]
        print(f"La {tipo_distancia} entre los puntos es: {resultado:.2f} {unidad}")
    else:
        print("Unidad de medida no válida.")
else:
    print("Opción de distancia no válida.")