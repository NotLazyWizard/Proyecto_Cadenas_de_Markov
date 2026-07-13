import random

# Importando textos limpios (sin puntuación, sin mayúsculas, sin acentos)

with open("EL_PRINCIPITO_limpio.txt", "r", encoding="utf-8") as archivo:
    principito = archivo.read().split()      

with open("No_Tengo_Boca_Y_Debo_Gritar_limpio.txt", "r", encoding="utf-8") as archivo:
    ntbydg = archivo.read().split()      

# Tablas de frecuencias de orden 1 y orden 2

def tabla_frecuencias(texto):

    tabla = {}
    for i in range(len(texto) - 1):
        par = (texto[i], texto[i + 1])
        tabla[par] = tabla.get(par, 0) + 1
    return tabla

def tabla_frecuencias_orden2(texto):

    tabla = {}
    for i in range(len(texto) - 2):
        tripleta = (texto[i], texto[i + 1], texto[i + 2])
        tabla[tripleta] = tabla.get(tripleta, 0) + 1
    return tabla

tabla1_principito = tabla_frecuencias(principito)
tabla1_ntbydg     = tabla_frecuencias(ntbydg)

tabla2_principito = tabla_frecuencias_orden2(principito)
tabla2_ntbydg     = tabla_frecuencias_orden2(ntbydg)

# Predicción

def predecir(contexto, tabla1, tabla2):

    if len(contexto) >= 2:
        a, b = contexto[-2], contexto[-1]
        conteos = {c: cnt for (x, y, c), cnt in tabla2.items() if (x, y) == (a, b)}
        if conteos:                           
            total = sum(conteos.values())
            return {pal: cnt / total for pal, cnt in conteos.items()}

    a = contexto[-1]
    conteos = {b: cnt for (x, b), cnt in tabla1.items() if x == a}
    if not conteos:
        return {}
    total = sum(conteos.values())
    return {pal: cnt / total for pal, cnt in conteos.items()}

# Temperatura

def ajustar_temperatura(distribucion, temperatura):

    if temperatura <= 0:
        raise ValueError("La temperatura debe ser mayor que 0.")
    ajustada = {pal: prob ** (1.0 / temperatura) for pal, prob in distribucion.items()}
    total = sum(ajustada.values())
    return {pal: prob / total for pal, prob in ajustada.items()}

# Generando textos

def generar_texto(tabla1, tabla2, texto_original, n_palabras=50, temperatura=1.0):

    palabra_inicial = random.choice(list({a for (a, _) in tabla1.keys()}))
    generado = [palabra_inicial]

    for _ in range(n_palabras - 1):
        distribucion = predecir(generado, tabla1, tabla2)

        if not distribucion:                     # sin salida: reiniciar contexto
            generado.append(random.choice(texto_original))
            continue

        distribucion = ajustar_temperatura(distribucion, temperatura)
        siguiente = random.choices(
            list(distribucion.keys()),
            weights=distribucion.values()
        )[0]
        generado.append(siguiente)

    return " ".join(generado)

# Comparando cualitativamente los textos generados

def comparar_textos(texto1, texto2, etiqueta1="Corpus 1", etiqueta2="Corpus 2"):
    print(f"\n{'─'*50}")
    print(f"Texto generado – {etiqueta1}:")
    print(texto1)
    print(f"\nTexto generado – {etiqueta2}:")
    print(texto2)
    print(f"{'─'*50}")

# Transiciones más frecuentes

def transiciones_frecuentes(tabla, n=10):
    transiciones = sorted(tabla.items(), key=lambda item: item[1], reverse=True)[:n]
    for transicion, frecuencia in transiciones:
        print(f"  {transicion}  →  {frecuencia}")

#Main

print("=" * 55)
print("  GENERACIÓN DE TEXTO – temperatura = 1.0 (normal)")
print("=" * 55)

texto_principito = generar_texto(tabla1_principito, tabla2_principito, principito, n_palabras=50, temperatura=1.0)
texto_ntbydg     = generar_texto(tabla1_ntbydg,     tabla2_ntbydg,     ntbydg,     n_palabras=50, temperatura=1.0)

comparar_textos(texto_principito, texto_ntbydg,
                etiqueta1="El Principito",
                etiqueta2="No Tengo Boca y Debo Gritar")

# Efecto de la temperatura
print("\n" + "=" * 55)
print("  EFECTO DE TEMPERATURA  (El Principito, 50 palabras)")
print("=" * 55)

for temp in [0.5, 1.0, 1.5]:
    print(f"\n  Temperatura = {temp}:")
    print(generar_texto(tabla1_principito, tabla2_principito, principito, n_palabras=50, temperatura=temp))


print("\n" + "=" * 69)
print("  EFECTO DE TEMPERATURA  (No tengo boca y debo gritar, 50 palabras)")
print("=" * 69)

for temp in [0.5, 1.0, 1.5]:
    print(f"\n  Temperatura = {temp}:")
    print(generar_texto(tabla1_ntbydg, tabla2_ntbydg, ntbydg, n_palabras=50, temperatura=temp))

# Analizando las 10 transiciones más frecuentes para cada modelo.
print("\n" + "=" * 55)
print("  TRANSICIONES MÁS FRECUENTES (orden 1)")
print("=" * 55)

print("\nEl Principito:")
transiciones_frecuentes(tabla1_principito)

print("\nNo Tengo Boca y Debo Gritar:")
transiciones_frecuentes(tabla1_ntbydg)

print("\n" + "=" * 55)
print("  TRANSICIONES MÁS FRECUENTES (orden 2)")
print("=" * 55)

print("\nEl Principito:")
transiciones_frecuentes(tabla2_principito)

print("\nNo Tengo Boca y Debo Gritar:")
transiciones_frecuentes(tabla2_ntbydg)