import json
import pandas as pd
import requests
import streamlit as st
from utils.myfunc import show_data_output, show_response_message
from utils.mystr import apto_input, empty_none_dict

# Seria ótimo que quando fosse registrar a foreign key (ID Proprietário) mostrasse o nome conforme o registro em sua tabela

st.set_page_config(page_title="Apartamentos", layout="wide")
st.title("Apartamentos")

tab1, tab2, tab3, tab4, tab5 = st.tabs(
    ["Registrar", "Consultar", "Modificar", "Deletar", "Listar"]
)

with tab1:
    st.header("Registrar Apartamento")
    st.markdown(
        '<p style="font-size: 12px;">Campos com * são obrigatórios</p>',
        unsafe_allow_html=True,
    )
    id = st.text_input(label="Apartamento *", value=None, key=2100)
    proprietario_id = st.number_input(
        label="ID Proprietário *",
        min_value=1,
        value=None,
        format="%d",
        step=1,
        key=2101,
    )
    cod_celesc = st.text_input(label="Unidade Consumidora Celesc", value=None, key=2102)
    cod_gas = st.text_input(label="Código Supergasbras", value=None, key=2103)
    prov_net = st.text_input(label="Provedor de Internet", value=None, key=2104)
    wifi = st.text_input(label="Nome da Rede WiFi", value=None, key=2105)
    wifi_senha = st.text_input(label="Senha da Rede Wifi", value=None, key=2106)
    lock_senha = st.text_input(label="Senha da Fechadura", value=None, key=2107)
    if st.button("Registrar", key=2108):
        apto_data = empty_none_dict(
            {
                "id": apto_input(id),
                "proprietario_id": proprietario_id,
                "cod_celesc": cod_celesc,
                "cod_gas": cod_gas,
                "prov_net": prov_net,
                "wifi": wifi,
                "wifi_senha": wifi_senha,
                "lock_senha": lock_senha,
            }
        )
        submit_data = json.dumps(obj=apto_data, separators=(",", ":"))
        try:
            post_response = requests.post("http://api:8000/apartamentos/", submit_data)
            show_response_message(post_response)
            if post_response.status_code == 200:
                st.subheader("Dados inseridos, tudo OK:")
            else:
                st.subheader("Dados NÃO inseridos, favor revisar:")
            show_data_output(apto_data)
        except Exception as e:
            raise (e)

with tab2:
    st.header("Consultar Apartamentos")
    get_id = st.text_input("ID Apartamento", value=None, key=2200)
    get_id = apto_input(get_id)
    if get_id:
        get_response = requests.get(f"http://api:8000/apartamentos/{get_id}")
        if get_response.status_code == 200:
            apto = get_response.json()
            df_get = pd.DataFrame([apto])
            st.dataframe(df_get.set_index("id"))
        else:
            show_response_message(get_response)

with tab3:
    st.header("Modificar Apartamento")
    st.markdown(
        '<p style="font-size: 12px;">Campos com * são obrigatórios</p>',
        unsafe_allow_html=True,
    )
    update_id = st.text_input("ID do Apartamento", value=None, key=2300)
    update_id = apto_input(update_id)
    if update_id:
        update_response = requests.get(f"http://api:8000/apartamentos/{update_id}")
        if update_response.status_code == 200:
            apto_up = update_response.json()
            df_up = pd.DataFrame([apto_up])
            st.dataframe(df_up.set_index("id"))
            id = st.text_input(label="Apartamento *", value=str(df_up.id[0]), key=2301)
            proprietario_id = st.number_input(
                label="ID Proprietário *",
                min_value=1,
                format="%d",
                step=1,
                value=df_up.loc[0, "proprietario_id"],
                key=2302,
            )
            cod_celesc = st.text_input(
                label="Unidade Consumidora Celesc",
                value=str(df_up.cod_celesc[0]),
                key=2304,
            )
            cod_gas = st.text_input(
                label="Código Supergasbras", value=str(df_up.cod_gas[0]), key=2305
            )
            prov_net = st.text_input(
                label="Provedor de Internet", value=str(df_up.prov_net[0]), key=2306
            )
            wifi = st.text_input(
                label="Nome da Rede WiFi", value=str(df_up.wifi[0]), key=2307
            )
            wifi_senha = st.text_input(
                label="Senha da Rede Wifi", value=str(df_up.wifi_senha[0]), key=2308
            )
            lock_senha = st.text_input(
                label="Senha da Fechadura", value=str(df_up.lock_senha[0]), key=2309
            )
            if st.button("Modificar", key=2310):
                apto_up_data = empty_none_dict(
                    {
                        "id": apto_input(id),
                        "proprietario_id": proprietario_id,
                        "cod_celesc": cod_celesc,
                        "cod_gas": cod_gas,
                        "prov_net": prov_net,
                        "wifi": wifi,
                        "wifi_senha": wifi_senha,
                        "lock_senha": lock_senha,
                    }
                )
                update_data = json.dumps(obj=apto_up_data, separators=(",", ":"))
                try:
                    put_response = requests.put(
                        f"http://api:8000/apartamentos/{update_id}", update_data
                    )
                    show_response_message(put_response)
                    if put_response.status_code == 200:
                        st.subheader("Dados inseridos, tudo OK:")
                    else:
                        st.subheader("Dados NÃO inseridos, favor revisar:")
                    show_data_output(apto_up_data)
                except Exception as e:
                    raise (e)
        else:
            show_response_message(update_response)

with tab4:
    st.header("Deletar Apartamento")
    delete_id = st.text_input(label="ID Apartamento", value=None, key=2400)
    delete_id = apto_input(delete_id)
    if delete_id:
        show_delete_response = requests.get(f"http://api:8000/apartamentos/{delete_id}")
        if show_delete_response.status_code == 200:
            apto_delete = show_delete_response.json()
            df_delete = pd.DataFrame([apto_delete])
            st.dataframe(df_delete.set_index("id"))
            delete_confirm = st.checkbox("Confirma que deseja deletar o registro?")
            delete_button = st.button("Deletar", key=1401)
            if delete_button and delete_confirm:
                delete_response = requests.delete(
                    f"http://api:8000/apartamentos/{delete_id}"
                )
                show_response_message(delete_response)
            elif delete_button and not delete_confirm:
                st.warning("Você deve confirmar primeiro para deletar o registro")
        else:
            show_response_message(show_delete_response)

with tab5:
    st.header("Listar Apartamentos")
    if st.button("Mostrar", key=2007):
        get_list_response = requests.get(f"http://api:8000/apartamentos/")
        if get_list_response.status_code == 200:
            apartamentos = get_list_response.json()
            if apartamentos:
                df_list = pd.DataFrame(apartamentos)
                st.dataframe(df_list.set_index("id"))
            else:
                st.warning("Não há apartamentos para listar")
        else:
            show_response_message(get_list_response)
