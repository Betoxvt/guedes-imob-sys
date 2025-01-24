from datetime import date
import pandas as pd
import requests
import streamlit as st
from utils.mydate import gen_reserv_table

st.set_page_config(page_title="Planilha de Reservas", layout="wide")
st.title("Planilha de Reservas")
tab1, tab2, tab3 = ["Planilha", "Reserva por Apto", "Disponibilidade"]
with tab1:
    st.header("Planilha de Reservas")
    ano = st.selectbox(
        label="Selecione o ano",
        options=range(2025, 2027),
        index=date.today().year - 2025,
    )
    mes = st.selectbox(
        label="Selecione o mês", options=range(1, 13), index=date.today().month - 1
    )

    planilha = gen_reserv_table(ano, mes)
    st.table(planilha)

with tab2:
    st.header("Consultar Reservas | Por Apartamento")
    consult_apto = st.text_input("Apto")
    consult_button = st.button("Consultar")
    if consult_button:
        alugueis_response = requests.get(f"http://api:8000/alugueis/")
        alugueis = alugueis_response.json()
        df_consult = pd.DataFrame(alugueis, columns=["apto_id", "checkin", "checkout"])
        df_consult = df_consult.set_index("apto_id")
        if consult_apto in df_consult.index:
            df_filter = df_consult.loc[consult_apto]
        else:
            st.warning(f"O apartamento {consult_apto} não possui aluguéis")

with tab3:
    st.header("Consultar Disponibilidade")
    disp_apto = st.text_input("Apto")
    disp_checkin = st.date_input("Check-in")
    disp_checkout = st.date_input("Check-out")
    disp_button = st.button("Consultar")
    if disp_button:
        disp_response = requests.get(f"http://api:8000/alugueis/")
        alugueis_2 = disp_response.json()
        df_disp = pd.DataFrame(
            alugueis_2, columns=["apto_id", "checkin", "checkout", "id"]
        )
        df_disp = df_disp.set_index("apto_id")
        if disp_apto in df_disp.index:
            df_apto = df_disp.loc[disp_apto]
            for aluguel in df_apto.iterrows():
                if not (
                    aluguel["checkout"] <= disp_checkin
                    or aluguel["checkin"] >= disp_checkout
                ):
                    st.warning(
                        f"O apartamento {disp_apto} está ocupado para o período de {disp_checkin} a {disp_checkout} com o aluguel de ID {aluguel['id']}"
                    )
                else:
                    st.success(
                        f"O apartamento {disp_apto} está livre para o período de {disp_checkin} a {disp_checkout}"
                    )
        else:
            st.success(
                f"O apartamento {disp_apto} está livre para o período de {disp_checkin} a {disp_checkout}"
            )
