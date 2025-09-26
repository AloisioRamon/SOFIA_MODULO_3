import streamlit as st
import pandas as pd
from controllers.estudante_controller import adicionar_estudante, listar_estudantes

def show():
    # CSS customizado para o tema chinês
    st.markdown(
        """
        <style>
        .cadastro-box {
            background: rgba(255, 255, 255, 0.9);
            padding: 25px;
            border-radius: 15px;
            box-shadow: 0px 4px 15px rgba(0,0,0,0.2);
            margin-bottom: 20px;
        }
        .title {
            font-size: 28px;
            color: #b22222;
            font-weight: bold;
            text-align: center;
            font-family: 'Noto Serif SC', serif;
            margin-bottom: 15px;
        }
        .sub-title {
            font-size: 22px;
            color: #d2691e;
            font-weight: bold;
            margin-top: 20px;
            margin-bottom: 10px;
            font-family: 'Noto Serif SC', serif;
        }
        .stDataFrame {
            border: 2px solid #b22222;
            border-radius: 10px;
            overflow: hidden;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Título principal
    st.markdown('<div class="title">📚 Cadastro de Estudantes 🀄</div>', unsafe_allow_html=True)

    # Caixa de cadastro
    st.markdown('<div class="cadastro-box">', unsafe_allow_html=True)
    with st.form("cadastro_form"):
        nome = st.text_input("Nome")
        nota1 = st.text_input("1º Nota")
        nota2 = st.text_input("2º Nota")
        submitted = st.form_submit_button("Cadastrar 🏮")
        
        if submitted:
            adicionar_estudante(nome, nota1, nota2)
            st.success("✅ Estudante cadastrado com sucesso! 🎉")
    st.markdown('</div>', unsafe_allow_html=True)

    # Lista de estudantes
    st.markdown('<div class="sub-title">👥 Lista de Estudantes</div>', unsafe_allow_html=True)
    estudantes = listar_estudantes()

    # Criando lista de dicionários
    dados_estudantes = [{
        "Matrícula": i.id,
        "Nome": i.nome,
        "1º Nota": i.nota1,
        "2º Nota": i.nota2,
        "Média": i.media
    } for i in estudantes]
    
    # DataFrame
    df_estudantes = pd.DataFrame(dados_estudantes)

    # Exibindo tabela estilizada
    st.dataframe(df_estudantes, use_container_width=True)
