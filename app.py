import streamlit as st
from utils.db import init_db
from views import cadastro, conteudo, dashboard, documentos  # import do módulo documentos

# Inicializa banco
init_db()

# Sessão de login
if "logado" not in st.session_state:
    st.session_state.logado = False

# Estilo customizado
st.markdown(
    """
    <style>
    body {
        background-color: #fff5f5;
    }
    .stApp {
        background-image: url("https://upload.wikimedia.org/wikipedia/commons/6/6a/Chinese_Red_Pattern.png");
        background-size: cover;
        background-position: center;
    }
    .login-box {
        background: rgba(255, 255, 255, 0.9);
        padding: 30px;
        border-radius: 20px;
        text-align: center;
        box-shadow: 0px 4px 20px rgba(0,0,0,0.2);
    }
    .title {
        font-size: 32px;
        color: #b22222;
        font-weight: bold;
        margin-bottom: 20px;
        font-family: 'Noto Serif SC', serif;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Função login
def login():
    st.markdown('<div class="login-box">', unsafe_allow_html=True)
    st.markdown('<div class="title">🐲 Login no Banguela</div>', unsafe_allow_html=True)

    usuario = st.text_input("Usuário")
    senha = st.text_input("Senha", type="password")

    if st.button("Entrar"):
        if usuario == "admin" and senha == "1234":
            st.session_state.logado = True
            st.success("登录成功! (Login realizado com sucesso!)")
        else:
            st.error("Usuário ou senha incorretos.")

    st.markdown('</div>', unsafe_allow_html=True)

# Se logado → mostra sistema
if st.session_state.logado:
    st.title("🐲 Banguela")

    st.sidebar.title("📌 MENU")
    opcao = st.sidebar.radio("Navegação", ["Cadastro", "Dashboard", "Conteúdo", "Documentos"])

    if opcao == "Cadastro":
        cadastro.show()
    elif opcao == "Conteúdo":
        conteudo.show()
    elif opcao == "Dashboard":
        dashboard.show()
    elif opcao == "Documentos":
        documentos.show_documentos()  # chamada da nova função

    if st.sidebar.button("Sair"):
        st.session_state.logado = False
else:
    login()
