import streamlit as st
from datetime import datetime
import uuid
import pandas as pd
import time

def main():
    st.sidebar.title("Menu")
    app_mode = st.sidebar.selectbox("Escolha a ação", ["Cadastrar", "Listar"])

    if app_mode == "Cadastrar":
        cadastrar()
    elif app_mode == "Listar":
        listar()

def cadastrar():
    options = ["Usuário", "Departamento", "Monitoria", "Aula"]
    choice = st.sidebar.selectbox("Escolha a opção de cadastro", options)

    if choice == "Usuário":
        cadastro_usuario()
    elif choice == "Departamento":
        cadastro_departamento()
    elif choice == "Monitoria":
        cadastro_monitoria()
    elif choice == "Aula":
        cadastro_aula()

def listar():
    options = ["Usuário", "Departamento", "Monitoria", "Aula"]
    choice = st.sidebar.selectbox("Escolha a opção de listagem", options)

    if choice == "Usuário":
        listar_usuarios()
    elif choice == "Departamento":
        listar_departamentos()
    elif choice == "Monitoria":
        listar_monitorias()
    elif choice == "Aula":
        listar_aulas()

def cadastro_usuario():
    st.title("Cadastro de Usuário")
    nome = st.text_input("Nome")
    email = st.text_input("Email")
    senha = st.text_input("Senha", type="password")
    if st.button("Cadastrar Usuário"):
        if 'usuarios' not in st.session_state:
            st.session_state.usuarios = []
        usuario_id = str(uuid.uuid4())
        st.session_state.usuarios.append({"ID": usuario_id, "Nome": nome, "Email": email})
        time.sleep(5)
        st.success(f"Usuário {nome} cadastrado com sucesso!")

def cadastro_departamento():
    st.title("Cadastro de Departamento")
    id_professor = st.text_input("ID do Professor")
    nome = st.text_input("Nome do Departamento")
    descricao = st.text_area("Descrição")
    data = st.date_input("Data")
    data_str = data.strftime("%Y-%m-%d")
    duracao = st.text_input("Duração")
    if st.button("Cadastrar Departamento"):
        if 'departamentos' not in st.session_state:
            st.session_state.departamentos = []
        dept_id = str(uuid.uuid4())
        st.session_state.departamentos.append({"ID": dept_id, "ID Professor": id_professor, "Nome": nome, "Descrição": descricao, "Data": data_str, "Duração": duracao})
        time.sleep(5)
        st.success(f"Departamento {nome} cadastrado com sucesso!")

def cadastro_monitoria():
    st.title("Cadastro de Monitoria")
    id_professor = st.text_input("ID do Professor")
    nome = st.text_input("Nome da Monitoria")
    descricao = st.text_area("Descrição")
    data = st.date_input("Data")
    data_str = data.strftime("%Y-%m-%d")
    duracao = st.text_input("Duração")
    departamento = st.text_input("Departamento")
    if st.button("Cadastrar Monitoria"):
        if 'monitorias' not in st.session_state:
            st.session_state.monitorias = []
        monitoria_id = str(uuid.uuid4())
        st.session_state.monitorias.append({"ID": monitoria_id, "ID Professor": id_professor, "Nome": nome, "Descrição": descricao, "Data": data_str, "Duração": duracao, "Departamento": departamento})
        time.sleep(5)
        st.success(f"Monitoria {nome} cadastrada com sucesso!")

def cadastro_aula():
    st.title("Cadastro de Aula")
    id_professor = st.text_input("ID do Professor")
    nome = st.text_input("Nome da Aula")
    descricao = st.text_area("Descrição")
    data = st.date_input("Data")
    data_str = data.strftime("%Y-%m-%d")
    duracao = st.text_input("Duração")
    departamento = st.text_input("Departamento")
    if st.button("Cadastrar Aula"):
        if 'aulas' not in st.session_state:
            st.session_state.aulas = []
        aula_id = str(uuid.uuid4())
        st.session_state.aulas.append({"ID": aula_id, "ID Professor": id_professor, "Nome": nome, "Descrição": descricao, "Data": data_str, "Duração": duracao, "Departamento": departamento})
        time.sleep(5)
        st.success(f"Aula {nome} cadastrada com sucesso!")

def listar_usuarios():
    st.title("Lista de Usuários")
    if 'usuarios' in st.session_state and st.session_state.usuarios:
        usuario_df = pd.DataFrame(st.session_state.usuarios)
        st.table(usuario_df)
    else:
        st.write("Nenhum usuário cadastrado.")
def listar_departamentos():
    st.title("Lista de Departamentos")
    if 'departamentos' in st.session_state and st.session_state.departamentos:
        dept_df = pd.DataFrame(st.session_state.departamentos)
        st.table(dept_df)
    else:
        st.write("Nenhum departamento cadastrado.")

def listar_monitorias():
    st.title("Lista de Monitorias")
    if 'monitorias' in st.session_state and st.session_state.monitorias:
        monitoria_df = pd.DataFrame(st.session_state.monitorias)
        st.table(monitoria_df)
    else:
        st.write("Nenhuma monitoria cadastrada.")

def listar_aulas():
    st.title("Lista de Aulas")
    if 'aulas' in st.session_state and st.session_state.aulas:
        aula_df = pd.DataFrame(st.session_state.aulas)
        st.table(aula_df)
    else:
        st.write("Nenhuma aula cadastrada.")

if __name__ == "__main__":
    main()
