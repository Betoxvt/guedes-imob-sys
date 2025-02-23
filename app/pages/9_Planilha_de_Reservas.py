from datetime import date
import locale
import pandas as pd
import requests
import streamlit as st
from utils.mydate import gen_reserv_table, showbr_dfdate, str_to_date
from utils.myfunc import show_response_message
from utils.mystr import apto_input
from utils.urls import ALUG_URL, PAG_URL

st.set_page_config(page_title="Planilha de Reservas", layout="wide")
st.title("Planilha de Reservas")

locale.setlocale(locale.LC_ALL, "pt_BR.UTF-8")

if not st.session_state["authentication_status"]:
    st.info("Por favor faça o login na Home page e tente novamente.")
    st.stop()
else:
    authenticator = st.session_state.authenticator
    st.write(f'Usuário: *{st.session_state["name"]}*')
    authenticator.logout(location="sidebar")

    def clear_session():
        if "planilha_g" in st.session_state:
            st.session_state.pop("planilha_g")
        if "planilha_p" in st.session_state:
            st.session_state.pop("planilha_p")

    tab1, tab2, tab3 = st.tabs(["Planilha", "Reserva por Apto", "Disponibilidade"])

    with tab1:
        st.markdown(
            '<p style="font-size: 12px;">Campos com * são obrigatórios</p>',
            unsafe_allow_html=True,
        )
        st.header("Planilha de Reservas")
        ano = st.selectbox(
            label="Selecione o ano *",
            options=range(2025, 2027),
            index=date.today().year - 2025,
            key=9100,
            on_change=clear_session(),
        )
        mes = st.selectbox(
            label="Selecione o mês *",
            options=range(1, 13),
            index=date.today().month - 1,
            key=9101,
            on_change=clear_session(),
        )
        st.markdown(f"### {mes} / {ano}")
        planilha = gen_reserv_table(ano, mes)
        grandes = planilha.index.str.startswith("A") | planilha.index.str.endswith("0")
        pequenos = ~grandes
        if "planilha_g" not in st.session_state:
            st.session_state.planilha_g = planilha.loc[grandes]
        if "planilha_p" not in st.session_state:
            st.session_state.planilha_p = planilha.loc[pequenos]
        if not st.session_state.planilha_g.empty:
            st.subheader("Apartamentos Grandes")
            event_g = st.dataframe(
                st.session_state.planilha_g,
                selection_mode=["single-column", "single-row"],
                on_select="rerun",
                key=91111,
            )
            if event_g.selection["rows"] and event_g.selection["columns"]:
                day_g = event_g.selection["columns"][0]
                date_g = str_to_date(f"{ano}-{mes}-{day_g}").isoformat()
                index_apto_g = event_g.selection["rows"][0]
                apto_g = st.session_state.planilha_g.iloc[index_apto_g].name
                st.markdown(f"##### Apartamento: {apto_g}. Data: {day_g}/{mes}/{ano}")
                params_g = {"apto_id": apto_g, "checkin": date_g}
                alugueis_g_response = requests.get(ALUG_URL, params=params_g)
                if alugueis_g_response.status_code == 200:
                    alugueis_g = alugueis_g_response.json()
                    df_ag = pd.DataFrame(alugueis_g)
                    if not df_ag.empty:
                        aluguel_id_ag = df_ag.iloc[0]["id"]
                        valor_tot_ag = df_ag.iloc[0]["valor_total"]
                        nome_ag = df_ag.iloc[0]["nome"]
                        st.markdown(f"#### Reserva em nome de **{nome_ag}**")
                        st.markdown(
                            f"#### :blue[Valor total: **{locale.currency(valor_tot_ag)}**]"
                        )
                        params_pg = {"aluguel_id": aluguel_id_ag}
                        pagamentos_g_response = requests.get(PAG_URL, params=params_pg)
                        if pagamentos_g_response.status_code == 200:
                            pagamentos_g = pagamentos_g_response.json()
                            df_pg = pd.DataFrame(pagamentos_g)
                            if not df_pg.empty:
                                valor_pago_pg = df_pg["valor"].sum()
                                pagou_pg = locale.currency(valor_pago_pg)
                                deve_pg = locale.currency(valor_tot_ag - valor_pago_pg)
                                st.markdown(f"#### :green[Pago: **{pagou_pg}**]")
                                st.write(f"#### :orange[Deve: **{deve_pg}**]")
                            else:
                                st.write(
                                    f"#### :red[Não há pagamentos para a reserva em **{day_g}/{mes}/{ano}** do apto **{apto_g}**]"
                                )
                        else:
                            show_response_message(pagamentos_g_response)
                    else:
                        st.markdown(
                            f"#### :orange[Não há reservas iniciando em **{day_g}/{mes}/{ano}** para o apto **{apto_g}**]"
                        )
                else:
                    show_response_message(alugueis_g_response)

        if not st.session_state.planilha_p.empty:
            st.subheader("Apartamentos Pequenos")
            event_p = st.dataframe(
                st.session_state.planilha_p,
                selection_mode=["single-column", "single-row"],
                on_select="rerun",
                key=92222,
            )
            if event_p.selection["rows"] and event_p.selection["columns"]:
                day_p = event_p.selection["columns"][0]
                date_p = str_to_date(f"{ano}-{mes}-{day_p}").isoformat()
                index_apto_p = event_p.selection["rows"][0]
                apto_p = st.session_state.planilha_p.iloc[index_apto_p].name
                st.markdown(f"##### Apartamento: {apto_p}. Data: {day_p}/{mes}/{ano}")
                params_p = {"apto_id": apto_p, "checkin": date_p}
                alugueis_p_response = requests.get(ALUG_URL, params=params_p)
                if alugueis_p_response.status_code == 200:
                    alugueis_p = alugueis_p_response.json()
                    df_ap = pd.DataFrame(alugueis_p)
                    if not df_ap.empty:
                        aluguel_id_ap = df_ap.iloc[0]["id"]
                        valor_tot_ap = df_ap.iloc[0]["valor_total"]
                        nome_ap = df_ap.iloc[0]["nome"]
                        st.markdown(f"#### Reserva em nome de **{nome_ap}**")
                        st.markdown(
                            f"#### :blue[Valor total: **{locale.currency(valor_tot_ap)}**]"
                        )
                        params_pp = {"aluguel_id": aluguel_id_ap}
                        pagamentos_p_response = requests.get(PAG_URL, params=params_pp)
                        if pagamentos_p_response.status_code == 200:
                            pagamentos_p = pagamentos_p_response.json()
                            df_pp = pd.DataFrame(pagamentos_p)
                            if not df_pp.empty:
                                valor_pago_pp = df_pp["valor"].sum()
                                pagou_pp = locale.currency(valor_pago_pp)
                                deve_pp = locale.currency(valor_tot_ap - valor_pago_pp)
                                st.markdown(f"#### :green[Pago: **{pagou_pp}**]")
                                st.write(f"#### :orange[Deve: **{deve_pp}**]")
                            else:
                                st.write(
                                    f"#### :red[Não há pagamentos para a reserva em **{day_p}/{mes}/{ano}** do apto **{apto_p}**]"
                                )
                        else:
                            show_response_message(pagamentos_p_response)
                    else:
                        st.markdown(
                            f"#### :orange[Não há reservas iniciando em **{day_p}/{mes}/{ano}** para o apto **{apto_p}**]"
                        )
                else:
                    show_response_message(alugueis_p_response)

    with tab2:
        st.header("Consultar Reservas | Por Apartamento")
        st.markdown(
            '<p style="font-size: 12px;">Campos com * são obrigatórios</p>',
            unsafe_allow_html=True,
        )
        consult_apto = apto_input(
            st.text_input("Apartamento *", key=9200, max_chars=5, value=None)
        )
        consult_button = st.button("Consultar", key=9201)
        if consult_button:
            if consult_apto is not None:
                alugueis_response = requests.get(ALUG_URL)
                alugueis = alugueis_response.json()
                df_consult = pd.DataFrame(
                    alugueis, columns=["apto_id", "checkin", "checkout"]
                )
                df_consult = df_consult.set_index("apto_id")
                if consult_apto in df_consult.index:
                    df_filter = pd.DataFrame(df_consult.loc[consult_apto])
                    st.dataframe(showbr_dfdate(df_filter))
                else:
                    st.warning(f"O apartamento {consult_apto} não possui reservas")
            else:
                st.error("Forneça um apartamento.")

    with tab3:
        st.header("Consultar Disponibilidade")
        st.markdown(
            '<p style="font-size: 12px;">Campos com * são obrigatórios</p>',
            unsafe_allow_html=True,
        )
        disp_apto = apto_input(
            st.text_input("Apartamento *", key=9300, max_chars=5, value=None)
        )
        disp_checkin = st.date_input(
            "Check-in *", key=9301, format="DD/MM/YYYY", value=None
        )
        disp_checkout = st.date_input(
            "Check-out *", key=9302, format="DD/MM/YYYY", value=None
        )
        if isinstance(disp_checkin, date) and isinstance(disp_checkout, date):
            difference = (disp_checkout - disp_checkin).days
            if difference < 1:
                st.warning("A data de check-out deve ser posterior à data de check-in.")
        else:
            st.warning(f"Insira as datas de Check-in e Check-out")
        disp_button = st.button("Consultar", key=9303)
        if disp_button:
            if disp_apto and disp_checkin and disp_checkout:
                disp_response = requests.get(ALUG_URL)
                alugueis_2 = disp_response.json()
                df_disp = pd.DataFrame(
                    alugueis_2, columns=["apto_id", "checkin", "checkout", "id"]
                )
                df_disp = df_disp.set_index("apto_id")
                if disp_apto in df_disp.index:
                    df_apto = df_disp.loc[[disp_apto]]
                    for _, aluguel in df_apto.iterrows():
                        checkin_date = date.fromisoformat(aluguel["checkin"])
                        checkout_date = date.fromisoformat(aluguel["checkout"])
                        ok = 0
                        if not (
                            checkout_date <= disp_checkin
                            or checkin_date >= disp_checkout
                        ):
                            st.warning(
                                f"O apartamento {disp_apto} está ocupado para o período de {disp_checkin} a {disp_checkout} com o aluguel de ID {aluguel['id']}"
                            )
                            break
                        ok += 1
                    if ok:
                        st.success(
                            f"O apartamento {disp_apto} está livre para o período de {disp_checkin} a {disp_checkout}"
                        )
                else:
                    if disp_apto is not None:
                        st.success(
                            f"O apartamento {disp_apto} está livre para o período de {disp_checkin} a {disp_checkout}"
                        )
            else:
                st.error("Todos os campos são obrigatórios para a consulta.")
