# Uso de IA, actividades académicas y ocio

Proyecto integrador de primer semestre del programa de Ingeniería de Datos e Inteligencia Artificial.

**Asignaturas:** Introducción a la Ingeniería de Datos e Inteligencia Artificial y Lógica Computacional.

## Contexto

La inteligencia artificial generativa es utilizada por estudiantes universitarios para realizar actividades académicas y personales. Este proyecto presenta una aplicación interactiva que permite explorar su relación con los hábitos de estudio y el uso de IA fuera del ámbito académico.

## Pregunta problema

¿De qué manera el uso diario de herramientas de Inteligencia Artificial Generativa influye en el tiempo dedicado a actividades académicas y de ocio por parte de los estudiantes?

## Objetivo general

Analizar la relación entre el uso diario de herramientas de inteligencia artificial generativa y el tiempo dedicado a actividades académicas y de ocio por parte de los estudiantes, mediante una aplicación interactiva de exploración de datos.

## Dataset

El archivo utilizado es `dataset_proyecto_ampliado.csv`, que contiene 357 registros de estudiantes universitarios, 12 variables y ningún valor faltante detectado con pandas. Es una versión preparada a partir de la encuesta original sobre hábitos de estudio y uso de IA.

**Fuente indicada en la aplicación:** Correa (2026), Mendeley Data. [Consultar el dataset original](https://doi.org/10.17632/mcwb2ppdsw.1).

Las variables principales para el análisis son:

| Variable | Descripción |
| --- | --- |
| `frecuencia_uso_ia` | Frecuencia de uso de inteligencia artificial. |
| `horas_estudio_semana` | Rango de horas semanales dedicadas al estudio. |
| `usa_ia_fuera_academico` | Uso de IA fuera del ámbito académico (sí o no). |
| `carrera` | Carrera universitaria. |
| `semestre` | Semestre académico. |
| `situacion_laboral` | Si el estudiante solo estudia o estudia y trabaja. |

El dataset también contiene variables de promedio académico, satisfacción con las notas, procrastinación, efectividad del método de estudio, herramientas de IA y ayuda de la IA para la comprensión. Estas se pueden consultar en la tabla de datos.

## Herramientas utilizadas

- Python: desarrollo del código.
- pandas: lectura, exploración y filtrado de datos.
- NumPy: cálculo de estadísticas y porcentajes.
- Matplotlib: elaboración de la gráfica circular.
- Streamlit: creación de la aplicación interactiva.
- Google Colab: preparación y exploración del dataset.
- VS Code: edición y ejecución del código.

## Funcionalidades de la aplicación

- Cargar el dataset en formato CSV y visualizar sus primeros registros.
- Filtrar por carrera, semestre, situación laboral y frecuencia de uso de IA.
- Calcular cinco estadísticas descriptivas: promedio, mediana, desviación estándar, mínimo y máximo de la frecuencia de uso de IA.
- Mostrar tres visualizaciones: barras verticales interactivas del porcentaje que estudia más de cinco horas semanales, gráfica circular de la distribución de horas de estudio por grupo y barras horizontales interactivas del uso de IA fuera del ámbito académico.
- Consultar los resultados y la tabla de datos filtrados.
- Guardar los datos filtrados en el archivo `datos_filtrados.csv`.

La frecuencia de uso se representa mediante una escala de 0 a 4: 0 = Nunca, 1 = Rara vez, 2 = Ocasionalmente, 3 = Casi siempre y 4 = Siempre. Estos valores no representan horas de uso.

## Estructura del repositorio

La organización básica recomendada para publicar el proyecto en GitHub es:

```text
proyecto_integrador/
    app.py
    dataset_proyecto_ampliado.csv
    requirements.txt
    README.md
```

- `app.py`: código fuente de la aplicación (última versión simplificada, renombrada como `app.py`).
- `dataset_proyecto_ampliado.csv`: datos limpios utilizados para el análisis.
- `requirements.txt`: librerías necesarias para ejecutar la aplicación.
- `README.md`: descripción del proyecto e instrucciones de uso.

El notebook de Google Colab con la limpieza y el análisis exploratorio puede incluirse como evidencia adicional del proceso.

## Instalación y ejecución

1. Descargar o clonar el repositorio de GitHub y abrir su carpeta en VS Code.
2. Tener Python instalado y abrir una terminal en la carpeta del proyecto.
3. Instalar las librerías indicadas en `requirements.txt`:

   ```bash
   python -m pip install -r requirements.txt
   ```

   El archivo debe incluir `streamlit`, `pandas`, `numpy` y `matplotlib`. Si no se dispone de él, se pueden instalar directamente con:

   ```bash
   python -m pip install --upgrade streamlit pandas numpy matplotlib
   ```

   Se necesita una versión de Streamlit compatible con las barras horizontales de `st.bar_chart`.

4. Ejecutar la aplicación:

   ```bash
   python -m streamlit run app.py
   ```

5. Abrir el enlace local que aparece en la terminal, cargar `dataset_proyecto_ampliado.csv` desde la página y utilizar los filtros para explorar las gráficas.

## Despliegue en Streamlit Cloud

Para publicar la aplicación, subir el código, el dataset, el README y el archivo de dependencias a GitHub. Desde [Streamlit Community Cloud](https://share.streamlit.io/), seleccionar el repositorio y `app.py` como archivo principal. Una vez desplegada, agregar aquí el enlace público de la aplicación.

## Principales hallazgos

Los siguientes resultados corresponden a los 357 registros, sin aplicar filtros:

| Frecuencia de uso de IA | Estudiantes | Estudian más de 5 horas semanales | Usan IA fuera del estudio |
| --- | ---: | ---: | ---: |
| Nunca o rara vez | 18 | 5,56 % | 88,89 % |
| Ocasionalmente | 88 | 36,36 % | 92,05 % |
| Casi siempre | 119 | 56,30 % | 94,12 % |
| Siempre | 132 | 62,88 % | 87,12 % |

Se observa que el porcentaje de estudiantes que estudia más de cinco horas semanales aumenta con la frecuencia declarada de uso de IA. Además, 324 de los 357 estudiantes (90,76 %) utilizan IA fuera del ámbito académico. El grupo que nunca o rara vez usa IA tiene pocos estudiantes, por lo que su comparación debe interpretarse con cautela.

## Conclusiones y limitaciones

Los resultados permiten identificar una relación entre la frecuencia de uso de IA y el tiempo semanal dedicado al estudio. También muestran que su utilización no se limita al ámbito académico.

Sin embargo, la encuesta no registra directamente el tiempo diario de uso de IA ni las horas de ocio. Usar IA fuera del estudio no significa necesariamente dedicar más tiempo al ocio. Por esta razón, la pregunta problema se responde parcialmente y no es posible afirmar que la IA cause cambios en el tiempo dedicado a estas actividades.

Como mejora futura se propone incorporar datos sobre las horas diarias de uso de IA y de ocio para complementar el análisis.
