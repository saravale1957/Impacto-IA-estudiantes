# Uso de IA, actividades académicas y ocio

## Acceso a la aplicación

**Aplicación en línea:** [Abrir aplicación en Streamlit](https://uyofbyorzvkohxlofzpyfe.streamlit.app/)

**Dataset limpio:** [Descargar dataset_limpio.csv desde GitHub](https://github.com/saravale1957/Impacto-IA-estudiantes/blob/main/dataset_limpio.csv) (utilizar la opción de descarga del archivo).

### Instrucciones de uso

1. Descargar el archivo `dataset_limpio.csv` del enlace anterior.
2. Abrir el enlace de la aplicación de Streamlit.
3. Cargar el archivo CSV mediante el botón de carga de la aplicación.
4. Seleccionar los filtros de carrera, semestre, situación laboral y frecuencia de uso de IA, si se desea.
5. Consultar las cinco estadísticas descriptivas, las tres gráficas y los resultados.

## Contexto

La inteligencia artificial generativa es utilizada por estudiantes universitarios para desarrollar actividades académicas y personales. Este proyecto busca explorar su relación con los hábitos de estudio y el uso de estas herramientas fuera del ámbito académico mediante una aplicación interactiva de exploración de datos.

## Pregunta problema

¿De qué manera el uso diario de herramientas de Inteligencia Artificial Generativa influye en el tiempo dedicado a actividades académicas y de ocio por parte de los estudiantes?

## Objetivo general

Analizar la relación entre el uso diario de herramientas de inteligencia artificial generativa y el tiempo dedicado a actividades académicas y de ocio por parte de los estudiantes, mediante una aplicación interactiva de exploración de datos.

## Dataset

El archivo `dataset_limpio.csv` corresponde a la versión limpia de la encuesta sobre hábitos de estudio y uso de IA. La versión preparada para el proyecto contiene 357 registros y 12 variables, sin valores faltantes detectados.

**Fuente:** Correa (2026), Mendeley Data. [Consultar la fuente original](https://doi.org/10.17632/mcwb2ppdsw.1).

Las principales variables utilizadas son:

| Variable | Descripción |
| --- | --- |
| `frecuencia_uso_ia` | Frecuencia declarada de uso de IA. |
| `horas_estudio_semana` | Rango de horas semanales de estudio. |
| `usa_ia_fuera_academico` | Uso de IA en actividades no académicas. |
| `carrera` | Carrera universitaria. |
| `semestre` | Semestre académico. |
| `situacion_laboral` | Situación laboral del estudiante. |

## Herramientas utilizadas

- Python: desarrollo del código.
- Pandas: lectura y filtrado del dataset.
- NumPy: cálculos estadísticos.
- Matplotlib: creación de la gráfica circular.
- Streamlit: desarrollo de la aplicación interactiva.
- Google Colab: limpieza y exploración de datos.
- Visual Studio Code: desarrollo del código.
- GitHub: almacenamiento del código y los datos del proyecto.
- Streamlit Cloud: despliegue de la aplicación.

## Funcionalidades de la aplicación

- Carga y visualización de datos en formato CSV.
- Filtros por carrera, semestre, situación laboral y frecuencia de uso de IA.
- Cinco estadísticas descriptivas: promedio, mediana, desviación estándar, mínimo y máximo.
- Tres visualizaciones:
  1. Barras verticales interactivas: porcentaje de estudiantes que estudian más de cinco horas semanales según la frecuencia de uso de IA.
  2. Gráfica circular: distribución de las horas semanales de estudio del grupo seleccionado.
  3. Barras horizontales interactivas: porcentaje de estudiantes que usan IA fuera del ámbito académico.
- Consulta de los resultados y la tabla de datos filtrados.

Las estadísticas se calculan sobre una escala de frecuencia de uso de IA: 0 = Nunca, 1 = Rara vez, 2 = Ocasionalmente, 3 = Casi siempre y 4 = Siempre.

## Principales hallazgos

Resultados de los 357 registros de la versión limpia preparada para el proyecto, sin aplicar filtros:

| Frecuencia de uso de IA | Estudiantes | Estudian más de 5 horas semanales | Usan IA fuera del estudio |
| --- | ---: | ---: | ---: |
| Nunca o rara vez | 18 | 5,56 % | 88,89 % |
| Ocasionalmente | 88 | 36,36 % | 92,05 % |
| Casi siempre | 119 | 56,30 % | 94,12 % |
| Siempre | 132 | 62,88 % | 87,12 % |

Se observa que el porcentaje de estudiantes que estudia más de cinco horas semanales aumenta conforme aumenta la frecuencia de uso de IA. Además, 324 estudiantes (90,76 %) utilizan IA fuera del ámbito académico. El grupo que nunca o rara vez usa IA es pequeño, por lo que las comparaciones deben interpretarse con precaución

## Conclusiones y limitaciones

Los resultados muestran una relación entre la frecuencia de uso de IA y el tiempo semanal de estudio. También indican que estas herramientas se utilizan fuera del ámbito académico.
Como mejora futura se propone incorporar datos específicos sobre el uso diario de IA y el tiempo dedicado al ocio.

## Estructura del repositorio

```text
Impacto-IA-estudiantes/
├── app.py
├── dataset_limpio.csv
├── requirements.txt
└── README.md
```

- `app.py`: código fuente de la aplicación.
- `dataset_limpio.csv`: datos limpios para cargar en la aplicación.
- `requirements.txt`: librerías necesarias.
- `README.md`: descripción e instrucciones de uso del proyecto.

## Ejecución local (opcional)

Esta sección es únicamente para quienes deseen ejecutar o modificar el código en su computador. 
Desde una terminal en la carpeta del repositorio, con Python instalado:

```bash
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

Abrir la dirección local indicada en la terminal y cargar el CSV.
