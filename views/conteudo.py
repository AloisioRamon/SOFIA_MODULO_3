import streamlit as st
#from controllers.conteudo_controller import gerar_conteudo
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import re

def limpar_resposta(text:str)-> str:
    return re.sub(r"<think>.*?</think", "", text, flags=re.DOTALL).strip()


def show():
    st.title("📝 Geração de Conteúdo com IA")

        # Entrada da chave do usuário
    api_key = st.text_input("Digite sua chave da Groq", type="password")

    # Escolha do modelo
    modelo = st.selectbox(
        "Escolha o modelo",
        ["deepseek-r1-distill-llama-70b", "llama3-70b-8192", "xxxxxxxx"]
    )

    with st.form("conteudo_form"):
        titulo = st.text_input("Título do Conteúdo")
        tema = st.text_area("Tema/Assunto")
        gerar = st.form_submit_button("Gerar Conteúdo")

    if gerar:
        if not api_key:
            st.error("❌ Você precisa informar a chave da Groq.")
        else:
            try:
                # Configura o LLM com a chave digitada
                llm = ChatGroq(model=modelo, api_key=api_key)

                # Prompt
                prompt = ChatPromptTemplate.from_messages([
                    ("system", "Você é um professor especialista em educação."),
                    ("user", "Crie um conteúdo didático sobre o tema: {tema}, com título: {titulo}.")
                ])

                chain = prompt | llm | StrOutputParser()

                with st.spinner("Gerando conteúdo..."):
                    resultado = chain.invoke({"titulo": titulo, "tema": tema})
                    resultado = limpar_resposta(resultado)

                st.success("✅ Conteúdo gerado com sucesso!")
                st.write("### Resultado")
                st.write(resultado)

            except Exception as e:
                st.error(f"Erro ao gerar conteúdo: {e}")
