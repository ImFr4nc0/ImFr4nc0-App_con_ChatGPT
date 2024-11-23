import streamlit as st
import requests

# URL de la API para obtener las tasas de cambio
API_URL = "https://api.exchangerate-api.com/v4/latest/USD"

# Diccionario con la moneda y su país o región (basado en ISO 4217)
monedas_a_paises = {
    "USD": "Estados Unidos",
    "EUR": "Zona Euro (Alemania, Francia, España, etc.)",
    "GBP": "Reino Unido",
    "JPY": "Japón",
    "AUD": "Australia",
    "CAD": "Canadá",
    "CHF": "Suiza",
    "CNY": "China",
    "INR": "India",
    "BRL": "Brasil",
    "MXN": "México",
    "ARS": "Argentina",
    "CLP": "Chile",
    "COP": "Colombia",
    "SEK": "Suecia",
    "NOK": "Noruega",
    "DKK": "Dinamarca",
    "KRW": "Corea del Sur",
    "RUB": "Rusia",
    "ZAR": "Sudáfrica",
    "SGD": "Singapur",
    "HKD": "Hong Kong",
    "NZD": "Nueva Zelanda",
    "TRY": "Turquía",
    "THB": "Tailandia",
    "PHP": "Filipinas",
    "MYR": "Malasia",
    "PLN": "Polonia",
    "CZK": "República Checa",
    "IDR": "Indonesia",
    "EGP": "Egipto",
    "KWD": "Kuwait",
    "SAR": "Arabia Saudita",
    "VND": "Vietnam",
    "AED": "Emiratos Árabes Unidos",
    "HUF": "Hungría",
    "RON": "Rumania",
    "BGN": "Bulgaria",
    "LKR": "Sri Lanka",
    "UAH": "Ucrania",
    "PEN": "Perú",
    "QAR": "Catar",
    "BHD": "Bahrein",
    "OMR": "Omán",
    "KZT": "Kazajistán",
    "UZS": "Uzbekistán",
    "JOD": "Jordania"
}

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

    # Mostrar el país o región correspondiente a la moneda de origen y destino
    st.write(f"Moneda de origen: {moneda_origen} - {monedas_a_paises.get(moneda_origen, 'Desconocido')}")
    st.write(f"Moneda de destino: {moneda_destino} - {monedas_a_paises.get(moneda_destino, 'Desconocido')}")

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
