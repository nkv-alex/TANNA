import re

def normalizar_codigo(codigo):
    # Elimina ; y espacios
    codigo = codigo.strip().replace(";", "")
    
    # Extrae solo la parte numérica
    match = re.search(r'\d+', codigo)
    return match.group() if match else None


def detectar_secuencias(ruta_csv):
    resultados = []
    
    with open(ruta_csv, 'r') as f:
        lineas = f.readlines()
    
    prev = None
    count = 0
    grupo = []

    for linea in lineas:
        raw = linea.strip()
        if not raw:
            continue
        
        actual = normalizar_codigo(raw)
        
        if actual == prev:
            count += 1
            grupo.append(raw)
        else:
            if count > 1:
                resultados.append({
                    "codigo_base": prev,
                    "repeticiones": count,
                    "variaciones": grupo
                })
            
            # reset
            prev = actual
            count = 1
            grupo = [raw]
    
    # último grupo
    if count > 1:
        resultados.append({
            "codigo_base": prev,
            "repeticiones": count,
            "variaciones": grupo
        })

    return resultados


# uso
res = detectar_secuencias("datos.csv")

for r in res:
    print(r)