import pandas as pd
import requests
import streamlit as st
from utils.myfunc import cat_index, show_data_output, show_response_message
from utils.urls import CAIXA_URL

st.set_page_config(page_title="Caixa", layout="wide")
st.title("Caixa")

if not st.session_state["authentication_status"]:
    st.info("Por favor faça o login na Home page e tente novamente.")
    st.stop()
else:
    authenticator = st.session_state.authenticator
    st.write(f'Usuário: *{st.session_state["name"]}*')
    authenticator.logout(location="sidebar")

    tab1, tab2, tab3, tab4 = st.tabs(["Registrar", "Consultar", "Modificar", "Deletar"])

    moedas = ["BRL", "USD"]

    with tab1:
        st.header("Registrar Fluxo de Caixa")
        moeda: str = st.selectbox(
            label="Moeda",
            options=moedas,
        )
        valor: float = st.number_input(
            label="Valor",
            format="%.2f",
        )
        if st.button("Registrar"):
            caixa_data = {
                "moeda": moeda,
                "valor": valor,
            }
            try:
                post_response = requests.post(CAIXA_URL, json=caixa_data)
                show_response_message(post_response)
                if post_response.status_code == 200:
                    st.subheader("Dados inseridos, tudo OK:")
                else:
                    st.subheader("Dados NÃO inseridos, favor revisar:")
                show_data_output(caixa_data)
            except Exception as e:
                raise e

    with tab2:
        st.header("Consultar Caixa")
        params = {}

        with st.expander(label="Filtros"):
            start_date = st.date_input(
                label="Data de Início",
                value=None,
                format="DD/MM/YYYY",
            )
            end_date = st.date_input(
                label="Data de Término", value=None, format="DD/MM/YYYY"
            )
            signal = st.selectbox(
                label="Tipo",
                options=["Todos", "Depósitos", "Saques"],
            )
            moeda = st.selectbox(label="Moeda", options=["Todos", "BRL", "USD"])

            params = {
                "start_date": start_date,
                "end_date": end_date,
                "signal": signal,
                "moeda": moeda,
            }

        if st.button("Consultar"):
            get_list_response = requests.get(CAIXA_URL, params=params)
            if get_list_response.status_code == 200:
                lista = get_list_response.json()
                if lista:
                    df_list = pd.DataFrame(lista)

                    st.dataframe(df_list.set_index("id"))
                else:
                    st.warning("Sem dados, verifque os filtros")
            else:
                show_response_message(get_list_response)

    with tab3:
        st.header("Modificar Registro de Caixa")
        update_id = st.number_input(
            "ID do Registro de Caixa", min_value=1, value=None, format="%d"
        )
        if update_id:
            update_response = requests.get(CAIXA_URL + update_id)
            if update_response.status_code == 200:
                caixa_up = update_response.json()
                df_up = pd.DataFrame([caixa_up])
                st.dataframe(df_up.set_index("id"))
                moeda: str = st.selectbox(
                    label="Moeda",
                    options=moedas,
                    index=cat_index(df_up, "moeda", moedas),
                    key="moeda_up",
                )
                valor: float = st.number_input(
                    label="Valor", format="%.2f", value=df_up.loc[0, "valor"]
                )
                if st.button("Modificar"):
                    caixa_up_data = {
                        "moeda": moeda,
                        "valor": valor,
                    }
                    try:
                        put_response = requests.put(
                            f"{CAIXA_URL}{update_id}", json=caixa_up_data
                        )
                        show_response_message(put_response)
                        if put_response.status_code == 200:
                            st.subheader("Dados inseridos, tudo OK:")
                        else:
                            st.subheader("Dados NÃO inseridos, favor revisar:")
                        show_data_output(caixa_up_data)
                    except Exception as e:
                        raise e
            else:
                show_response_message(update_response)

    with tab4:
        st.header("Deletar Registro de Caixa")
        delete_id = st.number_input(
            label="ID Registro", min_value=1, value=None, format="%d"
        )
        if delete_id:
            show_delete_response = requests.get(CAIXA_URL + delete_id)
            if show_delete_response.status_code == 200:
                caixa_delete = show_delete_response.json()
                df_delete = pd.DataFrame([caixa_delete])
                st.dataframe(df_delete.set_index("id"))
                delete_confirm = st.checkbox("Confirma que deseja deletar o registro?")
                delete_button = st.button("Deletar", disabled=(not delete_confirm))
                if delete_button:
                    delete_response = requests.delete(CAIXA_URL + delete_id)
                    show_response_message(delete_response)
            else:
                show_response_message(show_delete_response)
