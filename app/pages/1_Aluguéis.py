from datetime import date
from Home import ALUG_URL, FICHA_URL, PAG_URL
import locale
import pandas as pd
import requests
import streamlit as st
import streamlit_authenticator as stauth
from utils.mydate import brazil_datestr, calculate_diarias, showbr_dfdate, str_to_date
from utils.myfunc import show_data_output, show_response_message
from utils.mynum import calculate_saldo, calculate_valortotal
from utils.mystr import apto_input, empty_none, empty_none_dict

locale.setlocale(locale.LC_ALL, "pt_BR.UTF-8")

st.set_page_config(page_title="Aluguéis", layout="wide")
st.title("Aluguéis")

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
        st.header("Registrar Aluguel")
        st.markdown(
            '<p style="font-size: 12px;">Campos com * são obrigatórios</p>',
            unsafe_allow_html=True,
        )
        apto_id: str = apto_input(
            st.text_input(label="ID Apartamento *", value=None, key=1100)
        )
        ficha_id: int = st.number_input(
            label="ID Ficha", min_value=1, value=None, format="%d", step=1, key=1101
        )
        if ficha_id:
            get_ficha = requests.get(FICHA_URL + ficha_id)
            if get_ficha.status_code == 200:
                ficha_data = get_ficha.json()
                ficha_name = ficha_data["nome"]
                ficha_apto = (
                    ficha_data["apto_id"]
                    if ficha_data["apto_id"] is not None
                    else "Não registrado"
                )
                ficha_in = brazil_datestr(ficha_data["checkin"])
                ficha_out = brazil_datestr(ficha_data["checkout"])
                st.write(
                    f"Inquilino: {ficha_name} ~~~ Apto: {ficha_apto} ~~~ Check-in: {ficha_in} ~~~ Check-out: {ficha_out}"
                )
            else:
                st.write("Não foi encontrada a ficha com este ID")
        checkin: date = st.date_input(
            label="Check-in *", format="DD/MM/YYYY", key=1102, value=None
        )
        checkout: date = st.date_input(
            label="Check-out *", format="DD/MM/YYYY", key=1103, value=None
        )
        diarias: int = calculate_diarias(checkin, checkout)
        valor_diaria: float = st.number_input(
            label="Valor da Diária *",
            min_value=0.00,
            max_value=3000.00,
            value=None,
            format="%0.2f",
            step=10.00,
            key=1105,
        )
        valor_total: float = calculate_valortotal(diarias, valor_diaria)
        valor_depositado: float = st.number_input(
            label="Valor Depositado",
            min_value=0.00,
            max_value=90000.0,
            value=None,
            format="%0.2f",
            key=1106,
        )
        saldo: float = calculate_saldo(valor_total, valor_depositado)
        nome = st.text_input(label="Nome *", value=None, key=1107)
        contato = st.text_input(label="Contato *", value=None, key=1108)
        if st.button("Registrar", key=1109):
            aluguel_data = empty_none_dict(
                {
                    "apto_id": apto_id,
                    "ficha_id": ficha_id,
                    "checkin": checkin.isoformat(),
                    "checkout": checkout.isoformat(),
                    "diarias": diarias,
                    "valor_diaria": valor_diaria,
                    "valor_total": valor_total,
                    "nome": nome,
                    "contato": contato,
                }
            )
            try:
                post_response = requests.post(ALUG_URL, json=aluguel_data)
                show_response_message(post_response)
                if post_response.status_code == 200:
                    st.subheader("Dados inseridos, tudo OK:")
                    show_data_output(aluguel_data)
                    if empty_none(valor_depositado) is not None:
                        get_top_response = requests.get(ALUG_URL, params={"limit": 1})
                        if get_top_response.status_code == 200:
                            top_data = get_top_response.json()
                            aluguel_id = top_data[0].get("id")
                            pagamento_data = empty_none_dict(
                                {
                                    "tipo": "Reserva",
                                    "valor": valor_depositado,
                                    "aluguel_id": aluguel_id,
                                    "notas": f"Depósito para reserva do {apto_id} de {checkin.strftime('%d/%m/%Y')} a {checkout.strftime('%d/%m/%Y')}",
                                    "nome": nome,
                                    "contato": contato,
                                    "data": date.today().isoformat(),
                                }
                            )
                            post_pagamento_response = requests.post(
                                PAG_URL, json=pagamento_data
                            )
                            show_response_message(post_pagamento_response)
                            if post_pagamento_response.status_code == 200:
                                st.subheader("Dados do deposito salvos, tudo OK:")
                                show_data_output(pagamento_data)
                            else:
                                st.subheader(
                                    "Não foi possível salvar os dados do depósito"
                                )
                                show_data_output(pagamento_data)
                        else:
                            st.subheader("Erro ao obter o ID do aluguel")
                            show_response_message(get_top_response)
                    else:
                        st.write("Nenhum valor de depósito fornecido.")
                else:
                    st.subheader("Dados NÃO inseridos, favor revisar:")
                    st.write("Verifique as datas de check-in/out")
                    show_data_output(aluguel_data)
            except requests.exceptions.RequestException as e:
                st.error(f"Erro na requisição: {e}")
            except Exception as e:
                st.error(f"Um erro inesperado ocorreu: {e}")

    with tab2:
        alug_id = None
        apto = None
        chkin = None
        df_alug = pd.DataFrame
        df_pag = pd.DataFrame
        get_id = None
        warn = None
        valor_aluguel = 0
        pago = 0
        st.header("Consultar Aluguéis")
        st.markdown("#### Por ID")
        get_id = st.number_input(
            "ID Aluguel", min_value=1, value=None, format="%d", step=1, key=1200
        )
        st.markdown("#### Por Apartamento + Check-In")
        apto = apto_input(st.text_input("Apartamento", value=None, key=1201))
        chkin = st.date_input("Check-in", value=None, key=1202, format="DD/MM/YYYY")
        if chkin:
            chkin = chkin.isoformat()

        if get_id:
            get_response = requests.get(ALUG_URL + get_id)
            if get_response.status_code == 200:
                aluguel = get_response.json()
                df_alug = pd.DataFrame([aluguel])
                alug_id = get_id
            else:
                show_response_message(get_response)

        if apto:
            get_response = requests.get(ALUG_URL)
            if get_response.status_code == 200:
                alugueis = get_response.json()
                df_alug = pd.DataFrame(alugueis)
                df_alug = df_alug[df_alug["apto_id"] == apto]
                if df_alug.empty:
                    warn = f"Não há aluguéis para **{apto}**"
                if chkin:
                    df_alug = df_alug[df_alug["checkin"] == chkin]
                    if not df_alug.empty:
                        alug_id = df_alug.iloc[0]["id"]
                        valor_aluguel = df_alug.iloc[0]["valor_total"]
                    else:
                        warn = f"Não há aluguéis para **{apto}** com check-in em **{str_to_date(chkin).strftime('%d/%m/%Y')}**"
            else:
                show_response_message(get_response)

        if chkin:
            get_response = requests.get(ALUG_URL)
            if get_response.status_code == 200:
                alugueis = get_response.json()
                df_alug = pd.DataFrame(alugueis)
                df_alug = df_alug[df_alug["checkin"] == chkin]
                if df_alug.empty:
                    warn = f"Não há aluguéis com check-in em **{str_to_date(chkin).strftime('%d/%m/%Y')}**"
                if apto:
                    df_alug = df_alug[df_alug["apto_id"] == apto]
                    if not df_alug.empty:
                        alug_id = df_alug.iloc[0]["id"]
                        valor_aluguel = df_alug.iloc[0]["valor_total"]
                    else:
                        warn = f"Não há aluguéis para **{apto}** com check-in em **{str_to_date(chkin).strftime('%d/%m/%Y')}**"
            else:
                show_response_message(get_response)

        if warn:
            st.warning(warn)

        if not df_alug.empty:
            st.dataframe(showbr_dfdate(df_alug), hide_index=True)
            get_pag_response = requests.get(PAG_URL)
            if get_pag_response.status_code == 200:
                pagamentos = get_pag_response.json()
                df_pag = pd.DataFrame(pagamentos)
                df_pag = df_pag[df_pag["aluguel_id"] == alug_id]
                if not df_pag.empty:
                    st.markdown("#### Lista dos pagamentos para este aluguel:")
                    st.dataframe(showbr_dfdate(df_pag), hide_index=True)
                    pago = round(df_pag["valor"].sum(), 2)
                else:
                    if alug_id:
                        st.warning("Não há pagamentos registrados para este aluguel")
                    else:
                        pass
            else:
                show_response_message(get_pag_response)
            if valor_aluguel > 0:
                st.markdown(f"Valor do Aluguel: {valor_aluguel}")
                st.markdown(f"Total pago: {pago}")
                resta = round(valor_aluguel - pago, 2)
                if resta > 0:
                    st.error(f"Situação: Devendo {locale.currency(resta)}")
                if resta == 0:
                    st.success(f"Situação: Quitado")

    with tab3:
        st.header("Modificar Aluguel")
        st.markdown(
            '<p style="font-size: 12px;">Campos com * são obrigatórios</p>',
            unsafe_allow_html=True,
        )
        update_id = st.number_input(
            "ID do Aluguel", min_value=1, value=None, format="%d", key=1300
        )
        if update_id:
            update_response = requests.get(ALUG_URL + update_id)
            if update_response.status_code == 200:
                aluguel_up = update_response.json()
                df_up = pd.DataFrame([aluguel_up])
                st.dataframe(df_up, hide_index=True)
                apto_id: str = apto_input(
                    st.text_input(
                        label="ID Apartamento *", key=1301, value=df_up.apto_id[0]
                    )
                )
                ficha_id: int = st.number_input(
                    label="ID Ficha",
                    min_value=1,
                    format="%d",
                    step=1,
                    key=1302,
                    value=df_up.loc[0, "ficha_id"],
                )
                if ficha_id:
                    get_ficha = requests.get(FICHA_URL + ficha_id)
                    if get_ficha.status_code == 200:
                        ficha_data = get_ficha.json()
                        ficha_name = ficha_data["nome"]
                        ficha_apto = (
                            ficha_data["apto_id"]
                            if ficha_data["apto_id"] is not None
                            else "Não registrado"
                        )
                        ficha_in = brazil_datestr(ficha_data["checkin"])
                        ficha_out = brazil_datestr(ficha_data["checkout"])
                        st.write(
                            f"Inquilino: {ficha_name} ~~~ Apto: {ficha_apto} ~~~ Check-in: {ficha_in} ~~~ Check-out: {ficha_out}"
                        )
                    else:
                        st.write("Não foi encontrada a ficha com este ID")
                checkin: date = st.date_input(
                    label="Check-in *",
                    value=str_to_date(df_up.checkin[0]),
                    format="DD/MM/YYYY",
                    key=1303,
                )
                checkout: date = st.date_input(
                    label="Check-out *",
                    value=str_to_date(df_up.checkout[0]),
                    format="DD/MM/YYYY",
                    key=1304,
                )
                diarias: int = calculate_diarias(checkin, checkout)
                valor_diaria: float = st.number_input(
                    label="Valor da diária *",
                    min_value=0.00,
                    max_value=3000.00,
                    value=df_up.loc[0, "valor_diaria"],
                    format="%0.2f",
                    step=10.00,
                    key=1305,
                )
                valor_total: float = calculate_valortotal(diarias, valor_diaria)
                saldo: float = calculate_saldo(valor_total, valor_depositado)
                nome = st.text_input(label="Nome *", value=df_up.nome[0], key=1306)
                contato = st.text_input(
                    label="Contato *", value=df_up.contato[0], key=1307
                )
                if st.button("Modificar"):
                    aluguel_up_data = empty_none_dict(
                        {
                            "apto_id": apto_id,
                            "ficha_id": ficha_id,
                            "checkin": checkin.isoformat(),
                            "checkout": checkout.isoformat(),
                            "diarias": diarias,
                            "valor_diaria": valor_diaria,
                            "valor_total": valor_total,
                            "nome": nome,
                            "contato": contato,
                        }
                    )
                    try:
                        put_response = requests.put(
                            ALUG_URL + update_id,
                            json=aluguel_up_data,
                        )
                        show_response_message(put_response)
                        if put_response.status_code == 200:
                            st.subheader("Dados inseridos, tudo OK:")
                        else:
                            st.subheader("Dados NÃO inseridos, favor revisar:")
                        show_data_output(aluguel_up_data)
                    except Exception as e:
                        raise e
            else:
                show_response_message(update_response)

    with tab4:
        st.header("Deletar Aluguel")
        delete_id = st.number_input(
            label="ID Aluguel", min_value=1, value=None, format="%d", step=1, key=1400
        )
        if delete_id:
            show_delete_response = requests.get(ALUG_URL + delete_id)
            if show_delete_response.status_code == 200:
                aluguel_delete = show_delete_response.json()
                df_delete = pd.DataFrame([aluguel_delete])
                st.dataframe(df_delete.set_index("id"))
                delete_confirm = st.checkbox("Confirma que deseja deletar o registro?")
                delete_button = st.button("Deletar", disabled=(not delete_confirm))
                if delete_button:
                    delete_response = requests.delete(ALUG_URL + delete_id)
                    show_response_message(delete_response)
            else:
                show_response_message(show_delete_response)

    with tab5:
        st.header("Listar Aluguéis")
        if st.button("Mostrar", key=1500):
            get_list_response = requests.get(ALUG_URL)
            if get_list_response.status_code == 200:
                alugueis = get_list_response.json()
                if alugueis:
                    df_list = pd.DataFrame(alugueis)
                    st.dataframe(df_list.set_index("id"))
                else:
                    st.warning("Não há alugueis para listar")
            else:
                show_response_message(get_list_response)
