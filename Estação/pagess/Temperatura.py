import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import numpy as np

cor_de_fundo_gradiente = "linear-gradient(to top, #3735A3, #5F6DE9)" 
st.markdown(
    f"""
    <style>
    .stApp {{
        background: {cor_de_fundo_gradiente} !important;
        background-attachment: fixed;
        background-size: cover;
    }}
    .stTextInput, .stTextArea {{
        background-color: #333333; /* Cor de fundo das caixas de entrada */
        color: white; /* Cor do texto */
        border: 1px solid #808080; /* Cor da borda */
    }}
    .stTextInput:focus, .stTextArea:focus {{
        border-color: #5F6DE9; /* Cor da borda ao focar */
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Definindo as cidades e gerando temperaturas aleatórias
cidade1 = "São Carlos (SC)"
cidade2 = "Chapecó (SC)"

# Gerando temperaturas aleatórias para as cidades
np.random.seed(42)  # Para reprodutibilidade
temperatura_atual_a = np.random.randint(15, 31)  # Temperatura aleatória entre 15°C e 30°C
temperatura_atual_b = np.random.randint(15, 31)  # Temperatura aleatória entre 15°C e 30°C

# Definindo os dias da semana
dias_da_semana = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo']

# Gerando dados aleatórios de temperatura entre 15°C e 30°C para duas cidades
temperaturas_cidade_a = np.random.randint(15, 31, size=len(dias_da_semana))
temperaturas_cidade_b = np.random.randint(15, 31, size=len(dias_da_semana))

# Criar um DataFrame
data = {
    'Dia': dias_da_semana,
    'Cidade A (°C)': temperaturas_cidade_a,
    'Cidade B (°C)': temperaturas_cidade_b
}
df = pd.DataFrame(data)

# Estilo da página
st.set_page_config(
    page_title="Comparação de Temperaturas",
    page_icon=":thermometer:",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilo dos cartões
card_style_a = """
    <div style='background-color: #1E90FF; padding: 20px; border-radius: 10px; color: white; text-align: center;'>
        <h2>{}</h2>
        <h1 style='font-size: 48px;'>{} °C</h1>
    </div>
"""
card_style_b = """
    <div style='background-color: #FF4500; padding: 20px; border-radius: 10px; color: white; text-align: center;'>
        <h2>{}</h2>
        <h1 style='font-size: 48px;'>{} °C</h1>
    </div>
"""

# Layout da página
st.title("Comparação de Temperaturas")

# Exibir cartões de temperatura
col1, col2 = st.columns(2)

with col1:
    st.markdown(card_style_a.format(cidade1, temperatura_atual_a), unsafe_allow_html=True)

with col2:
    st.markdown(card_style_b.format(cidade2, temperatura_atual_b), unsafe_allow_html=True)

# Calcular a média das temperaturas para cada cidade
media_cidade_a = df['Cidade A (°C)'].mean()
media_cidade_b = df['Cidade B (°C)'].mean()

# Criar gráfico de barras para comparação das médias semanais
fig_media = go.Figure()
fig_media.add_trace(go.Bar(
    x=[cidade1, cidade2],
    y=[media_cidade_a, media_cidade_b],
    marker=dict(color=['#1E90FF', '#FF4500']),
    name='Média Semanal'
))
fig_media.update_layout(
    title='Comparação das Médias Semanais de Temperatura',
    xaxis_title='Cidades',
    yaxis_title='Temperatura (°C)',
    yaxis=dict(range=[0, 35]),
    template='plotly_white',  # Estilo do gráfico
    margin=dict(l=40, r=40, t=60, b=40)  # Margens do gráfico
)

# Exibir o gráfico de médias semanais
st.plotly_chart(fig_media, use_container_width=True)

# Seletor para escolher o dia da semana (apenas para o gráfico inferior)
dia_selecionado = st.selectbox('Selecione um dia da semana:', df['Dia'].tolist())

# Filtrar os dados com base no dia selecionado
temperatura_selecionada = df[df['Dia'] == dia_selecionado]

# Criar um gráfico de barras para comparação de temperaturas no dia selecionado
fig_comparacao = go.Figure()
fig_comparacao.add_trace(go.Bar(
    x=[cidade1, cidade2],
    y=[temperatura_selecionada['Cidade A (°C)'].values[0], temperatura_selecionada['Cidade B (°C)'].values[0]],
    marker=dict(color=['#1E90FF', '#FF4500']),
    name='Temperatura'
))
fig_comparacao.update_layout(
    title=f'Comparação de Temperaturas em {dia_selecionado}',
    xaxis_title='Cidades',
    yaxis_title='Temperatura (°C)',
    yaxis=dict(range=[0, 35]),
    template='plotly_white',  # Estilo do gráfico
    margin=dict(l=40, r=40, t=60, b=40)  # Margens do gráfico
)

# Exibir o gráfico de comparação por dia
st.plotly_chart(fig_comparacao, use_container_width=True)