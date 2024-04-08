import pandas as pd
import plotly.express as px
import streamlit as st

st.header('Dashboard de Anúncios de Carros')

car_data = pd.read_csv('vehicles.csv') # lendo os dados
build_histogram = st.checkbox('Criar um histograma') # criar uma caixa de seleção para histograma
build_scatter = st.checkbox('Criar um gráfico de dispersão') # criar uma caixa de seleção para gráfico de dispersão

if build_histogram: # se a caixa de seleção de histograma estiver marcada
    # escrever uma mensagem
    st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
    
    # criar um histograma
    fig = px.histogram(car_data, x="odometer")
    
    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)

if build_scatter: # se a caixa de seleção de gráfico de dispersão estiver marcada
    # escrever uma mensagem
    st.write('Criando um gráfico de dispersão para o conjunto de dados de anúncios de vendas de carros')
    
    # criar um gráfico de dispersão
    fig = px.scatter(car_data, x="year", y="price")
    
    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)
