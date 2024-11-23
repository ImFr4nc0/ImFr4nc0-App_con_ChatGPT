import streamlit as st
import requests

# URL de la API para obtener las tasas de cambio
API_URL = "https://api.exchangerate-api.com/v4/latest/USD"

# Función para obtener las tasas de cambio
def obtener_tasas():
    response = requests.get(API_URL)
    if response.status_code == 200:
        return response.json()['rates']
    else:
        st.error("Error al obtener las tasas de cambio.")
        return {}

# Título de la app
st.title("💱 Conversor de Monedas")

# Descripción de la app
st.write("Esta app fue elaborada por Alejandro Gomez Franco.")
st.write("Convierta una moneda a otra usando tasas de cambio actualizadas.")

# Obtener las tasas de cambio
tasas = obtener_tasas()

# Si las tasas se obtuvieron correctamente, mostrar los selectores
if tasas:
    # Selección de la moneda de origen
    moneda_origen = st.selectbox("Selecciona la moneda de origen", list(tasas.keys()))

    # Selección de la moneda de destino
    moneda_destino = st.selectbox("Selecciona la moneda de destino", list(tasas.keys()))

    # Campo para ingresar la cantidad a convertir
    cantidad = st.number_input(f"Ingrese la cantidad en {moneda_origen}", min_value=0.01, step=0.01)

    # Convertir la cantidad
    if cantidad > 0:
        # Convertir la cantidad a la moneda de destino
        tasa_origen = tasas[moneda_origen]
        tasa_destino = tasas[moneda_destino]
        resultado = cantidad * (tasa_destino / tasa_origen)

        # Mostrar el resultado
        st.write(f"{cantidad} {moneda_origen} es equivalente a {resultado:.2f} {moneda_destino}")
else:
    st.error("No se pudieron obtener las tasas de cambio en este momento.")
