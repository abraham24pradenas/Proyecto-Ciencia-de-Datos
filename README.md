# Proyecto: Predicción y Análisis de Exportaciones Mineras No Metálicas de Chile (2005-2024)

## 1. Contexto y Justificación del Caso
Este proyecto se centra en el comercio exterior y los recursos estratégicos de Chile, específicamente en la minería no metálica, la cual incluye minerales como yodo, litio, nitratos, sales y sus derivados[cite: 7]. Este sector posee un alto impacto económico a nivel país, especialmente en el contexto actual de la transición energética global[cite: 7]. 

El problema analítico principal consiste en proyectar y comprender la demanda internacional y el valor monetario de estas exportaciones[cite: 7]. Para lograr esto, se analizará la información en función del tipo de producto, el país comprador y las futuras condiciones macroeconómicas externas[cite: 7].

## 2. Alcance y Ventana Temporal
* **Ventana histórica total:** El análisis abarca un periodo continuo desde 2005 hasta 2024, entregando 20 años de datos anuales por país y producto[cite: 7].
* **Estrategia predictiva a futuro:** El modelado final dividirá estos datos en un conjunto de entrenamiento (2005-2019) y un conjunto de prueba (2020-2024), con el objetivo de evaluar la capacidad del algoritmo para predecir el impacto de la pandemia y el auge global de la demanda de litio[cite: 4, 7].

## 3. Ecosistema de Datos y Recolección
Para construir una visión económica integral, se construyó un ecosistema basado en tres pilares extraídos desde los registros oficiales de COCHILCO y el Servicio Nacional de Aduanas[cite: 4, 7]:
* **Rentabilidad Comercial:** Base histórica que aporta el ingreso monetario (Valor FOB)[cite: 4].
* **Demanda Real:** Estructura que aporta el volumen físico exportado en toneladas[cite: 4].
* **Oferta Macro:** Datos de producción nacional que actúan como restricción para identificar fluctuaciones de extracción local[cite: 4].

Mediante la combinación matemática de las dos primeras fuentes, se creó además una variable clave para el modelo: `Precio_Unitario = Valor_FOB / Volumen_Fisico`[cite: 4].

## 4. Perfilado Inicial del Dataset (Avance 1)
El proceso de integración inicial se ejecutó aplicando transformaciones de formato largo (`pd.melt()`) y cruces relacionales (`Inner Join` y `Left Join`)[cite: 4]. El diagnóstico técnico del archivo resultante (`Mineria_Integrada_Consistente.csv`) es el siguiente:

* **Dimensiones del Dataset:** El archivo consolidado contiene 18.540 registros y 7 columnas[cite: 4, 6].
* **Estructura Base (Llaves):** Los datos se encuentran indexados por `Producto`, `Pais_Destino` y `Año`[cite: 5, 6].
* **Variables Consolidadas:**
  * `Producto` (Categórica): Identificación del mineral[cite: 7].
  * `Pais_Destino` (Categórica): Mercado comprador[cite: 7].
  * `Año` (Numérica discreta): Eje temporal base (2005-2024)[cite: 7].
  * `Valor_FOB_Miles_USD` (Numérica continua): Monto anual valorizado en miles de dólares[cite: 7].
  * `Volumen_Fisico_Ton` (Numérica continua): Cantidad exportada.
  * `Precio_Unitario_USD_x_Ton` (Numérica continua): Indicador matemático calculado[cite: 6].
  * `Produccion_Nacional_Ton` (Variable a transformar): Volumen de extracción local[cite: 6].

**Diagnóstico de Calidad de Datos y Siguientes Pasos:**
Durante el perfilado inicial, se identificaron dos alertas estructurales:
1. **Valores Nulos Lógicos:** Se detectó la presencia de valores `NaN` generados por la integración en bruto[cite: 4, 6].
2. **Conversión de Tipos:** La columna `Produccion_Nacional_Ton` requiere una conversión forzada a un formato numérico continuo[cite: 4, 6].

## 5. Estructura de este Repositorio
* `Exportaciones-Chilenas-Valorizadas-por-Pais-de-Destino-2005-2024a.xls`: Dataset original de ingresos.
* `Exportaciones-Fisicas-por-Pais-de-destino-2005-2024a.xls`: Dataset original de volúmenes.
* `Produccion_1996-2024a.xls`: Dataset original de oferta local.
* `Integración datasets mineros.ipynb`: Jupyter Notebook que contiene el código completo en Python con las funciones de limpieza inicial, los cruces relacionales y el perfilado estadístico de las variables.
* `Mineria_Integrada_Consistente.csv`: Dataset final consolidado de 18.540 filas listo para la siguiente etapa de limpieza e ingeniería de características.
