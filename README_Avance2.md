# Proyecto de Ciencia de Datos - Avance 2: Análisis Exploratorio de Datos (EDA)

## 1. Objetivo del Avance 2
El objetivo principal de esta segunda etapa del proyecto consiste en transitar desde la definición inicial de la problemática planteada en el Avance 1 hacia un profundo entendimiento de los datos disponibles mediante un riguroso Análisis Exploratorio de Datos (EDA). En este avance no se busca implementar modelos predictivos finales ni soluciones de machine learning complejas, sino demostrar que comprendemos cabalmente la estructura del dataset, que detectamos y solucionamos problemas básicos de calidad de datos, que describimos con precisión las distribuciones univariadas y multivariadas de las variables, y que somos capaces de identificar patrones, tendencias, anomalías y relaciones clave entre las variables predictoras y el objetivo. Todo este proceso analítico se organiza y comunica a través de una aplicación interactiva desarrollada en Streamlit estructurada en tres páginas diferenciadas.

## 2. Enriquecimiento del Dataset y Nuevas Variables Integradas
Para responder de manera mucho más robusta a la pregunta de investigación del proyecto, el dataset base de exportaciones mineras no metálicas utilizado inicialmente ha sido sustancialmente enriquecido e integrado mediante scripts automatizados en Google Colab. Se incorporaron nuevas variables predictoras y dimensiones de análisis que provienen de fuentes externas oficiales:

* **Indicadores Macroeconómicos del Banco Mundial (`wbgapi`)**: Se extrajeron datos estadísticos anuales a la medida de cada socio comercial de Chile para capturar el entorno económico de los países receptores:
  * `PIB_Pais_Destino`: Producto Interno Bruto anual del país de destino expresado en dólares corrientes, permitiendo dimensionar el tamaño y la capacidad económica del mercado comprador.
  * `Crecimiento_PIB_Destino_%`: Tasa de variación porcentual anual del PIB del país receptor, útil para evaluar ciclos de expansión o contracción económica en el destino.
  * `Inflacion_Destino_%`: Variación porcentual anual del índice de precios al consumidor (IPC), que refleja la estabilidad de precios y el poder adquisitivo en el país importador.

* **Variables Financieras y Cambiarias (`yfinance`)**:
  * `Tipo_Cambio_Promedio_USD_CLP`: Serie histórica del tipo de cambio nominal convertida a un promedio anual ponderado. Esta variable resulta crucial para entender cómo las fluctuaciones de la paridad cambiaria local afectan la competitividad y el valor FOB declarado de las exportaciones chilenas.

* **Nuevas Variables Creadas y Estructurales**:
  * `Region_Destino`: Dimensión categórica derivada de la estandarización y agrupación de todos los países compradores.
  * `Familia_Producto`: Dimensión categórica que agrupa los productos mineros según su naturaleza comercial y química.

## 3. Agrupaciones Estructurales: Regiones de Destino y Familias de Productos
Con el fin de evitar la dispersión provocada por el análisis individual de cada socio comercial o producto específico, y lograr un enfoque macroestructural, se estructuraron clasificaciones globales que abarcan la **totalidad** de los registros históricos del dataset:

