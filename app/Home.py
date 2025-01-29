import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader
from utils.mydate import showbr_dfdate
from utils.myfunc import show_response_message
from utils.mystr import apto_input
import requests
import pandas as pd
import locale

locale.setlocale(locale.LC_ALL, "pt_BR.UTF-8")

st.set_page_config(page_title="Pagina Inicial", layout="wide")
st.title("Página Inicial")


with open("config.yaml", "r") as f:
    config = yaml.load(f, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config["credentials"],
    config["cookie"]["name"],
    config["cookie"]["key"],
    config["cookie"]["expiry_days"],
)

authenticator.login()

if st.session_state["authentication_status"]:
    authenticator.logout(location="sidebar")
    st.write(f'Usuário: *{st.session_state["name"]}*')
    st.subheader("Consultas Rápidas")
    tab1, tab2 = st.tabs(["Por Apartamento", "Por Datas"])
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
        check_day = st.date_input("Data", format="DD/MM/YYYY")


elif st.session_state["authentication_status"] is False:
    st.write("Usuário ou senha incorretos")
elif st.session_state["authentication_status"] is None:
    st.write("Por favor, faça login")
