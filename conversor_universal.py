import streamlit as st

# Título de la aplicación
st.title("Conversor Universal")

# Autor de la aplicación
st.write("Esta app fue elaborada por Alejandro Gomez Franco.")

# Seleccionar categoría
categoria = st.selectbox(
    "Selecciona una categoría para convertir:",
    [
        "Conversiones de temperatura",
        "Conversiones de longitud",
        "Conversiones de peso/masa",
        "Conversiones de volumen",
        "Conversiones de tiempo",
        "Conversiones de velocidad",
        "Conversiones de área",
        "Conversiones de energía",
        "Conversiones de presión",
        "Conversiones de tamaño de datos"
    ]
)

# Configurar conversiones según la categoría seleccionada
if categoria == "Conversiones de temperatura":
    conversion = st.selectbox(
        "Selecciona el tipo de conversión:",
        [
            "Celsius a Fahrenheit",
            "Fahrenheit a Celsius",
            "Celsius a Kelvin",
            "Kelvin a Celsius"
        ]
    )
    valor = st.number_input("Ingresa el valor a convertir:")
    if conversion == "Celsius a Fahrenheit":
        resultado = (valor * 9/5) + 32
        unidades = "Celsius a Fahrenheit"
    elif conversion == "Fahrenheit a Celsius":
        resultado = (valor - 32) * 5/9
        unidades = "Fahrenheit a Celsius"
    elif conversion == "Celsius a Kelvin":
        resultado = valor + 273.15
        unidades = "Celsius a Kelvin"
    elif conversion == "Kelvin a Celsius":
        resultado = valor - 273.15
        unidades = "Kelvin a Celsius"
    st.write(f"El resultado de convertir {valor} de {unidades} es: {resultado}")

elif categoria == "Conversiones de longitud":
    conversion = st.selectbox(
        "Selecciona el tipo de conversión:",
        [
            "Pies a metros",
            "Metros a pies",
            "Pulgadas a centímetros",
            "Centímetros a pulgadas"
        ]
    )
    valor = st.number_input("Ingresa el valor a convertir:")
    if conversion == "Pies a metros":
        resultado = valor * 0.3048
        unidades = "Pies a Metros"
    elif conversion == "Metros a pies":
        resultado = valor / 0.3048
        unidades = "Metros a Pies"
    elif conversion == "Pulgadas a centímetros":
        resultado = valor * 2.54
        unidades = "Pulgadas a Centímetros"
    elif conversion == "Centímetros a pulgadas":
        resultado = valor / 2.54
        unidades = "Centímetros a Pulgadas"
    st.write(f"El resultado de convertir {valor} de {unidades} es: {resultado}")

elif categoria == "Conversiones de peso/masa":
    conversion = st.selectbox(
        "Selecciona el tipo de conversión:",
        [
            "Libras a kilogramos",
            "Kilogramos a libras",
            "Onzas a gramos",
            "Gramos a onzas"
        ]
    )
    valor = st.number_input("Ingresa el valor a convertir:")
    if conversion == "Libras a kilogramos":
        resultado = valor * 0.453592
        unidades = "Libras a Kilogramos"
    elif conversion == "Kilogramos a libras":
        resultado = valor / 0.453592
        unidades = "Kilogramos a Libras"
    elif conversion == "Onzas a gramos":
        resultado = valor * 28.3495
        unidades = "Onzas a Gramos"
    elif conversion == "Gramos a onzas":
        resultado = valor / 28.3495
        unidades = "Gramos a Onzas"
    st.write(f"El resultado de convertir {valor} de {unidades} es: {resultado}")

elif categoria == "Conversiones de volumen":
    conversion = st.selectbox(
        "Selecciona el tipo de conversión:",
        [
            "Galones a litros",
            "Litros a galones",
            "Pulgadas cúbicas a centímetros cúbicos",
            "Centímetros cúbicos a pulgadas cúbicas"
        ]
    )
    valor = st.number_input("Ingresa el valor a convertir:")
    if conversion == "Galones a litros":
        resultado = valor * 3.78541
        unidades = "Galones a Litros"
    elif conversion == "Litros a galones":
        resultado = valor / 3.78541
        unidades = "Litros a Galones"
    elif conversion == "Pulgadas cúbicas a centímetros cúbicos":
        resultado = valor * 16.3871
        unidades = "Pulgadas cúbicas a Centímetros cúbicos"
    elif conversion == "Centímetros cúbicos a pulgadas cúbicas":
        resultado = valor / 16.3871
        unidades = "Centímetros cúbicos a Pulgadas cúbicas"
    st.write(f"El resultado de convertir {valor} de {unidades} es: {resultado}")

elif categoria == "Conversiones de tiempo":
    conversion = st.selectbox(
        "Selecciona el tipo de conversión:",
        [
            "Horas a minutos",
            "Minutos a segundos",
            "Días a horas",
            "Semanas a días"
        ]
    )
    valor = st.number_input("Ingresa el valor a convertir:")
    if conversion == "Horas a minutos":
        resultado = valor * 60
        unidades = "Horas a Minutos"
    elif conversion == "Minutos a segundos":
        resultado = valor * 60
        unidades = "Minutos a Segundos"
    elif conversion == "Días a horas":
        resultado = valor * 24
        unidades = "Días a Horas"
    elif conversion == "Semanas a días":
        resultado = valor * 7
        unidades = "Semanas a Días"
    st.write(f"El resultado de convertir {valor} de {unidades} es: {resultado}")

