import streamlit as st

st.set_page_config(page_title="Hallazgos", layout="wide", page_icon="💡")

st.title("3. Hallazgos Principales")
st.write("Interpretaciones obtenidas del EDA que guiarán las decisiones algorítmicas en la fase de modelado predictivo.")

st.info("**Hallazgo 1: Desbalance estructural (Sparsity) en la variable objetivo.**\n\nDado que casi el 60% de los cruces comerciales son cero, el modelado requerirá filtrar los registros inactivos para proyectar solo transacciones reales, o bien, emplear una arquitectura en dos etapas (modelo de clasificación de ocurrencia seguido de regresión de monto).")

st.warning("**Hallazgo 2: Ruptura del patrón temporal ($T$) por el superciclo de demanda.**\n\nLa evolución temporal muestra una relativa estabilidad hasta 2020, rompiéndose con un crecimiento exponencial reciente. Esta evidencia valida la decisión técnica de separar los años 2020-2024 como 'Conjunto de Prueba', evitando sesgar el entrenamiento del algoritmo con el reciente boom del mercado.")

st.success("**Hallazgo 3: Asimetría del mercado y dispersión regional.**\n\nComo evidenció el Boxplot comparativo, Asia-Pacífico no solo acumula la mayor frecuencia de transacciones, sino que presenta una dispersión y valores atípicos (outliers) drásticamente superiores al resto de las regiones. El modelo predictivo deberá incluir la variable `Region_Destino` codificada (One-Hot Encoding) para no sobreajustarse a la macroeconomía asiática e ignorar el comportamiento de mercados más estables como Europa o Norteamérica.")

st.error("**Hallazgo 4: Relaciones predictivas no lineales (Evidencia del Heatmap).**\n\nLa Matriz de Correlación de Pearson demuestra que, si bien el Volumen Físico tiene una relación esperable con el FOB, las variables macroeconómicas puras (PIB, Inflación, Tipo de Cambio) presentan coeficientes de correlación lineal moderados o bajos. Esto confirma empíricamente que la regresión lineal tradicional será insuficiente y que algoritmos basados en árboles de decisión (Random Forest, XGBoost), capaces de capturar interacciones complejas, tendrán un mejor rendimiento.")