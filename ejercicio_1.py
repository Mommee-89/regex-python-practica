# Ejercicio 1 - Validador de Correos Electronicos Simple

def validar_correo(correo):
    # Verificar que contenga '@'
    if "@" not in correo:
        return False
    
    # Separar en usuario y dominio
    partes = correo.split("@")
    
    # Debe haber exactamente dos partes: antes y despues del '@'
    if len(partes) != 2:
        return False
    
    usuario = partes[0]
    dominio = partes[1]
    
    # Usuario no puede estar vacio
    if usuario == "":
        return False
    
    # Dominio debe tener al menos un punto y terminar en .com, .mx, .org
    if "." not in dominio:
        return False
    
    # Revisar que termine con una extension valida
    if not (dominio.endswith(".com") or dominio.endswith(".mx") or dominio.endswith(".org")):
        return False
    
    return True


# Programa principal
correo = input("Ingresa un correo electronico: ")

if validar_correo(correo):
    print(correo, "-> Valido")
else:
    print(correo, "-> Invalido")