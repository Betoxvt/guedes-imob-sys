from datetime import date, timedelta
import json
import pandas as pd
import requests
import streamlit as st
from src.functions import show_response_message, string_to_date

st.set_page_config(
    page_title='Despesas',
    layout='wide'
)
st.title('Despesas')

tab1, tab2, tab3, tab4, tab5 = st.tabs(['Registrar', 'Consultar', 'Modificar', 'Deletar', 'Listar'])

with tab1:
    st.header('Registrar Despesa')
    with st.form('new_despesa'):
        apto_id: int = st.number_input(
        label='ID Apartamento',
        min_value=1,
        format='%d',
        step=1,
        key=3009
        )
        data_pagamento: date = st.date_input(
        label='Data de pagamento',
        min_value=date(2024, 1, 1),
        max_value=date.today() + timedelta(days=360),
        value=date.today(),
        format='DD/MM/YYYY',
        key=3011
        )
        valor: float = st.number_input(
        label='Valor da despesa',
        min_value=0.00,
        max_value=None,
        value=0.00,
        format='%0.2f',
        step=0.01,
        key=3014
        )
        descricao: str = st.text_area(
            label='Descrição',
            value=None,
            key=3015,
            placeholder='Obrigatório'
        )

        submit_button = st.form_submit_button('Registrar')
        if submit_button:
            registry = {
                "apto_id": apto_id,
                "data_pagamento": data_pagamento.isoformat(),
                "valor": valor,
                "descricao": descricao,
            }
            registry_json = json.dumps(obj=registry, indent=1, separators=(',',':'))
            response = requests.post("http://backend:8000/despesas/", registry_json)
            show_response_message(response)

with tab2:
    st.header('Consultar Despesas')
    get_id = st.number_input(
        'ID Despesa',
        min_value=1,
        format='%d',
        step=1,
        key=3000
    )
    if get_id:
        response = requests.get(f'http://backend:8000/despesas/{get_id}')
        if response.status_code == 200:
            despesa = response.json()
            df = pd.DataFrame([despesa])
            st.dataframe(df, hide_index=True)
        else:
            show_response_message(response)

with tab3:
    st.header('Modificar Despesa')
    update_id = st.number_input(
        'ID do Despesa',
        min_value=1,
        format='%d',
        key=3001
    )
    if update_id:
        response = requests.get(f'http://backend:8000/despesas/{update_id}')
        if response.status_code == 200:
            despesa_viz = response.json()
            df = pd.DataFrame([despesa_viz])
            st.dataframe(df, hide_index=True)
            with st.form('update_despesa'):
                apto_id: int = st.number_input(
                    label='ID Apartamento',
                    min_value=1,
                    format='%d',
                    step=1,
                    key=3309,
                    value=df.loc[0, 'apto_id']
                )
                data_pagamento: date = st.date_input(
                    label='Data de pagamento',
                    min_value=date(2024, 1, 1),
                    max_value=date.today() + timedelta(days=360),
                    value=string_to_date(df.data_pagamento[0]),
                    format='DD/MM/YYYY',
                    key=3311
                )
                valor: float = st.number_input(
                    label='Valor da despesa',
                    min_value=0.00,
                    max_value=None,
                    value=df.loc[0, 'valor'],
                    format='%0.2f',
                    step=0.01,
                    key=3314
                )
                descricao: str = st.text_area(
                    label='Descrição',
                    value=str(df.descricao[0]),
                    key=3315,
                    placeholder='Obrigatório'
                )
                update_button = st.form_submit_button('Modificar')
                if update_button:
                    updated = {
                        "apto_id": apto_id,
                        "data_pagamento": data_pagamento.isoformat(),
                        "valor": valor,
                        "descricao": descricao,
                    }
                    updated_json = json.dumps(obj=updated, indent=1, separators=(',',':'))
                    response = requests.put(f"http://backend:8000/despesas/{update_id}", updated_json)
                    show_response_message(response)
        else:
            show_response_message(response)

with tab4:
    st.header('Deletar Despesa')
    delete_id = st.number_input(
        label="ID Despesa",
        min_value=1,
        format='%d',
        key=3002
    )
    if delete_id:
        response = requests.get(f'http://backend:8000/despesas/{delete_id}')
        if response.status_code == 200:
            despesa_viz = response.json()
            df = pd.DataFrame([despesa_viz])
            st.dataframe(df, hide_index=True)
        else:
            show_response_message(response)
        if st.button(
            'Deletar',
            key=3006
        ):
            response = requests.delete(f'http://backend:8000/despesas/{delete_id}')
            show_response_message(response)

with tab5:
    st.header('Listar Despesas')
    if st.button(
        "Mostrar",
        key=3007
    ):
        response = requests.get(f'http://backend:8000/despesas/')
        if response.status_code == 200:
            despesas = response.json()
            df = pd.DataFrame(despesas)
            st.dataframe(df, hide_index=True)
        else:
            show_response_message(response)