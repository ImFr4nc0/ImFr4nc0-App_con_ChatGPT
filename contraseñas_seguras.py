import streamlit as st
import random
import string

# Función para generar la contraseña
def generar_contraseña(longitud, mayusculas, numeros, caracteres_especiales):
    # Caracteres base
    caracteres = string.ascii_lowercase  # Letras minúsculas

    if mayusculas:
        caracteres += string.ascii_uppercase  # Letras mayúsculas
    if numeros:
        caracteres += string.digits  # Números
    if caracteres_especiales:
        caracteres += string.punctuation  # Caracteres especiales

    # Generar la contraseña
    contraseña = ''.join(random.choice(caracteres) for i in range(longitud))
    return contraseña

# Título
st.title("🔑 Generador de Contraseñas Seguras")

# Descripción
st.write("Este generador crea contraseñas aleatorias y seguras según los criterios que elijas.")

# Entradas del usuario
longitud = st.slider("Selecciona la longitud de la contraseña:", 8, 32, 12)
mayusculas = st.checkbox("Incluir mayúsculas")
numeros = st.checkbox("Incluir números")
caracteres_especiales = st.checkbox("Incluir caracteres especiales")

# Botón para generar la contraseña
if st.button("Generar Contraseña"):
    # Generar la contraseña según los parámetros
    contraseña = generar_contraseña(longitud, mayusculas, numeros, caracteres_especiales)
    st.success(f"Tu nueva contraseña segura es: {contraseña}")

    # Opción para copiar al portapapeles
    st.download_button(
        label="Descargar Contraseña",
        data=contraseña,
        file_name="contraseña_segura.txt",
        mime="text/plain",
    )
