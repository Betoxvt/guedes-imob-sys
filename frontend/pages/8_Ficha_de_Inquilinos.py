import pandas as pd
import requests
import streamlit as st
from datetime import date


# Função para preencher valores None de acompanhantes
def null_acomp(init: int, acomp_dict: dict) -> dict:
    for i in range(init+1,11):
        acomp_dict[f'acomp_{i:02d}_nome'] = None
        acomp_dict[f'acomp_{i:02d}_rg'] = None
        acomp_dict[f'acomp_{i:02d}_cpf'] = None
        acomp_dict[f'acomp_{i:02d}_idade'] = None
        acomp_dict[f'acomp_{i:02d}_parentesco'] = None

    return acomp_dict


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

st.set_page_config(
    page_title='Ficha de Inquilinos',
    layout='wide'
)
st.title('Ficha de Inquilinos')
st.sidebar.markdown('# Inquilinos')

tab1, tab2, tab3, tab4, tab5 = st.tabs(['Registrar', 'Consultar', 'Modificar', 'Deletar', 'Listar'])

# Em registrar deve ser possível fazer upload de um arquivo ou forms essas coisas que o inquilino pode já ter preenchido em casa e enviado para nós (google forms ou sei lá)

# Em consultar, deve ser possível então exportar a ficha em pdf no modelo proposto pelo condomínio

with tab1:
    st.header('Registrar')
    with st.form('new_inquilino'):
        apartamento = st.text_input('Apartamento alugado')
        nome = st.text_input('Nome completo')
        tipo_residencia = st.radio(
            label='Tipo de residência',
            options=['Anual', 'Temporária'],
            index=1
        )
        cidade = st.text_input('Naturalidade (cidade)')
        cep = st.number_input(
            label='CEP',
            value=int,
            format='%08d',
            help='Somente números'
        )
        estado = st.text_input('Estado (UF)')
        pais = st.text_input('País')
        telefone = st.number_input(
            label='Telefone',
            value=int,
            help='Somente números: ddi+ddd+numero'
        )
        estado_civil = st.selectbox(
            label='Estado civíl',
            options=['Solteiro', 'Casado', 'Separado', 'Divorciado', 'Viúvo']
        )
        profissao = st.text_input('Profissão')
        rg = st.number_input(
            laber='Identidade',
            value=None,
            help='Somente números'
        )
        cpf = st.number_input(
            label='CPF',
            value=int,
            help='Somente números'
        )
        mae = st.text_input('Nome completo da mãe')
        check_automovel = st.radio(
            label='Com automóvel?',
            options=['Sim', 'Não']
        )

        if check_automovel == 'Sim':
            automovel = st.text_input('Automóvel')
            modelo_auto = st.text_input('Modelo')
            placa_auto = st.text_input('Placa')
            cor_auto = st.text_input('Cor')
        else:
            automovel = None
            modelo_auto = None
            placa_auto = None
            cor_auto = None
        
        checkin = st.date_input(
            label='Check-in',
            value='today',
            min_value=date('2022, 01, 01'),
            format='DD/MM/YYYY'
        )
        checkout = st.date_input(
            label='Check-out',
            value='today',
            min_value=date('2022, 01, 01'),
            format='DD/MM/YYYY'
        )
        observacoes = st.text_area(
            label='Observações',
            value=None
        )
        proprietario = st.text_input('Proprietário')
        imob_fone = st.number_input(
            label='Telefone Imobiliária',
            value = 3311112222
        )
        qtd_acomp = st.select_slider(
            label='Quantidade de acompanhantes',
            options=(0,1,2,3,4,5,6,7,8,9,10),
            value=0
        )

        acomp_dict = {}

        match qtd_acomp:
            case 0:

                acomp_dict = null_acomp(init=qtd_acomp, acomp_dict=acomp_dict)

            case 1:
                
                st.subheader('Acompanhante 01')
                acomp_01_nome = st.text_input('Nome')
                acomp_01_rg = st.number_input('RG')
                acomp_01_cpf = st.number_input('CPF')
                acomp_01_idade = st.number_input('Idade')
                acomp_01_parentesco = st.number_input('Parentesco')

                acomp_dict = null_acomp(init=qtd_acomp, acomp_dict=acomp_dict)


        acomp_02_nome
        acomp_02_rg
        acomp_02_cpf
        acomp_02_idade
        acomp_02_parentesco
        acomp_03_nome
        acomp_03_rg
        acomp_03_cpf
        acomp_03_idade
        acomp_03_parentesco
        acomp_04_nome
        acomp_04_rg
        acomp_04_cpf
        acomp_04_idade
        acomp_04_parentesco
        acomp_05_nome
        acomp_05_rg
        acomp_05_cpf
        acomp_05_idade
        acomp_05_parentesco
        acomp_06_nome
        acomp_06_rg
        acomp_06_cpf
        acomp_06_idade
        acomp_06_parentesco
        acomp_07_nome    
        acomp_07_rg
        acomp_07_cpf
        acomp_07_idade
        acomp_07_parentesco
        acomp_08_nome
        acomp_08_rg
        acomp_08_cpf
        acomp_08_idade
        acomp_08_parentesco
        acomp_09_nome
        acomp_09_rg
        acomp_09_cpf
        acomp_09_idade
        acomp_09_parentesco
        acomp_10_nome
        acomp_10_rg
        acomp_10_cpf
        acomp_10_idade
        acomp_10_parentesco

        

    
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

            st.dataframe(df, hide_index=True)
        else:
            show_response_message(response)

with tab3:
    st.header('Modificar')

with tab4:
    st.header('Deletar')

with tab5:
    st.header('Listar')