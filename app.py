import streamlit as st
from utils.db import init_db
from views import cadastro, conteudo, dashboard

# Inicializa banco
init_db()
st.title("🥷 SofIA")
# Menu
st.sidebar.title("📌 Menu")
opcao = st.sidebar.radio("Navegação", ["Cadastro","Dashboard", "Conteúdo","Documentos"])

if opcao == "Cadastro":
    cadastro.show()
elif opcao == "Conteúdo":
    conteudo.show()
elif opcao == "Dashboard":
    dashboard.show()
elif opcao == "Documentos":
    pass
