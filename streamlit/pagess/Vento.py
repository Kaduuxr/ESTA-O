import streamlit as st

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

def main():
    st.header("Vento")
    st.write("Aqui você pode visualizar informações sobre a vento.")

if __name__ == "__main__":
    main()