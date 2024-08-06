import streamlit as st
import pandas as pd
import os
from streamlit_star_rating import st_star_rating



# Nome do arquivo Excel
excel_file = 'feedbacks.xlsx'

# Função para inserir feedback no arquivo Excel
def inserir_feedback(Nome, Mensagem, Estrelas):
    # Cria um DataFrame com os dados do feedback
    feedback_data = {
        'Nome': [Nome],
        'Mensagem': [Mensagem],
        'Estrelas': [Estrelas]
    }
    feedback_df = pd.DataFrame(feedback_data)

    # Verifica se o arquivo já existe
    if os.path.exists(excel_file):
        # Se existir, lê o conteúdo atual e anexa o novo feedback
        existing_df = pd.read_excel(excel_file)
        updated_df = pd.concat([existing_df, feedback_df], ignore_index=True)
    else:
        # Se não existir, usa o novo DataFrame
        updated_df = feedback_df

    # Salva o DataFrame atualizado no arquivo Excel
    updated_df.to_excel(excel_file, index=False)

# Inicialize uma lista para armazenar feedbacks
if 'feedback_list' not in st.session_state:
    st.session_state.feedback_list = []

# Cabeçalho da página
st.markdown("<h1 style='text-align: center; color: #808080;'>Nos dê seu feedback ✍️</h1>", unsafe_allow_html=True)
st.write('')
st.write('')

# Campos de entrada para feedback
Nome = st.text_input('Digite o seu nome:')
Mensagem = st.text_area('Nos conte mais sobre sua experiência:', height=200)
Estrelas = st_star_rating(label='Qual sua avaliação?', maxValue=5, defaultValue=0, key="Estrelas")
st.write(f'Você avaliou com {Estrelas} estrelas.')
st.write('')

# Botão para enviar feedback
if st.button('Enviar feedback'):
    missing_fields = False

    if not Nome or not Mensagem or Estrelas == 0:  # Verifica se Estrelas é 0
        missing_fields = True
        st.warning('Por favor, preencha todos os campos obrigatórios.')

    if not missing_fields:
        inserir_feedback(Nome, Mensagem, Estrelas)
        st.session_state.feedback_list.append({'Nome': Nome, 'Mensagem': Mensagem, 'Estrelas': Estrelas})
        st.success('Obrigado pelo seu feedback!')