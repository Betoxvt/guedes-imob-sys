from datetime import date
import json
import pandas as pd
import requests
import streamlit as st
from utils.mydate import calculate_diarias, str_to_date
from utils.myfunc import show_data_output, show_response_message
from utils.mynum import calculate_saldo, calculate_valortotal
from utils.mystr import apto_input, empty_none, empty_none_dict

st.set_page_config(page_title="Aluguéis", layout="wide")
st.title("Aluguéis")

tab1, tab2, tab3, tab4, tab5 = st.tabs(
    ["Registrar", "Consultar", "Modificar", "Deletar", "Listar"]
)

with tab1:
    st.header("Registrar Aluguel")
    st.markdown(
        '<p style="font-size: 12px;">Campos com * são obrigatórios</p>',
        unsafe_allow_html=True,
    )
    apto_id: str = st.text_input(label="ID Apartamento *", value=None, key=1100)
    ficha_id: int = st.number_input(
        label="ID Ficha", min_value=1, value=None, format="%d", step=1, key=1101
    )
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
    if st.button("Registrar", key=1108):
        aluguel_data = empty_none_dict(
            {
                "apto_id": apto_input(apto_id),
                "ficha_id": ficha_id,
                "checkin": checkin.isoformat(),
                "checkout": checkout.isoformat(),
                "diarias": diarias,
                "valor_diaria": valor_diaria,
                "valor_total": valor_total,
            }
        )
        submit_data = json.dumps(obj=aluguel_data, separators=(",", ":"))
        try:
            post_response = requests.post("http://api:8000/alugueis/", submit_data)
            show_response_message(post_response)
            if post_response.status_code == 200:
                st.subheader("Dados inseridos, tudo OK:")
                show_data_output(aluguel_data)
                st.write(empty_none(valor_depositado))
                if empty_none(valor_depositado) is not None:
                    get_top_response = requests.get(
                        "http://api:8000/alugueis/", params={"limit": 1}
                    )
                    if get_top_response.status_code == 200:
                        top_data = get_top_response.json()
                        aluguel_id = top_data[0].get("id")
                        pagamento_data = empty_none_dict(
                            {
                                "tipo": "Entrada",
                                "valor": valor_depositado,
                                "apto_id": apto_input(apto_id),
                                "aluguel_id": aluguel_id,
                                "notas": "Reserva",
                                "nome": None,
                                "contato": None,
                            }
                        )
                        st.write(pagamento_data)
                        post_pagamento_response = requests.post(
                            "http://api:8000/pagamentos/", json=pagamento_data
                        )
                        show_response_message(post_pagamento_response)
                        if post_pagamento_response.status_code == 200:
                            st.subheader("Dados do deposito salvos, tudo OK:")
                            show_data_output(pagamento_data)
                        else:
                            st.subheader("Não foi possível salvar os dados do depósito")
                            show_data_output(pagamento_data)
                    else:
                        st.subheader("Erro ao obter o ID do aluguel")
                        show_response_message(get_top_response)
                else:
                    st.write("Nenhum valor de depósito fornecido.")
            else:
                st.subheader("Dados NÃO inseridos, favor revisar:")
                st.write("Dica: Verifique a ID do apartamento")
                show_data_output(aluguel_data)
        except requests.exceptions.RequestException as e:
            st.error(f"Erro na requisição: {e}")
        except Exception as e:
            st.error(f"Um erro inesperado ocorreu: {e}")

with tab2:
    st.header("Consultar Aluguéis")
    get_id = st.number_input(
        "ID Aluguel", min_value=1, value=None, format="%d", step=1, key=1200
    )
    if get_id:
        get_response = requests.get(f"http://api:8000/alugueis/{get_id}")
        if get_response.status_code == 200:
            aluguel = get_response.json()
            df_get = pd.DataFrame([aluguel])
            st.dataframe(df_get, hide_index=True)
        else:
            show_response_message(get_response)

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
        update_response = requests.get(f"http://api:8000/alugueis/{update_id}")
        if update_response.status_code == 200:
            aluguel_up = update_response.json()
            df_up = pd.DataFrame([aluguel_up])
            st.dataframe(df_up, hide_index=True)
            apto_id: str = st.text_input(
                label="ID Apartamento *", key=1301, value=df_up.apto_id[0]
            )
            ficha_id: int = st.number_input(
                label="ID Ficha",
                min_value=1,
                format="%d",
                step=1,
                key=1302,
                value=df_up.loc[0, "ficha_id"],
            )
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
                key=1306,
            )
            valor_total: float = calculate_valortotal(diarias, valor_diaria)
            valor_depositado: float = st.number_input(
                label="Valor Depositado",
                min_value=0.00,
                max_value=90000.0,
                value=df_up.loc(0, "valor_depositado"),
                format="%0.2f",
                key=1106,
            )
            saldo: float = calculate_saldo(valor_total, valor_depositado)
            if st.button("Modificar"):
                aluguel_up_data = empty_none_dict(
                    {
                        "apto_id": apto_input(apto_id),
                        "ficha_id": ficha_id if ficha_id > 0 else None,
                        "checkin": checkin.isoformat(),
                        "checkout": checkout.isoformat(),
                        "diarias": diarias,
                        "valor_diaria": valor_diaria,
                        "valor_total": valor_total,
                        "valor_depositado": valor_depositado,
                    }
                )
                update_data = json.dumps(obj=aluguel_up_data, separators=(",", ":"))
                try:
                    put_response = requests.put(
                        f"http://api:8000/alugueis/{update_id}", update_data
                    )
                    show_response_message(put_response)
                    if put_response.status_code == 200:
                        st.subheader("Dados inseridos, tudo OK:")
                    else:
                        st.subheader("Dados NÃO inseridos, favor revisar:")
                    show_data_output(aluguel_up_data)
                except Exception as e:
                    raise (e)
        else:
            show_response_message(update_response)

with tab4:
    st.header("Deletar Aluguel")
    delete_id = st.number_input(
        label="ID Aluguel", min_value=1, value=None, format="%d", step=1, key=1400
    )
    if delete_id:
        show_delete_response = requests.get(f"http://api:8000/alugueis/{delete_id}")
        if show_delete_response.status_code == 200:
            aluguel_delete = show_delete_response.json()
            df_delete = pd.DataFrame([aluguel_delete])
            st.dataframe(df_delete.set_index("id"))
            delete_confirm = st.checkbox("Confirma que deseja deletar o registro?")
            delete_button = st.button("Deletar", key=1401)
            if delete_button and delete_confirm:
                delete_response = requests.delete(
                    f"http://api:8000/alugueis/{delete_id}"
                )
                show_response_message(delete_response)
            elif delete_button and not delete_confirm:
                st.warning("Você deve confirmar primeiro para deletar o registro")
        else:
            show_response_message(show_delete_response)

with tab5:
    st.header("Listar Aluguéis")
    if st.button("Mostrar", key=1500):
        get_list_response = requests.get(f"http://api:8000/alugueis/")
        if get_list_response.status_code == 200:
            alugueis = get_list_response.json()
            if alugueis:
                df_list = pd.DataFrame(alugueis)
                st.dataframe(df_list.set_index("id"))
            else:
                st.warning("Não há alugueis para listar")
        else:
            show_response_message(get_list_response)
