from datetime import date
import json
import pandas as pd
import requests
import streamlit as st
from utils.mydate import str_to_date
from utils.myfunc import cat_index, show_data_output, show_response_message
from utils.mystr import empty_none_dict

st.set_page_config(
    page_title='Despesas',
    layout='wide'
)
st.title('Despesas')

tab1, tab2, tab3, tab4, tab5 = st.tabs(['Registrar', 'Consultar', 'Modificar', 'Deletar', 'Listar'])

with tab1:
    st.header('Registrar Despesa')
    apto_id: int = st.number_input(
    label='ID Apartamento',
    min_value=1,
    value=None,
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
    value=None,
    format='%0.2f',
    step=0.01,
    key=3103
    )
    categoria: str = st.selectbox(
        label='Categoria',
        options=['IPTU', 'CONDOMÍNIO', 'LUZ', 'GÁS', 'INTERNET', 'MANUTENÇÃO', 'OUTROS'],
        key=3104
    )
    descricao: str = st.text_area(
        label='Descrição',
        value=None,
        key=3105
    )
    if st.button('Registrar', key=3106):
        despesa_data = empty_none_dict({
            "apto_id": apto_id,
            "data_pagamento": data_pagamento.isoformat(),
            "valor": valor,
            "categoria": categoria,
            "descricao": descricao
        })
        submit_data = json.dumps(obj=despesa_data, separators=(',',':'))
        try:
            post_response = requests.post("http://api:8000/despesas/", submit_data)
            show_response_message(post_response)
            if post_response.status_code == 200:
                st.subheader('Dados inseridos, tudo OK:')
            else:
                st.subheader('Dados NÃO inseridos, favor revisar:')
            show_data_output(despesa_data)
        except Exception as e:
            raise(e)

with tab2:
    st.header('Consultar Despesas')
    get_id = st.number_input(
        'ID Despesa',
        min_value=1,
        value=None,
        format='%d',
        step=1,
        key=3200
    )
    if get_id:
        get_response = requests.get(f'http://api:8000/despesas/{get_id}')
        if get_response.status_code == 200:
            despesa = get_response.json()
            df_get = pd.DataFrame([despesa])
            st.dataframe(df_get.set_index('id'))
        else:
            show_response_message(get_response)

with tab3:
    categorias = ['IPTU', 'CONDOMÍNIO', 'LUZ', 'GÁS', 'INTERNET', 'MANUTENÇÃO', 'OUTROS']
    st.header('Modificar Despesa')
    update_id = st.number_input(
        'ID do Despesa',
        min_value=1,
        value=None,
        format='%d',
        key=3300
    )
    if update_id:
        update_response = requests.get(f'http://api:8000/despesas/{update_id}')
        if update_response.status_code == 200:
            despesa_up = update_response.json()
            df_up = pd.DataFrame([despesa_up])
            st.dataframe(df_up.set_index('id'))
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
            categoria: str = st.selectbox(
                label='Categoria',
                options=['IPTU', 'CONDOMÍNIO', 'LUZ', 'GÁS', 'INTERNET', 'MANUTENÇÃO', 'OUTROS'],
                index=cat_index(df_up, 'categoria', categorias),
                key=3304
            )
            descricao: str = st.text_area(
                label='Descrição',
                value=str(df_up.descricao[0]),
                key=3305
            )
            if st.button('Modificar', key=3306):
                despesa_up_data = empty_none_dict({
                    "apto_id": apto_id,
                    "data_pagamento": data_pagamento.isoformat(),
                    "valor": valor,
                    "descricao": descricao,
                })
                update_data = json.dumps(obj=despesa_up_data, separators=(',',':'))
                try:
                    put_response = requests.put(f"http://api:8000/despesas/{update_id}", update_data)
                    show_response_message(put_response)
                    if put_response.status_code == 200:
                        st.subheader('Dados inseridos, tudo OK:')
                    else:
                        st.subheader('Dados NÃO inseridos, favor revisar:')
                    show_data_output(despesa_up_data)
                except Exception as e:
                    raise(e) 
        else:
            show_response_message(update_response)

with tab4:
    st.header('Deletar Despesa')
    delete_id = st.number_input(
        label="ID Despesa",
        min_value=1,
        value=None,
        format='%d',
        key=3400
    )
    if delete_id:
        show_delete_response = requests.get(f'http://api:8000/despesas/{delete_id}')
        if show_delete_response.status_code == 200:
            despesa_delete = show_delete_response.json()
            df_delete = pd.DataFrame([despesa_delete])
            st.dataframe(df_delete.set_index('id'))
        else:
            show_response_message(show_delete_response)
        if st.button(
            'Deletar',
            key=3401
        ):
            delete_response = requests.delete(f'http://api:8000/despesas/{delete_id}')
            show_response_message(delete_response)

with tab5:
    st.header('Listar Despesas')
    if st.button(
        "Mostrar",
        key=3500
    ):
        get_list_response = requests.get(f'http://api:8000/despesas/')
        if get_list_response.status_code == 200:
            despesas = get_list_response.json()
            if despesas:
                df_list = pd.DataFrame(despesas)
                st.dataframe(df_list.set_index('id'))
            else:
                st.warning('Não há despesas para listar')
        else:
            show_response_message(get_list_response)