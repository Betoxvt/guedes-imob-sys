import json
import pandas as pd
import requests
import streamlit as st
from src.functions import show_response_message

st.set_page_config(
    page_title='Aluguéis',
    layout='wide'
)
st.title('Aluguéis')

tab1, tab2, tab3, tab4, tab5 = st.tabs(['Registrar', 'Consultar', 'Modificar', 'Deletar', 'Listar'])

with tab1:
    st.header('Registrar Aluguel')
    with st.form('new_aluguel'):
        apartamento_id: int = st.number_input(
            label='ID Apartamento',
            min_value=1,
            step=1,
            key=1008
        )
        inquilino_id: int | None = st.number_input(
            label='ID Ficha',
            min_value=1,
            step=1,
            key=1009
        )
        checkin: str
        checkout: str
        diarias: int
        valor_diaria: int | None = None
        taxa_adm: float
        valor_total: float
        valor_imob: float
        valor_prop: float

        submit_button = st.form_submit_button('Registrar')
        if submit_button:
            registry = {
                "inputs": inputs
            }
            registry_json = json.dumps(obj=registry, indent=1, separators=(',',':'))
            response = requests.post("http://backend:8000/alugueis/", registry_json)
            show_response_message(response)

with tab2:
    st.header('Consultar Aluguéis')
    get_id = st.number_input(
        'ID Aluguel',
        min_value=1,
        format='%d',
        key=1000
    )
    if st.button(
        'Consultar',
        key=1003
    ):
        response = requests.get(f'http://backend:8000/alugueis/{get_id}')
        if response.status_code == 200:
            aluguel = response.json()
            df = pd.DataFrame([aluguel])
            st.dataframe(df, hide_index=True)
        else:
            show_response_message(response)

with tab3:
    st.header('Modificar Aluguel')
    update_id = st.number_input(
        'ID do Aluguel',
        min_value=1,
        format='%d',
        key=1001
    )
    if st.button(
        'Mostrar',
        key=1004
    ):
        response = requests.get(f'http://backend:8000/alugueis/{update_id}')
        if response.status_code == 200:
            aluguel_viz = response.json()
            df = pd.DataFrame([aluguel_viz])
            st.dataframe(df, hide_index=True)
            with st.form('update_aluguel'):
                update_inputs = ' '
                update_button = st.form_submit_button('Modificar')
                if update_button:
                    updated = {
                        "update_inputs": update_inputs
                    }
                    updated_json = json.dumps(obj=updated, indent=1, separators=(',',':'))
                    response = requests.put(f"http://backend:8000/alugueis/{update_id}", updated_json)
                    show_response_message(response)
        else:
            show_response_message(response)

with tab4:
    st.header('Deletar Aluguel')
    delete_id = st.number_input(
        label="ID Aluguel",
        min_value=1,
        format='%d',
        key=1002
    )
    if st.button(
        'Mostrar',
        key=1005
    ):
        response = requests.get(f'http://backend:8000/alugueis/{delete_id}')
        if response.status_code == 200:
            aluguel_viz = response.json()
            df = pd.DataFrame([aluguel_viz])
            st.dataframe(df, hide_index=True)
        else:
            show_response_message(response)
        if st.button(
            'Deletar',
            key=1006
        ):
            response = requests.delete(f'http://backend:8000/alugueis/{delete_id}')
            show_response_message(response)

with tab5:
    st.header('Listar Aluguéis')
    if st.button(
        "Mostrar",
        key=1007
    ):
        response = requests.get(f'http://backend:8000/alugueis/')
        if response.status_code == 200:
            alugueis = response.json()
            df = pd.DataFrame(alugueis)
            st.dataframe(df, hide_index=True)
        else:
            show_response_message(response)