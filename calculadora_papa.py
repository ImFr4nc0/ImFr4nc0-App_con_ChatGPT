import streamlit as st
import pandas as pd

# Título de la aplicación
st.title("Cálculo del PAPA")

# Autor de la aplicación
st.write("Esta app fue elaborada por Alejandro Gomez Franco.")

# Inicialización de datos
if "materias" not in st.session_state:
    st.session_state["materias"] = []

# Función para calcular el PAPA
def calcular_papa(data):
    if not data:
        return 0
    total_puntos = sum(m["calificacion"] * m["creditos"] for m in data)
    total_creditos = sum(m["creditos"] for m in data)
    return total_puntos / total_creditos if total_creditos > 0 else 0

# Sección para registrar materias
st.subheader("Registro de materias")
col1, col2, col3, col4 = st.columns(4)

with col1:
    nombre = st.text_input("Nombre de la materia:")

with col2:
    tipologia = st.selectbox(
        "Tipología:",
        [
            "Libre elección",
            "Disciplinar obligatoria",
            "Nivelación",
            "Trabajo de grado",
            "Fundamental obligatoria",
            "Disciplinar optativa",
            "Fundamental optativa",
        ],
    )

with col3:
    calificacion = st.number_input("Calificación (0.0 - 5.0):", min_value=0.0, max_value=5.0, step=0.1)

with col4:
    creditos = st.number_input("Créditos:", min_value=1, step=1)

if st.button("Agregar materia"):
    st.session_state["materias"].append(
        {
            "nombre": nombre,
            "tipologia": tipologia,
            "calificacion": calificacion,
            "creditos": creditos,
        }
    )
    st.success("Materia agregada.")

# Mostrar materias registradas
st.subheader("Materias registradas")
if st.session_state["materias"]:
    df_materias = pd.DataFrame(st.session_state["materias"])
    st.dataframe(df_materias)

    # Cálculo del PAPA global
    st.subheader("Cálculo del PAPA global")
    papa_global = calcular_papa(st.session_state["materias"])
    st.write(f"Tu PAPA global es: **{papa_global:.2f}**")

    # Cálculo del PAPA por tipología
    st.subheader("Cálculo del PAPA por tipología")
    tipologias = df_materias["tipologia"].unique()
    for tipo in tipologias:
        materias_tipo = [
            m for m in st.session_state["materias"] if m["tipologia"] == tipo
        ]
        papa_tipo = calcular_papa(materias_tipo)
        st.write(f"El PAPA para la tipología **{tipo}** es: **{papa_tipo:.2f}**")

else:
    st.write("No hay materias registradas.")
