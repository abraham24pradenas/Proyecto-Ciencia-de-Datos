import streamlit as st
import pandas as pd

# 1. CONFIGURACIÓN INICIAL
st.set_page_config(page_title="Inicio", layout="wide", page_icon="⛏️")

# 2. CARGA DE DATOS
@st.cache_data
def cargar_datos():
    # Ahora lee el archivo final corregido (sin necesidad de arreglar comas)
    df = pd.read_csv("Mineria_Final.csv", sep=";", encoding="utf-8")
    df['Año'] = df['Año'].astype(int)
    df['Exportacion_Real'] = df['Valor_FOB_Miles_USD'] > 0
    return df

try:
    df = cargar_datos()
    
    # --- FILTROS INTERACTIVOS EN LA BARRA LATERAL ---
    st.sidebar.header("Filtros del Modelo")
    
    # Nuevo filtro por Familia de Producto
    lista_familias = df['Familia_Producto'].unique().tolist()
    seleccion_familia = st.sidebar.multiselect(
        "Seleccione Familia de Minerales:", 
        options=lista_familias, 
        default=lista_familias
    )
    
    lista_regiones = df['Region_Destino'].dropna().unique().tolist()
    seleccion_region = st.sidebar.multiselect(
        "Seleccione Región de Destino:", 
        options=lista_regiones, 
        default=lista_regiones
    )
    
    anio_min, anio_max = int(df['Año'].min()), int(df['Año'].max())
    rango_anios = st.sidebar.slider(
        "Ventana Temporal (Año):", 
        min_value=anio_min, max_value=anio_max, value=(anio_min, anio_max)
    )
    
    # --- APLICAR FILTROS Y GUARDAR EN MEMORIA ---
    df_filtrado = df[
        (df['Familia_Producto'].isin(seleccion_familia)) &
        (df['Region_Destino'].isin(seleccion_region)) &
        (df['Año'] >= rango_anios[0]) &
        (df['Año'] <= rango_anios[1])
    ]
    st.session_state["datos_mineria"] = df_filtrado

except FileNotFoundError:
    st.error("No se encontró el archivo 'Mineria_Final.csv'. Asegúrate de haber ejecutado el script de preparación y que el archivo esté en la misma carpeta.")
    st.stop()

# ==========================================
# PÁGINA 1: PROBLEMA Y DATOS
# ==========================================
st.title("⛏ Proyecto: Exportaciones Mineras No Metálicas (2005-2024)")
st.markdown("### Contexto del Proyecto")
st.write("**Pregunta Principal:** ¿Qué variables de demanda física, oferta nacional y macroeconomía internacional ($X$) permiten estimar el valor monetario FOB de las exportaciones no metálicas de Chile ($Y$) en una ventana temporal anual ($T$)?")

st.markdown("""
* **Variable Objetivo (Y):** Valor FOB en miles de dólares (`Valor_FOB_Miles_USD`).
* **Predictores (X):** Variables categóricas de mercado (`Familia_Producto`, `Region_Destino`), demanda física (`Volumen_Fisico_Ton`), oferta nacional (`Produccion_Nacional_Ton`), y contexto macroeconómico (PIB, Inflación, Tipo de Cambio, etc.).
* **Contexto temporal (T):** Ventana de evaluación anual entre los años 2005 y 2024.
""")

st.markdown("### Estructura del Dataset Final")
col1, col2, col3 = st.columns(3)
col1.metric("Registros Totales", f"{df.shape[0]:,}".replace(",", "."))
col2.metric("Variables Predictoras (X)", 9) # Número exacto sin contar Y ni T
col3.metric("Rango Temporal", f"{anio_min} - {anio_max}")

st.markdown("### Calidad de los Datos y Limpieza")
st.write("Antes de iniciar el EDA, identificamos y tratamos los siguientes problemas estructurales en el dataset integrado:")
st.markdown("""
* **Reducción de Dimensionalidad:** Se agruparon 19 productos aduaneros en 4 grandes `Familias de Producto` (Litio, Yodo, Potasio/Fertilizantes, Otros) para evitar ruido estadístico en el modelo predictivo.
* **Ceros Estructurales (Sparsity):** El 59% de los registros en `Valor_FOB_Miles_USD` son cero, generado por cruces de periodos comerciales inactivos.
* **Nulos Matemáticos:** Los nulos en `Precio_Unitario_USD_x_Ton` resultan de divisiones por cero en el volumen físico (Variable excluida del modelo para evitar *Data Leakage*).
""")

st.markdown("### Resumen del Subconjunto Filtrado")
c1, c2, c3, c4 = st.columns(4)
c1.metric("Registros Activos", f"{len(df_filtrado):,}".replace(",", "."))
c2.metric("FOB Total", f"${(df_filtrado['Valor_FOB_Miles_USD'].sum() / 1000):,.0f}M".replace(",", "."))
c3.metric("Volumen Total", f"{(df_filtrado['Volumen_Fisico_Ton'].sum() / 1000):,.0f}k Ton".replace(",", "."))
c4.metric("TC Promedio", f"${df_filtrado['Tipo_Cambio_Promedio_USD_CLP'].mean():,.0f}".replace(",", "."))