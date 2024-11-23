import streamlit as st
import random

# Lista de palabras
palabras = ["streamlit", "python", "programacion", "desarrollo", "aplicaciones"]

# Inicializar variables de sesión
if "palabra_secreta" not in st.session_state:
    st.session_state["palabra_secreta"] = random.choice(palabras)
if "letras_adivinadas" not in st.session_state:
    st.session_state["letras_adivinadas"] = []
if "intentos_restantes" not in st.session_state:
    st.session_state["intentos_restantes"] = 6

# Función para mostrar la palabra con las letras adivinadas
def mostrar_palabra(palabra, letras_adivinadas):
    return " ".join([letra if letra in letras_adivinadas else "_" for letra in palabra])

# Título y descripción
st.title("🎮 Juego del Ahorcado")
st.write("¡Adivina la palabra antes de que se acaben tus intentos!")

# Mostrar progreso
st.subheader("Palabra:")
st.write(mostrar_palabra(st.session_state["palabra_secreta"], st.session_state["letras_adivinadas"]))

# Mostrar letras adivinadas
st.subheader("Letras adivinadas:")
st.write(", ".join(st.session_state["letras_adivinadas"]) if st.session_state["letras_adivinadas"] else "Ninguna")

# Mostrar intentos restantes
st.subheader(f"Intentos restantes: {st.session_state['intentos_restantes']}")

# Entrada para adivinar letras
if st.session_state["intentos_restantes"] > 0 and "_" in mostrar_palabra(st.session_state["palabra_secreta"], st.session_state["letras_adivinadas"]):
    letra = st.text_input("Ingresa una letra:", max_chars=1).lower()

    if st.button("Adivinar"):
        if letra in st.session_state["letras_adivinadas"]:
            st.warning(f"Ya adivinaste la letra '{letra}'. Intenta con otra.")
        elif letra in st.session_state["palabra_secreta"]:
            st.session_state["letras_adivinadas"].append(letra)
            st.success(f"¡Bien hecho! La letra '{letra}' está en la palabra.")
        else:
            st.session_state["letras_adivinadas"].append(letra)
            st.session_state["intentos_restantes"] -= 1
            st.error(f"Lo siento, la letra '{letra}' no está en la palabra.")

# Verificar si ganó o perdió
if "_" not in mostrar_palabra(st.session_state["palabra_secreta"], st.session_state["letras_adivinadas"]):
    st.success("🎉 ¡Felicidades, adivinaste la palabra!")
    if st.button("Jugar de nuevo"):
        st.session_state["palabra_secreta"] = random.choice(palabras)
        st.session_state["letras_adivinadas"] = []
        st.session_state["intentos_restantes"] = 6
elif st.session_state["intentos_restantes"] == 0:
    st.error(f"😢 Te quedaste sin intentos. La palabra era '{st.session_state['palabra_secreta']}'.")
    if st.button("Intentar de nuevo"):
        st.session_state["palabra_secreta"] = random.choice(palabras)
        st.session_state["letras_adivinadas"] = []
        st.session_state["intentos_restantes"] = 6
