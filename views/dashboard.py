import streamlit as st
from controllers.estudante_controller import listar_estudantes
import pandas as pd
import plotly.express as px  # Para gráficos

def show():
    st.title("📊 Dashboard Escolar")
    st.write("Relatórios e estatísticas dos alunos aqui...")

    listaDeEstudantes = listar_estudantes()

    if not listaDeEstudantes:
        st.warning("Nenhum estudante foi cadastrado ainda")
        return

    estudantesCadastrados = []
    
    # Preenchendo a lista de estudantes para exibição em tabela
    for e in listaDeEstudantes:
        estudantesCadastrados.append({
            "Nome": e.nome, 
            "1º Nota": f"{e.nota1:.2f}", 
            "2º Nota": f"{e.nota2:.2f}", 
            "Média": f"{e.media:.2f}"
        })

    st.subheader("Lista de Estudantes Cadastrados")
    st.table(estudantesCadastrados)

    # Gráfico de barras: médias por estudante
    # Criando um DataFrame para o gráfico de barras
    df_bar = pd.DataFrame(estudantesCadastrados)
    fig_bar = px.bar(
        df_bar,
        x="Nome",
        y="Média",
        title="Média Individual dos Estudantes",
        labels={"Média": "Média", "Nome": "Estudante"},
        text="Média",
        range_y=[0, 10]  # As notas variam de 0 a 10
    )
    fig_bar.update_traces(texttemplate='%{text:.2f}', textposition='outside')
    st.plotly_chart(fig_bar, use_container_width=True)

    # Categorizando estudantes por média para gráfico de pizza
    categorias = {
        "Abaixo de 5": 0,
        "Entre 5 e 7": 0,
        "Acima de 7": 0
    }
    for e in listaDeEstudantes:
        if e.media < 5:
            categorias["Abaixo de 5"] += 1
        elif e.media <= 7:
            categorias["Entre 5 e 7"] += 1
        else:
            categorias["Acima de 7"] += 1

    fig_pie = px.pie(
        names=list(categorias.keys()),
        values=list(categorias.values()),
        title="Distribuição das Médias dos Estudantes",
        color_discrete_sequence=px.colors.qualitative.Pastel
    )
    st.plotly_chart(fig_pie, use_container_width=True)
