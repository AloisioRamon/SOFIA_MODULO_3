import streamlit as st
import pandas as pd
from controllers.estudante_controller import adicionar_estudante, listar_estudantes

def show():
    st.title("📚 Cadastro de Estudantes")
    
    with st.form("cadastro_form"):
        nome = st.text_input("Nome")
        nota1 = st.text_input("1º Nota")
        nota2 = st.text_input("2º Nota")
        submitted = st.form_submit_button("Cadastrar")
        
        if submitted:
            adicionar_estudante(nome, nota1, nota2)
            st.success("✅ Estudante cadastrado com sucesso!")
    
    st.subheader("Lista de Estudantes")
    estudantes = listar_estudantes()

    # Criando uma lista de dicionários para a tabela
    dados_estudantes = [{
        "Matricula": i.id,
        "Nome": i.nome,
        "1º Nota": i.nota1,
        "2º Nota": i.nota2,
        "Média": i.media
    } for i in estudantes]
    
    # Criando um DataFrame
    df_estudantes = pd.DataFrame(dados_estudantes)
    
    # Exibindo a tabela no Streamlit
    st.dataframe(df_estudantes)

