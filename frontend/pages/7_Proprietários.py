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
        inputs = '...'


        submit_button = st.form_submit_button('Registrar')
        if submit_button:
            registry = {
                "inputs": inputs
            }
            registry_json = json.dumps(obj=registry, indent=1, separators=(',',':'))
            response = requests.post("http://backend:8000/proprietarios/", registry_json)
            show_response_message(response)

with tab2:
    st.header('Consultar Proprietário')
    get_id = st.number_input(
        'ID Proprietário',
        min_value=1,
        format='%d',
        key=7000
    )
    if st.button('Consultar'):
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
        'ID Proprietário',
        min_value=1,
        format='%d',
        key=7001
    )
    show_button = st.button('Mostrar')
    if show_button:
        response = requests.get(f'http://backend:8000/proprietarios/{update_id}')
    if response.status_code == 200:
        proprietario_viz = response.json()
        df = pd.DataFrame([proprietario_viz])
        st.dataframe(df, hide_index=True)
        with st.form('update_proprietario'):
            update_inputs = ' '
            update_button = st.form_submit_button('Modificar')
            if update_button:
                updated = {
                    "update_inputs": update_inputs
                }
                updated_json = json.dumps(obj=updated, indent=1, separators=(',',':'))
                response = requests.put(f"http://backend:8000/proprietarios/{update_id}", updated_json)
                show_response_message(response)
    else:
        show_response_message(response)

with tab4:
    st.header('Deletar Proprietário')
    delete_id = st.number_input(
        label="ID Proprietário",
        min_value=1,
        format='%d',
        key=7002
    )
    show_button = st.button('Mostrar')
    if show_button:
        response = requests.get(f'http://backend:8000/proprietarios/{delete_id}')
        if response.status_code == 200:
            proprietario_viz = response.json()
            df = pd.DataFrame([proprietario_viz])
            st.dataframe(df, hide_index=True)
        else:
            show_response_message(response)
        if st.button('Deletar'):
            response = requests.delete(f'http://backend:8000/proprietarios/{delete_id}')
            show_response_message(response)

with tab5:
    st.header('Listar Proprietários')
    if st.button("Mostrar"):
        response = requests.get(f'http://backend:8000/proprietarios/')
        if response.status_code == 200:
            proprietarios = response.json()
            df = pd.DataFrame(proprietarios)
            st.dataframe(df, hide_index=True)
        else:
            show_response_message(response)