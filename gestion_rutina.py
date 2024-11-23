import streamlit as st
import pandas as pd
import plotly.express as px

# Título de la app
st.title("Gestión de Rutinas Diarias")

# Introducción
st.write("Esta app fue elaborada por Alejandro Gomez Franco.")
st.write("Planifica tu día, registra tus tareas y analiza el tiempo invertido para mejorar tu productividad.")

# Inicializar datos
if "tareas" not in st.session_state:
    st.session_state["tareas"] = []

# Sección para agregar tareas
st.subheader("Planificación del día")
col1, col2, col3, col4 = st.columns(4)

with col1:
    tarea = st.text_input("Tarea:")
with col2:
    duracion_estimada = st.number_input("Duración estimada (min):", min_value=1, step=1)
with col3:
    prioridad = st.selectbox("Prioridad:", ["Alta", "Media", "Baja"])
with col4:
    if st.button("Agregar tarea"):
        st.session_state["tareas"].append(
            {"tarea": tarea, "estimado": duracion_estimada, "real": None, "prioridad": prioridad}
        )
        st.success("Tarea agregada.")

# Mostrar tareas planificadas
st.subheader("Tareas planificadas")
if st.session_state["tareas"]:
    df = pd.DataFrame(st.session_state["tareas"])
    st.dataframe(df)

    # Sección para registrar tiempo real
    st.subheader("Registro del tiempo real")
    for i, tarea in enumerate(st.session_state["tareas"]):
        tiempo_real = st.number_input(f"Tiempo real para '{tarea['tarea']}' (min):", min_value=0, step=1, key=i)
        st.session_state["tareas"][i]["real"] = tiempo_real

    # Generar análisis
    if st.button("Generar análisis"):
        df = pd.DataFrame(st.session_state["tareas"])
        
        # Calcular métricas
        df["diferencia"] = df["real"] - df["estimado"]
        cumplimiento = (df["real"].sum() / df["estimado"].sum()) * 100 if df["estimado"].sum() > 0 else 0
        
        st.subheader("Resumen de tiempo")
        st.write(f"**Porcentaje de cumplimiento:** {cumplimiento:.2f}%")
        st.write("**Tareas más desviadas:**")
        st.write(df.sort_values("diferencia", key=abs, ascending=False).head(3))

        # Gráfica de tiempo por prioridad
        st.subheader("Análisis por prioridad")
        fig = px.bar(
            df.groupby("prioridad")[["estimado", "real"]].sum().reset_index(),
            x="prioridad",
            y=["estimado", "real"],
            barmode="group",
            title="Tiempo estimado vs real por prioridad",
        )
        st.plotly_chart(fig)

else:
    st.write("No hay tareas registradas.")

# Pie de página
st.write("---")
st.write("¡Optimiza tu rutina diaria con esta app!")
