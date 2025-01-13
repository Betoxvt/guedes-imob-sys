import json
import pandas as pd
import requests
import streamlit as st
from src.functions import show_response_message

st.set_page_config(
    page_title='Edifícios',
    layout='wide'
)
st.title('Edifícios')

tab1, tab2, tab3, tab4, tab5 = st.tabs(['Registrar', 'Consultar', 'Modificar', 'Deletar', 'Listar'])

with tab1:
    st.header('Registrar Edifício')
    with st.form('new_edificio'):
        inputs = '...'


        submit_button = st.form_submit_button('Registrar')
        if submit_button:
            registry = {
                "inputs": inputs
            }
            registry_json = json.dumps(obj=registry, indent=1, separators=(',',':'))
            response = requests.post("http://backend:8000/edificios/", registry_json)
            show_response_message(response)

with tab2:
    st.header('Consultar Edifício')
    get_id = st.number_input(
        'ID Edifício',
        min_value=1,
        format='%d',
        key=4000
    )
    if st.button('Consultar'):
        response = requests.get(f'http://backend:8000/edificios/{get_id}')
        if response.status_code == 200:
            edificio = response.json()
            df = pd.DataFrame([edificio])
            st.dataframe(df, hide_index=True)
        else:
            show_response_message(response)

with tab3:
    st.header('Modificar Edifício')
    update_id = st.number_input(
        'ID Edifício',
        min_value=1,
        format='%d',
        key=4001
    )
    show_button = st.button('Mostrar')
    if show_button:
        response = requests.get(f'http://backend:8000/edificios/{update_id}')
        if response.status_code == 200:
            edificio_viz = response.json()
            df = pd.DataFrame([edificio_viz])
            st.dataframe(df, hide_index=True)
            with st.form('update_edificio'):
                update_inputs = ' '
                update_button = st.form_submit_button('Modificar')
                if update_button:
                    updated = {
                        "update_inputs": update_inputs
                    }
                    updated_json = json.dumps(obj=updated, indent=1, separators=(',',':'))
                    response = requests.put(f"http://backend:8000/edificios/{update_id}", updated_json)
                    show_response_message(response)
        else:
            show_response_message(response)

with tab4:
    st.header('Deletar Edifício')
    delete_id = st.number_input(
        label="ID Edifício",
        min_value=1,
        format='%d',
        key=4002
    )
    show_button = st.button('Mostrar')
    if show_button:
        response = requests.get(f'http://backend:8000/edificios/{delete_id}')
        if response.status_code == 200:
            edificio_viz = response.json()
            df = pd.DataFrame([edificio_viz])
            st.dataframe(df, hide_index=True)
        else:
            show_response_message(response)
        if st.button('Deletar'):
            response = requests.delete(f'http://backend:8000/edificios/{delete_id}')
            show_response_message(response)

with tab5:
    st.header('Listar Edifícios')
    if st.button("Mostrar"):
        response = requests.get(f'http://backend:8000/edificios/')
        if response.status_code == 200:
            edificios = response.json()
            df = pd.DataFrame(edificios)
            st.dataframe(df, hide_index=True)
        else:
            show_response_message(response)