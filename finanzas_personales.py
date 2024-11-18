import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

# Título de la aplicación
st.title("Gestor de Finanzas Personales")

# Autor de la aplicación
st.write("Esta app fue elaborada por Alejandro Gomez Franco.")

# Inicialización de datos
if "finanzas" not in st.session_state:
    st.session_state["finanzas"] = {
        "presupuestos": [],
        "ingresos": [],
        "gastos": [],
        "ahorro": []
    }

# Función para registrar datos
def registrar_dato(tipo, categoria, monto, fecha):
    st.session_state["finanzas"][tipo].append({"categoria": categoria, "monto": monto, "fecha": fecha})

# Sección de presupuestos
st.subheader("Registro de Presupuestos")
presupuesto_categoria = st.text_input("Categoría del presupuesto:")
presupuesto_monto = st.number_input("Monto presupuestado:", min_value=0.0, step=0.01)
if st.button("Agregar presupuesto"):
    registrar_dato("presupuestos", presupuesto_categoria, presupuesto_monto, datetime.now())
    st.success("Presupuesto registrado.")

# Sección de ingresos
st.subheader("Registro de Ingresos")
ingreso_categoria = st.text_input("Categoría del ingreso:")
ingreso_monto = st.number_input("Monto del ingreso:", min_value=0.0, step=0.01)
if st.button("Agregar ingreso"):
    registrar_dato("ingresos", ingreso_categoria, ingreso_monto, datetime.now())
    st.success("Ingreso registrado.")

# Sección de gastos
st.subheader("Registro de Gastos")
gasto_categoria = st.text_input("Categoría del gasto:")
gasto_monto = st.number_input("Monto del gasto:", min_value=0.0, step=0.01)
if st.button("Agregar gasto"):
    registrar_dato("gastos", gasto_categoria, gasto_monto, datetime.now())
    st.success("Gasto registrado.")

# Sección de metas de ahorro
st.subheader("Registro de Metas de Ahorro")
meta_categoria = st.text_input("Meta de ahorro:")
meta_monto = st.number_input("Monto de la meta de ahorro:", min_value=0.0, step=0.01)
if st.button("Agregar meta de ahorro"):
    registrar_dato("ahorro", meta_categoria, meta_monto, datetime.now())
    st.success("Meta de ahorro registrada.")

# Mostrar los datos registrados
st.subheader("Datos Registrados")
for tipo, datos in st.session_state["finanzas"].items():
    st.write(f"### {tipo.capitalize()}")
    if datos:
        df = pd.DataFrame(datos)
        st.dataframe(df)
    else:
        st.write(f"No hay datos registrados en {tipo}.")

# Generación de reportes
st.subheader("Generación de Reportes")

# Selección del rango de fechas
reporte_tipo = st.radio("Selecciona el periodo del reporte:", ["Semanal", "Mensual"])
hoy = datetime.now()
if reporte_tipo == "Semanal":
    inicio = hoy - timedelta(days=7)
else:
    inicio = hoy - timedelta(days=30)

# Cálculo del reporte
st.write(f"Reporte desde {inicio.date()} hasta {hoy.date()}:")

# Filtrar datos
def filtrar_por_fecha(datos, inicio, hoy):
    return [dato for dato in datos if inicio <= dato["fecha"] <= hoy]

presupuestos_filtrados = filtrar_por_fecha(st.session_state["finanzas"]["presupuestos"], inicio, hoy)
ingresos_filtrados = filtrar_por_fecha(st.session_state["finanzas"]["ingresos"], inicio, hoy)
gastos_filtrados = filtrar_por_fecha(st.session_state["finanzas"]["gastos"], inicio, hoy)

# Calcular totales
total_presupuestado = sum(d["monto"] for d in presupuestos_filtrados)
total_ingresos = sum(d["monto"] for d in ingresos_filtrados)
total_gastos = sum(d["monto"] for d in gastos_filtrados)
diferencia = total_presupuestado - total_gastos

# Mostrar reporte
st.write(f"- Total presupuestado: {total_presupuestado:.2f}")
st.write(f"- Total de ingresos: {total_ingresos:.2f}")
st.write(f"- Total de gastos: {total_gastos:.2f}")
st.write(f"- Diferencia (Presupuesto - Gastos): {diferencia:.2f}")
