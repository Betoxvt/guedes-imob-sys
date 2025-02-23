from datetime import date
import pandas as pd
import requests
import streamlit as st
from utils.mydate import str_to_date
from utils.myfunc import cat_index, show_data_output, show_response_message
from utils.mystr import empty_none_dict
from utils.urls import PAG_URL

st.set_page_config(page_title="Pagamentos", layout="wide")
st.title("Pagamentos")

if not st.session_state["authentication_status"]:
    st.info("Por favor faça o login na Home page e tente novamente.")
    st.stop()
else:
    authenticator = st.session_state.authenticator
    st.write(f'Usuário: *{st.session_state["name"]}*')
    authenticator.logout(location="sidebar")

    tab1, tab2, tab3, tab4, tab5 = st.tabs(
        ["Registrar", "Consultar", "Modificar", "Deletar", "Listar"]
    )

    with tab1:
        st.header("Registrar Pagamento")
        st.markdown(
            '<p style="font-size: 12px;">Campos com * são obrigatórios</p>',
            unsafe_allow_html=True,
        )
        tipo: str = st.radio(
            label="Tipo de pagamento *",
            options=["Reserva", "Parcela", "Integral", "Quitação", "Garagem"],
            index=0,
            horizontal=True,
            key=7100,
        )
        valor: float = st.number_input(
            label="Valor *",
            min_value=0.00,
            max_value=90000.00,
            format="%0.2f",
            key=7101,
            value=None,
        )
        data: date = st.date_input(
            label="Data de pagamento *",
            format="DD/MM/YYYY",
            key=7103,
            value=date.today(),
        )
        aluguel_id: int = st.number_input(
            label="ID Aluguel", min_value=0, value=None, format="%d", step=1, key=7104
        )
        nome: str = st.text_input(
            label="Nome",
            value=None,
            key=7105,
        )
        contato: str = st.text_input(
            label="Contato",
            value=None,
            key=7106,
        )
        notas: str = st.text_input(label="Notas", value=None, key=7107)
        if st.button("Registrar", key=7108):
            pagamento_data = empty_none_dict(
                {
                    "tipo": tipo,
                    "valor": valor,
                    "data": data.isoformat(),
                    "aluguel_id": aluguel_id,
                    "nome": nome,
                    "contato": contato,
                    "notas": notas,
                }
            )
            try:
                post_response = requests.post(PAG_URL, json=pagamento_data)
                show_response_message(post_response)
                if post_response.status_code == 200:
                    st.subheader("Dados inseridos, tudo OK:")
                else:
                    st.subheader("Dados NÃO inseridos, favor revisar:")
                show_data_output(pagamento_data)
            except Exception as e:
                raise e

    with tab2:
        st.header("Consultar Pagamentos")
        get_id = st.number_input(
            "ID Pagamento", min_value=1, value=None, format="%d", step=1, key=7200
        )
        if get_id:
            get_response = requests.get(f"{PAG_URL}{get_id}")
            if get_response.status_code == 200:
                pagamento = get_response.json()
                df_get = pd.DataFrame([pagamento])
                st.dataframe(df_get.set_index("id"))
            else:
                show_response_message(get_response)

    with tab3:
        st.header("Modificar Pagamento")
        st.markdown(
            '<p style="font-size: 12px;">Campos com * são obrigatórios</p>',
            unsafe_allow_html=True,
        )
        update_id = st.number_input(
            "ID do Pagamento", min_value=1, value=None, step=1, format="%d", key=7300
        )
        if update_id:
            update_response = requests.get(f"{PAG_URL}{update_id}")
            if update_response.status_code == 200:
                pagamento_up = update_response.json()
                df_up = pd.DataFrame([pagamento_up])
                st.dataframe(df_up.set_index("id"))
                tipo: str = st.radio(
                    label="Tipo de pagamento *",
                    options=["Reserva", "Parcela", "Integral", "Quitação", "Garagem"],
                    index=cat_index(
                        df_up,
                        "tipo",
                        ["Reserva", "Parcela", "Integral", "Quitação", "Garagem"],
                    ),
                    horizontal=True,
                    key=7301,
                )
                valor: float = st.number_input(
                    label="Valor *",
                    min_value=0.00,
                    max_value=90000.00,
                    format="%0.2f",
                    value=df_up.loc[0, "valor"],
                    key=7302,
                )
                data: date = st.date_input(
                    label="Data de pagamento *",
                    format="DD/MM/YYYY",
                    key=7303,
                    value=str_to_date(df_up.data[0]),
                )
                aluguel_id: int = st.number_input(
                    label="ID Aluguel",
                    min_value=0,
                    value=df_up.loc[0, "aluguel_id"],
                    format="%d",
                    step=1,
                    key=7304,
                )
                nome: str = st.text_input(
                    label="Nome",
                    value=df_up.nome[0],
                    key=7305,
                )
                contato: str = st.text_input(
                    label="Contato",
                    value=df_up.contato[0],
                    key=7306,
                )
                notas: str = st.text_input(
                    label="Notas", value=df_up.notas[0], key=7307
                )
                if st.button("Modificar", key=7308):
                    pagamento_up_data = empty_none_dict(
                        {
                            "tipo": tipo,
                            "valor": valor,
                            "data": data.isoformat(),
                            "aluguel_id": aluguel_id,
                            "nome": nome,
                            "contato": contato,
                            "notas": notas,
                        }
                    )
                    try:
                        put_response = requests.put(
                            f"{PAG_URL}{update_id}",
                            json=pagamento_up_data,
                        )
                        show_response_message(put_response)
                        if put_response.status_code == 200:
                            st.subheader("Dados inseridos, tudo OK:")
                        else:
                            st.subheader("Dados NÃO inseridos, favor revisar:")
                        show_data_output(pagamento_up_data)
                    except Exception as e:
                        raise e
            else:
                show_response_message(update_response)

    with tab4:
        st.header("Deletar Pagamento")
        delete_id = st.number_input(
            label="ID Pagamento", min_value=1, value=None, format="%d", step=1, key=7400
        )
        if delete_id:
            show_delete_response = requests.get(f"{PAG_URL}{delete_id}")
            if show_delete_response.status_code == 200:
                pagamento_delete = show_delete_response.json()
                df_delete = pd.DataFrame([pagamento_delete])
                st.dataframe(df_delete.set_index("id"))
                delete_confirm = st.checkbox("Confirma que deseja deletar o registro?")
                delete_button = st.button("Deletar", disabled=(not delete_confirm))
                if delete_button:
                    delete_response = requests.delete(f"{PAG_URL}{delete_id}")
                    show_response_message(delete_response)
            else:
                show_response_message(show_delete_response)

    with tab5:
        st.header("Listar Pagamentos")
        if st.button("Mostrar", key=7500):
            get_list_response = requests.get(PAG_URL)
            if get_list_response.status_code == 200:
                pagamentos = get_list_response.json()
                if pagamentos:
                    df_list = pd.DataFrame(pagamentos)
                    st.dataframe(df_list.set_index("id"))
                else:
                    st.warning("Não há pagamentos para listar")
            else:
                show_response_message(get_list_response)
