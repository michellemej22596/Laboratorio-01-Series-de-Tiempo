# Laboratorio 01 y 02 – Series de Tiempo y Deep Learning

**Curso:** CC3084 – Data Science
**Semestre:** II – 2025
**Universidad del Valle de Guatemala**
**Integrantes del grupo:** \[Silvia Illescas], \[Emilio Reyes], \[Michelle Mejía]

---

## Descripción General

Estos laboratorios tienen como objetivo analizar el comportamiento histórico y proyectado de la importación y consumo de **gasolina regular**, **gasolina superior** y **diésel bajo azufre** en Guatemala, desde el año 2001 hasta mayo de 2025.
En el **Laboratorio 1**, se aplicaron modelos clásicos de series de tiempo como **ARIMA** y **Prophet**.
En el **Laboratorio 2**, se emplearon redes neuronales recurrentes del tipo **Long Short-Term Memory (LSTM)**, comparando su rendimiento frente a los modelos tradicionales.

---

## Herramientas Utilizadas

* Python 3.11+
* Prophet (Meta), statsmodels
* Keras / TensorFlow
* pandas, matplotlib, seaborn
* scikit-learn

---

## Análisis Realizado

### Laboratorio 1: Series Temporales Clásicas

1. **Análisis Exploratorio**

   * Tendencias y estacionalidades por tipo de combustible.
   * Impacto de eventos como la pandemia (2020-2021).

2. **Modelado Clásico**

   * Modelos ARIMA y Prophet.
   * Evaluación con métricas como RMSE y visualizaciones.
   * Predicciones para 2025 (usando datos hasta 2024) y validación con valores reales hasta mayo.

3. **Resultados**

   * Prophet destacó por su precisión en gasolina regular y superior.
   * Diésel presentó mayor variabilidad mensual, afectando la precisión.

### Laboratorio 2: Modelado con Deep Learning

1. **Modelado con LSTM**

   * Se usaron dos de las series del laboratorio anterior.
   * Se construyeron **al menos dos modelos LSTM** por serie con diferentes configuraciones.
   * Se aplicó **tuneo de hiperparámetros** (número de unidades, dropout, epochs, etc.).

2. **Evaluación y Comparación**

   * Se eligió el mejor modelo LSTM por serie.
   * Se comparó el rendimiento frente a ARIMA y Prophet.
   * Se analizó la capacidad del modelo para capturar patrones temporales complejos.

3. **Conclusiones**

   * En algunas series, LSTM logró superar en precisión a ARIMA y Prophet, especialmente cuando existía **no linealidad** en los datos.
   * Sin embargo, Prophet siguió siendo competitivo en datos con **alta estacionalidad estable**.

---

## Resultados Clave

* **Gasolina Regular:** Prophet tuvo un gran desempeño, pero LSTM con configuración optimizada mostró menor RMSE.
* **Gasolina Superior:** Ambos enfoques (clásico y LSTM) ofrecieron buenos resultados, pero LSTM presentó mejor respuesta a variaciones súbitas.
* **Diésel Bajo Azufre:** LSTM superó a Prophet en predicción de patrones no lineales, aunque con mayor complejidad computacional.

---

## Instalación

1. Clona el repositorio:

```bash
git clone https://github.com/michellemej22596/Laboratorio-01-y-02-Series-de-Tiempo.git
cd Laboratorio-01-y-02-Series-de-Tiempo
```

