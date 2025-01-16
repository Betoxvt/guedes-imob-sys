from datetime import date
import json
import pandas as pd
import requests
import streamlit as st
from src.fdate import str_to_date
from src.functions import empty_none_dict, show_data_output, show_response_message

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
        key=3100
        )
        data_pagamento: date = st.date_input(
        label='Data de pagamento',
        format='DD/MM/YYYY',
        key=3102,
        value=date.today()
        )
        valor: float = st.number_input(
        label='Valor da despesa',
        min_value=0.00,
        max_value=None,
        value=0.00,
        format='%0.2f',
        step=0.01,
        key=3103
        )
        descricao: str = st.text_area(
            label='Descrição',
            value=None,
            key=3104
        )

        submit_button = st.form_submit_button('Registrar')
        if submit_button:
            despesa_data = empty_none_dict({
                "apto_id": apto_id,
                "data_pagamento": data_pagamento.isoformat(),
                "valor": valor,
                "descricao": descricao,
            })
            submit_data = json.dumps(obj=despesa_data, separators=(',',':'))
            try:
                post_response = requests.post("http://backend:8000/despesas/", submit_data)
                show_response_message(post_response)
                st.subheader('Dados inseridos:')
                show_data_output(despesa_data)
            except Exception as e:
                show_response_message(post_response)
                st.subheader('Dados NÃO inseridos:')
                show_data_output(despesa_data)
                print(e)

with tab2:
    st.header('Consultar Despesas')
    get_id = st.number_input(
        'ID Despesa',
        min_value=1,
        format='%d',
        step=1,
        key=3200
    )
    if get_id:
        get_response = requests.get(f'http://backend:8000/despesas/{get_id}')
        if get_response.status_code == 200:
            despesa = get_response.json()
            df_get = pd.DataFrame([despesa])
            st.dataframe(df_get, hide_index=True)
        else:
            show_response_message(get_response)

with tab3:
    st.header('Modificar Despesa')
    update_id = st.number_input(
        'ID do Despesa',
        min_value=1,
        format='%d',
        key=3300
    )
    if update_id:
        update_response = requests.get(f'http://backend:8000/despesas/{update_id}')
        if update_response.status_code == 200:
            despesa_up = update_response.json()
            df_up = pd.DataFrame([despesa_up])
            st.dataframe(df_up, hide_index=True)
            with st.form('update_despesa'):
                apto_id: int = st.number_input(
                    label='ID Apartamento',
                    min_value=1,
                    format='%d',
                    step=1,
                    key=3301,
                    value=df_up.loc[0, 'apto_id']
                )
                data_pagamento: date = st.date_input(
                    label='Data de pagamento',
                    value=str_to_date(df_up.data_pagamento[0]),
                    format='DD/MM/YYYY',
                    key=3302
                )
                valor: float = st.number_input(
                    label='Valor da despesa',
                    min_value=0.00,
                    max_value=None,
                    value=df_up.loc[0, 'valor'],
                    format='%0.2f',
                    step=0.01,
                    key=3303
                )
                descricao: str = st.text_area(
                    label='Descrição',
                    value=str(df_up.descricao[0]),
                    key=3304
                )
                update_button = st.form_submit_button('Modificar')
                if update_button:
                    despesa_up_data = empty_none_dict({
                        "apto_id": apto_id,
                        "data_pagamento": data_pagamento.isoformat(),
                        "valor": valor,
                        "descricao": descricao,
                    })
                    update_data = json.dumps(obj=despesa_up_data, separators=(',',':'))
                    try:
                        put_response = requests.put(f"http://backend:8000/despesas/{update_id}", update_data)
                        show_response_message(put_response)
                        st.subheader('Dados inseridos:')
                        show_data_output(update_data)
                    except Exception as e:
                        show_response_message(despesa_up_data)
                        st.subheader('Dados NÃO inseridos:')
                        show_data_output(despesa_up_data)
                        print(e) 
        else:
            show_response_message(update_response)

with tab4:
    st.header('Deletar Despesa')
    delete_id = st.number_input(
        label="ID Despesa",
        min_value=1,
        format='%d',
        key=3400
    )
    if delete_id:
        show_delete_response = requests.get(f'http://backend:8000/despesas/{delete_id}')
        if show_delete_response.status_code == 200:
            despesa_delete = show_delete_response.json()
            df_delete = pd.DataFrame([despesa_delete])
            st.dataframe(df_delete, hide_index=True)
        else:
            show_response_message(show_delete_response)
        if st.button(
            'Deletar',
            key=3401
        ):
            delete_response = requests.delete(f'http://backend:8000/despesas/{delete_id}')
            show_response_message(delete_response)

with tab5:
    st.header('Listar Despesas')
    if st.button(
        "Mostrar",
        key=3500
    ):
        get_list_response = requests.get(f'http://backend:8000/despesas/')
        if get_list_response.status_code == 200:
            despesas = get_list_response.json()
            df_list = pd.DataFrame(despesas)
            st.dataframe(df_list, hide_index=True)
        else:
            show_response_message(get_list_response)