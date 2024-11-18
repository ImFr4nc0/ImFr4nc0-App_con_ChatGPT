import streamlit as st
import pandas as pd

# Título de la aplicación
st.title("Calculadora de PAPA")

# Autor de la aplicación
st.write("Esta app fue elaborada por Alejandro Gomez Franco.")

# Inicialización de datos
if "materias" not in st.session_state:
    st.session_state["materias"] = []

# Función para registrar materias
def registrar_materia(nombre, tipologia, calificacion, creditos):
    st.session_state["materias"].append({
        "Nombre": nombre,
        "Tipología": tipologia,
        "Calificación": calificacion,
        "Créditos": creditos
    })

# Sección de ingreso de materias
st.subheader("Ingreso de materias cursadas")

materia_nombre = st.text_input("Nombre de la materia:")
materia_tipologia = st.selectbox(
    "Tipología de la asignatura:",
    ["Básica", "Profesional", "Electiva", "Otra"]
)
materia_calificacion = st.number_input(
    "Calificación definitiva (0.0 - 5.0):", min_value=0.0, max_value=5.0, step=0.01
)
materia_creditos = st.number_input("Número de créditos de la asignatura:", min_value=1, step=1)

if st.button("Agregar materia"):
    if materia_nombre and materia_calificacion > 0 and materia_creditos > 0:
        registrar_materia(materia_nombre, materia_tipologia, materia_calificacion, materia_creditos)
        st.success("Materia registrada correctamente.")
    else:
        st.error("Por favor, complete todos los campos correctamente.")

# Mostrar materias registradas
st.subheader("Materias registradas")
if st.session_state["materias"]:
    materias_df = pd.DataFrame(st.session_state["materias"])
    st.dataframe(materias_df)
else:
    st.write("No hay materias registradas.")

# Función para calcular el PAPA
def calcular_papa(materias):
    if not materias:
        return 0.0
    total_ponderado = sum(m["Calificación"] * m["Créditos"] for m in materias)
    total_creditos = sum(m["Créditos"] for m in materias)
    return total_ponderado / total_creditos if total_creditos > 0 else 0.0

# Cálculo del PAPA global
st.subheader("Cálculo del PAPA Global")
if st.session_state["materias"]:
    papa_global = calcular_papa(st.session_state["materias"])
    st.write(f"El PAPA global es: **{papa_global:.2f}**")
else:
    st.write("No hay datos suficientes para calcular el PAPA global.")

# Cálculo del PAPA por tipología de asignatura
st.subheader("Cálculo del PAPA por Tipología")
if st.session_state["materias"]:
    tipologias = materias_df["Tipología"].unique()
    for tipologia in tipologias:
        materias_tipologia = [
            m for m in st.session_state["materias"] if m["Tipología"] == tipologia
        ]
        papa_tipologia = calcular_papa(materias_tipologia)
        st.write(f"El PAPA para la tipología **{tipologia}** es: **{papa_tipologia:.2f}**")
else:
    st.write("No hay datos suficientes para calcular el PAPA por tipología.")
