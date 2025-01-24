import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader

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
    authenticator.logout()
    st.write(f'Bem Vindo(a), *{st.session_state["name"]}*')
    st.title("Página de Sistema")
elif st.session_state["authentication_status"] is False:
    st.write("Usuário ou senha incorretos")
elif st.session_state["authentication_status"] is None:
    st.write("Por favor, faça login")

# Escolher um apartamento e a partir dai acessar funções relacionadas diretamente a ele
