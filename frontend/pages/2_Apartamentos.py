import json
import pandas as pd
import requests
import streamlit as st
from src.functions import show_response_message

st.set_page_config(
    page_title='Apartamentos',
    layout='wide'
)
st.title('Apartamentos')

tab1, tab2, tab3, tab4, tab5 = st.tabs(['Registrar', 'Consultar', 'Modificar', 'Deletar', 'Listar'])

with tab1:
    st.header('Registrar Apartamento')
    with st.form('new_apartamento'):
        inputs = '...'


        submit_button = st.form_submit_button('Registrar')
        if submit_button:
            registry = {
                "inputs": inputs
            }
            registry_json = json.dumps(obj=registry, indent=1, separators=(',',':'))
            response = requests.post("http://backend:8000/apartamentos/", registry_json)
            show_response_message(response)

with tab2:
    st.header('Consultar Apartamento')
    get_id = st.number_input(
        'ID Apartamento',
        min_value=1,
        format='%d',
        key=2000
    )
    if st.button('Consultar'):
        response = requests.get(f'http://backend:8000/apartamentos/{get_id}')
        if response.status_code == 200:
            apartamento = response.json()
            df = pd.DataFrame([apartamento])
            st.dataframe(df, hide_index=True)
        else:
            show_response_message(response)

with tab3:
    st.header('Modificar Apartamento')
    update_id = st.number_input(
        'ID Apartamento',
        min_value=1,
        format='%d',
        key=2001
    )
    show_button = st.button('Mostrar')
    if show_button:
        response = requests.get(f'http://backend:8000/apartamentos/{update_id}')
    if response.status_code == 200:
        apartamento_viz = response.json()
        df = pd.DataFrame([apartamento_viz])
        st.dataframe(df, hide_index=True)
        with st.form('update_apartamento'):
            update_inputs = ' '
            update_button = st.form_submit_button('Modificar')
            if update_button:
                updated = {
                    "update_inputs": update_inputs
                }
                updated_json = json.dumps(obj=updated, indent=1, separators=(',',':'))
                response = requests.put(f"http://backend:8000/apartamentos/{update_id}", updated_json)
                show_response_message(response)
    else:
        show_response_message(response)

with tab4:
    st.header('Deletar Apartamento')
    delete_id = st.number_input(
        label="ID Apartamento",
        min_value=1,
        format='%d',
        key=2002
    )
    show_button = st.button('Mostrar')
    if show_button:
        response = requests.get(f'http://backend:8000/apartamentos/{delete_id}')
        if response.status_code == 200:
            apartamento_viz = response.json()
            df = pd.DataFrame([apartamento_viz])
            st.dataframe(df, hide_index=True)
        else:
            show_response_message(response)
        if st.button('Deletar'):
            response = requests.delete(f'http://backend:8000/apartamentos/{delete_id}')
            show_response_message(response)

with tab5:
    st.header('Listar Apartamentos')
    if st.button("Mostrar"):
        response = requests.get(f'http://backend:8000/apartamentos/')
        if response.status_code == 200:
            apartamentos = response.json()
            df = pd.DataFrame(apartamentos)
            st.dataframe(df, hide_index=True)
        else:
            show_response_message(response)