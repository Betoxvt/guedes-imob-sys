import json
import pandas as pd
import requests
import streamlit as st
from src.functions import show_response_message

st.set_page_config(
    page_title='Despesas Recorrentes',
    layout='wide'
)
st.title('Despesas Recorrentes')

tab1, tab2, tab3, tab4, tab5 = st.tabs(['Registrar', 'Consultar', 'Modificar', 'Deletar', 'Listar'])

with tab1:
    st.header('Registrar Despesa Recorrente')
    with st.form('new_despesa'):
        inputs = '...'


        submit_button = st.form_submit_button('Registrar')
        if submit_button:
            registry = {
                "inputs": inputs
            }
            registry_json = json.dumps(obj=registry, indent=1, separators=(',',':'))
            response = requests.post("http://backend:8000/despesas/", registry_json)
            show_response_message(response)

with tab2:
    st.header('Consultar Despesa Recorrente')
    get_id = st.number_input(
        'ID Despesa Recorrente',
        min_value=1,
        format='%d',
        key=3000
    )
    if st.button('Consultar'):
        response = requests.get(f'http://backend:8000/despesas/{get_id}')
        if response.status_code == 200:
            despesa = response.json()
            df = pd.DataFrame([despesa])
            st.dataframe(df, hide_index=True)
        else:
            show_response_message(response)

with tab3:
    st.header('Modificar Despesa Recorrente')
    update_id = st.number_input(
        'ID Despesa Recorrente',
        min_value=1,
        format='%d',
        key=3001
    )
    show_button = st.button('Mostrar')
    if show_button:
        response = requests.get(f'http://backend:8000/despesas/{update_id}')
        if response.status_code == 200:
            despesa_viz = response.json()
            df = pd.DataFrame([despesa_viz])
            st.dataframe(df, hide_index=True)
            with st.form('update_despesa'):
                update_inputs = ' '
                update_button = st.form_submit_button('Modificar')
                if update_button:
                    updated = {
                        "update_inputs": update_inputs
                    }
                    updated_json = json.dumps(obj=updated, indent=1, separators=(',',':'))
                    response = requests.put(f"http://backend:8000/despesas/{update_id}", updated_json)
                    show_response_message(response)
        else:
            show_response_message(response)

with tab4:
    st.header('Deletar Despesa Recorrente')
    delete_id = st.number_input(
        label="ID Despesa Recorrente",
        min_value=1,
        format='%d',
        key=3002
    )
    show_button = st.button('Mostrar')
    if show_button:
        response = requests.get(f'http://backend:8000/despesas/{delete_id}')
        if response.status_code == 200:
            despesa_viz = response.json()
            df = pd.DataFrame([despesa_viz])
            st.dataframe(df, hide_index=True)
        else:
            show_response_message(response)
        if st.button('Deletar'):
            response = requests.delete(f'http://backend:8000/despesas/{delete_id}')
            show_response_message(response)

with tab5:
    st.header('Listar Despesas Recorrentes')
    if st.button("Mostrar"):
        response = requests.get(f'http://backend:8000/despesas/')
        if response.status_code == 200:
            despesas = response.json()
            df = pd.DataFrame(despesas)
            st.dataframe(df, hide_index=True)
        else:
            show_response_message(response)