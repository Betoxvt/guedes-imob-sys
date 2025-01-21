from datetime import date
import json
import pandas as pd
import requests
import streamlit as st
from utils.mydate import calculate_diarias, str_to_date
from utils.myfunc import show_data_output, show_response_message
from utils.mynum import calculate_saldo, calculate_valortotal
from utils.mystr import empty_none_dict

st.set_page_config(
    page_title='Garagens',
    layout='wide'
)
st.title('Garagens')

tab1, tab2, tab3, tab4, tab5 = st.tabs(['Registrar', 'Consultar', 'Modificar', 'Deletar', 'Listar'])

with tab1:
    st.header('Registrar Garagem')
    st.markdown('<p style="font-size: 12px;">Campos com * são obrigatórios</p>', unsafe_allow_html=True)
    apto_origem_id: int = st.number_input(
        label='ID Apartamento de origem *',
        min_value=1,
        value=None,
        format='%d',
        step=1,
        key=4100
    )
    apto_destino_id: int = st.number_input(
        label='ID Apartamento de destino *',
        min_value=1,
        format='%d',
        step=1,
        key=4101
    )
    checkin: date = st.date_input(
        label='Check-in *' ,
        format='DD/MM/YYYY',
        key=4102,
        value=None
    )
    checkout: date = st.date_input(
        label='Check-out *',
        format='DD/MM/YYYY',
        key=4103,
        value=None
    )
    diarias: int = calculate_diarias(checkin, checkout)
    st.write(f'Diárias: {diarias}')
    valor_diaria: float = st.number_input(
        label='Valor da diária *',
        min_value=0.00,
        max_value=900.00,
        value=None,
        format='%0.2f',
        step=10.00,
        key=4105
    )
    valor_total: float = calculate_valortotal(diarias, valor_diaria)
    valor_depositado: float = st.number_input(
        label='Valor Depositado',
        min_value=0.00,
        max_value=9000.00,
        value=None,
        format='%0.2f',
        step=10.00,
        key=4106
    )
    saldo = calculate_saldo(valor_total, valor_depositado)
    if st.button('Registrar', key=4107):
        garagem_data = empty_none_dict({
            "apto_origem_id": apto_origem_id,
            "apto_destino_id": apto_destino_id,
            "checkin": checkin.isoformat(),
            "checkout": checkout.isoformat(),
            "diarias": diarias,
            "valor_diaria": valor_diaria,
            "valor_total": valor_total,
            "valor_depositado": valor_depositado
        })
        submit_data = json.dumps(obj=garagem_data, separators=(',',':'))
        try:
            post_response = requests.post("http://api:8000/garagens/", submit_data)
            show_response_message(post_response)
            if post_response.status_code == 200:
                st.subheader('Dados inseridos, tudo OK:')
            else:
                st.subheader('Dados NÃO inseridos, favor revisar:')
            show_data_output(garagem_data)
        except Exception as e:
            raise(e)

with tab2:
    st.header('Consultar Garagens')
    get_id = st.number_input(
        'ID Garagem',
        min_value=1,
        value=None,
        format='%d',
        step=1,
        key=4200
    )
    if get_id:
        get_response = requests.get(f'http://api:8000/garagens/{get_id}')
        if get_response.status_code == 200:
            garagem = get_response.json()
            df_get = pd.DataFrame([garagem])
            st.dataframe(df_get.set_index('id'))
        else:
            show_response_message(get_response)

with tab3:
    st.header('Modificar Garagem')
    st.markdown('<p style="font-size: 12px;">Campos com * são obrigatórios</p>', unsafe_allow_html=True)
    update_id = st.number_input(
        'ID do Garagem',
        min_value=1,
        value=None,
        format='%d',
        step=1,
        key=4300
    )
    if update_id:
        update_response = requests.get(f'http://api:8000/garagens/{update_id}')
        if update_response.status_code == 200:
            garagem_up = update_response.json()
            df_up = pd.DataFrame([garagem_up])
            st.dataframe(df_up.set_index('id'))
            apto_origem_id: int = st.number_input(
                label='ID Apartamento de origem *',
                min_value=1,
                format='%d',
                step=1,
                key=4301,
                value=df_up.loc[0, 'apto_origem_id']
            )
            apto_destino_id: int = st.number_input(
                label='ID Apartamento de destino *',
                min_value=1,
                format='%d',
                step=1,
                key=4302,
                value=df_up.loc[0, 'apto_destino_id']
            )
            checkin: date = st.date_input(
                label='Check-in *',
                value=str_to_date(df_up.checkin[0]),
                format='DD/MM/YYYY',
                key=4303
            )
            checkout: date = st.date_input(
                label='Check-out *',
                value=str_to_date(df_up.checkout[0]),
                format='DD/MM/YYYY',
                key=4304
            )
            diarias: int = calculate_diarias(checkin, checkout)
            st.write(f'Diárias: {diarias}')
            valor_diaria: float = st.number_input(
                label='Valor da diária *',
                min_value=0.00,
                max_value=3000.00,
                value=df_up.loc[0, 'valor_diaria'],
                format='%0.2f',
                step=10.00,
                key=4306
            )
            valor_total: float = calculate_valortotal(diarias, valor_diaria)
            valor_depositado: float = st.number_input(
                label='Valor Depositado',
                min_value=0.00,
                max_value=9000.00,
                value=df_up.loc[0, valor_depositado],
                format='%0.2f',
                step=10.00,
                key=4307
            )
            saldo = calculate_saldo(valor_total, valor_depositado)
            if st.button('Modificar', key=4308):
                garagem_up_data = {
                    "apto_origem_id": apto_origem_id,
                    "apto_destino_id": apto_destino_id,
                    "checkin": checkin.isoformat(),
                    "checkout": checkout.isoformat(),
                    "diarias": diarias,
                    "valor_diaria": valor_diaria,
                    "valor_total": valor_total,
                    "valor_depositado": valor_depositado
                }
                update_data = json.dumps(obj=garagem_up_data, separators=(',',':'))
                try:
                    put_response = requests.put(f"http://api:8000/garagens/{update_id}", update_data)
                    show_response_message(put_response)
                    if put_response.status_code == 200:
                        st.subheader('Dados inseridos, tudo OK:')
                    else:
                        st.subheader('Dados NÃO inseridos, favor revisar:')
                    show_data_output(garagem_up_data)
                except Exception as e:
                    raise(e) 
        else:
            show_response_message(update_response)

with tab4:
    st.header('Deletar Garagem')
    delete_id = st.number_input(
        label="ID Garagem",
        min_value=1,
        value=None,
        format='%d',
        key=4400
    )
    if delete_id:
        show_delete_response = requests.get(f'http://api:8000/garagens/{delete_id}')
        if show_delete_response.status_code == 200:
            garagem_delete = show_delete_response.json()
            df_delete = pd.DataFrame([garagem_delete])
            st.dataframe(df_delete.set_index('id'))
        else:
            show_response_message(show_delete_response)
        if st.button(
            'Deletar',
            key=4401
        ):
            delete_response = requests.delete(f'http://api:8000/garagens/{delete_id}')
            show_response_message(delete_response)

with tab5:
    st.header('Listar Garagens')
    if st.button(
        "Mostrar",
        key=4500
    ):
        get_list_response = requests.get(f'http://api:8000/garagens/')
        if get_list_response.status_code == 200:
            garagens = get_list_response.json()
            if garagens:
                df_list = pd.DataFrame(garagens)
                st.dataframe(df_list.set_index('id'))
            else:
                st.warning('Não há garagens para listar')
        else:
            show_response_message(get_list_response)