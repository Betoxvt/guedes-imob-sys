import pandas as pd
import requests
import streamlit as st

st.set_page_config(
    page_title='Ficha de Inquilinos',
    layout='wide'
)
st.title('Ficha de Inquilinos')
st.sidebar.markdown('# Inquilinos')

# Função auxiliar para exibir mensagens de erro detalhadas
def show_response_message(response):
    if response.status_code == 200:
        st.success('Operação realizada com sucesso!')
    else:
        try:
            data = response.json()
            if 'detail' in data:
                # Se o erro for uma lista, extraia as mensagens de cada erro
                if isinstance(data['detail'], list):
                    errors = '\n'.join([error['msg'] for error in data['detail']])
                    st.error(f'Erro: {errors}')
                else:
                    # Caso contrário, mostre a mensagem de erro diretamente
                    st.error(f'Erro: {data["detail"]}')
        except ValueError:
            st.error('Erro desconhecido. Não foi possível decodificar a resposta.')

tab1, tab2, tab3, tab4, tab5 = st.tabs(['Registrar', 'Consultar', 'Modificar', 'Deletar', 'Listar'])


# Em registrar deve ser possível fazer upload de um arquivo ou forms essas coisas que o inquilino pode já ter preenchido em casa e enviado para nós (google forms ou sei lá)

# Em consultar, deve ser possível então exportar a ficha em pdf no modelo proposto pelo condomínio

with tab2:
    st.header('Consultar')
    get_id = st.number_input('ID da Ficha de Inquilino', min_value=1, format='%d')
    if st.button('Buscar Ficha de Inquilino'):
        response = requests.get(f'http://backend:8000/inquilinos/{get_id}')
        if response.status_code == 200:
            ficha = response.json()
            ficha_filtered = {key: value for key, value in ficha.items() if value}

            columns = [
                "id",
                "apartamento",
                "nome",
                "tipo_residencia",
                "cidade",
                "cep",
                "estado",
                "pais",
                "telefone",
                "estado_civil",
                "profissão",
                "rg",
                "cpf",
                "mae",
                "automovel",
                "modelo_auto",
                "placa_auto",
                "cor_auto",
                "checkin",
                "checkout",
                "observacoes",
            ]

            ficha_filtered = {key: ficha_filtered.get(key, "") for key in columns}

            df = pd.DataFrame([ficha_filtered])

            st.write(df.to_html(index=False), unsafe_allow_html=True)
        else:
            show_response_message(response)