import streamlit as st


def calculate_valortotal(diarias, valor_diaria):
    if diarias is None or valor_diaria is None:
        return None
    if not isinstance(diarias, (int, float)) or not isinstance(valor_diaria, (int, float)):
        st.warning("As diárias e o valor da diária devem ser números.")
        return 0
    if diarias <= 0:
        st.warning("O mínimo de diárias é 1.")
    if valor_diaria <= 0:
        st.warning("O valor da diária deve ser positivo.")
    valor_total = diarias * valor_diaria
    return valor_total