# Ejercicio 1 - Validador de Correos Electronicos con Lectura de Archivo
# Autor: Diego Flores Ortiz

# Importaciones necesarias
import matplotlib.pyplot as plt

# Funcion para validar correos electronicos
def validar_correo(correo):
    if "@" not in correo:
        return False
    
    partes = correo.split("@")
    if len(partes) != 2:
        return False
    
    usuario = partes[0]
    dominio = partes[1]
    
    if usuario == "":
        return False
    
    if "." not in dominio:
        return False
    
    if not (dominio.endswith(".com") or dominio.endswith(".mx") or dominio.endswith(".org")):
        return False
    
    return True


# Lectura del archivo de texto
try:
    with open("correos.txt", "r") as archivo:
        lineas = archivo.readlines()
except FileNotFoundError:
    print("Error: No se encontro el archivo 'correos.txt'")
    exit()

# Contadores
validos = 0
invalidos = 0

# Procesar cada correo del archivo
for linea in lineas:
    correo = linea.strip()
    if correo == "":
        continue  # Ignora lineas vacias
    if validar_correo(correo):
        validos += 1
    else:
        invalidos += 1

# Mostrar resultados en consola (bash)
print("Resultados del analisis de correos:")
print("Correos validos:", validos)
print("Correos invalidos:", invalidos)

# Mostrar resultados graficamente
etiquetas = ['Validos', 'Invalidos']
valores = [validos, invalidos]

plt.bar(etiquetas, valores, color=['green', 'red'])
plt.title("Analisis de Correos Electronicos")
plt.ylabel("Cantidad")
plt.xlabel("Tipo de correo")
plt.show()