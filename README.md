# Generación de Texto con Cadenas de Markov

## Descripción

Este proyecto implementa un generador de texto basado en **Cadenas de Markov**, utilizando dos textos literarios como corpus de entrenamiento:

- **El Principito** (de Antoine de Saint-Exupéry)
- **No Tengo Boca y Debo Gritar** (de Harlan Ellison)

El programa analiza patrones de transición entre palabras y genera nuevo texto que imita el estilo y estructura de los textos originales.

## Funcionalidad Principal

### 1. **Análisis de Frecuencias**

El código construye tablas de frecuencias que registran con qué frecuencia ciertas palabras siguen a otras:

- **Orden 1**: Pares de palabras consecutivas (bigramas)
- **Orden 2**: Triples de palabras consecutivas (trigramas)

### 2. **Predicción de Palabras**

La función `predecir()` utiliza el contexto (palabras anteriores) para determinar qué palabra es probable que siga a continuación, basándose en las frecuencias observadas en el corpus.

### 3. **Control de Temperatura**

El parámetro de temperatura controla el balance entre coherencia y creatividad:

- **Temperatura baja (< 1.0)**: Texto más predecible y coherente
- **Temperatura alta (> 1.0)**: Texto más aleatorio y creativo

### 4. **Generación de Texto**

El código genera nuevos textos de una longitud especificada, seleccionando palabras según sus probabilidades predichas.

## Archivos del Proyecto

| Archivo                                    | Descripción                                                             |
| ------------------------------------------ | ------------------------------------------------------------------------ |
| `logica.py`                              | Script principal con la lógica de Cadenas de Markov                     |
| `cadenas_de_markov.ipynb`                | Notebook con análisis adicional (opcional)                              |
| `EL_PRINCIPITO_limpio.txt`               | Corpus limpio: El Principito (sin puntuación, minúsculas, sin acentos) |
| `No_Tengo_Boca_Y_Debo_Gritar_limpio.txt` | Corpus limpio: No Tengo Boca y Debo Gritar                               |
| `EL PRINCIPITO.txt`                      | Texto original: El Principito                                            |
| `No Tengo Boca Y Debo Gritar.txt`        | Texto original: No Tengo Boca y Debo Gritar                              |

## Ejecución

```bash
python logica.py
```

## Salida del Programa

El programa ejecuta los siguientes análisis:

1. **Generación básica** con temperatura = 1.0

   - Genera 50 palabras a partir de cada corpus
   - Compara los textos generados
2. **Efecto de temperatura**

   - Demuestra cómo valores de temperatura (0.5, 1.0, 1.5) afectan la salida
   - Se prueba con ambos textos
3. **Análisis de transiciones frecuentes**

   - Las 10 transiciones más comunes de orden 1 (pares de palabras)
   - Las 10 transiciones más comunes de orden 2 (triples de palabras)

## Conceptos Clave

### Cadenas de Markov

Un modelo probabilístico donde el siguiente estado depende únicamente del estado actual, no de toda la historia. En este caso, la próxima palabra depende de las palabras anteriores.

### Bigramas (Orden 1)

Pares de palabras consecutivas. Ej: ("el", "principito"), ("no", "tengo")

### Trigramas (Orden 2)

Triples de palabras consecutivas. Ej: ("el", "principito", "es"), ("no", "tengo", "boca")

### Temperatura

Parámetro que controla la distribución de probabilidades:

- Formula: `prob_ajustada = prob ^ (1/temperatura)`
- Valores menores hacen la distribución más concentrada (menor entropía)
- Valores mayores hacen la distribución más uniforme (mayor aleatoriedad)
