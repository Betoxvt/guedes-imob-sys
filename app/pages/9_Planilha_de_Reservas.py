from datetime import date
import streamlit as st
from utils.mydate import gen_reserv_table

st.set_page_config(page_title="Planilha de Reservas", layout="wide")
st.title("Planilha de Reservas")

ano = st.selectbox(
    label="Selecione o ano", options=range(2025, 2027), index=date.today().year - 2025
)
mes = st.selectbox(
    label="Selecione o mês", options=range(1, 13), index=date.today().month - 1
)

planilha = gen_reserv_table(ano, mes)
st.table(planilha)
