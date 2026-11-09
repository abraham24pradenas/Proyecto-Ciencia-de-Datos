# 📊 Avance 3: Rendimiento y Explicabilidad
**Proyecto:** Predicción del Valor FOB en Exportaciones de Minería No Metálica (Chile)

Este documento resume la evaluación de rendimiento y la explicabilidad matemática de los modelos predictivos desarrollados para estimar el Valor FOB (en miles de USD) de las transacciones comerciales activas.

---

## 🎯 1. Motivación y Objetivo
El sector de la minería no metálica chilena (Litio, Yodo, etc.) presenta una altísima volatilidad en sus ingresos debido a su dependencia de factores internacionales. 

**Objetivo predictivo:** Identificar qué algoritmo y conjunto de entradas nos permite estimar con el menor error el Valor FOB de las exportaciones activas, aislando el 59% de ceros estructurales justificados durante nuestro Análisis Exploratorio de Datos (EDA).

---

## 🛠️ 2. Solución y Validación (Anti-Fuga)
Para evaluar la robustez de los modelos ante cambios de régimen económico (*concept drift*), se aplicó una partición temporal estricta que aísla el boom de precios:
* **Entrenamiento (Train):** 2005 - 2019 (Comportamiento histórico).
* **Prueba (Test):** 2020 - 2024 (Disrupción por el superciclo minero).

Se compararon dos algoritmos sobre la misma tarea de regresión continua:
1. **Modelo Baseline:** Regresión Lineal Múltiple.
2. **Modelo Avanzado:** Random Forest Regressor.

> **Nota sobre el Pipeline:** Se aplicó imputación de nulos y escalado (`StandardScaler`) ajustados exclusivamente en el set de entrenamiento, junto con codificación One-Hot para variables categóricas (Región y Familia). Se excluyó el precio unitario para evitar fugas de información.

---

## 📈 3. Rendimiento Comparado (Test Set 2020-2024)

| Métrica | Regresión Lineal | Random Forest |
| :--- | :--- | :--- |
| **MAE** | 19,576.04 | 14,534.22 |
| **RMSE** | 188,628.41 | 185,618.35 |
| **R²** | 0.0098 | 0.0411 |

**Lectura de Errores y Residuos:**
* El **Random Forest** supera al modelo Baseline al reducir significativamente el MAE (error absoluto medio por transacción).
* El **RMSE** se dispara en la Regresión Lineal porque la ecuación intenta extrapolar su pendiente sobre los valores extremos del superciclo, generando errores masivos (e incluso predicciones negativas). El Random Forest mitiga esto al no poder proyectar valores superiores a su rango máximo de entrenamiento.
* El **R²** es críticamente bajo en ambos modelos. Esto evidencia el shock de precios del litio no capturado en la data de entrenamiento, lo que hace esperable un bajo rendimiento ante un cambio de régimen tan abrupto.

---

## 🧠 4. Explicabilidad del Modelo (SHAP)

### 4.1 Explicabilidad Global (Summary Plot / Beeswarm)
El análisis SHAP del Random Forest confirma matemáticamente los hallazgos de nuestro EDA:
* **Volumen Físico:** Es el predictor dominante. Volúmenes altos inyectan el mayor peso positivo a la predicción del FOB.
* **Familias Minerales:** La pertenencia a familias como el `Yodo` o el `Litio` empujan drásticamente las predicciones al alza, mientras que la familia `Otros No Metálicos` las penaliza.
* **Filtro Macroeconómico:** Variables como la `Inflación` o el `Tipo de Cambio` fueron relegadas por el algoritmo. Su impacto se mantuvo neutro (cero) independientemente de si sus valores reales eran altos o bajos.

### 4.2 Explicabilidad Local (Waterfall Plot)
Al aislar una transacción de prueba con **error bajo** (comportamiento comercial estándar previo al boom):
* El modelo inicia desde un valor esperado base de **4,766.55** (miles de USD).
* El algoritmo ajusta esta cifra restando **-3,010.11** debido al bajo volumen específico de esa transacción, y aplica ajustes adicionales según la familia del mineral y la región de destino.
* Converge en una predicción final de **116.03** miles de USD. Esto demuestra que el algoritmo funciona con alta precisión cuando las entradas operan dentro de la distribución normal histórica.

---

## 🚀 5. Conclusión y Siguientes Mejoras
Recomendamos el uso del **Random Forest** por su mayor estabilidad frente a valores atípicos y su capacidad para capturar umbrales no lineales sin extrapolar valores absurdos o negativos, superando en MAE y RMSE al modelo lineal. 

**Limitación Principal:** El ensamble carece de robustez ante el *concept drift* y shocks de precios internacionales, ya que los árboles no extrapolan fuera del rango de entrenamiento histórico.

**Próximas Mejoras a Evaluar:**
1. Entrenar el modelo prediciendo el logaritmo natural del FOB ($ln(Y)$) para estabilizar la varianza.
2. Incorporar un índice trimestral de *Precio Internacional de Commodities* como nuevo predictor (X) para otorgar tracción económica al modelo ante futuros superciclos.
