import streamlit as st

# Título de la aplicación
st.title("Conversor de Grados Celsius a Fahrenheit")

# Descripción o instrucción para el usuario
st.write("Ingresa una temperatura en grados Celsius y presiona 'Convertir' para ver su valor en Fahrenheit.")

# Campo de entrada para el usuario
celsius = st.number_input("Grados Celsius", value=0.0, step=0.1)

# Botón para ejecutar la conversión
if st.button("Convertir"):
    # Realiza la conversión de Celsius a Fahrenheit
    fahrenheit = (celsius * 9/5) + 32
    
    # Muestra el resultado
    st.success(f"{celsius}°C son equivalentes a {fahrenheit:.2f}°F")