from datetime import date
import pandas as pd
import requests
import streamlit as st
from utils.mydate import gen_reserv_table, showbr_dfdate
from utils.mystr import apto_input

st.set_page_config(page_title="Planilha de Reservas", layout="wide")
st.title("Planilha de Reservas")

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
    )
    mes = st.selectbox(
        label="Selecione o mês *",
        options=range(1, 13),
        index=date.today().month - 1,
        key=9101,
    )
    if ano and mes:
        planilha = gen_reserv_table(ano, mes)
    grandes = planilha.index.str.startswith("A") | planilha.index.str.endswith("0")
    pequenos = ~grandes
    planilha_g = planilha.loc[grandes]
    planilha_p = planilha.loc[pequenos]
    if not planilha_g.empty:
        st.subheader("Apartamentos Grandes")
        st.dataframe(planilha_g)
    if not planilha_p.empty:
        st.subheader("Apartamentos Pequenos")
        st.dataframe(planilha_p)

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
            alugueis_response = requests.get(f"http://api:8000/alugueis/")
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
            disp_response = requests.get(f"http://api:8000/alugueis/")
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
                        checkout_date <= disp_checkin or checkin_date >= disp_checkout
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
