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


# Função de chaves para variáveis
def key_to_var(dictionary):
    """
    Converts keys of a dictionary to variables in the local scope.

    Args:
        dictionary: The dictionary whose keys will be converted to variables.

    Returns:
        None
    """
    for k in dictionary:
        exec('{KEY} = {VALUE}'.format(KEY=k, VALUE=repr(dictionary[k])))
    return None


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

                key_to_var(acomp_dict)
            
            case 2:

                st.subheader('Acompanhante 01')
                acomp_01_nome = st.text_input('Nome')
                acomp_01_rg = st.number_input('RG')
                acomp_01_cpf = st.number_input('CPF')
                acomp_01_idade = st.number_input('Idade')
                acomp_01_parentesco = st.number_input('Parentesco')

                st.subheader('Acompanhante 02')
                acomp_02_nome = st.text_input('Nome')
                acomp_02_rg = st.number_input('RG')
                acomp_02_cpf = st.number_input('CPF')
                acomp_02_idade = st.number_input('Idade')
                acomp_02_parentesco = st.number_input('Parentesco')

                acomp_dict = null_acomp(init=qtd_acomp, acomp_dict=acomp_dict)

                key_to_var(acomp_dict)

            case 3:

                st.subheader('Acompanhante 01')
                acomp_01_nome = st.text_input('Nome')
                acomp_01_rg = st.number_input('RG')
                acomp_01_cpf = st.number_input('CPF')
                acomp_01_idade = st.number_input('Idade')
                acomp_01_parentesco = st.number_input('Parentesco')

                st.subheader('Acompanhante 02')
                acomp_02_nome = st.text_input('Nome')
                acomp_02_rg = st.number_input('RG')
                acomp_02_cpf = st.number_input('CPF')
                acomp_02_idade = st.number_input('Idade')
                acomp_02_parentesco = st.number_input('Parentesco')

                st.subheader('Acompanhante 03')
                acomp_03_nome = st.text_input('Nome')
                acomp_03_rg = st.number_input('RG')
                acomp_03_cpf = st.number_input('CPF')
                acomp_03_idade = st.number_input('Idade')
                acomp_03_parentesco = st.number_input('Parentesco')

                acomp_dict = null_acomp(init=qtd_acomp, acomp_dict=acomp_dict)

                key_to_var(acomp_dict)

            case 4:

                st.subheader('Acompanhante 01')
                acomp_01_nome = st.text_input('Nome')
                acomp_01_rg = st.number_input('RG')
                acomp_01_cpf = st.number_input('CPF')
                acomp_01_idade = st.number_input('Idade')
                acomp_01_parentesco = st.number_input('Parentesco')

                st.subheader('Acompanhante 02')
                acomp_02_nome = st.text_input('Nome')
                acomp_02_rg = st.number_input('RG')
                acomp_02_cpf = st.number_input('CPF')
                acomp_02_idade = st.number_input('Idade')
                acomp_02_parentesco = st.number_input('Parentesco')

                st.subheader('Acompanhante 03')
                acomp_03_nome = st.text_input('Nome')
                acomp_03_rg = st.number_input('RG')
                acomp_03_cpf = st.number_input('CPF')
                acomp_03_idade = st.number_input('Idade')
                acomp_03_parentesco = st.number_input('Parentesco')

                st.subheader('Acompanhante 04')
                acomp_04_nome = st.text_input('Nome')
                acomp_04_rg = st.number_input('RG')
                acomp_04_cpf = st.number_input('CPF')
                acomp_04_idade = st.number_input('Idade')
                acomp_04_parentesco = st.number_input('Parentesco')

                acomp_dict = null_acomp(init=qtd_acomp, acomp_dict=acomp_dict)

                key_to_var(acomp_dict)

            case 5:

                st.subheader('Acompanhante 01')
                acomp_01_nome = st.text_input('Nome')
                acomp_01_rg = st.number_input('RG')
                acomp_01_cpf = st.number_input('CPF')
                acomp_01_idade = st.number_input('Idade')
                acomp_01_parentesco = st.number_input('Parentesco')

                st.subheader('Acompanhante 02')
                acomp_02_nome = st.text_input('Nome')
                acomp_02_rg = st.number_input('RG')
                acomp_02_cpf = st.number_input('CPF')
                acomp_02_idade = st.number_input('Idade')
                acomp_02_parentesco = st.number_input('Parentesco')

                st.subheader('Acompanhante 03')
                acomp_03_nome = st.text_input('Nome')
                acomp_03_rg = st.number_input('RG')
                acomp_03_cpf = st.number_input('CPF')
                acomp_03_idade = st.number_input('Idade')
                acomp_03_parentesco = st.number_input('Parentesco')

                st.subheader('Acompanhante 04')
                acomp_04_nome = st.text_input('Nome')
                acomp_04_rg = st.number_input('RG')
                acomp_04_cpf = st.number_input('CPF')
                acomp_04_idade = st.number_input('Idade')
                acomp_04_parentesco = st.number_input('Parentesco')

                st.subheader('Acompanhante 05')
                acomp_05_nome = st.text_input('Nome')
                acomp_05_rg = st.number_input('RG')
                acomp_05_cpf = st.number_input('CPF')
                acomp_05_idade = st.number_input('Idade')
                acomp_05_parentesco = st.number_input('Parentesco')

                acomp_dict = null_acomp(init=qtd_acomp, acomp_dict=acomp_dict)

                key_to_var(acomp_dict)

            case 6:

                st.subheader('Acompanhante 01')
                acomp_01_nome = st.text_input('Nome')
                acomp_01_rg = st.number_input('RG')
                acomp_01_cpf = st.number_input('CPF')
                acomp_01_idade = st.number_input('Idade')
                acomp_01_parentesco = st.number_input('Parentesco')

                st.subheader('Acompanhante 02')
                acomp_02_nome = st.text_input('Nome')
                acomp_02_rg = st.number_input('RG')
                acomp_02_cpf = st.number_input('CPF')
                acomp_02_idade = st.number_input('Idade')
                acomp_02_parentesco = st.number_input('Parentesco')

                st.subheader('Acompanhante 03')
                acomp_03_nome = st.text_input('Nome')
                acomp_03_rg = st.number_input('RG')
                acomp_03_cpf = st.number_input('CPF')
                acomp_03_idade = st.number_input('Idade')
                acomp_03_parentesco = st.number_input('Parentesco')

                st.subheader('Acompanhante 04')
                acomp_04_nome = st.text_input('Nome')
                acomp_04_rg = st.number_input('RG')
                acomp_04_cpf = st.number_input('CPF')
                acomp_04_idade = st.number_input('Idade')
                acomp_04_parentesco = st.number_input('Parentesco')

                st.subheader('Acompanhante 05')
                acomp_05_nome = st.text_input('Nome')
                acomp_05_rg = st.number_input('RG')
                acomp_05_cpf = st.number_input('CPF')
                acomp_05_idade = st.number_input('Idade')
                acomp_05_parentesco = st.number_input('Parentesco')

                st.subheader('Acompanhante 06')
                acomp_06_nome = st.text_input('Nome')
                acomp_06_rg = st.number_input('RG')
                acomp_06_cpf = st.number_input('CPF')
                acomp_06_idade = st.number_input('Idade')
                acomp_06_parentesco = st.number_input('Parentesco')

                acomp_dict = null_acomp(init=qtd_acomp, acomp_dict=acomp_dict)

                key_to_var(acomp_dict)

            case 7:

                
                st.subheader('Acompanhante 01')
                acomp_01_nome = st.text_input('Nome')
                acomp_01_rg = st.number_input('RG')
                acomp_01_cpf = st.number_input('CPF')
                acomp_01_idade = st.number_input('Idade')
                acomp_01_parentesco = st.number_input('Parentesco')

                st.subheader('Acompanhante 02')
                acomp_02_nome = st.text_input('Nome')
                acomp_02_rg = st.number_input('RG')
                acomp_02_cpf = st.number_input('CPF')
                acomp_02_idade = st.number_input('Idade')
                acomp_02_parentesco = st.number_input('Parentesco')

                st.subheader('Acompanhante 03')
                acomp_03_nome = st.text_input('Nome')
                acomp_03_rg = st.number_input('RG')
                acomp_03_cpf = st.number_input('CPF')
                acomp_03_idade = st.number_input('Idade')
                acomp_03_parentesco = st.number_input('Parentesco')

                st.subheader('Acompanhante 04')
                acomp_04_nome = st.text_input('Nome')
                acomp_04_rg = st.number_input('RG')
                acomp_04_cpf = st.number_input('CPF')
                acomp_04_idade = st.number_input('Idade')
                acomp_04_parentesco = st.number_input('Parentesco')

                st.subheader('Acompanhante 05')
                acomp_05_nome = st.text_input('Nome')
                acomp_05_rg = st.number_input('RG')
                acomp_05_cpf = st.number_input('CPF')
                acomp_05_idade = st.number_input('Idade')
                acomp_05_parentesco = st.number_input('Parentesco')

                st.subheader('Acompanhante 06')
                acomp_06_nome = st.text_input('Nome')
                acomp_06_rg = st.number_input('RG')
                acomp_06_cpf = st.number_input('CPF')
                acomp_06_idade = st.number_input('Idade')
                acomp_06_parentesco = st.number_input('Parentesco')

                st.subheader('Acompanhante 07')
                acomp_07_nome = st.text_input('Nome')
                acomp_07_rg = st.number_input('RG')
                acomp_07_cpf = st.number_input('CPF')
                acomp_07_idade = st.number_input('Idade')
                acomp_07_parentesco = st.number_input('Parentesco')

                acomp_dict = null_acomp(init=qtd_acomp, acomp_dict=acomp_dict)

                key_to_var(acomp_dict)

            case 8:

                st.subheader('Acompanhante 01')
                acomp_01_nome = st.text_input('Nome')
                acomp_01_rg = st.number_input('RG')
                acomp_01_cpf = st.number_input('CPF')
                acomp_01_idade = st.number_input('Idade')
                acomp_01_parentesco = st.number_input('Parentesco')

                st.subheader('Acompanhante 02')
                acomp_02_nome = st.text_input('Nome')
                acomp_02_rg = st.number_input('RG')
                acomp_02_cpf = st.number_input('CPF')
                acomp_02_idade = st.number_input('Idade')
                acomp_02_parentesco = st.number_input('Parentesco')

                st.subheader('Acompanhante 03')
                acomp_03_nome = st.text_input('Nome')
                acomp_03_rg = st.number_input('RG')
                acomp_03_cpf = st.number_input('CPF')
                acomp_03_idade = st.number_input('Idade')
                acomp_03_parentesco = st.number_input('Parentesco')

                st.subheader('Acompanhante 04')
                acomp_04_nome = st.text_input('Nome')
                acomp_04_rg = st.number_input('RG')
                acomp_04_cpf = st.number_input('CPF')
                acomp_04_idade = st.number_input('Idade')
                acomp_04_parentesco = st.number_input('Parentesco')

                st.subheader('Acompanhante 05')
                acomp_05_nome = st.text_input('Nome')
                acomp_05_rg = st.number_input('RG')
                acomp_05_cpf = st.number_input('CPF')
                acomp_05_idade = st.number_input('Idade')
                acomp_05_parentesco = st.number_input('Parentesco')

                st.subheader('Acompanhante 06')
                acomp_06_nome = st.text_input('Nome')
                acomp_06_rg = st.number_input('RG')
                acomp_06_cpf = st.number_input('CPF')
                acomp_06_idade = st.number_input('Idade')
                acomp_06_parentesco = st.number_input('Parentesco')

                st.subheader('Acompanhante 07')
                acomp_07_nome = st.text_input('Nome')
                acomp_07_rg = st.number_input('RG')
                acomp_07_cpf = st.number_input('CPF')
                acomp_07_idade = st.number_input('Idade')
                acomp_07_parentesco = st.number_input('Parentesco')

                st.subheader('Acompanhante 08')
                acomp_08_nome = st.text_input('Nome')
                acomp_08_rg = st.number_input('RG')
                acomp_08_cpf = st.number_input('CPF')
                acomp_08_idade = st.number_input('Idade')
                acomp_08_parentesco = st.number_input('Parentesco')

                acomp_dict = null_acomp(init=qtd_acomp, acomp_dict=acomp_dict)

                key_to_var(acomp_dict)

            case 9:

                st.subheader('Acompanhante 01')
                acomp_01_nome = st.text_input('Nome')
                acomp_01_rg = st.number_input('RG')
                acomp_01_cpf = st.number_input('CPF')
                acomp_01_idade = st.number_input('Idade')
                acomp_01_parentesco = st.number_input('Parentesco')

                st.subheader('Acompanhante 02')
                acomp_02_nome = st.text_input('Nome')
                acomp_02_rg = st.number_input('RG')
                acomp_02_cpf = st.number_input('CPF')
                acomp_02_idade = st.number_input('Idade')
                acomp_02_parentesco = st.number_input('Parentesco')

                st.subheader('Acompanhante 03')
                acomp_03_nome = st.text_input('Nome')
                acomp_03_rg = st.number_input('RG')
                acomp_03_cpf = st.number_input('CPF')
                acomp_03_idade = st.number_input('Idade')
                acomp_03_parentesco = st.number_input('Parentesco')

                st.subheader('Acompanhante 04')
                acomp_04_nome = st.text_input('Nome')
                acomp_04_rg = st.number_input('RG')
                acomp_04_cpf = st.number_input('CPF')
                acomp_04_idade = st.number_input('Idade')
                acomp_04_parentesco = st.number_input('Parentesco')

                st.subheader('Acompanhante 05')
                acomp_05_nome = st.text_input('Nome')
                acomp_05_rg = st.number_input('RG')
                acomp_05_cpf = st.number_input('CPF')
                acomp_05_idade = st.number_input('Idade')
                acomp_05_parentesco = st.number_input('Parentesco')

                st.subheader('Acompanhante 06')
                acomp_06_nome = st.text_input('Nome')
                acomp_06_rg = st.number_input('RG')
                acomp_06_cpf = st.number_input('CPF')
                acomp_06_idade = st.number_input('Idade')
                acomp_06_parentesco = st.number_input('Parentesco')

                st.subheader('Acompanhante 07')
                acomp_07_nome = st.text_input('Nome')
                acomp_07_rg = st.number_input('RG')
                acomp_07_cpf = st.number_input('CPF')
                acomp_07_idade = st.number_input('Idade')
                acomp_07_parentesco = st.number_input('Parentesco')

                st.subheader('Acompanhante 08')
                acomp_08_nome = st.text_input('Nome')
                acomp_08_rg = st.number_input('RG')
                acomp_08_cpf = st.number_input('CPF')
                acomp_08_idade = st.number_input('Idade')
                acomp_08_parentesco = st.number_input('Parentesco')

                st.subheader('Acompanhante 09')
                acomp_09_nome = st.text_input('Nome')
                acomp_09_rg = st.number_input('RG')
                acomp_09_cpf = st.number_input('CPF')
                acomp_09_idade = st.number_input('Idade')
                acomp_09_parentesco = st.number_input('Parentesco')

                acomp_dict = null_acomp(init=qtd_acomp, acomp_dict=acomp_dict)

                key_to_var(acomp_dict)

            case 10:

                st.subheader('Acompanhante 01')
                acomp_01_nome = st.text_input('Nome')
                acomp_01_rg = st.number_input('RG')
                acomp_01_cpf = st.number_input('CPF')
                acomp_01_idade = st.number_input('Idade')
                acomp_01_parentesco = st.number_input('Parentesco')

                st.subheader('Acompanhante 02')
                acomp_02_nome = st.text_input('Nome')
                acomp_02_rg = st.number_input('RG')
                acomp_02_cpf = st.number_input('CPF')
                acomp_02_idade = st.number_input('Idade')
                acomp_02_parentesco = st.number_input('Parentesco')

                st.subheader('Acompanhante 03')
                acomp_03_nome = st.text_input('Nome')
                acomp_03_rg = st.number_input('RG')
                acomp_03_cpf = st.number_input('CPF')
                acomp_03_idade = st.number_input('Idade')
                acomp_03_parentesco = st.number_input('Parentesco')

                st.subheader('Acompanhante 04')
                acomp_04_nome = st.text_input('Nome')
                acomp_04_rg = st.number_input('RG')
                acomp_04_cpf = st.number_input('CPF')
                acomp_04_idade = st.number_input('Idade')
                acomp_04_parentesco = st.number_input('Parentesco')

                st.subheader('Acompanhante 05')
                acomp_05_nome = st.text_input('Nome')
                acomp_05_rg = st.number_input('RG')
                acomp_05_cpf = st.number_input('CPF')
                acomp_05_idade = st.number_input('Idade')
                acomp_05_parentesco = st.number_input('Parentesco')

                st.subheader('Acompanhante 06')
                acomp_06_nome = st.text_input('Nome')
                acomp_06_rg = st.number_input('RG')
                acomp_06_cpf = st.number_input('CPF')
                acomp_06_idade = st.number_input('Idade')
                acomp_06_parentesco = st.number_input('Parentesco')

                st.subheader('Acompanhante 07')
                acomp_07_nome = st.text_input('Nome')
                acomp_07_rg = st.number_input('RG')
                acomp_07_cpf = st.number_input('CPF')
                acomp_07_idade = st.number_input('Idade')
                acomp_07_parentesco = st.number_input('Parentesco')

                st.subheader('Acompanhante 08')
                acomp_08_nome = st.text_input('Nome')
                acomp_08_rg = st.number_input('RG')
                acomp_08_cpf = st.number_input('CPF')
                acomp_08_idade = st.number_input('Idade')
                acomp_08_parentesco = st.number_input('Parentesco')

                st.subheader('Acompanhante 09')
                acomp_09_nome = st.text_input('Nome')
                acomp_09_rg = st.number_input('RG')
                acomp_09_cpf = st.number_input('CPF')
                acomp_09_idade = st.number_input('Idade')
                acomp_09_parentesco = st.number_input('Parentesco')

                st.subheader('Acompanhante 10')
                acomp_10_nome = st.text_input('Nome')
                acomp_10_rg = st.number_input('RG')
                acomp_10_cpf = st.number_input('CPF')
                acomp_10_idade = st.number_input('Idade')
                acomp_10_parentesco = st.number_input('Parentesco')

                

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