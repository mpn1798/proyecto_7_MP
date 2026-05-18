import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

car_data = pd.read_csv(
    'C:\\Users\\melhe\\GitHub_repos\\proyecto_7_MP\\vehicles_us.csv')

st.header('Análisis de datos de vehículos en Estados Unidos')

# Crear un botón en la aplicación Streamlit
hist_button = st.button('Construir histograma')

# Lógica a ejecutar cuando se hace clic en el botón
if hist_button:
    # Escribir un mensaje en la aplicación
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # Crear un histograma utilizando plotly.graph_objects
    # Se crea una figura vacía y luego se añade un rastro de histograma
    fig = go.Figure(data=[go.Histogram(x=car_data['odometer'])])
    # Anadir un título al gráfico
    fig.update_layout(title_text='Distribución del Odómetro')

    # Mostrar el gráfico Plotly interactivo en la aplicación Streamlit
    # 'use_container_width=True' ajusta el ancho del gráfico al contenedor
    st.plotly_chart(fig, use_container_width=True)

dispersion_button = st.button('Construir gráfico de dispersión')

if dispersion_button:
    st.write(
        'Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')

    # Crear un gráfico de dispersión utilizando plotly.graph_objects
    fig_dispersion = go.Figure(data=go.Scatter(
        x=car_data['odometer'], y=car_data['price'], mode='markers'))

    # Añadir un título al gráfico
    fig_dispersion.update_layout(title_text='Relación entre Odómetro y Precio')

    # Mostrar el gráfico Plotly interactivo en la aplicación Streamlit
    # 'use_container_width=True' ajusta el ancho del gráfico al contenedo
    st.plotly_chart(fig_dispersion, use_container_width=True)
