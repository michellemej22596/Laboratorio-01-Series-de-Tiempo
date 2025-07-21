# Laboratorio 01 – Series de Tiempo

**Curso:** CC3084 – Data Science
**Semestre:** II – 2025
**Universidad del Valle de Guatemala**
**Integrantes del grupo:** \[Silvia Illescas], \[Emilio Reyes], \[Michelle Mejía]

---

## Descripción General

Este laboratorio explora el comportamiento histórico y futuro del consumo e importación de **gasolina regular**, **gasolina superior** y **diésel bajo azufre** en Guatemala, desde el año 2001 hasta mayo de 2025. Se trabajó con dos conjuntos de datos: uno sobre consumo y otro sobre importación, ambos en unidades de barriles (42 galones). El análisis se enfoca en la construcción de modelos de series de tiempo para entender tendencias, estacionalidad, estacionariedad, y realizar predicciones usando algoritmos como **ARIMA** y **Prophet**.

---

##  Herramientas Utilizadas

* Python 3.11+
* Prophet (Meta)
* pandas, matplotlib, seaborn
* statsmodels (para pruebas de estacionariedad)
* scikit-learn (evaluación de modelos)

---

## Análisis Realizado

### 1. Análisis Exploratorio

* Se graficaron tendencias anuales y mensuales.
* Se identificaron picos por tipo de combustible.
* Se analizó el impacto de la pandemia entre 2020-2021.

### 2. Modelado de Series Temporales

Se crearon series univariantes para cada variable, y se evaluaron:

* Inicio, fin y frecuencia.
* Comportamiento estacional y de tendencia.
* Estacionariedad en media y varianza (con ADF y gráficos ACF/PACF).
* Transformaciones necesarias (diferencias logarítmicas si aplica).

### 3. Modelos Aplicados

* Modelos ARIMA y Prophet.
* Comparación de rendimiento y ajuste.
* Evaluación con RMSE para validar precisión.

### 4. Predicción y Evaluación 2025

* Se utilizaron datos hasta diciembre 2024 para predecir importaciones en 2025.
* Las predicciones se compararon con los datos reales de enero a mayo 2025.
* Se analizó el grado de apego entre predicción y realidad (gráficos + métricas).

---

## Resultados Clave

* **Gasolina Regular:** Alta precisión en predicción. La serie es altamente estacional y el modelo Prophet logró replicar el comportamiento con mínima desviación.
* **Gasolina Superior:** Buen ajuste general. Las fluctuaciones leves fueron anticipadas correctamente por el modelo.
* **Diésel Bajo Azufre:** El modelo logró predecir la tendencia general, pero no capturó bien los cambios bruscos mensuales.

---

## Instalación

1. Clona el repositorio:

```bash
git clone https://github.com/michellemej22596/Laboratorio-01-Series-de-Tiempo.git
cd Laboratorio-01-Series-de-Tiempo

