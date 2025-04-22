import streamlit as st
import pandas as pd
import numpy as np


# import streamlit_authenticator as stauth
# import yaml
# from yaml.loader import SafeLoader


def per_aluno(A, B):
    p = (A / B) * 100
    return p


st.set_page_config(
    page_title="SIMULADOS SAEB",
    page_icon=":book:",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://github.com/MauricioRibeiroTech',
        'Report a bug': "https://github.com/MauricioRibeiroTech",
        'About': "# Aplicativo para os Indices dos Simulados do SAEB-HD "
    }
)

# with open('config.yaml') as file:
#    config = yaml.load(file, Loader=SafeLoader)

# authenticator = stauth.Authenticate(
#    config['credentials'],
#    config['cookie']['name'],
#    config['cookie']['key'],
#    config['cookie']['expiry_days']
# )

# authenticator.login()
# if st.session_state["authentication_status"]:
#    authenticator.logout()
# st.write(f'Bem Vindo *{st.session_state["name"]}*')


with st.sidebar:
    st.title('Relatório Parcial \n SAEB 2025  \n Escola Estadual Helena Dionysio')
    df = pd.read_csv("Dados_Planilha_9A/Dados_simples_simulados.csv", sep=";")

    with st.sidebar:
        salas_distintas = df["Componente"].unique().tolist()
        #salas_selecionadas = st.selectbox("Componente", ["Matematica", "Portugues"])

        componente_selecionada = st.selectbox("Componente", ["Matematica", "Portugues"])

        #if componente_selecionada:
        #    df = df[df["Turma"] == salas_selecionadas]

        if componente_selecionada:
            df = df[df["Componente"] == componente_selecionada]

        st.markdown("Desenvolvido por Mauricio A. Ribeiro")
        st.markdown("EMAIL: mau.ap.ribeiro@gmail.com")

if componente_selecionada == "Matematica"  == "9A":
    df['Porcentagem Simulado 1'] = (df['Sim1'] / 10) * 100
    df['Porcentagem Simulado 2'] = (df['Sim2'] / 10) * 100
    df['Porcentagem Simulado 3'] = (df['Sim3'] / 12) * 100
    df['Porcentagem Simulado 4'] = (df['Sim4'] / 15) * 100
    df['Porcentagem Simulado 5'] = (df['Sim5'] / 18) * 100
    df['Porcentagem Simulado 6'] = (df['Sim6'] / 18) * 100
    df['Porcentagem Simulado 7'] = (df['Sim7'] / 20) * 100
    df['Porcentagem Simulado 8'] = (df['Sim8'] / 16) * 100


elif componente_selecionada == "Portugues" == "9A":
    Numero_questoes = 10
    df['Porcentagem Simulado 1'] = (df['Sim1'] / Numero_questoes) * 100
    df['Porcentagem Simulado 2'] = (df['Sim2'] / Numero_questoes) * 100
    df['Porcentagem Simulado 3'] = (df['Sim3'] / Numero_questoes) * 100
    df['Porcentagem Simulado 4'] = (df['Sim4'] / 15) * 100
    df['Porcentagem Simulado 5'] = (df['Sim5'] / 18) * 100
    df['Porcentagem Simulado 6'] = (df['Sim6'] / 18) * 100
    df['Porcentagem Simulado 7'] = (df['Sim7'] / 14) * 100
    df['Porcentagem Simulado 8'] = (df['Sim8'] / 16) * 100
else:
    Numero_questoes = 10
    df['Porcentagem Simulado 1'] = (df['Sim1'] / 10) * 100
    df['Porcentagem Simulado 2'] = (df['Sim2'] / 10) * 100
    df['Porcentagem Simulado 3'] = (df['Sim3'] / 10) * 100
    df['Porcentagem Simulado 4'] = (df['Sim4'] / 15) * 100
    df['Porcentagem Simulado 5'] = (df['Sim5'] / 18) * 100
    df['Porcentagem Simulado 6'] = (df['Sim6'] / 18) * 100
    df['Porcentagem Simulado 7'] = (df['Sim7'] / 20) * 100
    df['Porcentagem Simulado 8'] = (df['Sim8'] / 16) * 100

SIM = ['Porcentagem Simulado 1', 'Porcentagem Simulado 2', 'Porcentagem Simulado 3', 'Porcentagem Simulado 4',
           'Porcentagem Simulado 5', 'Porcentagem Simulado 6', 'Porcentagem Simulado 7', 'Porcentagem Simulado 8']

st.header("Relatório de notas de " + str(componente_selecionada))

    # st.table(df)
st.markdown("Porcentagem de acertos dos simulados")
st.bar_chart(df, x='Aluno', y=SIM, stack=False)
df_filtrado_1 = df[df['Sim1'] >= 6]
st.markdown("## Média Percentual de Acertos:")
a, b, c = st.columns(3)

