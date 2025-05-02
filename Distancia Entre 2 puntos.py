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
    # Solicitar las coordenadas de los dos puntos
    x1 = float(input("Introduce la coordenada x del primer punto: "))
    y1 = float(input("Introduce la coordenada y del primer punto: "))
    x2 = float(input("Introduce la coordenada x del segundo punto: "))
    y2 = float(input("Introduce la coordenada y del segundo punto: "))
    
    # Crear los puntos como listas
    punto1 = [x1, y1]
    punto2 = [x2, y2]
    
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