import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


st.set_page_config(page_title="Uso de IA en estudiantes", layout="wide")


def calcular_estadisticas(uso):
    """Calcula cinco estadísticas de la frecuencia de uso de IA."""
    return {
        "Promedio": round(np.mean(uso), 2),
        "Mediana": round(np.median(uso), 2),
        "Desviación": round(np.std(uso), 2),
        "Mínimo": np.min(uso),
        "Máximo": np.max(uso)
    }

st.title("Uso de IA, actividades académicas y ocio")
st.markdown("""
### Pregunta problema
¿De qué manera el uso diario de herramientas de Inteligencia Artificial
Generativa influye en el tiempo dedicado a actividades académicas y de ocio
por parte de los estudiantes?

Se analiza la relación entre el uso diario de herramientas de inteligencia
artificial generativa y el tiempo dedicado a actividades académicas y de
ocio por parte de los estudiantes.
""")

archivo = st.file_uploader("Carga dataset_proyecto_ampliado.csv", type="csv")
if archivo is None:
    st.info("Carga el dataset para continuar.")
    st.stop()

datos = pd.read_csv(archivo)
columnas = ["frecuencia_uso_ia", "horas_estudio_semana",
            "usa_ia_fuera_academico", "carrera", "semestre",
            "situacion_laboral"]
for columna in columnas:
    if columna not in datos.columns:
        st.error("Falta la columna: " + columna)
        st.stop()

st.write("Cantidad de estudiantes:", len(datos))
st.write("Cantidad de variables:", datos.shape[1])
st.dataframe(datos.head())

niveles = {"Nunca": 0, "Rara vez": 1, "Ocasionalmente": 2,
           "Casi siempre": 3, "Siempre": 4}
datos["Uso_IA"] = datos["frecuencia_uso_ia"].map(niveles)

carreras = ["Todas"]
for carrera in datos["carrera"]:
    if carrera not in carreras:
        carreras.append(carrera)

semestres = ["Todos"]
for semestre in datos["semestre"]:
    if semestre not in semestres:
        semestres.append(semestre)

st.header("Filtros")
carrera = st.selectbox("Carrera", carreras)
semestre = st.selectbox("Semestre", semestres)
situacion = st.selectbox("Situación laboral", [
    "Todas", "Estudiante tiempo completo", "Estudiar y trabajar"
])
rango = st.slider("Frecuencia de uso de IA", 0, 4, (0, 4))

if carrera != "Todas":
    datos = datos[datos["carrera"] == carrera]
if semestre != "Todos":
    datos = datos[datos["semestre"] == semestre]
if situacion != "Todas":
    datos = datos[datos["situacion_laboral"] == situacion]

datos = datos[(datos["Uso_IA"] >= rango[0]) & (datos["Uso_IA"] <= rango[1])]
st.write("Estudiantes encontrados:", len(datos))
if len(datos) == 0:
    st.warning("No hay estudiantes con estos filtros.")
    st.stop()

st.header("Estadísticas descriptivas")
estadisticas = calcular_estadisticas(datos["Uso_IA"])
col1, col2, col3, col4, col5 = st.columns(5)
col1.metric("Promedio", estadisticas["Promedio"])
col2.metric("Mediana", estadisticas["Mediana"])
col3.metric("Desviación estándar", estadisticas["Desviación"])
col4.metric("Mínimo", estadisticas["Mínimo"])
col5.metric("Máximo", estadisticas["Máximo"])
st.caption("0 = Nunca, 1 = Rara vez, 2 = Ocasionalmente, "
           "3 = Casi siempre, 4 = Siempre. No son horas de uso.")

grupo1 = datos[datos["Uso_IA"] < 2]
grupo2 = datos[datos["Uso_IA"] == 2]
grupo3 = datos[datos["Uso_IA"] == 3]
grupo4 = datos[datos["Uso_IA"] == 4]
grupos = [grupo1, grupo2, grupo3, grupo4]
nombres = ["1. Nunca o rara vez", "2. Ocasionalmente",
           "3. Casi siempre", "4. Siempre"]

estudio = []
fuera = []
cantidades = []
for grupo in grupos:
    cantidades.append(len(grupo))
    if len(grupo) > 0:
        estudio.append(np.mean(grupo["horas_estudio_semana"] == "Más de 5")
                       * 100)
        fuera.append(np.mean(grupo["usa_ia_fuera_academico"] == "Si") * 100)
    else:
        estudio.append(np.nan)
        fuera.append(np.nan)

resumen = pd.DataFrame({
    "Frecuencia": nombres,
    "Estudiantes": cantidades,
    "Estudio (%)": estudio,
    "IA fuera del estudio (%)": fuera
})

# Gráfica 1:
st.subheader("1. Uso de IA y tiempo de estudio")
st.bar_chart(resumen, x="Frecuencia", y="Estudio (%)", height=300)
st.write("Porcentaje de estudiantes que estudian más de 5 horas semanales.")

# Gráfica 2: 
st.subheader("2. Distribución de las horas de estudio")
disponibles = []
for i in range(len(grupos)):
    if len(grupos[i]) > 0:
        disponibles.append(nombres[i])

elegido = st.selectbox("Selecciona un grupo", disponibles)
grupo = grupos[nombres.index(elegido)]
horas = ["0-1", "1-2", "2-3", "3-4", "4-5", "Más de 5"]
etiquetas = []
cantidades_horas = []
for hora in horas:
    cantidad = len(grupo[grupo["horas_estudio_semana"] == hora])
    if cantidad > 0:
        etiquetas.append(hora)
        cantidades_horas.append(cantidad)

if len(cantidades_horas) > 0:
    figura, eje = plt.subplots(figsize=(4, 3))
    eje.pie(cantidades_horas, labels=etiquetas, autopct="%1.1f%%")
    figura.tight_layout()
    izquierda, centro, derecha = st.columns([1, 2, 1])
    centro.pyplot(figura)
    plt.close(figura)
    st.write("Distribución porcentual de horas semanales de estudio.")
else:
    st.info("No hay horas de estudio válidas en este grupo.")

# Gráfica 3: 
st.subheader("3. Uso de IA en actividades no académicas")
izquierda, centro, derecha = st.columns([1, 4, 1])
centro.bar_chart(resumen, x="Frecuencia", y="IA fuera del estudio (%)",
                 horizontal=True, height=300)
st.write("Porcentaje de estudiantes que utilizan IA fuera del estudio.")

st.header("Resultados")
st.dataframe(resumen.round(2))
if len(grupo1) > 0 and len(grupo4) > 0:
    st.write("Estudian más de 5 horas semanales:")
    st.write("Nunca o rara vez:", round(estudio[0], 2), "%")
    st.write("Siempre:", round(estudio[3], 2), "%")
    if estudio[3] > estudio[0]:
        st.write("El grupo que usa IA siempre tiene un porcentaje mayor.")
    elif estudio[3] < estudio[0]:
        st.write("El grupo que usa IA nunca o rara vez tiene uno mayor.")
    else:
        st.write("Ambos grupos tienen el mismo porcentaje.")

porcentaje = np.mean(datos["usa_ia_fuera_academico"] == "Si") * 100
st.write("Usan IA fuera del estudio:", round(porcentaje, 2), "%")

st.header("Datos filtrados")
st.dataframe(datos)
if st.button("Guardar archivo CSV"):
    datos.to_csv("datos_filtrados.csv", index=False)
    st.success("Archivo guardado.")
