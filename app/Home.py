import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader
from utils.mystr import apto_input
from utils.myfunc import show_response_message
import requests
import pandas as pd
import locale

locale.setlocale(locale.LC_ALL, "pt_BR.UTF-8")

st.set_page_config(page_title="Pagina Inicial", layout="wide")
st.title("Página Inicial")


with open("config.yaml", "r") as f:
    config = yaml.load(f, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config["credentials"],
    config["cookie"]["name"],
    config["cookie"]["key"],
    config["cookie"]["expiry_days"],
)

authenticator.login()

if st.session_state["authentication_status"]:
    authenticator.logout(location="sidebar")
    st.write(f'Usuário: *{st.session_state["name"]}*')
    apto_id = apto_input(st.text_input(label="Apartamento", value=None, max_chars=5))
    if apto_id:
        get_apto_response = requests.get(f"http://api:8000/apartamentos/{apto_id}/")
        if get_apto_response.status_code == 200:
            alugueis_button = st.button("Alugueis", use_container_width=True)
            if alugueis_button:
                get_alugueis_response = requests.get(
                    f"http://api:8000/alugueis/?apto_id={apto_id}"
                )
                if get_alugueis_response.status_code == 200:
                    alugueis = get_alugueis_response.json()
                else:
                    show_response_message(get_alugueis_response)
            despesas_button = st.button("Despesas", use_container_width=True)
            if despesas_button:
                get_despesas_response = requests.get(
                    f"http://api:8000/despesas/?apto_id={apto_id}"
                )
                if get_despesas_response.status_code == 200:
                    despesas = get_despesas_response.json()
                else:
                    show_response_message(get_despesas_response)
            garagens_button = st.button("Garagens", use_container_width=True)
            if garagens_button:
                get_garagens_origem_response = requests.get(
                    f"http://api:8000/garagens/?apto_id_origem={apto_id}"
                )
                if get_garagens_origem_response.status_code == 200:
                    garagens_origem = get_garagens_origem_response.json()
                else:
                    show_response_message(get_garagens_origem_response)
                get_garagens_destino_response = requests.get(
                    f"http://api:8000/garagens/?apto_id_destino={apto_id}"
                )
                if get_garagens_destino_response.status_code == 200:
                    garagens_destino = get_garagens_destino_response.json()
                else:
                    show_response_message(get_garagens_destino_response)
            pagamentos_button = st.button("Pagamentos", use_container_width=True)
            if pagamentos_button:
                get_pagamentos_response = requests.get(
                    f"http://api:8000/pagamentos/?apto_id={apto_id}"
                )
                if get_pagamentos_response.status_code == 200:
                    pagamentos = get_pagamentos_response.json()
                else:
                    show_response_message(get_pagamentos_response)
            relatorios_button = st.button("Relatórios", use_container_width=True)
            if relatorios_button:
                get_relatorios_response = requests.get(
                    f"http://api:8000/relatorios/?apto_id={apto_id}"
                )
                if get_relatorios_response.status_code == 200:
                    relatorios = get_relatorios_response.json()
                else:
                    show_response_message(get_relatorios_response)
        else:
            show_response_message(get_apto_response)

elif st.session_state["authentication_status"] is False:
    st.write("Usuário ou senha incorretos")
elif st.session_state["authentication_status"] is None:
    st.write("Por favor, faça login")
