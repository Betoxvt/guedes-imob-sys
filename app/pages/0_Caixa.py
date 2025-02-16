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
