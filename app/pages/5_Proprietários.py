import pandas as pd
import requests
import streamlit as st
from utils.myfunc import show_data_output, show_response_message
from utils.mynum import cpf_input, tel_input_br
from utils.mystr import empty_none_dict

st.set_page_config(page_title="Proprietários", layout="wide")
st.title("Proprietários")

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
    st.header("Registrar Proprietário")
    st.markdown(
        '<p style="font-size: 12px;">Campos com * são obrigatórios</p>',
        unsafe_allow_html=True,
    )
    nome: str = st.text_input(label="Nome *", key=5000, value=None)
    cpf: str = cpf_input(st.text_input(label="CPF", key=5101, value=None))
    tel: str = tel_input_br(st.text_input(label="Telefone", key=5102, value=None))
    email: str = st.text_input(label="E-Mail", key=5103, value=None)
    if st.button("Registrar", key=5104):
        prop_data = empty_none_dict(
            {
                "nome": nome,
                "cpf": cpf,
                "tel": tel,
                "email": email,
            }
        )
        try:
            post_response = requests.post(
                "http://api:8000/proprietarios/", json=prop_data
            )
            show_response_message(post_response)
            if post_response.status_code == 200:
                st.subheader("Dados inseridos, tudo OK:")
            else:
                st.subheader("Dados NÃO inseridos, favor revisar:")
            show_data_output(prop_data)
        except Exception as e:
            raise (e)

with tab2:
    st.header("Consultar Proprietários")
    get_id = st.number_input(
        "ID Proprietário", min_value=1, value=None, format="%d", step=1, key=5200
    )
    if get_id:
        get_response = requests.get(f"http://api:8000/proprietarios/{get_id}")
        if get_response.status_code == 200:
            proprietario = get_response.json()
            df_get = pd.DataFrame([proprietario])
            st.dataframe(df_get.set_index("id"))
        else:
            show_response_message(get_response)

with tab3:
    st.header("Modificar Proprietário")
    st.markdown(
        '<p style="font-size: 12px;">Campos com * são obrigatórios</p>',
        unsafe_allow_html=True,
    )
    update_id = st.number_input(
        "ID do Proprietário", min_value=1, value=None, step=1, format="%d", key=5300
    )
    if update_id:
        update_response = requests.get(f"http://api:8000/proprietarios/{update_id}")
        if update_response.status_code == 200:
            prop_up = update_response.json()
            df_up = pd.DataFrame([prop_up])
            st.dataframe(df_up.set_index("id"))
            nome: str = st.text_input(
                label="Nome *", key=5301, value=str(df_up.nome[0])
            )
            cpf: str = cpf_input(
                st.text_input(label="CPF", key=5302, value=str(df_up.cpf[0]))
            )
            tel: str = tel_input_br(
                st.text_input(label="Telefone", key=5303, value=str(df_up.tel[0]))
            )
            email: str = st.text_input(
                label="E-Mail", key=5304, value=str(df_up.email[0])
            )
            if st.button("Modificar", key=5305):
                prop_up_data = empty_none_dict(
                    {
                        "nome": nome,
                        "cpf": cpf,
                        "tel": tel,
                        "email": email,
                    }
                )
                try:
                    put_response = requests.put(
                        f"http://api:8000/proprietarios/{update_id}", json=prop_up_data
                    )
                    show_response_message(put_response)
                    if put_response.status_code == 200:
                        st.subheader("Dados inseridos, tudo OK:")
                    else:
                        st.subheader("Dados NÃO inseridos, favor revisar:")
                    show_data_output(prop_up_data)
                except Exception as e:
                    raise (e)
        else:
            show_response_message(update_response)

with tab4:
    st.header("Deletar Proprietário")
    delete_id = st.number_input(
        label="ID Proprietário", min_value=1, value=None, format="%d", step=1, key=5400
    )
    if delete_id:
        show_delete_response = requests.get(
            f"http://api:8000/proprietarios/{delete_id}"
        )
        if show_delete_response.status_code == 200:
            proprietario_delete = show_delete_response.json()
            df_delete = pd.DataFrame([proprietario_delete])
            st.dataframe(df_delete.set_index("id"))
            delete_confirm = st.checkbox("Confirma que deseja deletar o registro?")
            delete_button = st.button("Deletar", key=1401)
            if delete_button and delete_confirm:
                delete_response = requests.delete(
                    f"http://api:8000/proprietarios/{delete_id}"
                )
                show_response_message(delete_response)
            elif delete_button and not delete_confirm:
                st.warning("Você deve confirmar primeiro para deletar o registro")
        else:
            show_response_message(show_delete_response)

with tab5:
    st.header("Listar Proprietários")
    if st.button("Mostrar", key=5500):
        get_list_response = requests.get(f"http://api:8000/proprietarios/")
        if get_list_response.status_code == 200:
            proprietarios = get_list_response.json()
            if proprietarios:
                df_list = pd.DataFrame(proprietarios)
                st.dataframe(df_list.set_index("id"))
            else:
                st.warning("Não há proprietários para listar")
        else:
            show_response_message(get_list_response)
