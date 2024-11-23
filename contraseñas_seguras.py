import streamlit as st
import random
import string

# Función para generar la contraseña
def generar_contraseña(longitud, mayusculas, numeros, caracteres_especiales, palabra_incluida):
    # Caracteres base
    caracteres = string.ascii_lowercase  # Letras minúsculas

    if mayusculas:
        caracteres += string.ascii_uppercase  # Letras mayúsculas
    if numeros:
        caracteres += string.digits  # Números
    if caracteres_especiales:
        caracteres += string.punctuation  # Caracteres especiales

    # Asegurar que la palabra incluida esté en la contraseña
    if palabra_incluida:
        # Comprobar que la palabra no sea demasiado larga
        if len(palabra_incluida) > longitud:
            st.warning("La palabra incluida es demasiado larga para la longitud seleccionada.")
            return None
        # Añadir la palabra a la contraseña
        contraseña = palabra_incluida
        # Rellenar el resto de la contraseña con caracteres aleatorios
        contraseña += ''.join(random.choice(caracteres) for i in range(longitud - len(palabra_incluida)))
    else:
        # Si no hay palabra incluida, simplemente generar una contraseña aleatoria
        contraseña = ''.join(random.choice(caracteres) for i in range(longitud))

    # Mezclar la contraseña para que la palabra no siempre esté al principio
    contraseña = ''.join(random.sample(contraseña, len(contraseña)))

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

# Campo para ingresar una palabra que debe estar en la contraseña
palabra_incluida = st.text_input("Ingresa una palabra que debe incluirse en la contraseña (opcional):")

# Botón para generar la contraseña
if st.button("Generar Contraseña"):
    # Generar la contraseña según los parámetros
    contraseña = generar_contraseña(longitud, mayusculas, numeros, caracteres_especiales, palabra_incluida)
    
    if contraseña:
        st.success(f"Tu nueva contraseña segura es: {contraseña}")

        # Opción para copiar al portapapeles
        st.download_button(
            label="Descargar Contraseña",
            data=contraseña,
            file_name="contraseña_segura.txt",
            mime="text/plain",
        )
