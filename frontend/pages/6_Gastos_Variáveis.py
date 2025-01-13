import json
import pandas as pd
import requests
import streamlit as st
from src.functions import show_response_message

st.set_page_config(
    page_title='Gastos Variáveis',
    layout='wide'
)
st.title('Gastos Variáveis')

tab1, tab2, tab3, tab4, tab5 = st.tabs(['Registrar', 'Consultar', 'Modificar', 'Deletar', 'Listar'])

with tab1:
    st.header('Registrar Gastos Variável')
    with st.form('new_gasto'):
        inputs = '...'


        submit_button = st.form_submit_button('Registrar')
        if submit_button:
            registry = {
                "inputs": inputs
            }
            registry_json = json.dumps(obj=registry, indent=1, separators=(',',':'))
            response = requests.post("http://backend:8000/gastos/", registry_json)
            show_response_message(response)

with tab2:
    st.header('Consultar Gastos Variável')
    get_id = st.number_input(
        'ID Gastos Variável',
        min_value=1,
        format='%d',
        key=6000
    )
    if st.button('Consultar'):
        response = requests.get(f'http://backend:8000/gastos/{get_id}')
        if response.status_code == 200:
            gasto = response.json()
            df = pd.DataFrame([gasto])
            st.dataframe(df, hide_index=True)
        else:
            show_response_message(response)

with tab3:
    st.header('Modificar Gastos Variável')
    update_id = st.number_input(
        'ID Gastos Variável',
        min_value=1,
        format='%d',
        key=6001
    )
    show_button = st.button('Mostrar')
    if show_button:
        response = requests.get(f'http://backend:8000/gastos/{update_id}')
        if response.status_code == 200:
            gasto_viz = response.json()
            df = pd.DataFrame([gasto_viz])
            st.dataframe(df, hide_index=True)
            with st.form('update_gasto'):
                update_inputs = ' '
                update_button = st.form_submit_button('Modificar')
                if update_button:
                    updated = {
                        "update_inputs": update_inputs
                    }
                    updated_json = json.dumps(obj=updated, indent=1, separators=(',',':'))
                    response = requests.put(f"http://backend:8000/gastos/{update_id}", updated_json)
                    show_response_message(response)
        else:
            show_response_message(response)

with tab4:
    st.header('Deletar Gastos Variável')
    delete_id = st.number_input(
        label="ID Gastos Variável",
        min_value=1,
        format='%d',
        key=6002
    )
    show_button = st.button('Mostrar')
    if show_button:
        response = requests.get(f'http://backend:8000/gastos/{delete_id}')
        if response.status_code == 200:
            gasto_viz = response.json()
            df = pd.DataFrame([gasto_viz])
            st.dataframe(df, hide_index=True)
        else:
            show_response_message(response)
        if st.button('Deletar'):
            response = requests.delete(f'http://backend:8000/gastos/{delete_id}')
            show_response_message(response)

with tab5:
    st.header('Listar Gastos Variáveis')
    if st.button("Mostrar"):
        response = requests.get(f'http://backend:8000/gastos/')
        if response.status_code == 200:
            gastos = response.json()
            df = pd.DataFrame(gastos)
            st.dataframe(df, hide_index=True)
        else:
            show_response_message(response)