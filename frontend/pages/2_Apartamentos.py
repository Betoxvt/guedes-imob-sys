import json
import pandas as pd
import requests
import streamlit as st
from utils.myfunc import show_data_output, show_response_message
from utils.mystr import empty_none_dict

# Seria ótimo que quando fosse registrar a foreign key (ID Proprietário) mostrasse o nome conforme o registro em sua tabela

st.set_page_config(
    page_title='Apartamentos',
    layout='wide'
)
st.title('Apartamentos')

tab1, tab2, tab3, tab4, tab5 = st.tabs(['Registrar', 'Consultar', 'Modificar', 'Deletar', 'Listar'])

with tab1:
    st.header('Registrar Apartamento')
    with st.form('new_apartamento'):
        apto = st.text_input(
            label='Apartamento',
            value=None,
            key=2100
        )
        proprietario_id = st.number_input(
            label='ID Proprietário',
            min_value=1,
            format='%d',
            step=1,
            key=2101
        )
        cod_celesc = st.text_input(
            label='Unidade Consumidora Celesc',
            value=None,
            key=2102
        )
        cod_gas = st.text_input(
            label='Código Supergasbras',
            value=None,
            key=2103
        )
        prov_net = st.text_input(
            label='Provedor de Internet',
            value=None,
            key=2104
        )
        wifi = st.text_input(
            label='Nome da Rede WiFi',
            value=None,
            key=2105
        )
        wifi_senha = st.text_input(
            label='Senha da Rede Wifi',
            value=None,
            key=2106
        )
        lock_senha = st.text_input(
            label='Senha da Fechadura',
            value=None,
            key=2107
        )

        submit_button = st.form_submit_button('Registrar')
        if submit_button:
            apto_data = empty_none_dict({
                "apto": apto,
                "proprietario_id": proprietario_id,
                "cod_celesc": cod_celesc,
                "cod_gas": cod_gas,
                "prov_net": prov_net,
                "wifi": wifi,
                "wifi_senha": wifi_senha,
                "lock_senha": lock_senha
            })
            submit_data = json.dumps(obj=apto_data, separators=(',',':'))
            try:
                post_response = requests.post("http://backend:8000/apartamentos/", submit_data)
                show_response_message(post_response)
                st.subheader('Dados inseridos:')
                show_data_output(apto_data)
            except Exception as e:
                show_response_message(post_response)
                st.subheader('Dados NÃO inseridos:')
                show_data_output(apto_data)
                print(e)

with tab2:
    st.header('Consultar Apartamentos')
    get_id = st.number_input(
        'ID Apartamento',
        min_value=1,
        format='%d',
        step=1,
        key=2200
    )
    if get_id:
        get_response = requests.get(f'http://backend:8000/apartamentos/{get_id}')
        if get_response.status_code == 200:
            apto = get_response.json()
            df_get = pd.DataFrame([apto])
            st.dataframe(df_get.set_index('id'))
        else:
            show_response_message(get_response)

with tab3:
    st.header('Modificar Apartamento')
    update_id = st.number_input(
        'ID do Apartamento',
        min_value=1,
        format='%d',
        step=1,
        key=2300
    )
    if update_id:
        update_response = requests.get(f'http://backend:8000/apartamentos/{update_id}')
        if update_response.status_code == 200:
            apto_up = update_response.json()
            df_up = pd.DataFrame([apto_up])
            st.dataframe(df_up.set_index('id'))
            with st.form('update_apartamento'):
                apto = st.text_input(
                    label='Apartamento',
                    value=str(df_up.apto[0]),
                    key=2301
                )
                proprietario_id = st.number_input(
                    label='ID Proprietário',
                    min_value=1,
                    format='%d',
                    step=1,
                    value=df_up.loc[0, 'proprietario_id'],
                    key=2302
                )
                cod_celesc = st.text_input(
                    label='Unidade Consumidora Celesc',
                    value=str(df_up.cod_celesc[0]),
                    key=2304
                )
                cod_gas = st.text_input(
                    label='Código Supergasbras',
                    value=str(df_up.cod_gas[0]),
                    key=2305
                )
                prov_net = st.text_input(
                    label='Provedor de Internet',
                    value=str(df_up.prov_net[0]),
                    key=2306
                )
                wifi = st.text_input(
                    label='Nome da Rede WiFi',
                    value=str(df_up.wifi[0]),
                    key=2307
                )
                wifi_senha = st.text_input(
                    label='Senha da Rede Wifi',
                    value=str(df_up.wifi_senha[0]),
                    key=2308
                )
                lock_senha = st.text_input(
                    label='Senha da Fechadura',
                    value=str(df_up.lock_senha[0]),
                    key=2309
                )
                update_button = st.form_submit_button('Modificar')
                if update_button:
                    apto_up_data = empty_none_dict({
                        "apto": apto,
                        "proprietario_id": proprietario_id,
                        "cod_celesc": cod_celesc,
                        "cod_gas": cod_gas,
                        "prov_net": prov_net,
                        "wifi": wifi,
                        "wifi_senha": wifi_senha,
                        "lock_senha": lock_senha
                    })
                    update_data = json.dumps(obj=apto_up_data, separators=(',',':'))
                    try:
                        put_response = requests.put(f"http://backend:8000/apartamentos/{update_id}", update_data)
                        show_response_message(put_response)
                        st.subheader('Dados inseridos:')
                        show_data_output(apto_up_data)
                    except Exception as e:
                        show_response_message(put_response)
                        st.subheader('Dados NÃO inseridos:')
                        show_data_output(apto_up_data)
                        print(e) 
        else:
            show_response_message(update_response)

with tab4:
    st.header('Deletar Apartamento')
    delete_id = st.number_input(
        label="ID Apartamento",
        min_value=1,
        format='%d',
        step=1,
        key=2400
    )
    if delete_id:
        show_delete_response = requests.get(f'http://backend:8000/apartamentos/{delete_id}')
        if show_delete_response.status_code == 200:
            apto_delete = show_delete_response.json()
            df_delete = pd.DataFrame([apto_delete])
            st.dataframe(df_delete.set_index('id'))
        else:
            show_response_message(show_delete_response)
        if st.button(
            'Deletar',
            key=2401
        ):
            delete_response = requests.delete(f'http://backend:8000/apartamentos/{delete_id}')
            show_response_message(delete_response)

with tab5:
    st.header('Listar Apartamentos')
    if st.button(
        "Mostrar",
        key=2007
    ):
        get_list_response = requests.get(f'http://backend:8000/apartamentos/')
        if get_list_response.status_code == 200:
            apartamentos = get_list_response.json()
            df_list = pd.DataFrame(apartamentos)
            st.dataframe(df_list.set_index('id'))
        else:
            show_response_message(get_list_response)