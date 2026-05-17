import pandas as pd
import plotly.express as px
import streamlit as st

# lendo os dados
car_data = pd.read_csv(
    'C:/Users/rafae/anaconda_projects/sprint5-project/vehicles_us.csv')

st.header('Tabela de Veículos')

# criar um checkbox para histograma
hist_checkbox = st.checkbox('Criar histograma')

if hist_checkbox:  # se o checkbox for selecionado
    # escrever uma mensagem
    st.write(
        'Criando um histograma para o conjunto de dados de anúncios de vendas de carros')

    # criar um histograma
    fig = px.histogram(car_data, x="odometer")

    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)

# criar  um checkbox para gráfico de dispersão
disp_checkbox = st.checkbox('Criar dispersão')

if disp_checkbox:  # se o checkbox for selecionado
    # escrever uma mensagem
    st.write(
        'Criando um gráfico de dispersão para o conjunto de dados de anúncios de vendas de carros')

    # criar um gráfico de dispersão
    fig = px.scatter(car_data, x="odometer", y="price")

    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)