* **Regiones de Destino**: La totalidad de los **125 países de destino** registrados en las estadísticas oficiales de exportación fueron depurados, validados mediante códigos ISO-3 y agrupados exhaustivamente en **8 grandes regiones geográficas y económicas**:
  1. *Norteamérica* (Estados Unidos, Canadá, México).
  2. *Mercosur* (Brasil, Argentina, Paraguay, Uruguay, Venezuela, Bolivia).
  3. *Unión Europea* (Bélgica, Países Bajos, Italia, Francia, España, Alemania, Austria, Dinamarca, Grecia, Finlandia, Portugal, Polonia, Letonia, Lituania, Suecia, Irlanda, Chipre, Rumanía, Luxemburgo, entre otros).
  4. *Europa No-UE* (Reino Unido, Noruega, Suiza, Rusia).
  5. *Asia-Pacífico* (China, India, Japón, Corea del Sur, Australia, Vietnam, Malasia, Taiwán, Singapur, Indonesia, Filipinas, Tailandia, Nueva Zelanda, entre otros).
  6. *Resto de LATAM y Caribe* (Colombia, Perú, Ecuador, Costa Rica, Guatemala, El Salvador, Panamá, República Dominicana, Cuba, entre otros).
  7. *Medio Oriente y Norte de África (MENA)* (Arabia Saudita, Emiratos Árabes Unidos, Turquía, Egipto, Argelia, Israel, Marruecos, entre otros).
  8. *África Subsahariana* (Sudáfrica, Nigeria, Kenia, Etiopía, Ghana, Angola, entre otros).

* **Familias de Producto**: Todos los productos mineros no metálicos contenidos en el registro histórico oficial fueron clasificados íntegramente en cuatro categorías homogéneas principales:
  1. *Litio*: Agrupa todas las variantes y compuestos derivados del litio (cloruro de litio, carbonato de litio, etc.).
  2. *Yodo*: Concentra las exportaciones de yodo en sus diferentes grados de pureza y presentaciones comerciales.
  3. *Potasio y Fertilizantes*: Agrupa los nitratos de potasio, salitre y sales potásicas destinadas principalmente a la industria agrícola mundial.
  4. *Otros No Metálicos*: Agrupa el resto de minerales no metálicos complementarios presentes en las estadísticas de comercio exterior chileno.

## 4. Proceso de Limpieza, Estandarización y Análisis Exploratorio de Datos (EDA)
A partir de la integración automatizada de las APIs y de la creación de las nuevas agrupaciones estructurales, los datos pasaron por un riguroso proceso técnico de depuración: se trataron valores nulos críticos, se corrigieron inconsistencias categóricas en las denominaciones geográficas y se estandarizaron formatos numéricos, generando como resultado el archivo maestro consolidado `Mineria_Final.csv`.

Sobre este dataset procesado, se ejecutó el **Análisis Exploratorio de Datos (EDA)** estructurado en el cuaderno de trabajo y plasmado de forma interactiva en la aplicación Streamlit. Esto permitió examinar a fondo las distribuciones univariadas de la variable objetivo ($Y$) —tanto el valor FOB en dólares como el volumen físico en toneladas—, contrastar las diferencias de comportamiento comercial entre las distintas familias de productos y regiones geográficas, y evaluar de manera preliminar la presencia de patrones, tendencias temporales ($T$) y relaciones lineales o no lineales frente a las variables predictoras ($X$).

## 5. Estructura del Repositorio de GitHub
El repositorio se encuentra organizado de la siguiente manera para separar los datos originales, los datos procesados, la documentación técnica y los códigos fuente de la aplicación:

```text
Proyecto-Ciencia-de-Datos/
├── data/
│   ├── raw/
│   │   ├── Exportaciones-Chilenas-Valorizadas...
│   │   ├── Exportaciones-Fisicas-por-Pais...
│   │   └── Produccion_1996-2024a.xls
│   └── processed/
│       ├── DATASET COMPLETO.csv.xlsx
│       ├── Mineria_Enriquecida_Corregida.csv
│       ├── Mineria_Final.csv
│       └── Mineria_Integrada_Consistente...
├── docs/
│   ├── Propuestas de Nuevas Variables...
│   └── Reporte nuevo dataset.pdf
├── figures/
│   └── .gitkeep
├── src/
│   └── app/                  (o src/EDA/)
│       ├── Inicio.py
│       └── pages/
│           ├── 1_EDA.py
│           └── 2_Hallazgos.py
├── requirements.txt
├── README.md                 (Documentación del Avance 1)
└── README_Avance2.md         (Documentación detallada del Avance 2 - Este archivo)
