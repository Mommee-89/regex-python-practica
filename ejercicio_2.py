# Ejercicio 2 - Extractor de Numeros de Telefono

def es_digito(car):
    # Verifica si un caracter es numero del 0 al 9
    return car >= "0" and car <= "9"

def extraer_telefonos(texto):
    telefonos = []
    palabra = ""
    
    for car in texto:
        # Vamos construyendo palabra con numeros y posibles simbolos validos
        if es_digito(car) or car in ["-", " ", "(", ")",]:
            palabra += car
        else:
            # Cuando encontramos un separador diferente, revisamos la palabra
            if palabra != "":
                if validar_formato(palabra):
                    telefonos.append(palabra.strip())
                palabra = ""
    
    # Revisar al final por si el texto termina con telefono
    if palabra != "":
        if validar_formato(palabra):
            telefonos.append(palabra.strip())
    
    return telefonos

def validar_formato(palabra):
    # Quitar espacios, guiones y parentesis para contar solo numeros
    limpio = ""
    for c in palabra:
        if es_digito(c):
            limpio += c
    
    # Debe tener exactamente 10 digitos
    if len(limpio) != 10:
        return False
    
    return True


# Programa principal
texto = input("Ingresa un texto que contenga numeros de telefono: ")

telefonos = extraer_telefonos(texto)

print("Telefonos encontrados:", telefonos)