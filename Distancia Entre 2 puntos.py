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
distancia = input("¿Qué distancia quieres calcular? (t: taxi / e: euclidiana / m: máxima): ").strip().lower()

# Solicitar la unidad de medida
medida = input("¿Qué unidad de medida quieres usar? (k: kilómetros / a: millas / m: metros): ").strip().lower()

# Validar entradas
if distancia in ["t", "e", "m"] and medida in ["k", "a", "m"]:
    try:
        # Solicitar coordenadas
        x1 = float(input("Introduce la coordenada x del primer punto: "))
        y1 = float(input("Introduce la coordenada y del primer punto: "))
        x2 = float(input("Introduce la coordenada x del segundo punto: "))
        y2 = float(input("Introduce la coordenada y del segundo punto: "))
        
        punto1 = [x1, y1]
        punto2 = [x2, y2]

        # Calcular distancia
        if distancia == "t":
            resultado = distancia_taxi(punto1, punto2)
            tipo_distancia = "distancia de taxi"
        elif distancia == "e":
            resultado = distancia_euclidea(punto1, punto2)
            tipo_distancia = "distancia euclidiana"
        else:
            resultado = distancia_maximo(punto1, punto2)
            tipo_distancia = "distancia máxima"

        # Convertir resultado a unidad
        if medida == "a":
            resultado *= 0.621371  # kilómetros a millas
        elif medida == "m":
            resultado *= 1000      # kilómetros a metros

        unidad = {"k": "Kilómetros", "a": "Millas", "m": "Metros"}[medida]
        print(f"La {tipo_distancia} entre los puntos es: {resultado:.2f} {unidad}")
    except ValueError:
        print("Error: debes introducir valores numéricos válidos para las coordenadas.")
else:
    print("Error: opción de distancia o unidad de medida no válida.")
