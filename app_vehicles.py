import pandas as pd
import plotly.express as px
import streamlit as st

# Cargar el dataset
df = pd.read_csv('vehicles_us.csv')

# Encabezado de la aplicación
st.header("Análisis Exploratorio de Datos de Vehículos")

# Casilla de verificación para mostrar el dataframe
if st.checkbox("Mostrar los primeros registros del dataset"):
    st.write(df.head())

# Botón para construir un histograma del odómetro
if st.button("Mostrar Histograma de Odómetro"):
    st.write("Histograma de la columna 'odometer'")
    fig = px.histogram(df, x='odometer', title='Histograma de Odómetro')
    st.plotly_chart(fig, use_container_width=True)

# Segundo histograma: precio
if st.button("Mostrar Histograma de Precio"):
    st.write("Histograma de la columna 'price'")
    fig_price = px.histogram(df, x='price', title='Histograma de Precio')
    st.plotly_chart(fig_price, use_container_width=True)

# Gráfico de dispersión: precio vs odómetro
if st.button("Construir Scatter Plot Precio vs Odómetro"):
    st.write("Gráfico de dispersión: Precio vs Odómetro")
    fig2 = px.scatter(df, x='odometer', y='price', title='Precio vs Odómetro')
    st.plotly_chart(fig2, use_container_width=True)

# Otro encabezado para mayor claridad
st.subheader("Análisis Interactivo por Condición del Vehículo")

# Casilla de verificación para mostrar gráfico según condición
if st.checkbox("Mostrar gráfico de precios por condición"):
    fig3 = px.box(df, x='condition', y='price', title='Precio por Condición del Vehículo')
    st.plotly_chart(fig3, use_container_width=True)