from datetime import date, timedelta
import locale
import numpy as np
import os
import pandas as pd
import requests
import streamlit as st
import streamlit_authenticator as stauth
from utils.myfunc import show_response_message
from utils.mystr import apto_input
import yaml
from yaml.loader import SafeLoader

locale.setlocale(locale.LC_ALL, "pt_BR.UTF-8")

USERS_PATH = os.environ.get("USERS_PATH")

st.set_page_config(page_title="Pagina Inicial", layout="wide")
st.title("Página Inicial")


def st_authenticator():
    with open(USERS_PATH) as f:
        config = yaml.load(f, Loader=SafeLoader)
        f.close()

    authenticator = stauth.Authenticate(
        config["credentials"],
        config["cookie"]["name"],
        config["cookie"]["key"],
        config["cookie"]["expiry_days"],
    )

    return authenticator


if "authenticator" not in st.session_state:
    st.session_state.authenticator = st_authenticator()

authenticator = st.session_state.authenticator

try:
    authenticator.login()
except Exception as e:
    st.error(e)

if st.session_state["authentication_status"]:
    st.write(f'Usuário: *{st.session_state["name"]}*')
    authenticator.logout(location="sidebar")
    st.subheader("Consultas Rápidas")
    tab1, tab2, tab3 = st.tabs(["Por Apartamento", "Por Datas", "Caixa"])

    with tab1:
        apto_id = apto_input(
            st.text_input(label="Apartamento", value=None, max_chars=5, key=10000)
        )
        if apto_id:
            get_apto_response = requests.get(f"http://api:8000/apartamentos/{apto_id}")
            if get_apto_response.status_code == 200:
                alugueis_button = st.button("Alugueis", use_container_width=True)
                if alugueis_button:
                    get_alugueis_response = requests.get(
                        f"http://api:8000/alugueis/?apto_id={apto_id}"
                    )
                    if get_alugueis_response.status_code == 200:
                        alugueis = get_alugueis_response.json()
                        df = pd.DataFrame(alugueis)
                        if not df.empty:
                            df["Pago (R$)"] = 0
                            df["Deve (R$)"] = 0
                            for index, row in df.iterrows():
                                aluguel_id = row["id"]
                                response = requests.get(
                                    f"http://api:8000/pagamentos/?aluguel_id={aluguel_id}"
                                )
                                if response.status_code == 200:
                                    data = response.json()
                                    df_pag = pd.DataFrame(data)
                                    if not df_pag.empty:
                                        pago = df_pag["valor"].sum()
                                        df.loc[index, "Pago (R$)"] = pago
                                else:
                                    show_response_message(response)
                                df.loc[index, "Deve (R$)"] = (
                                    df.loc[index, "valor_total"]
                                    - df.loc[index, "Pago (R$)"]
                                )
                            df = df.drop(columns=["id", "criado_em", "modificado_em"])
                            st.dataframe(
                                df,
                                hide_index=True,
                                column_config={
                                    "valor_total": st.column_config.NumberColumn(
                                        "Total (R$)"
                                    ),
                                    "valor_diaria": st.column_config.NumberColumn(
                                        "Por dia (R$)"
                                    ),
                                    "checkin": st.column_config.DateColumn(
                                        "Check-in", format="DD/MM/YYYY"
                                    ),
                                    "checkout": st.column_config.DateColumn(
                                        "Check-out", format="DD/MM/YYYY"
                                    ),
                                },
                            )
                        else:
                            st.warning(f"Sem registros de aluguéis para {apto_id}")
                    else:
                        show_response_message(get_alugueis_response)
                garagens_button = st.button("Garagens", use_container_width=True)
                if garagens_button:
                    get_garagens_origem_response = requests.get(
                        f"http://api:8000/garagens/?apto_id_origem={apto_id}"
                    )
                    if get_garagens_origem_response.status_code == 200:
                        garagens_origem = get_garagens_origem_response.json()
                        df = pd.DataFrame(garagens_origem)
                        if not df.empty:
                            df["Pago (R$)"] = 0
                            df["Deve (R$)"] = 0
                            for index, row in df.iterrows():
                                aluguel_id = row["id"]
                                tipo = "Garagem"
                                response = requests.get(
                                    f"http://api:8000/pagamentos/?aluguel_id={aluguel_id}&tipo={tipo}"
                                )
                                if response.status_code == 200:
                                    data = response.json()
                                    df_pag = pd.DataFrame(data)
                                    if not df_pag.empty:
                                        pago = df_pag["valor"].sum()
                                        df.loc[index, "Pago (R$)"] = pago
                                else:
                                    show_response_message(response)
                                df.loc[index, "Deve (R$)"] = (
                                    df.loc[index, "valor_total"]
                                    - df.loc[index, "Pago (R$)"]
                                )
                            df = df.drop(columns=["id", "criado_em", "modificado_em"])

                            st.dataframe(
                                df,
                                hide_index=True,
                                column_config={
                                    "apto_id_origem": st.column_config.TextColumn(
                                        "Vaga:"
                                    ),
                                    "apto_id_destino": st.column_config.TextColumn(
                                        "Usando:"
                                    ),
                                    "checkin": st.column_config.DateColumn(
                                        "Check-in", format="DD/MM/YYYY"
                                    ),
                                    "checkout": st.column_config.DateColumn(
                                        "Check-out", format="DD/MM/YYYY"
                                    ),
                                    "valor_diaria": st.column_config.NumberColumn(
                                        "Por dia (R$)"
                                    ),
                                    "valor_total": st.column_config.NumberColumn(
                                        "Total (R$)"
                                    ),
                                },
                            )
                        else:
                            st.warning(
                                f"Sem registros de uso da vaga de garagem do {apto_id}"
                            )
                    else:
                        show_response_message(get_garagens_origem_response)

    with tab2:

        def color_df(val: str):
            is_index_col = val.name == "Apto."
            return pd.Series(
                np.where(
                    is_index_col,
                    "font-weight: bold",
                    np.where(
                        val == "Livre",
                        "background-color: green",
                        "background-color: red",
                    ),
                ),
                index=val.index,
            )

        checkin = st.date_input("Check-in", format="DD/MM/YYYY")
        checkout = st.date_input("Check-out", format="DD/MM/YYYY", value=None)
        days = st.number_input("Diarias", step=1, format="%d", value=None)

        if checkout is None and days is not None:
            checkout = checkin + timedelta(days=days)

        verify_button = st.button("Verificar")
        if verify_button:
            aptos_response = requests.get(f"http://api:8000/apartamentos/")
            if aptos_response.status_code == 200:
                aptos_data = aptos_response.json()
                df_aptos = pd.DataFrame(aptos_data, columns=["id"])
                df_aptos["Situação"] = "Livre"
                df_aptos["Até"] = None
                df_aptos = df_aptos.set_index("id")
            else:
                show_response_message(aptos_response)
            alug_response = requests.get(f"http://api:8000/alugueis/")
            if alug_response.status_code == 200:
                alug_data = alug_response.json()
                df_alug = pd.DataFrame(
                    alug_data, columns=["apto_id", "checkin", "checkout"]
                )
                df_alug = df_alug.set_index("apto_id")
                if not df_alug.empty and not df_aptos.empty:
                    for index, aluguel in df_alug.iterrows():
                        checkin_date = date.fromisoformat(aluguel["checkin"])
                        checkout_date = date.fromisoformat(aluguel["checkout"])
                        if checkin and checkout:
                            if not (
                                checkout_date <= checkin or checkin_date >= checkout
                            ):
                                # df_aptos.loc[index, "Situação"] = "Reservado"
                                df_aptos = df_aptos.drop(index=index)
                            else:
                                try:
                                    if df_aptos.loc[index, "Até"] is None:
                                        df_aptos.loc[index, "Até"] = checkin_date
                                    elif checkin_date < df_aptos.loc[index, "Até"]:
                                        df_aptos.loc[index, "Até"] = checkin_date
                                except:
                                    pass
                        elif checkin and not checkout:
                            if checkin < checkin_date:
                                try:
                                    if df_aptos.loc[index, "Até"] is None:
                                        df_aptos.loc[index, "Até"] = checkin_date
                                    elif checkin_date < df_aptos.loc[index, "Até"]:
                                        df_aptos.loc[index, "Até"] = checkin_date
                                except:
                                    pass
                            else:
                                try:
                                    if (
                                        checkin_date <= checkin
                                        and checkin < checkout_date
                                    ):
                                        # df_aptos.loc[index, "Situação"] = "Reservado"
                                        df_aptos = df_aptos.drop(index=index)
                                except:
                                    pass
                    df_aptos["Apto."] = df_aptos.index
                    df_aptos = df_aptos[["Apto.", "Situação", "Até"]]
                    st.dataframe(
                        hide_index=True,
                        data=df_aptos.style.apply(
                            color_df, subset=["Situação", "Apto."]
                        ),
                        column_config={
                            "Até": st.column_config.DateColumn(
                                "Até", format="DD/MM/YYYY"
                            ),
                        },
                    )

                else:
                    st.warning("Não há alugueis e/ou apartamentos registrados")
            else:
                show_response_message(alug_response)

    with tab3:

        st.markdown("R$ ...")
        st.markdown("$ ...")
        st.markdown("Registrar...")

elif st.session_state["authentication_status"] is False:
    st.error("Usuário ou senha incorretos")
elif st.session_state["authentication_status"] is None:
    st.write("Por favor, faça login")
