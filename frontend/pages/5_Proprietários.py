import json
import pandas as pd
import requests
import streamlit as st
from src.functions import show_response_message, update_fields_generator

st.set_page_config(
    page_title='Proprietários',
    layout='wide'
)
st.title('Proprietários')

tab1, tab2, tab3, tab4, tab5 = st.tabs(['Registrar', 'Consultar', 'Modificar', 'Deletar', 'Listar'])

with tab1:
    st.header('Registrar Proprietário')
    with st.form('new_proprietario'):
        nome: str = st.text_input(
            'Nome',
            key=7008,
            value=None,
            placeholder='Obrigatório'
        )
        cpf: str = st.text_input(
            'CPF',
            key=7009,
            value=None
        )
        tel: str = st.text_input(
            'Telefone',
            key=7010,
            value=None
        )
        email: str = st.text_input(
            'E-Mail',
            key=7011,
            value=None
        )

        submit_button = st.form_submit_button('Registrar')
        if submit_button:
            registry = {
                "nome": nome,
                "cpf": cpf,
                "tel": tel,
                "email": email
            }
            registry_json = json.dumps(obj=registry, indent=1, separators=(',',':'))
            response = requests.post("http://backend:8000/proprietarios/", registry_json)
            show_response_message(response)

with tab2:
    st.header('Consultar Proprietários')
    get_id = st.number_input(
        'ID Proprietário',
        min_value=1,
        format='%d',
        step=1,
        key=7000
    )
    if get_id:
        response = requests.get(f'http://backend:8000/proprietarios/{get_id}')
        if response.status_code == 200:
            proprietario = response.json()
            df = pd.DataFrame([proprietario])
            st.dataframe(df, hide_index=True)
        else:
            show_response_message(response)

with tab3:
    st.header('Modificar Proprietário')
    update_id = st.number_input(
        'ID do Proprietário',
        min_value=1,
        step=1,
        format='%d',
        key=7300,
    )
    if update_id:
        update_fields_generator(id=update_id, table='proprietarios', reg='proprietario', page_n=7)

with tab4:
    st.header('Deletar Proprietário')
    delete_id = st.number_input(
        label="ID Proprietário",
        min_value=1,
        format='%d',
        step=1,
        key=7002
    )
    if delete_id:
        response = requests.get(f'http://backend:8000/proprietarios/{delete_id}')
        if response.status_code == 200:
            proprietario_viz = response.json()
            df = pd.DataFrame([proprietario_viz])
            st.dataframe(df, hide_index=True)
        else:
            show_response_message(response)
    if st.button(
        'Deletar',
        key=7006
    ):
        response = requests.delete(f'http://backend:8000/proprietarios/{delete_id}')
        show_response_message(response)

with tab5:
    st.header('Listar Proprietários')
    if st.button(
        "Mostrar",
        key=7007
    ):
        response = requests.get(f'http://backend:8000/proprietarios/')
        if response.status_code == 200:
            proprietarios = response.json()
            df = pd.DataFrame(proprietarios)
            st.dataframe(df, hide_index=True)
        else:
            show_response_message(response)