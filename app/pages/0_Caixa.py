from datetime import date
import pandas as pd
import requests
import streamlit as st
from utils.mydate import str_to_date
from utils.myfunc import cat_index, show_data_output, show_response_message

st.set_page_config(page_title="Caixa", layout="wide")
st.title("Caixa")

if not st.session_state["authentication_status"]:
    st.info("Por favor faça o login na Home page e tente novamente.")
    st.stop()
else:
    authenticator = st.session_state.authenticator
    st.write(f'Usuário: *{st.session_state["name"]}*')
    authenticator.logout(location="sidebar")

tab1, tab2, tab3, tab4, tab5 = st.tabs(
    ["Registrar", "Consultar", "Modificar", "Deletar", "listar"]
)

moedas = ["BRL", "USD"]

with tab1:
    st.header("Registrar Fluxo de Caixa")
    moeda: str = st.selectbox(
        label="Moeda",
        options=moedas,
    )
    valor: float = st.number_input(
        label="Valor",
        format="%.2f",
    )
    if st.button("Registrar"):
        caixa_data = {
            "moeda": moeda,
            "valor": valor,
        }
        try:
            post_response = requests.post("http://api:8000/caixa/", json=caixa_data)
            show_response_message(post_response)
            if post_response.status_code == 200:
                st.subheader("Dados inseridos, tudo OK:")
            else:
                st.subheader("Dados NÃO inseridos, favor revisar:")
            show_data_output(caixa_data)
        except Exception as e:
            raise e

with tab2:
    st.header("Consultar Caixa")

    with st.expander(label="Filtros"):
        start_date = st.date_input(
            label="Data de Início",
            value=None,
            format="DD/MM/YYYY",
        )
        end_date = st.date_input(
            label="Data de Término", value=None, format="DD/MM/YYYY"
        )
        signal = st.selectbox(
            label="Tipo",
            options=["Todos", "Depósitos", "Saques"],
        )
        moeda = st.selectbox(label="Moeda", options=["Todos", "BRL", "USD"])

    if st.button("Consultar"):
        get_list_response = requests.get(
            f"http://api:8000/caixa/?start_date={start_date}&end_date={end_date}&signal={signal}&moeda={moeda}"
        )
