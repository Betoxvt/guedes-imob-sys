import json
import pandas as pd
import requests
import streamlit as st
from src.functions import show_response_message, update_fields_generator

# Seria ótimo que quando fosse registrar as foreign keys (ID Edifício e ID Proprietário) mostrasse os nomes conforme os registros em suas respectivas tabelas

st.set_page_config(
    page_title='Apartamentos',
    layout='wide'
)
st.title('Apartamentos')

tab1, tab2, tab3, tab4, tab5 = st.tabs(['Registrar', 'Consultar', 'Modificar', 'Deletar', 'Listar'])

with tab1:
    st.header('Registrar Apartamento')
    with st.form('new_apartamento'):
        apto = st.text_input(
            label='Apartamento',
            value=None,
            key=2008
        )
        proprietario_id = st.number_input(
            label='ID Proprietário',
            min_value=1,
            format='%d',
            step=1,
            key=2010
        )
        cod_celesc = st.text_input(
            label='Unidade Consumidora Celesc',
            value=None,
            key=2011
        )
        cod_gas = st.text_input(
            label='Código Supergasbras',
            value=None,
            key=2012
        )
        prov_net = st.text_input(
            label='Provedor de Internet',
            value=None,
            key=2013
        )
        wifi = st.text_input(
            label='Nome da Rede WiFi',
            value=None,
            key=2014
        )
        wifi_senha = st.text_input(
            label='Senha da Rede Wifi',
            value=None,
            key=2015
        )
        lock_senha = st.text_input(
            label='Senha da Fechadura',
            value=None,
            key=2016
        )

        submit_button = st.form_submit_button('Registrar')
        if submit_button:
            registry = {
                "apto": apto,
                "proprietario_id": proprietario_id,
                "cod_celesc": cod_celesc,
                "cod_gas": cod_gas,
                "prov_net": prov_net,
                "wifi": wifi,
                "wifi_senha": wifi_senha,
                "lock_senha": lock_senha
            }
            registry_json = json.dumps(obj=registry, indent=1, separators=(',',':'))
            response = requests.post("http://backend:8000/apartamentos/", registry_json)
            show_response_message(response)

with tab2:
    st.header('Consultar Apartamentos')
    get_id = st.number_input(
        'ID Apartamento',
        min_value=1,
        format='%d',
        step=1,
        key=2000
    )
    if get_id:
        response = requests.get(f'http://backend:8000/apartamentos/{get_id}')
        if response.status_code == 200:
            apto = response.json()
            df = pd.DataFrame([apto])
            st.dataframe(df, hide_index=True)
        else:
            show_response_message(response)

with tab3:
    st.header('Modificar Apartamento')
    update_id = st.number_input(
        'ID do Apartamento',
        min_value=1,
        format='%d',
        step=1,
        key=2001
    )
    if update_id:
        update_fields_generator(id=update_id, table='apartamentos', reg='proprietario', page_n=2)

with tab4:
    st.header('Deletar Apartamento')
    delete_id = st.number_input(
        label="ID Apartamento",
        min_value=1,
        format='%d',
        step=1,
        key=2002
    )
    if delete_id:
        response = requests.get(f'http://backend:8000/apartamentos/{delete_id}')
        if response.status_code == 200:
            apartamento_viz = response.json()
            df = pd.DataFrame([apartamento_viz])
            st.dataframe(df, hide_index=True)
        else:
            show_response_message(response)
        if st.button(
            'Deletar',
            key=2006
        ):
            response = requests.delete(f'http://backend:8000/apartamentos/{delete_id}')
            show_response_message(response)

with tab5:
    st.header('Listar Apartamentos')
    if st.button(
        "Mostrar",
        key=2007
    ):
        response = requests.get(f'http://backend:8000/apartamentos/')
        if response.status_code == 200:
            apartamentos = response.json()
            df = pd.DataFrame(apartamentos)
            st.dataframe(df, hide_index=True)
        else:
            show_response_message(response)