elif categoria == "Conversiones de velocidad":
    conversion = st.selectbox(
        "Selecciona el tipo de conversión:",
        [
            "Millas por hora a kilómetros por hora",
            "Kilómetros por hora a metros por segundo",
            "Nudos a millas por hora",
            "Metros por segundo a pies por segundo"
        ]
    )
    valor = st.number_input("Ingresa el valor a convertir:")
    if conversion == "Millas por hora a kilómetros por hora":
        resultado = valor * 1.60934
        unidades = "Millas por Hora a Kilómetros por Hora"
    elif conversion == "Kilómetros por hora a metros por segundo":
        resultado = valor / 3.6
        unidades = "Kilómetros por Hora a Metros por Segundo"
    elif conversion == "Nudos a millas por hora":
        resultado = valor * 1.15078
        unidades = "Nudos a Millas por Hora"
    elif conversion == "Metros por segundo a pies por segundo":
        resultado = valor * 3.28084
        unidades = "Metros por Segundo a Pies por Segundo"
    st.write(f"El resultado de convertir {valor} de {unidades} es: {resultado}")

elif categoria == "Conversiones de área":
    conversion = st.selectbox(
        "Selecciona el tipo de conversión:",
        [
            "Metros cuadrados a pies cuadrados",
            "Pies cuadrados a metros cuadrados",
            "Kilómetros cuadrados a millas cuadradas",
            "Millas cuadradas a kilómetros cuadrados"
        ]
    )
    valor = st.number_input("Ingresa el valor a convertir:")
    if conversion == "Metros cuadrados a pies cuadrados":
        resultado = valor * 10.7639
        unidades = "Metros Cuadrados a Pies Cuadrados"
    elif conversion == "Pies cuadrados a metros cuadrados":
        resultado = valor / 10.7639
        unidades = "Pies Cuadrados a Metros Cuadrados"
    elif conversion == "Kilómetros cuadrados a millas cuadradas":
        resultado = valor * 0.386102
        unidades = "Kilómetros Cuadrados a Millas Cuadradas"
    elif conversion == "Millas cuadradas a kilómetros cuadrados":
        resultado = valor / 0.386102
        unidades = "Millas Cuadradas a Kilómetros Cuadrados"
    st.write(f"El resultado de convertir {valor} de {unidades} es: {resultado}")

elif categoria == "Conversiones de energía":
    conversion = st.selectbox(
        "Selecciona el tipo de conversión:",
        [
            "Julios a calorías",
            "Calorías a kilojulios",
            "Kilovatios-hora a megajulios",
            "Megajulios a kilovatios-hora"
        ]
    )
    valor = st.number_input("Ingresa el valor a convertir:")
    if conversion == "Julios a calorías":
        resultado = valor / 4.184
        unidades = "Julios a Calorías"
    elif conversion == "Calorías a kilojulios":
        resultado = valor * 4.184
        unidades = "Calorías a Kilojulios"
    elif conversion == "Kilovatios-hora a megajulios":
        resultado = valor * 3.6
        unidades = "Kilovatios-hora a Megajulios"
    elif conversion == "Megajulios a kilovatios-hora":
        resultado = valor / 3.6
        unidades = "Megajulios a Kilovatios-hora"
    st.write(f"El resultado de convertir {valor} de {unidades} es: {resultado}")

elif categoria == "Conversiones de presión":
    conversion = st.selectbox(
        "Selecciona el tipo de conversión:",
        [
            "Pascales a atmósferas",
            "Atmósferas a pascales",
            "Barras a libras por pulgada cuadrada",
            "Libras por pulgada cuadrada a bares"
        ]
    )
    valor = st.number_input("Ingresa el valor a convertir:")
    if conversion == "Pascales a atmósferas":
        resultado = valor / 101325
        unidades = "Pascales a Atmósferas"
    elif conversion == "Atmósferas a pascales":
        resultado = valor * 101325
        unidades = "Atmósferas a Pascales"
    elif conversion == "Barras a libras por pulgada cuadrada":
        resultado = valor * 14.5038
        unidades = "Barras a Libras por Pulgada Cuadrada"
    elif conversion == "Libras por pulgada cuadrada a bares":
        resultado = valor / 14.5038
        unidades = "Libras por Pulgada Cuadrada a Barras"
    st.write(f"El resultado de convertir {valor} de {unidades} es: {resultado}")

elif categoria == "Conversiones de tamaño de datos":
    conversion = st.selectbox(
        "Selecciona el tipo de conversión:",
        [
            "Megabytes a gigabytes",
            "Gigabytes a Terabytes",
            "Kilobytes a megabytes",
            "Terabytes a petabytes"
        ]
    )
    valor = st.number_input("Ingresa el valor a convertir:")
    if conversion == "Megabytes a gigabytes":
        resultado = valor / 1024
        unidades = "Megabytes a Gigabytes"
    elif conversion == "Gigabytes a Terabytes":
        resultado = valor / 1024
        unidades = "Gigabytes a Terabytes"
    elif conversion == "Kilobytes a megabytes":
        resultado = valor / 1024
        unidades = "Kilobytes a Megabytes"
    elif conversion == "Terabytes a petabytes":
        resultado = valor / 1024
        unidades = "Terabytes a Petabytes"
    st.write(f"El resultado de convertir {valor} de {unidades} es: {resultado}")
