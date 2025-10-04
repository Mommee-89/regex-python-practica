# Ejercicio 5 - Analizador de Fechas y Formateador

# Mapas de meses (claves en minusculas)
meses_corto = {
    "ene":"01","jan":"01",
    "feb":"02","mar":"03",
    "abr":"04","apr":"04",
    "may":"05",
    "jun":"06","jul":"07",
    "ago":"08","aug":"08",
    "sep":"09","sept":"09",
    "oct":"10","nov":"11",
    "dic":"12","dec":"12"
}

meses_largo = {
    "enero":"01","january":"01",
    "febrero":"02","february":"02",
    "marzo":"03","march":"03",
    "abril":"04","april":"04",
    "mayo":"05","may":"05",
    "junio":"06","june":"06",
    "julio":"07","july":"07",
    "agosto":"08","august":"08",
    "septiembre":"09","september":"09",
    "octubre":"10","october":"10",
    "noviembre":"11","november":"11",
    "diciembre":"12","december":"12"
}

def strip_trailing(s):
    # Quitar punto o coma final para la deteccion
    return s.rstrip(".,") 

def extraer_y_convertir(texto):
    words = texto.split()
    n = len(words)
    i = 0
    resultados = []
    
    while i < n:
        token = words[i]
        tc = strip_trailing(token)  # token limpio de punto/coma final
        
        # Formato DD/MM/YYYY
        if tc.count("/") == 2:
            partes = tc.split("/")
            if len(partes) == 3 and all(p.isdigit() for p in partes):
                d = partes[0].zfill(2)
                m = partes[1].zfill(2)
                y = partes[2]
                if len(y) == 4:
                    original = tc
                    estandar = f"{y}-{m}-{d}"
                    resultados.append((original, estandar))
        
        # Formato con guiones: YYYY-MM-DD o DD-MMM-YYYY
        elif tc.count("-") == 2:
            partes = tc.split("-")
            if len(partes) == 3:
                # YYYY-MM-DD
                if partes[0].isdigit() and len(partes[0]) == 4 and partes[1].isdigit() and partes[2].isdigit():
                    y = partes[0]
                    m = partes[1].zfill(2)
                    d = partes[2].zfill(2)
                    original = tc
                    estandar = f"{y}-{m}-{d}"
                    resultados.append((original, estandar))
                # DD-MMM-YYYY (mes corto alfabetico)
                elif partes[0].isdigit() and partes[2].isdigit():
                    month_key = partes[1].lower()
                    if month_key in meses_corto:
                        d = partes[0].zfill(2)
                        m = meses_corto[month_key]
                        y = partes[2]
                        original = tc
                        estandar = f"{y}-{m}-{d}"
                        resultados.append((original, estandar))
        
        # Formato "Mes DD, YYYY" (ej: Junio 30, 2024) - se usan 3 tokens
        else:
            key = tc.lower()
            if key in meses_largo and i + 2 < n:
                day_raw = words[i+1]
                year_raw = words[i+2]
                day_clean = day_raw.rstrip(",.")   # 30, -> 30
                year_clean = year_raw.rstrip(".,") # 2024. -> 2024
                if day_clean.isdigit() and year_clean.isdigit() and len(year_clean) == 4:
                    m = meses_largo[key]
                    d = day_clean.zfill(2)
                    y = year_clean
                    # Reconstruir original manteniendo la coma si existia despues del dia
                    original = f"{words[i]} {words[i+1].rstrip('.')} {words[i+2].rstrip('.')}"
                    estandar = f"{y}-{m}-{d}"
                    resultados.append((original, estandar))
                    i += 3
                    continue  # saltar los tokens consumidos
        
        i += 1
    
    return resultados

# Programa principal
texto = input("Ingresa un texto que contenga fechas: ")
fechas = extraer_y_convertir(texto)

print("Fechas encontradas y convertidas:")
for original, estandar in fechas:
    print(f"- Formato original: {original} -> Estandar: {estandar}")