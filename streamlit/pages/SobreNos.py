import streamlit as st

# Configuração do fundo com gradiente
cor_de_fundo_gradiente = "linear-gradient(to top, #3735A3, #5F6DE9)" 
st.markdown(
    f"""
    <style>
    .stApp {{
        background: {cor_de_fundo_gradiente} !important;
        background-attachment: fixed;
        background-size: cover;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

def main():
    st.title("Sobre Nós 💚")
    
    # Usando diferentes métodos para exibir o conteúdo
    st.header("Nossa Missão")
    st.write("Nossa missão é fornecer informações precisas e acessíveis sobre as condições climáticas, ajudando as pessoas a se prepararem melhor para o dia a dia.")

    st.header("Nossa Equipe")
    st.write("Somos uma equipe dedicada de desenvolvedores que acreditam no valor dos dados climáticos no dia a dia. Nosso time é composto pelos estudantes da turma 302, que estão atualmente matriculados no curso de Ciências de Dados.")
    
    st.image("turma.jpeg", caption="A equipe Weamet", use_column_width=True, width=150) 

    
if __name__ == "__main__":
    main()