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

## 4. Análisis Exploratorio de Datos (EDA) y Hallazgos Principales
El Análisis Exploratorio de Datos (EDA), desarrollado en el cuaderno de trabajo `02_eda.ipynb` y expuesto interactivamente a través de las tres páginas de la aplicación Streamlit, permitió profundizar en el comportamiento y las dinámicas de las variables del proyecto:
* **Estructura y Calidad de Datos**: Se analizó la integridad del dataset consolidado (`Mineria_Final.csv`), evaluando dimensiones, tipos de variables y aplicando un tratamiento riguroso sobre valores nulos e inconsistencias categóricas detectadas tras la integración de las fuentes externas.
* **Análisis de la Variable Objetivo ($Y$)**: Se examinó la distribución del Valor FOB (en miles de USD) y del Volumen Físico (en toneladas), identificando asimetrías marcadas, concentración de valores en productos clave (como el litio y el yodo) y la presencia de registros atípicos que deberán considerarse en futuras etapas.
* **Relaciones entre Predictores ($X$) y Objetivo ($Y$)**: Se exploraron asociaciones entre el valor de exportación, los precios unitarios, el tipo de cambio y los indicadores macroeconómicos de destino (`PIB_Pais_Destino`, inflación), identificando tanto comportamientos lineales como relaciones no lineales condicionadas por la dinámica de los mercados internacionales.
* **Dimensión Temporal y Contextual ($T$)**: Se estudió la evolución histórica de las exportaciones entre 2005 y 2024, evidenciando tendencias de crecimiento, ciclos económicos y diferencias estructurales importantes entre las distintas **Regiones de Destino** y **Familias de Producto**.
* **Hallazgos Principales**: 
  1. La concentración de las exportaciones no metálicas recae fuertemente en las regiones de Asia-Pacífico y Norteamérica, impulsadas fundamentalmente por la familia del litio.
  2. Se observa una relación directa entre el dinamismo del PIB del país de destino y el volumen importado de sales potásicas y fertilizantes.
  3. Las fluctuaciones del tipo de cambio local generan variaciones y desfases temporales en la competitividad de los valores FOB declarados.

## 5. Estructura del Repositorio de GitHub
El repositorio mantiene una organización modular y limpia para facilitar su revisión:

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
│   └── app/
│       ├── Inicio.py
│       └── pages/
│           ├── 1_EDA.py
│           └── 2_Hallazgos.py
├── requirements.txt
├── README.md                 (Documentación del Avance 1)
└── README_Avance2.md         (Documentación detallada del Avance 2 - Este archivo)
```

## 6. Instrucciones de Ejecución
Para poner en marcha la aplicación interactiva de Streamlit en un entorno local y verificar los resultados del EDA:

1. Clonar o descargar el repositorio y abrir una terminal en la carpeta raíz del proyecto.
2. Instalar las dependencias requeridas ejecutando el siguiente comando en la consola:
   ```bash
   pip install -r requirements.txt
   ```
3. Ejecutar la aplicación multi-página con el comando de Streamlit:
   ```bash
   streamlit run src/app/Inicio.py
   ```

## 7. Principales Dependencias del Proyecto
El proyecto utiliza herramientas de código abierto en Python especificadas en el archivo `requirements.txt`:
* `streamlit`: Framework principal para el desarrollo de la aplicación web interactiva de tres páginas.
* `pandas` y `numpy`: Librerías fundamentales para la manipulación, limpieza y agregación tabular de datos.
* `plotly`: Herramienta avanzada para la generación de visualizaciones interactivas orientadas al análisis exploratorio.
* `wbgapi`: Interfaz de conexión directa con las bases de datos estadísticas del Banco Mundial.
* `yfinance`: Librería de extracción de datos financieros históricos de Yahoo Finance.
* `pycountry`: Utilidad para la normalización y conversión de nombres y códigos internacionales de países.
