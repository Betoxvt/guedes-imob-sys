import json
import pandas as pd
import requests
import streamlit as st
from src.functions import show_response_message

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
            label='Nome',
            key=5000,
            value=None
        )
        cpf: str = st.text_input(
            label='CPF',
            key=5101,
            value=None
        )
        tel: str = st.text_input(
            label='Telefone',
            key=5102,
            value=None
        )
        email: str = st.text_input(
            label='E-Mail',
            key=5103,
            value=None
        )

        submit_button = st.form_submit_button('Registrar')
        if submit_button:
            prop_data = {
                "nome": nome,
                "cpf": cpf,
                "tel": tel,
                "email": email
            }
            submit_data = json.dumps(obj=prop_data, separators=(',',':'))
            post_response = requests.post("http://backend:8000/proprietarios/", submit_data)
            show_response_message(post_response)

with tab2:
    st.header('Consultar Proprietários')
    get_id = st.number_input(
        'ID Proprietário',
        min_value=1,
        format='%d',
        step=1,
        key=5200
    )
    if get_id:
        get_response = requests.get(f'http://backend:8000/proprietarios/{get_id}')
        if get_response.status_code == 200:
            proprietario = get_response.json()
            df_get = pd.DataFrame([proprietario])
            st.dataframe(df_get, hide_index=True)
        else:
            show_response_message(get_response)

with tab3:
    st.header('Modificar Proprietário')
    update_id = st.number_input(
        'ID do Proprietário',
        min_value=1,
        step=1,
        format='%d',
        key=5300,
    )
    if update_id:
        update_response = requests.get(f'http://backend:8000/proprietarios/{update_id}')
        if update_response.status_code == 200:
            prop_up = update_response.json()
            df_up = pd.DataFrame([prop_up])
            st.dataframe(df_up, hide_index=True)
            with st.form('update_proprietario'):
                nome: str = st.text_input(
                    label='Nome',
                    key=5301,
                    value=str(df_up.nome[0])
                )
                cpf: str = st.text_input(
                    label='CPF',
                    key=5302,
                    value=str(df_up.cpf[0])
                )
                tel: str = st.text_input(
                    label='Telefone',
                    key=5303,
                    value=str(df_up.tel[0])
                )
                email: str = st.text_input(
                    label='E-Mail',
                    key=5304,
                    value=str(df_up.email[0])
                )
                update_button = st.form_submit_button('Modificar')
                if update_button:
                    prop_up_data = {
                        "nome": nome,
                        "cpf": cpf,
                        "tel": tel,
                        "email": email,
                    }
                    update_data = json.dumps(obj=prop_up_data, separators=(',',':'))
                    put_response = requests.put(f"http://backend:8000/proprietarios/{update_id}", update_data)
                    show_response_message(put_response)
        else:
            show_response_message(update_response)
with tab4:
    st.header('Deletar Proprietário')
    delete_id = st.number_input(
        label="ID Proprietário",
        min_value=1,
        format='%d',
        step=1,
        key=5400
    )
    if delete_id:
        show_delete_response = requests.get(f'http://backend:8000/proprietarios/{delete_id}')
        if show_delete_response.status_code == 200:
            despesa_delete = show_delete_response.json()
            df_delete = pd.DataFrame([despesa_delete])
            st.dataframe(df_delete, hide_index=True)
            if st.button(
                'Deletar',
                key=5401
            ):
                show_delete_response = requests.delete(f'http://backend:8000/proprietarios/{delete_id}')
                show_response_message(show_delete_response)
        else:
            show_response_message(show_delete_response)

with tab5:
    st.header('Listar Proprietários')
    if st.button(
        "Mostrar",
        key=5500
    ):
        get_list_response = requests.get(f'http://backend:8000/proprietarios/')
        if get_list_response.status_code == 200:
            proprietarios = get_list_response.json()
            df_list = pd.DataFrame(proprietarios)
            st.dataframe(df_list, hide_index=True)
        else:
            show_response_message(get_list_response)