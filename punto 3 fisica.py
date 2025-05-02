import numpy as np

# Función para calcular la distancia de taxi
def distancia_taxi(puntos):
    return sum(np.sum(np.abs(np.array(puntos[i]) - np.array(puntos[i+1]))) for i in range(len(puntos) - 1)) 

# Función para calcular la distancia euclidiana
def distancia_euclidea(puntos):
    return sum(np.sqrt(np.sum((np.array(puntos[i]) - np.array(puntos[i+1])) ** 2)) for i in range(len(puntos) - 1))

# Función para calcular la distancia máxima
def distancia_maximo(puntos):
    return sum(np.max(np.abs(np.array(puntos[i]) - np.array(puntos[i+1]))) for i in range(len(puntos) - 1))

# Solicitar al usuario el tipo de distancia
distancia = input("¿Qué distancia quieres calcular? (t/e/m/z): ")
if distancia in "z":
    print("Saliendo del programa.")
    exit()

# Calcular distancia
print("Introduce las coordenadas de los puntos (escribe '0,0' para terminar):")
puntos = []
while True:
    try:
        entrada = input("Introduce las coordenadas (x, y) separadas por coma: ")
        if entrada.strip().lower() == "0,0":
            if len(puntos) < 2:
                print("Debes introducir al menos dos puntos.")
                continue
            break

        x, y = map(float, entrada.split(","))
        
        # Validar que el punto sea mayor al anterior
        if puntos and (x <= puntos[-1][0] or y <= puntos[-1][1]):
            print("El punto ingresado debe ser mayor al anterior en ambas coordenadas.")
            continue
        
        puntos.append([x, y])
    except ValueError:
        print("Por favor, introduce valores válidos (ejemplo: 1.0, 2.0).")

# Convertir las coordenadas a metros
puntos = [[coord * 1000 for coord in punto] for punto in puntos]

# Calcular la distancia total según la opción seleccionada
if distancia == "t":
    resultado = distancia_taxi(puntos)
    tipo_distancia = "distancia de taxi"
elif distancia == "e":
    resultado = distancia_euclidea(puntos)
    tipo_distancia = "distancia euclidiana"
elif distancia == "m":
    resultado = distancia_maximo(puntos)
    tipo_distancia = "distancia máxima"
else:
    print("Opción de distancia no válida.")
    resultado = None

# Mostrar el resultado total
if resultado is not None:
    print(f"La {tipo_distancia} total entre los puntos es: {resultado:.2f} metros")