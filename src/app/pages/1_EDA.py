import streamlit as st
import plotly.express as px

st.set_page_config(page_title="EDA", layout="wide", page_icon="📊")

# Recuperar los datos filtrados desde la memoria (session_state)
if "datos_mineria" not in st.session_state:
    st.warning("⚠️ Por favor, ve a la página 'Inicio' para cargar y filtrar los datos.")
    st.stop()

df_filtrado = st.session_state["datos_mineria"]
df_ventas = df_filtrado[df_filtrado['Exportacion_Real'] == True]

st.title("2. Análisis Exploratorio de Datos (EDA)")

# --- 1. ESTADÍSTICA DESCRIPTIVA ---
st.markdown("### 1. Resumen Estadístico (Medidas de Tendencia y Dispersión)")
vars_numericas = ['Valor_FOB_Miles_USD', 'Volumen_Fisico_Ton', 'PIB_Pais_Destino', 'Inflacion_Destino_%']
st.dataframe(df_filtrado[vars_numericas].describe().T.style.format("{:,.2f}"))

# --- 2. DISTRIBUCIÓN Y DISPERSIÓN POR CATEGORÍA ---
st.markdown("### 2. Distribución y Dispersión de la Variable Objetivo ($Y$)")
col_hist, col_box = st.columns(2)
with col_hist:
    fig_hist = px.histogram(df_ventas, x="Valor_FOB_Miles_USD", log_y=True, nbins=50, title="Histograma Valor FOB (Escala Log)")
    st.plotly_chart(fig_hist, use_container_width=True)
with col_box:
    # Nuevo Boxplot Comparativo por Región
    fig_box = px.box(df_ventas, x="Region_Destino", y="Valor_FOB_Miles_USD", 
                     color="Region_Destino", log_y=True, 
                     title="Dispersión del FOB por Macro-Región")
    fig_box.update_layout(showlegend=False, xaxis_title=None)
    st.plotly_chart(fig_box, use_container_width=True)

# --- 3. FRECUENCIA DE CATEGORÍAS ---
st.markdown("### 3. Frecuencia de Registros por Destino")
df_frecuencia = df_filtrado['Region_Destino'].value_counts().reset_index()
df_frecuencia.columns = ['Region_Destino', 'Frecuencia']
fig_bar = px.bar(df_frecuencia, x='Frecuencia', y='Region_Destino', orientation='h', title="Concentración de envíos por Macro-Región")
st.plotly_chart(fig_bar, use_container_width=True)

# --- 4. CORRELACIÓN Y TEMPORALIDAD ---
st.markdown("### 4. Relaciones Bivariadas y Dimensión Temporal")
col_corr, col_temp = st.columns(2)
with col_corr:
    # Nueva Matriz de Correlación (Heatmap)
    vars_corr = ['Valor_FOB_Miles_USD', 'Volumen_Fisico_Ton', 'PIB_Pais_Destino', 'Inflacion_Destino_%', 'Tipo_Cambio_Promedio_USD_CLP']
    df_corr = df_ventas[vars_corr].corr()
    fig_heatmap = px.imshow(df_corr, text_auto=".2f", aspect="auto", 
                            color_continuous_scale='RdBu_r', 
                            title="Correlación de Pearson")
    st.plotly_chart(fig_heatmap, use_container_width=True)
with col_temp:
    df_agrupado_anio = df_filtrado.groupby('Año')['Valor_FOB_Miles_USD'].sum().reset_index()
    fig_temp = px.line(df_agrupado_anio, x='Año', y='Valor_FOB_Miles_USD', markers=True, title="Evolución del FOB (Sumatoria)")
    st.plotly_chart(fig_temp, use_container_width=True)