a.metric("Simulado 1", df['Porcentagem Simulado 1'].mean().round(2), border=True)
b.metric("Simulado 2", df['Porcentagem Simulado 2'].mean().round(2), border=True)
c.metric("Simulado 3", df['Porcentagem Simulado 3'].mean().round(2), border=True)
a.metric("Simulado 4", df['Porcentagem Simulado 4'].mean().round(2), border=True)
b.metric("Simulado 5", df['Porcentagem Simulado 5'].mean().round(2), border=True)
c.metric("Simulado 6", df['Porcentagem Simulado 6'].mean().round(2), border=True)
a.metric("Simulado 7", df['Porcentagem Simulado 7'].mean().round(2), border=True)
b.metric("Simulado 8", df['Porcentagem Simulado 8'].mean().round(2), border=True)

    # st.markdown("## Média de Notas Acertos:")
    # a, b, c = st.columns(3)

    # a.metric("Simulado 1", df['Sim1'].mean().round(2), border=True)
    # b.metric("Simulado 2", df['Sim2'].mean().round(2), border=True)
    # c.metric("Simulado 3", df['Sim3'].mean().round(2), border=True)
    # a.metric("Simulado 4", df['Sim4'].mean().round(2), border=True)

grafico_per = {'Simulados': ['Simulado 1', 'Simulado 2', 'Simulado 3', 'Simulado 4', 'Simulado 5', 'Simulado 6', 'Simulado 7', 'Simulado 8'],'Porcentagens': [df['Porcentagem Simulado 1'].mean().round(2), df['Porcentagem Simulado 2'].mean().round(2),
                                                                                                                                                              df['Porcentagem Simulado 3'].mean().round(2), df['Porcentagem Simulado 4'].mean().round(2),
                                                                                                                                                              df['Porcentagem Simulado 5'].mean().round(2), df['Porcentagem Simulado 6'].mean().round(2),
                                                                                                                                                              df['Porcentagem Simulado 7'].mean().round(2), df['Porcentagem Simulado 8'].mean().round(2)]}

st.markdown("## Gráfico de Porcentagem Média")
st.bar_chart(grafico_per, x='Simulados', y='Porcentagens', stack=False)

len_df_fil_1 = len(df[df['Porcentagem Simulado 1'] >= 60])
len_df_fil_2 = len(df[df['Porcentagem Simulado 2'] >= 60])
len_df_fil_3 = len(df[df['Porcentagem Simulado 3'] >= 60])
len_df_fil_4 = len(df[df['Porcentagem Simulado 4'] >= 60])
len_df_fil_5 = len(df[df['Porcentagem Simulado 5'] >= 60])
len_df_fil_6 = len(df[df['Porcentagem Simulado 6'] >= 60])
len_df_fil_7 = len(df[df['Porcentagem Simulado 7'] >= 60])
len_df_fil_8 = len(df[df['Porcentagem Simulado 8'] >= 60])
grafico_num_alunos = {'Simulados': ['Simulado 1', 'Simulado 2', 'Simulado 3', 'Simulado 4', 'Simulado 5', 'Simulado 6', 'Simulado 7', 'Simulado 8'],
                      'Numero de Alunos': [len_df_fil_1, len_df_fil_2, len_df_fil_3, len_df_fil_4, len_df_fil_5, len_df_fil_6, len_df_fil_7, len_df_fil_8]}

st.markdown("## Número de alunos acima de 60%")
st.bar_chart(grafico_num_alunos, x='Simulados', y='Numero de Alunos', stack=False)

st.markdown("## Alunos acima de 60% pontos")
st.markdown("### Primeiro Simulado")
st.table(df_filtrado_1[["Aluno", "Porcentagem Simulado 1"]].sort_values("Porcentagem Simulado 1", ascending=False).round(2))

st.markdown("### Segundo Simulado")
df_filtrado_1 = df[df['Porcentagem Simulado 2'] >= 60]
st.table(df_filtrado_1[["Aluno", "Porcentagem Simulado 2"]].sort_values("Porcentagem Simulado 2", ascending=False).round(2))

st.markdown("### Terceiro Simulado")
df_filtrado_1 = df[df['Porcentagem Simulado 3'] >= 60]
st.table(df_filtrado_1[["Aluno", "Porcentagem Simulado 3"]].sort_values("Porcentagem Simulado 3", ascending=False).round(2))

st.markdown("### Quarto Simulado")
df_filtrado_1 = df[df['Porcentagem Simulado 4'] >= 60]
st.table(df_filtrado_1[["Aluno", "Porcentagem Simulado 4"]].sort_values("Porcentagem Simulado 4", ascending=False).round(2))

st.markdown("### Quinto Simulado")
df_filtrado_1 = df[df['Porcentagem Simulado 5'] >= 60]
st.table(df_filtrado_1[["Aluno", "Porcentagem Simulado 5"]].sort_values("Porcentagem Simulado 5", ascending=False).round(2))

st.markdown("### Sexto Simulado")
df_filtrado_1 = df[df['Porcentagem Simulado 6'] >= 60]
st.table(df_filtrado_1[["Aluno", "Porcentagem Simulado 6"]].sort_values("Porcentagem Simulado 6", ascending=False).round(2))

st.markdown("### Sétimo Simulado")
df_filtrado_1 = df[df['Porcentagem Simulado 7'] >= 60]
st.table(df_filtrado_1[["Aluno", "Porcentagem Simulado 7"]].sort_values("Porcentagem Simulado 7", ascending=False).round(2))

st.markdown("### Oitavo Simulado")
df_filtrado_1 = df[df['Porcentagem Simulado 8'] >= 60]
st.table(df_filtrado_1[["Aluno", "Porcentagem Simulado 8"]].sort_values("Porcentagem Simulado 8", ascending=False).round(2))



# elif st.session_state["authentication_status"] is False:
#    st.error('Usuário/Senha é inválido')
# elif st.session_state["authentication_status"] is None:
#    st.warning('Por Favor, utilize seu usuário e senha!')
