import streamlit as st
from streamlit_extras.app_logo import add_logo

st.set_page_config(page_title="Weamet", page_icon="🐸")

cor_de_fundo_gradiente = "linear-gradient(to top, #3735A3, #5F6DE9)" 

st.markdown(
    f"""
    <style>
    .stApp {{
        background: {cor_de_fundo_gradiente} !important;
        background-attachment: fixed;
        background-size: cover;
    }}
    .card {{
        background-color: #ffffff;
        border-radius: 10px;
        padding: 20px;
        margin: 10px 0;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        text-align: center;
        cursor: pointer;
    }}
    .card:hover {{
        background-color: #f0f0f0;
    }}
    .card img {{
        width: 50px;
        height: 50px;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Barra de título
st.title("Weamet")

def logo():
    add_logo("image.png", height=300)

# Função para criar um card
def card(label, icon, page):
    return f"""
    <div class="card" onclick="window.location.href='{page}'">
        <img src="{icon}" alt="{label} icon"/>
        <h3>{label}</h3>
    </div>
    """

with st.sidebar:
    logo()
    st.markdown("### Navegação")
    
    # Adicionando os cards
    st.markdown(card("Vento", "https://img.icons8.com/ios/50/000000/wind.png", "pagess/Vento.py"), unsafe_allow_html=True)
    st.markdown(card("Temperatura", "https://img.icons8.com/ios/50/000000/thermometer.png", "pagess/Temperatura.py"), unsafe_allow_html=True)
    st.markdown(card("Umidade", "https://img.icons8.com/ios/50/000000/humidity.png", "pagess/Umidade.py"), unsafe_allow_html=True)
    st.markdown(card("Pressão Atmosférica", "https://img.icons8.com/ios/50/000000/barometer.png", "pagess/PressaoAtmosferica.py"), unsafe_allow_html=True)
    st.markdown(card("Sobre nós", "https://img.icons8.com/ios/50/000000/frog.png", "pagess/SobreNos.py"), unsafe_allow_html=True)
    st.markdown(card("Precipitação", "https://img.icons8.com/ios/50/000000/rain.png", "pagess/Precipitacao.py"), unsafe_allow_html=True)
    st.markdown(card("Luminosidade", "https://img.icons8.com/ios/50/000000/sun.png", "pagess/Luminosidade.py"), unsafe_allow_html=True)
    st.markdown(card("Feedback", "https://img.icons8.com/ios/50/000000/feedback.png", "pagess/Feedback.py"), unsafe_allow_html=True)

st.image("image.png", use_column_width=True)  
