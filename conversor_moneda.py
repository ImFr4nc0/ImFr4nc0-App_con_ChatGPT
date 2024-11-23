import streamlit as st
import requests

# URL de la API para obtener las tasas de cambio
API_URL = "https://api.exchangerate-api.com/v4/latest/USD"

# Diccionario con la moneda y su país o región (basado en ISO 4217)
monedas_a_paises = {
    "USD": "Estados Unidos (Dólar estadounidense)",
    "AED": "Emiratos Árabes Unidos (Dirham de los Emiratos Árabes Unidos)",
    "AFN": "Afganistán (Afgani)",
    "ALL": "Albania (Lek)",
    "AMD": "Armenia (Dram armenio)",
    "ANG": "Antillas Neerlandesas (Florín antillano)",
    "AOA": "Angola (Kwanza angoleño)",
    "ARS": "Argentina (Peso argentino)",
    "AUD": "Australia (Dólar australiano)",
    "AWG": "Aruba (Florín arubeño)",
    "AZN": "Azerbaiyán (Manat azerbaiyano)",
    "BAM": "Bosnia y Herzegovina (Marco convertible)",
    "BBD": "Barbados (Dólar de Barbados)",
    "BDT": "Bangladesh (Taka)",
    "BGN": "Bulgaria (Lev búlgaro)",
    "BHD": "Bahrein (Dinar bahreiní)",
    "BIF": "Burundi (Franco burundés)",
    "BMD": "Bermudas (Dólar bermudeño)",
    "BND": "Brunéi (Dólar de Brunei)",
    "BOB": "Bolivia (Boliviano)",
    "BOP": "Bolivia (Peso boliviano)",
    "BRL": "Brasil (Real brasileño)",
    "BSD": "Bahamas (Dólar bahameño)",
    "BTN": "Bután (Ngultrum butanés)",
    "BWP": "Botsuana (Pula botsuano)",
    "BYN": "Bielorrusia (Rublo bielorruso)",
    "BZD": "Belice (Dólar beliceño)",
    "CAD": "Canadá (Dólar canadiense)",
    "CDF": "República Democrática del Congo (Franco congoleño)",
    "CHF": "Suiza (Franco suizo)",
    "CLP": "Chile (Peso chileno)",
    "CNY": "China (Yuan chino)",
    "COP": "Colombia (Peso colombiano)",
    "CRC": "Costa Rica (Colón costarricense)",
    "CUP": "Cuba (Peso cubano)",
    "CVS": "Cabo Verde (Escudo cabo-verdiano)",
    "CZK": "República Checa (Corona checa)",
    "DJF": "Yibuti (Franco yibutiano)",
    "DKK": "Dinamarca (Corona danesa)",
    "DOP": "República Dominicana (Peso dominicano)",
    "DZD": "Argelia (Dinar argelino)",
    "EGP": "Egipto (Libra egipcia)",
    "ERN": "Eritrea (Nakfa eritreo)",
    "ETB": "Etiopía (Birr etíope)",
    "EUR": "Zona Euro (Euro)",
    "FJD": "Fiyi (Dólar fijiano)",
    "FKP": "Islas Malvinas (Libra malvinense)",
    "GBP": "Reino Unido (Libra esterlina)",
    "GEL": "Georgia (Lari georgiano)",
    "GHS": "Ghana (Cedi ghanés)",
    "GIP": "Gibraltar (Libra de Gibraltar)",
    "GMD": "Gambia (Dalasi gambiano)",
    "GNF": "Guinea (Franco guineano)",
    "GTQ": "Guatemala (Quetzal guatemalteco)",
    "GYD": "Guyana (Dólar guyanés)",
    "HKD": "Hong Kong (Dólar de Hong Kong)",
    "HNL": "Honduras (Lempira hondureña)",
    "HRK": "Croacia (Kuna croata)",
    "HTG": "Haití (Gourde haitiano)",
    "HUF": "Hungría (Forint húngaro)",
    "IDR": "Indonesia (Rupia indonesia)",
    "ILS": "Israel (Nuevo shekel israelí)",
    "INR": "India (Rupia india)",
    "IQD": "Irak (Dinar iraquí)",
    "IRR": "Irán (Rial iraní)",
    "ISK": "Islandia (Corona islandesa)",
    "JMD": "Jamaica (Dólar jamaiquino)",
    "JOD": "Jordania (Dinar jordano)",
    "JPY": "Japón (Yen japonés)",
    "KES": "Kenia (Chelín keniano)",
    "KGS": "Kirguistán (Som kirguís)",
    "KHR": "Camboya (Riel camboyano)",
    "KMF": "Comoras (Franco comorano)",
    "KRW": "Corea del Sur (Won surcoreano)",
    "KWD": "Kuwait (Dinar kuwaití)",
    "KYD": "Islas Caimán (Dólar de las Islas Caimán)",
    "KZT": "Kazajistán (Tenge kazajo)",
    "LAK": "Laos (Kip laosiano)",
    "LBP": "Líbano (Libra libanesa)",
    "LKR": "Sri Lanka (Rupia de Sri Lanka)",
    "LRD": "Liberia (Dólar liberiano)",
    "LSL": "Lesoto (Loti lesotense)",
    "LTL": "Lituania (Litas lituano)",
    "LVL": "Letonia (Lats letón)",
    "LYD": "Libia (Dinar libio)",
    "MAD": "Marruecos (Dirham marroquí)",
    "MDL": "Moldavia (Leu moldavo)",
    "MGA": "Madagascar (Ariary malgache)",
    "MKD": "Macedonia (Denar macedonio)",
    "MMK": "Myanmar (Kyat birmano)",
    "MNT": "Mongolia (Tugrik mongol)",
    "MOP": "Macau (Pataca macanesa)",
    "MRU": "Mauritania (Ouguiya mauritano)",
    "MTL": "Malta (Lira maltesa)",
    "MUR": "Mauricio (Rupia mauriciana)",
    "MVR": "Maldivas (Rufiyaa maldivo)",
    "MWK": "Malawi (Kwacha malawiano)",
    "MXN": "México (Peso mexicano)",
    "MYR": "Malasia (Ringgit malayo)",
    "MZN": "Mozambique (Metical mozambiqueño)",
    "NAD": "Namibia (Dólar namibio)",
    "NGN": "Nigeria (Naira nigeriana)",
    "NIO": "Nicaragua (Córdoba nicaragüense)",
    "NOK": "Noruega (Corona noruega)",
    "NPR": "Nepal (Rupia nepalí)",
    "NZD": "Nueva Zelanda (Dólar neozelandés)",
    "OMR": "Omán (Rial omaní)",
    "PAB": "Panamá (Balboa panameño)",
    "PEN": "Perú (Nuevo sol)",
    "PGK": "Papúa Nueva Guinea (Kina de Papúa Nueva Guinea)",
    "PHP": "Filipinas (Peso filipino)",
    "PKR": "Pakistán (Rupia pakistaní)",
    "PLN": "Polonia (Zloty polaco)",
    "PYG": "Paraguay (Guaraní paraguayo)",
    "QAR": "Catar (Rial catarí)",
    "RON": "Rumania (Leu rumano)",
    "RSD": "Serbia (Dinar serbio)",
    "RUB": "Rusia (Rublo ruso)",
    "RWF": "Ruanda (Franco ruandés)",
    "SAR": "Arabia Saudita (Rial saudí)",
    "SBD": "Islas Salomón (Dólar de las Islas Salomón)",
    "SCR": "Seychelles (Rupia seychellense)",
    "SEK": "Suecia (Corona sueca)",
    "SGD": "Singapur (Dólar de Singapur)",
    "SHP": "Santa Elena (Libra de Santa Elena)",
    "SLL": "Sierra Leona (Leone sierra leoneano)",
    "SOS": "Somalia (Chelín somalí)",
    "SRD": "Surinam (Dólar surinamés)",
    "SSP": "Sudán del Sur (Libra sursudanesa)",
    "STN": "Santo Tomé y Príncipe (Dobras de Santo Tomé y Príncipe)",
    "SYP": "Siria (Libra siria)",
    "SZL": "Suazilandia (Lilangeni suazi)",
    "THB": "Tailandia (Baht tailandés)",
    "TJS": "Tayikistán (Somoni tayiko)",
    "TMT": "Turkmenistán (Manat turcomano)",
    "TND": "Túnez (Dinar tunecino)",
    "TOP": "Tonga (Paʻanga tonga)",
    "TRY": "Turquía (Lira turca)",
    "TTD": "Trinidad y Tobago (Dólar de Trinidad y Tobago)",
    "TWD": "Taiwán (Nuevo dólar taiwanés)",
    "TZS": "Tanzania (Chelín tanzano)",
    "UAH": "Ucrania (Hryvnia ucraniana)",
    "UGX": "Uganda (Chelín ugandés)",
    "UYU": "Uruguay (Peso uruguayo)",
    "UZS": "Uzbekistán (Som uzbeko)",
    "VND": "Vietnam (Dong vietnamita)",
    "VUV": "Vanuatu (Vatu vanuatuano)",
    "WST": "Samoa (Tala samoano)",
    "XOF": "Franco CFA (Franco CFA de la UEMOA)",
    "XPF": "Franco CFP (Franco CFP)",
    "YER": "Yemen (Rial yemení)",
    "ZAR": "Sudáfrica (Rand sudafricano)",
    "ZMK": "Zambia (Kwacha zambiano)",
    "ZWL": "Zimbabue (Dólar zimbabuense)"
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
