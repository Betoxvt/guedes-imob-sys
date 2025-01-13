import json
import pandas as pd
import requests
import streamlit as st
from src.functions import show_response_message

st.set_page_config(
    page_title='Garagens',
    layout='wide'
)
st.title('Garagens')

tab1, tab2, tab3, tab4, tab5 = st.tabs(['Registrar', 'Consultar', 'Modificar', 'Deletar', 'Listar'])

with tab1:
    st.header('Registrar Garagem')
    with st.form('new_garagem'):
        inputs = '...'


        submit_button = st.form_submit_button('Registrar')
        if submit_button:
            registry = {
                "inputs": inputs
            }
            registry_json = json.dumps(obj=registry, indent=1, separators=(',',':'))
            response = requests.post("http://backend:8000/garagens/", registry_json)
            show_response_message(response)

with tab2:
    st.header('Consultar Garagens')
    get_id = st.number_input(
        'ID Garagem',
        min_value=1,
        format='%d',
        key=5000
    )
    if st.button(
        'Consultar',
        key=5003
    ):
        response = requests.get(f'http://backend:8000/garagens/{get_id}')
        if response.status_code == 200:
            garagem = response.json()
            df = pd.DataFrame([garagem])
            st.dataframe(df, hide_index=True)
        else:
            show_response_message(response)

with tab3:
    st.header('Modificar Garagem')
    update_id = st.number_input(
        'ID do Garagem',
        min_value=1,
        format='%d',
        key=5001
    )
    if st.button(
        'Mostrar',
        key=5004
    ):
        response = requests.get(f'http://backend:8000/garagens/{update_id}')
        if response.status_code == 200:
            garagem_viz = response.json()
            df = pd.DataFrame([garagem_viz])
            st.dataframe(df, hide_index=True)
            with st.form('update_garagem'):
                update_inputs = ' '
                update_button = st.form_submit_button('Modificar')
                if update_button:
                    updated = {
                        "update_inputs": update_inputs
                    }
                    updated_json = json.dumps(obj=updated, indent=1, separators=(',',':'))
                    response = requests.put(f"http://backend:8000/garagens/{update_id}", updated_json)
                    show_response_message(response)
        else:
            show_response_message(response)

with tab4:
    st.header('Deletar Garagem')
    delete_id = st.number_input(
        label="ID Garagem",
        min_value=1,
        format='%d',
        key=5002
    )
    if st.button(
        'Mostrar',
        key=5005
    ):
        response = requests.get(f'http://backend:8000/garagens/{delete_id}')
        if response.status_code == 200:
            garagem_viz = response.json()
            df = pd.DataFrame([garagem_viz])
            st.dataframe(df, hide_index=True)
        else:
            show_response_message(response)
        if st.button(
            'Deletar',
            key=5006
        ):
            response = requests.delete(f'http://backend:8000/garagens/{delete_id}')
            show_response_message(response)

with tab5:
    st.header('Listar Garagens')
    if st.button(
        "Mostrar",
        key=5007
    ):
        response = requests.get(f'http://backend:8000/garagens/')
        if response.status_code == 200:
            garagens = response.json()
            df = pd.DataFrame(garagens)
            st.dataframe(df, hide_index=True)
        else:
            show_response_message(response)