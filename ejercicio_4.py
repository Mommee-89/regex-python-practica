# Ejercicio 4 - Extractor de URLs y Dominios

def extraer_urls(texto):
    urls = []
    palabras = texto.split()
    
    for palabra in palabras:
        # Revisar si la palabra parece una url valida
        if palabra.startswith("http://") or palabra.startswith("https://") or palabra.startswith("www."):
            # Quitar signos de puntuacion final si los hay
            while palabra.endswith(".") or palabra.endswith(","):
                palabra = palabra[:-1]
            urls.append(palabra)
    return urls

def analizar_url(url):
    protocolo = ""
    dominio = ""
    ruta = ""
    
    if url.startswith("http://"):
        protocolo = "http"
        resto = url[len("http://"):]
    elif url.startswith("https://"):
        protocolo = "https"
        resto = url[len("https://"):]
    else:
        resto = url
        protocolo = "sin protocolo"
    
    # Separar dominio y ruta
    if "/" in resto:
        partes = resto.split("/", 1)
        dominio = partes[0]
        ruta = "/" + partes[1]
    else:
        dominio = resto
    
    return protocolo, dominio, ruta


# Programa principal
texto = input("Ingresa un texto que contenga URLs: ")

urls = extraer_urls(texto)

contador = 1
for url in urls:
    print("URL", contador, ":", url)
    protocolo, dominio, ruta = analizar_url(url)
    print("  Protocolo:", protocolo)
    print("  Dominio:", dominio)
    if ruta != "":
        print("  Ruta:", ruta)
    contador += 1