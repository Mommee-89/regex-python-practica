# Ejercicio 3 - Validador de Contrasenas Seguras

def validar_contrasena(contra):
    # Verificar longitud minima de 8 caracteres
    if len(contra) < 8:
        return False
    
    # Variables de control
    tiene_mayus = False
    tiene_minus = False
    tiene_numero = False
    tiene_especial = False
    
    # Lista de caracteres especiales permitidos
    especiales = "@$!%*?&#"
    
    # Recorrer cada caracter de la contrasena
    for c in contra:
        if c >= "A" and c <= "Z":
            tiene_mayus = True
        elif c >= "a" and c <= "z":
            tiene_minus = True
        elif c >= "0" and c <= "9":
            tiene_numero = True
        elif c in especiales:
            tiene_especial = True
    
    # Validar que cumpla todas las condiciones
    if tiene_mayus and tiene_minus and tiene_numero and tiene_especial:
        return True
    else:
        return False


# Programa principal
contra = input("Ingresa una contrasena: ")

if validar_contrasena(contra):
    print(contra, "-> Valida")
else:
    print(contra, "-> Invalida")