from datetime import date, timedelta
import json
import pandas as pd
import requests
import streamlit as st
from src.functions import show_response_message, string_to_date

st.set_page_config(
    page_title='Aluguéis',
    layout='wide'
)
st.title('Aluguéis')

tab1, tab2, tab3, tab4, tab5 = st.tabs(['Registrar', 'Consultar', 'Modificar', 'Deletar', 'Listar'])

with tab1:
    st.header('Registrar Aluguel')
    with st.form('new_aluguel'):
        apto_id: int = st.number_input(
            label='ID Apartamento',
            min_value=1,
            format='%d',
            step=1,
            key=1009
        )
        ficha_id: int = st.number_input(
            label='ID Ficha',
            min_value=1,
            format='%d',
            step=1,
            key=1010
        )
        checkin: str | date = st.date_input(
            label='Check-in',
            min_value=date(2024, 1, 1),
            max_value=date.today() + timedelta(days=360),
            value=date.today(),
            format='DD/MM/YYYY',
            key=1011
        )

        if isinstance(checkin, date):
            min_checkout = checkin + timedelta(days=1)
        else:
            min_checkout = None

        checkout: str | date = st.date_input(
            label='Check-out',
            min_value=min_checkout,
            max_value=date.today() + timedelta(days=360),
            format='DD/MM/YYYY',
            key=1012
        )

        diarias: int = 0
        if isinstance(checkin, date) and isinstance(checkout, date):
            diferenca = (checkout - checkin).days
            if diferenca >= 1:
                diarias = diferenca
            else:
                st.warning("A data de check-out deve ser posterior à data de check-in.")

        st.number_input(
            label='Diárias',
            min_value=1,
            max_value=365,
            value=diarias,
            format='%d',
            step=1,
            key=1013,
            disabled=True
        )
        valor_diaria: float = st.number_input(
            label='Valor da diária',
            min_value=0.00,
            max_value=3000.00,
            value=0.00,
            format='%0.2f',
            step=10.00,
            key=1014
        )

        valor_total: float = 0.00
        if diarias > 0 and valor_diaria > 0:
            valor_total = diarias * valor_diaria

        st.number_input(
        label='Valor total',
        value=valor_total,
        format='%0.2f',
        disabled=True,
        key=1015
        )

        submit_button = st.form_submit_button('Registrar')
        if submit_button:
            registry = {
                    "apto_id": apto_id,
                    "ficha_id": ficha_id,
                    "checkin": checkin.isoformat(),
                    "checkout": checkout.isoformat(),
                    "diarias": diarias,
                    "valor_diaria": valor_diaria,
                    "valor_total": valor_total
                }
            registry_json = json.dumps(obj=registry, indent=1, separators=(',',':'))
            response = requests.post("http://backend:8000/alugueis/", registry_json)
            show_response_message(response)

with tab2:
    st.header('Consultar Aluguéis')
    get_id = st.number_input(
        'ID Aluguel',
        min_value=1,
        format='%d',
        step=1,
        key=1000
    )
    if get_id:
        response = requests.get(f'http://backend:8000/alugueis/{get_id}')
        if response.status_code == 200:
            aluguel = response.json()
            df = pd.DataFrame([aluguel])
            st.dataframe(df, hide_index=True)
        else:
            show_response_message(response)

with tab3:
    st.header('Modificar Aluguel')
    update_id = st.number_input(
        'ID do Aluguel',
        min_value=1,
        format='%d',
        key=1001
    )
    if update_id:
        response = requests.get(f'http://backend:8000/alugueis/{update_id}')
        if response.status_code == 200:
            aluguel_viz = response.json()
            df = pd.DataFrame([aluguel_viz])
            st.dataframe(df, hide_index=True)
            with st.form('update_aluguel'):
                apto_id: int = st.number_input(
                    label='ID Apartamento',
                    min_value=1,
                    format='%d',
                    step=1,
                    key=1309,
                    value=df.loc[0, 'apto_id']
                )
                ficha_id: int = st.number_input(
                    label='ID Ficha',
                    min_value=1,
                    format='%d',
                    step=1,
                    key=1310,
                    value=df.loc[0, 'ficha_id']
                )
                checkin: str | date = st.date_input(
                    label='Check-in',
                    min_value=date(2024, 1, 1),
                    max_value=date.today() + timedelta(days=360),
                    value=string_to_date(df.checkin[0]),
                    format='DD/MM/YYYY',
                    key=1311
                )

                if isinstance(checkin, date):
                    min_checkout = checkin + timedelta(days=1)
                else:
                    min_checkout = None

                checkout: str | date = st.date_input(
                    label='Check-out',
                    min_value=min_checkout,
                    max_value=date.today() + timedelta(days=360),
                    value=string_to_date(df.checkout[0]),
                    format='DD/MM/YYYY',
                    key=1312
                )

                diarias: int = 0
                if isinstance(checkin, date) and isinstance(checkout, date):
                    diferenca = (checkout - checkin).days
                    if diferenca >= 1:
                        diarias = diferenca
                    else:
                        st.warning("A data de check-out deve ser posterior à data de check-in.")

                st.number_input(
                    label='Diárias',
                    min_value=1,
                    max_value=365,
                    value=diarias,
                    format='%d',
                    step=1,
                    key=1313,
                    disabled=True
                )
                valor_diaria: float = st.number_input(
                    label='Valor da diária',
                    min_value=0.00,
                    max_value=3000.00,
                    value=df.loc[0, 'valor_diaria'],
                    format='%0.2f',
                    step=10.00,
                    key=1314
                )

                valor_total: float = 0.00
                if diarias > 0 and valor_diaria > 0:
                    valor_total = diarias * valor_diaria

                st.number_input(
                label='Valor total',
                value=valor_total,
                format='%0.2f',
                disabled=True,
                key=1315
                )
                update_button = st.form_submit_button('Modificar')
                if update_button:
                    updated = {
                        "apto_id": apto_id,
                        "ficha_id": ficha_id,
                        "checkin": checkin.isoformat(),
                        "checkout": checkout.isoformat(),
                        "diarias": diarias,
                        "valor_diaria": valor_diaria,
                        "valor_total": valor_total
                    }
                    updated_json = json.dumps(obj=updated, indent=1, separators=(',',':'))
                    response = requests.put(f"http://backend:8000/alugueis/{update_id}", updated_json)
                    show_response_message(response)
        else:
            show_response_message(response)

with tab4:
    st.header('Deletar Aluguel')
    delete_id = st.number_input(
        label="ID Aluguel",
        min_value=1,
        step=1,
        format='%d',
        key=1402
    )
    if delete_id:
        response = requests.get(f'http://backend:8000/alugueis/{delete_id}')
        if response.status_code == 200:
            aluguel_viz = response.json()
            df = pd.DataFrame([aluguel_viz])
            st.dataframe(df, hide_index=True)
            if st.button(
                'Deletar',
                key=1006
            ):
                response = requests.delete(f'http://backend:8000/alugueis/{delete_id}')
                show_response_message(response)
        else:
            show_response_message(response)

with tab5:
    st.header('Listar Aluguéis')
    if st.button(
        "Mostrar",
        key=1007
    ):
        response = requests.get(f'http://backend:8000/alugueis/')
        if response.status_code == 200:
            alugueis = response.json()
            df = pd.DataFrame(alugueis)
            st.dataframe(df, hide_index=True)
        else:
            show_response_message(response)