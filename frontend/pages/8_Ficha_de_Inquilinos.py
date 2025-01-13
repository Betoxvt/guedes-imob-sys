import pandas as pd
import requests
import streamlit as st
from datetime import date, timedelta


def convert_empty_to_none():
    """Converts global empty strings to None."""
    global_vars = globals().copy()
    for var_name, var_value in global_vars.items():
        if var_name.startswith("__") or callable(var_value) or isinstance(var_value, type(convert_empty_to_none)):
            continue
        if isinstance(var_value, str) and var_value == "":
            globals()[var_name] = None


def show_response_message(response) -> None:
    if response.status_code == 200:
        st.success('Operação realizada com sucesso!')
    else:
        try:
            data = response.json()
            if 'detail' in data:
                if isinstance(data['detail'], list):
                    errors = '\n'.join([error['msg'] for error in data['detail']])
                    st.error(f'Erro: {errors}')
                else:
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
    st.header('Registrar uma Ficha de Inquilino')
    with st.form('new_inquilino'):
        apartamento = st.text_input(
            label='Apartamento alugado',
            value=None,
            key=8001
        )
        nome = st.text_input(
            label='Nome completo',
            value=None,
            key=8002
        )
        tipo_residencia = st.radio(
            label='Tipo de residência',
            options=['Anual', 'Temporária'],
            index=None,
            horizontal=True,
            key=8003
        )
        cidade = st.text_input(
            label='Naturalidade (cidade)',
            value=None,
            key=8004
        )
        cep_input = st.text_input(
            label='CEP',
            help='Somente números',
            value=None,
            key=8005
        )
        if cep_input:
                cep = cep_input.replace('-', '')
                if cep.isdigit() and len(cep) == 8:
                    st.success(f'CEP válido: {cep_input}')
                else:
                    st.error('O CEP deve conter exatamente 8 dígitos')
        estado = st.text_input(
            label='Estado (UF)',
            max_chars=2,
            value=None,
            key=8006
        )
        pais = st.text_input(
            label='País',
            value=None,
            key=8007
        )
        telefone_input = st.text_input(
            label='Telefone',
            help='Somente números: +DDI (DDD) 0 0000-0000',
            value=None,
            key=8008
        )
        if telefone_input:
            telefone = telefone_input.replace('+', '').replace('-', '').replace(' ', '').replace('(', '').replace(')', '')
            if telefone.isdigit() and len(telefone) == 13:
                st.success(f'Telefone válido: {telefone_input}')
            else:
                st.error('O telefone deve conter exatamente 9 dígitos.')
        estado_civil = st.selectbox(
            label='Estado civíl',
            index=None,
            placeholder='Selecione uma opção',
            options=['Solteiro', 'Casado', 'Separado', 'Divorciado', 'Viúvo'],
            key=8009
        )
        profissao = st.text_input(
            label='Profissão',
            value=None,
            key=8010
        )
        rg_input = st.text_input(
            label='Identidade',
            help='Somente números no formato XXX.XXX.XXX-X',
            value=None,
            key=8011
        )
        if rg_input:
            rg = rg_input.replace('.', '').replace('-', '')
            if rg.isdigit() and (len(rg) >= 8 and len(rg) <= 10):
                st.success(f'RG válido: {rg_input}')
            else:
                st.error('O RG deve conter entre 8 e 10 dígitos.')
        cpf_input = st.text_input(
            label='CPF',
            help='Somente números',
            value=None,
            key=8012
        )
        if cpf_input:
            cpf = cpf_input.replace('.', '').replace('-', '')
            if cpf.isdigit() and len(cpf) == 11:
                st.success(f'CPF válido: {cpf_input}')
            else:
                st.error('O CPF deve conter exatamente 11 dígitos.')
        mae = st.text_input(
            label='Nome completo da mãe',
            value=None,
            key=8013
        )        
        automovel = st.text_input(
            label='Automóvel',
            value=None,
            key=8014
        )
        modelo_auto = st.text_input(
            label='Modelo',
            value=None,
            key=8015
        )
        placa_auto = st.text_input(
            label='Placa',
            value=None,
            key=8016
        )
        cor_auto = st.text_input(
            label='Cor',
            value=None,
            key=8017
        )
        checkin = st.date_input(
            label='Check-in',
            min_value=date(2022, 1, 1),
            max_value=date.today()+timedelta(days=300),
            format='DD/MM/YYYY',
            key=8018
        )
        checkout = st.date_input(
            label='Check-out',
            min_value=checkin+timedelta(days=1),
            max_value=date.today()+timedelta(days=300),
            format='DD/MM/YYYY',
            key=8019
        )
        observacoes = st.text_area(
            label='Observações',
            value=None,
            key=8020
        )
        proprietario = st.text_input(
            label='Proprietário',
            value=None,
            key=8021
        )
        imob_fone = st.text_input(
            label='Telefone Imobiliária',
            help='Somente números: +DDI (DDD) 0 0000-0000',
            value=None,
            key=8022
        )
        st.subheader('Acompanhante 01')
        acomp_01_nome = st.text_input(
            label='Nome',
            value=None,
            key=8023
        )
        acomp_01_rg = st.text_input(
            label='RG',
            value=None,
            key=8024
        )
        acomp_01_cpf = st.text_input(
            label='CPF',
            value=None,
            key=8025
        )
        acomp_01_idade = st.number_input(
            label='Idade',
            value=None,
            key=8026
        )
        acomp_01_parentesco = st.text_input(
            label='Parentesco',
            value=None,
            key=8027
        )

        st.subheader('Acompanhante 02')
        acomp_02_nome = st.text_input(
            label='Nome',
            value=None,
            key=8028
        )
        acomp_02_rg = st.text_input(
            label='RG',
            value=None,
            key=8029
        )
        acomp_02_cpf = st.text_input(
            label='CPF',
            value=None,
            key=8030
        )
        acomp_02_idade = st.number_input(
            label='Idade',
            value=None,
            key=8031
        )
        acomp_02_parentesco = st.text_input(
            label='Parentesco',
            value=None,
            key=8032
        )

        st.subheader('Acompanhante 03')
        acomp_03_nome = st.text_input(
            label='Nome',
            value=None,
            key=8033
        )
        acomp_03_rg = st.text_input(
            label='RG',
            value=None,
            key=8034
        )
        acomp_03_cpf = st.text_input(
            label='CPF',
            value=None,
            key=8035
        )
        acomp_03_idade = st.number_input(
            label='Idade',
            value=None,
            key=8036
        )
        acomp_03_parentesco = st.text_input(
            label='Parentesco',
            value=None,
            key=8037
        )

        st.subheader('Acompanhante 04')
        acomp_04_nome = st.text_input(
            label='Nome',
            value=None,
            key=8038
        )
        acomp_04_rg = st.text_input(
            label='RG',
            value=None,
            key=8039
        )
        acomp_04_cpf = st.text_input(
            label='CPF',
            value=None,
            key=8040
        )
        acomp_04_idade = st.number_input(
            label='Idade',
            value=None,
            key=8041
        )
        acomp_04_parentesco = st.text_input(
            label='Parentesco',
            value=None,
            key=8042
        )

        st.subheader('Acompanhante 05')
        acomp_05_nome = st.text_input(
            label='Nome',
            value=None,
            key=8043
        )
        acomp_05_rg = st.text_input(
            label='RG',
            value=None,
            key=8044
        )
        acomp_05_cpf = st.text_input(
            label='CPF',
            value=None,
            key=8045
        )
        acomp_05_idade = st.number_input(
            label='Idade',
            value=None,
            key=8046
        )
        acomp_05_parentesco = st.text_input(
            label='Parentesco',
            value=None,
            key=8047
        )

        st.subheader('Acompanhante 06')
        acomp_06_nome = st.text_input(
            label='Nome',
            value=None,
            key=8048
        )
        acomp_06_rg = st.text_input(
            label='RG',
            value=None,
            key=8049
        )
        acomp_06_cpf = st.text_input(
            label='CPF',
            value=None,
            key=8050
        )
        acomp_06_idade = st.number_input(
            label='Idade',
            value=None,
            key=8051
        )
        acomp_06_parentesco = st.text_input(
            label='Parentesco',
            value=None,
            key=8052
        )

        st.subheader('Acompanhante 07')
        acomp_07_nome = st.text_input(
            label='Nome',
            value=None,
            key=8053
        )
        acomp_07_rg = st.text_input(
            label='RG',
            value=None,
            key=8054
        )
        acomp_07_cpf = st.text_input(
            label='CPF',
            value=None,
            key=8055
        )
        acomp_07_idade = st.number_input(
            label='Idade',
            value=None,
            key=8056
        )
        acomp_07_parentesco = st.text_input(
            label='Parentesco',
            value=None,
            key=8057
        )

        st.subheader('Acompanhante 08')
        acomp_08_nome = st.text_input(
            label='Nome',
            value=None,
            key=8058
        )
        acomp_08_rg = st.text_input(
            label='RG',
            value=None,
            key=8059
        )
        acomp_08_cpf = st.text_input(
            label='CPF',
            value=None,
            key=8060
        )
        acomp_08_idade = st.number_input(
            label='Idade',
            value=None,
            key=8061
        )
        acomp_08_parentesco = st.text_input(
            label='Parentesco',
            value=None,
            key=8062
        )

        st.subheader('Acompanhante 09')
        acomp_09_nome = st.text_input(
            label='Nome',
            value=None,
            key=8063
        )
        acomp_09_rg = st.text_input(
            label='RG',
            value=None,
            key=8064
        )
        acomp_09_cpf = st.text_input(
            label='CPF',
            value=None,
            key=8065
        )
        acomp_09_idade = st.number_input(
            label='Idade',
            value=None,
            key=8066
        )
        acomp_09_parentesco = st.text_input(
            label='Parentesco',
            value=None,
            key=8067
        )

        st.subheader('Acompanhante 10')
        acomp_10_nome = st.text_input(
            label='Nome',
            value=None,
            key=8068
        )
        acomp_10_rg = st.text_input(
            label='RG',
            value=None,
            key=8069
        )
        acomp_10_cpf = st.text_input(
            label='CPF',
            value=None,
            key=8070
        )
        acomp_10_idade = st.number_input(
            label='Idade',
            value=None,
            key=8071
        )
        acomp_10_parentesco = st.text_input(
            label='Parentesco',
            value=None,
            key=8072
        )

        submit_button = st.form_submit_button('Registrar Ficha')
        if submit_button:
            response = requests.post(
                "http://backend:8000/inquilinos/",
                json={
                    "apartamento": apartamento,
                    "nome": nome,
                    "tipo_residencia": tipo_residencia,
                    "cidade": cidade,
                    "cep": cep,
                    "estado": estado,
                    "pais": pais,
                    "telefone": telefone,
                    "estado_civil": estado_civil,
                    "profissão": profissao,
                    "rg": rg,
                    "cpf": cpf,
                    "mae": mae,
                    "automovel": automovel,
                    "modelo_auto": modelo_auto,
                    "placa_auto": placa_auto,
                    "cor_auto": cor_auto,
                    "checkin": checkin.isoformat(),
                    "checkout": checkout.isoformat(),
                    "observacoes": observacoes,
                    "proprietario": proprietario,
                    "imob_fone": imob_fone,
                    "acomp_01_nome": acomp_01_nome,
                    "acomp_01_rg": acomp_01_rg,
                    "acomp_01_cpf": acomp_01_cpf,
                    "acomp_01_idade": acomp_01_idade,
                    "acomp_01_parentesco": acomp_01_parentesco,
                    "acomp_02_nome": acomp_02_nome,
                    "acomp_02_rg": acomp_02_rg,
                    "acomp_02_cpf": acomp_02_cpf,
                    "acomp_02_idade": acomp_02_idade,
                    "acomp_02_parentesco": acomp_02_parentesco,
                    "acomp_03_nome": acomp_03_nome,
                    "acomp_03_rg": acomp_03_rg,
                    "acomp_03_cpf": acomp_03_cpf,
                    "acomp_03_idade": acomp_03_idade,
                    "acomp_03_parentesco": acomp_03_parentesco,
                    "acomp_04_nome": acomp_04_nome,
                    "acomp_04_rg": acomp_04_rg,
                    "acomp_04_cpf": acomp_04_cpf,
                    "acomp_04_idade": acomp_04_idade,
                    "acomp_04_parentesco": acomp_04_parentesco,
                    "acomp_05_nome": acomp_05_nome,
                    "acomp_05_rg": acomp_05_rg,
                    "acomp_05_cpf": acomp_05_cpf,
                    "acomp_05_idade": acomp_05_idade,
                    "acomp_05_parentesco": acomp_05_parentesco,
                    "acomp_06_nome": acomp_06_nome,
                    "acomp_06_rg": acomp_06_rg,
                    "acomp_06_cpf": acomp_06_cpf,
                    "acomp_06_idade": acomp_06_idade,
                    "acomp_06_parentesco": acomp_06_parentesco,
                    "acomp_07_nome": acomp_07_nome,
                    "acomp_07_rg": acomp_07_rg,
                    "acomp_07_cpf": acomp_07_cpf,
                    "acomp_07_idade": acomp_07_idade,
                    "acomp_07_parentesco": acomp_07_parentesco,
                    "acomp_08_nome": acomp_08_nome,
                    "acomp_08_rg": acomp_08_rg,
                    "acomp_08_cpf": acomp_08_cpf,
                    "acomp_08_idade": acomp_08_idade,
                    "acomp_08_parentesco": acomp_08_parentesco,
                    "acomp_09_nome": acomp_09_nome,
                    "acomp_09_rg": acomp_09_rg,
                    "acomp_09_cpf": acomp_09_cpf,
                    "acomp_09_idade": acomp_09_idade,
                    "acomp_09_parentesco": acomp_09_parentesco,
                    "acomp_10_nome": acomp_10_nome,
                    "acomp_10_rg": acomp_10_rg,
                    "acomp_10_cpf": acomp_10_cpf,
                    "acomp_10_idade": acomp_10_idade,
                    "acomp_10_parentesco": acomp_10_parentesco,
                }
            )
            show_response_message(response)

with tab2:
    st.header('Consultar uma Ficha de Inquilino')
    get_id = st.number_input(
        'ID da Ficha de Inquilino',
        min_value=1,
        format='%d',
        key=8150
        )
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
    st.header('Atualizar uma Ficha de Inquilino')
    update_id = st.number_input(
        'ID da Ficha',
        min_value=1,
        format='%d',
        key=8151
    )
    if update_id:
        response = requests.get(f'http://backend:8000/inquilinos/{update_id}')
    if response.status_code == 200:
        ficha_viz = response.json()
        df = pd.DataFrame([ficha_viz])
        st.dataframe(df, hide_index=True)
        with st.form('update_inquilino'):
            apartamento = st.text_input(
                label='Apartamento alugado',
                value=str(df.apartamento[0]),
                key=8073
            )
            nome = st.text_input(
                label='Nome completo',
                value=str(df.nome[0]),
                key=8074
            )
            tipo_residencia = st.radio(
                label='Tipo de residência',
                options=['Anual', 'Temporária'],
                index=1,
                horizontal=True,
                key=8075
            )
            cidade = st.text_input(
                label='Naturalidade (cidade)',
                value=str(df.cidade[0]),
                key=8076
            )
            cep_input = st.text(
                label='CEP',
                value=f'{df.cep[0][:5]}-{df.cep[0][5:8]}',
                help='Somente números',
                key=8077
            )
            if cep_input:
                cep = cep_input.replace('-', '')
                if cep.isdigit() and len(cep) == 8:
                    st.success(f'CEP válido: {cep_input}')
                else:
                    st.error('O CEP deve conter exatamente 8 dígitos')
            estado = st.text_input(
                label='Estado (UF)',
                max_chars=2,
                value=str(df.estado[0]),
                key=8078
            )
            pais = st.text_input(
                label='País',
                value=str(df.pais[0]),
                key=8079
            )
            telefone_input = st.text_input(
                label='Telefone',
                value=f'+{df.telefone[0][:2]} ({df.telefone[0][2:4]}) {df.telefone[0][4]} {df.telefone[0][5:9]}-{df.telefone[0][9:]}',
                help='Somente números: +DDI (DDD) 0 0000-0000',
                key=8080
            )
            if telefone_input:
                telefone = telefone_input.replace('+', '').replace('-', '').replace(' ', '').replace('(', '').replace(')', '')
                if telefone.isdigit() and len(telefone) == 13:
                    st.success(f'Telefone válido: {telefone_input}')
                else:
                    st.error('O telefone deve conter exatamente 9 dígitos.')
            estado_civil = st.selectbox(
                label='Estado civíl',
                options=['Solteiro', 'Casado', 'Separado', 'Divorciado', 'Viúvo'],
                placeholder=str(df.estado_civil[0]),
                key=8081
            )
            profissao = st.text_input(
                label='Profissão',
                value=str(df.profissao[0]),
                key=8082
            )
            rg_input = st.text_input(
                label='Identidade',
                value=f"{df.rg[0][:3]}.{df.rg[0][3:6]}.{df.rg[0][6:9]}-{df.rg[0][9:]}",
                help='Somente números no formato XXX.XXX.XXX-X',
                key=8083
            )
            if rg_input:
                rg = rg_input.replace('.', '').replace('-', '')
                if rg.isdigit() and (len(rg) >= 8 and len(rg) <= 10):
                    st.success(f'RG válido: {rg_input}')
                else:
                    st.error('O RG deve conter entre 8 e 10 dígitos.')
            cpf_input = st.text_input(
                label='CPF',
                value=f'{df.cpf[0][:3]}.{df.cpf[0][3:6]}.{df.cpf[0][6:9]}-{df.cpf[0][9:]}',
                help='Somente números',
                key=8084
            )
            if cpf_input:
                cpf = cpf_input.replace('.', '').replace('-', '')
                if cpf.isdigit() and len(cpf) == 11:
                    st.success(f'CPF válido: {cpf_input}')
                else:
                    st.error('O CPF deve conter exatamente 11 dígitos.')
            mae = st.text_input(
                label='Nome completo da mãe',
                value=str(df.mae[0]),
                key=8085
            )
            if pd.isna(df.loc[0, 'automovel']):
                automovel = st.text_input(
                    label='Automóvel',
                    value=None,
                    key=8086
                )
            else:
                automovel = st.text_input(
                    label='Automóvel',
                    value=str(df.automovel[0]),
                    key=8087
                )
            if pd.isna(df.loc[0, 'modelo']):
                modelo_auto = st.text_input(
                    label='Modelo',
                    value=None,
                    key=8088
                )
            else:
                modelo_auto = st.text_input(
                    label='Modelo',
                    value=str(df.modelo[0]),
                    key=8089
                )
            if pd.isna(df.loc[0, 'placa']):
                placa_auto = st.text_input(
                    label='Placa',
                    value=None,
                    key=8090
                )
            else:
                placa_auto = st.text_input(
                    label='Placa',
                    value=str(df.placa[0]),
                    key=8091
                )
            if pd.isna(df.loc[0, 'automovel']):
                cor_auto = st.text_input(
                    label='Cor',
                    value=None,
                    key=8092
                )
            else:
                cor_auto = st.text_input(
                    label='Cor',
                    value=str(df.cor_auto[0]),
                    key=8093
                )
            checkin = st.date_input(
                label='Check-in',
                value=date(df.checkin[0]),
                min_value=date(2022, 1, 1),
                max_value=date.today()+timedelta(days=300),
                format='DD/MM/YYYY',
                key=8094
            )
            checkout = st.date_input(
                label='Check-out',
                value=date(df.checkout[0]),
                min_value=checkin+timedelta(days=1),
                max_value=date.today()+timedelta(days=300),
                format='DD/MM/YYYY',
                key=8095
            )
            observacoes = st.text_area(
                label='Observações',
                value=None if pd.isna(df.loc[0, 'observacoes']) else str(df.observacoes[0]),
                key=8096
            )
            proprietario = st.text_input(
                label='Proprietário',
                value=str(df.proprietario[0]),
                key=8097
            )
            imob_fone = st.text_input(
                label='Telefone Imobiliária',
                value=f'+{df.imob_fone[0][:2]} ({df.imob_fone[0][2:4]}) {df.imob_fone[0][4]} {df.imob_fone[0][5:9]}-{df.imob_fone[0][9:]}',
                help='Somente números: +DDI (DDD) 0 0000-0000',
                key=8098
            )

            st.subheader('Acompanhante 01')
            acomp_01_nome = st.text_input(
                label='Nome',
                value=str(df.acomp_01_nome[0]),
                key=8099
            )
            acomp_01_rg = st.text_input(
                label='RG',
                value=str(df.acomp_01_rg[0]),
                key=8100
            )
            acomp_01_cpf = st.text_input(
                label='CPF',
                value=str(df.acomp_01_cpf[0]),
                key=8101
            )
            acomp_01_idade = st.number_input(
                label='Idade',
                value=int(df.loc[0, 'acomp_01_idade']),
                key=8102
            )
            acomp_01_parentesco = st.text_input(
                label='Parentesco',
                value=str(df.acomp_01_parentesco[0]),
                key=8103
            )

            st.subheader('Acompanhante 02')
            acomp_02_nome = st.text_input(
                label='Nome',
                value=str(df.acomp_02_nome[0]),
                key=8104
            )
            acomp_02_rg = st.text_input(
                label='RG',
                value=str(df.acomp_02_rg[0]),
                key=8105
            )
            acomp_02_cpf = st.text_input(
                label='CPF',
                value=str(df.acomp_02_cpf[0]),
                key=8106
            )
            acomp_02_idade = st.number_input(
                label='Idade',
                value=int(df.loc[0, 'acomp_02_idade']),
                key=8107
            )
            acomp_02_parentesco = st.text_input(
                label='Parentesco',
                value=str(df.acomp_02_parentesco[0]),
                key=8108
            )

            st.subheader('Acompanhante 03')
            acomp_03_nome = st.text_input(
                label='Nome',
                value=str(df.acomp_03_nome[0]),
                key=8109
            )
            acomp_03_rg = st.text_input(
                label='RG',
                value=str(df.acomp_03_rg[0]),
                key=8110
            )
            acomp_03_cpf = st.text_input(
                label='CPF',
                value=str(df.acomp_03_cpf[0]),
                key=8111
            )
            acomp_03_idade = st.number_input(
                label='Idade',
                value=int(df.loc[0, 'acomp_03_idade']),
                key=8112
            )
            acomp_03_parentesco = st.text_input(
                label='Parentesco',
                value=str(df.acomp_03_parentesco[0]),
                key=8113
            )

            st.subheader('Acompanhante 04')
            acomp_04_nome = st.text_input(
                label='Nome',
                value=str(df.acomp_04_nome[0]),
                key=8114
            )
            acomp_04_rg = st.text_input(
                label='RG',
                value=str(df.acomp_04_rg[0]),
                key=8115
            )
            acomp_04_cpf = st.text_input(
                label='CPF',
                value=str(df.acomp_04_cpf[0]),
                key=8116
            )
            acomp_04_idade = st.number_input(
                label='Idade',
                value=int(df.loc[0, 'acomp_04_idade']),
                key=8117
            )
            acomp_04_parentesco = st.text_input(
                label='Parentesco',
                value=str(df.acomp_04_parentesco[0]),
                key=8118
            )

            st.subheader('Acompanhante 05')
            acomp_05_nome = st.text_input(
                label='Nome',
                value=str(df.acomp_05_nome[0]),
                key=8119
            )
            acomp_05_rg = st.text_input(
                label='RG',
                value=str(df.acomp_05_rg[0]),
                key=8120
            )
            acomp_05_cpf = st.text_input(
                label='CPF',
                value=str(df.acomp_05_cpf[0]),
                key=8121
            )
            acomp_05_idade = st.number_input(
                label='Idade',
                value=int(df.loc[0, 'acomp_05_idade']),
                key=8122
            )
            acomp_05_parentesco = st.text_input(
                label='Parentesco',
                value=str(df.acomp_05_parentesco[0]),
                key=8123
            )

            st.subheader('Acompanhante 06')
            acomp_06_nome = st.text_input(
                label='Nome',
                value=str(df.acomp_06_nome[0]),
                key=8124
            )
            acomp_06_rg = st.text_input(
                label='RG',
                value=str(df.acomp_06_rg[0]),
                key=8125
            )
            acomp_06_cpf = st.text_input(
                label='CPF',
                value=str(df.acomp_06_cpf[0]),
                key=8126
            )
            acomp_06_idade = st.number_input(
                label='Idade',
                value=int(df.loc[0, 'acomp_06_idade']),
                key=8127
            )
            acomp_06_parentesco = st.text_input(
                label='Parentesco',
                value=str(df.acomp_06_parentesco[0]),
                key=8128
            )

            st.subheader('Acompanhante 07')
            acomp_07_nome = st.text_input(
                label='Nome',
                value=str(df.acomp_07_nome[0]),
                key=8129
            )
            acomp_07_rg = st.text_input(
                label='RG',
                value=str(df.acomp_07_rg[0]),
                key=8130
            )
            acomp_07_cpf = st.text_input(
                label='CPF',
                value=str(df.acomp_07_cpf[0]),
                key=8131
            )
            acomp_07_idade = st.number_input(
                label='Idade',
                value=int(df.loc[0, 'acomp_07_idade']),
                key=8132
            )
            acomp_07_parentesco = st.text_input(
                label='Parentesco',
                value=str(df.acomp_07_parentesco[0]),
                key=8133
            )

            st.subheader('Acompanhante 08')
            acomp_08_nome = st.text_input(
                label='Nome',
                value=str(df.acomp_08_nome[0]),
                key=8134
            )
            acomp_08_rg = st.text_input(
                label='RG',
                value=str(df.acomp_08_rg[0]),
                key=8135
            )
            acomp_08_cpf = st.text_input(
                label='CPF',
                value=str(df.acomp_08_cpf[0]),
                key=8136
            )
            acomp_08_idade = st.number_input(
                label='Idade',
                value=int(df.loc[0, 'acomp_08_idade']),
                key=8137
            )
            acomp_08_parentesco = st.text_input(
                label='Parentesco',
                value=str(df.acomp_08_parentesco[0]),
                key=8138
            )

            st.subheader('Acompanhante 09')
            acomp_09_nome = st.text_input(
                label='Nome',
                value=str(df.acomp_09_nome[0]),
                key=8139
            )
            acomp_09_rg = st.text_input(
                label='RG',
                value=str(df.acomp_09_rg[0]),
                key=8140
            )
            acomp_09_cpf = st.text_input(
                label='CPF',
                value=str(df.acomp_09_cpf[0]),
                key=8141
            )
            acomp_09_idade = st.number_input(
                label='Idade',
                value=int(df.loc[0, 'acomp_09_idade']),
                key=8142
            )
            acomp_09_parentesco = st.text_input(
                label='Parentesco',
                value=str(df.acomp_09_parentesco[0]),
                key=8143
            )

            st.subheader('Acompanhante 10')
            acomp_10_nome = st.text_input(
                label='Nome',
                value=str(df.acomp_10_nome[0]),
                key=8144
            )
            acomp_10_rg = st.text_input(
                label='RG',
                value=str(df.acomp_10_rg[0]),
                key=8145
            )
            acomp_10_cpf = st.text_input(
                label='CPF',
                value=str(df.acomp_10_cpf[0]),
                key=8146
            )
            acomp_10_idade = st.number_input(
                label='Idade',
                value=int(df.loc[0, 'acomp_10_idade']),
                key=8147
            )
            acomp_10_parentesco = st.text_input(
                label='Parentesco',
                value=str(df.acomp_10_parentesco[0]),
                key=8148
            )

            update_button = st.form_submit_button('Atualizar Dados')
            
            if update_button:
                convert_empty_to_none()
                response = requests.post(
                    "http://backend:8000/inquilinos/",
                    json={
                        "apartamento": apartamento,
                        "nome": nome,
                        "tipo_residencia": tipo_residencia,
                        "cidade": cidade,
                        "cep": cep,
                        "estado": estado,
                        "pais": pais,
                        "telefone": telefone,
                        "estado_civil": estado_civil,
                        "profissão": profissao,
                        "rg": rg,
                        "cpf": cpf,
                        "mae": mae,
                        "automovel": automovel,
                        "modelo_auto": modelo_auto,
                        "placa_auto": placa_auto,
                        "cor_auto": cor_auto,
                        "checkin": checkin.isoformat(),
                        "checkout": checkout.isoformat(),
                        "observacoes": observacoes,
                        "proprietario": proprietario,
                        "imob_fone": imob_fone,
                        "acomp_01_nome": acomp_01_nome,
                        "acomp_01_rg": acomp_01_rg,
                        "acomp_01_cpf": acomp_01_cpf,
                        "acomp_01_idade": acomp_01_idade,
                        "acomp_01_parentesco": acomp_01_parentesco,
                        "acomp_02_nome": acomp_02_nome,
                        "acomp_02_rg": acomp_02_rg,
                        "acomp_02_cpf": acomp_02_cpf,
                        "acomp_02_idade": acomp_02_idade,
                        "acomp_02_parentesco": acomp_02_parentesco,
                        "acomp_03_nome": acomp_03_nome,
                        "acomp_03_rg": acomp_03_rg,
                        "acomp_03_cpf": acomp_03_cpf,
                        "acomp_03_idade": acomp_03_idade,
                        "acomp_03_parentesco": acomp_03_parentesco,
                        "acomp_04_nome": acomp_04_nome,
                        "acomp_04_rg": acomp_04_rg,
                        "acomp_04_cpf": acomp_04_cpf,
                        "acomp_04_idade": acomp_04_idade,
                        "acomp_04_parentesco": acomp_04_parentesco,
                        "acomp_05_nome": acomp_05_nome,
                        "acomp_05_rg": acomp_05_rg,
                        "acomp_05_cpf": acomp_05_cpf,
                        "acomp_05_idade": acomp_05_idade,
                        "acomp_05_parentesco": acomp_05_parentesco,
                        "acomp_06_nome": acomp_06_nome,
                        "acomp_06_rg": acomp_06_rg,
                        "acomp_06_cpf": acomp_06_cpf,
                        "acomp_06_idade": acomp_06_idade,
                        "acomp_06_parentesco": acomp_06_parentesco,
                        "acomp_07_nome": acomp_07_nome,
                        "acomp_07_rg": acomp_07_rg,
                        "acomp_07_cpf": acomp_07_cpf,
                        "acomp_07_idade": acomp_07_idade,
                        "acomp_07_parentesco": acomp_07_parentesco,
                        "acomp_08_nome": acomp_08_nome,
                        "acomp_08_rg": acomp_08_rg,
                        "acomp_08_cpf": acomp_08_cpf,
                        "acomp_08_idade": acomp_08_idade,
                        "acomp_08_parentesco": acomp_08_parentesco,
                        "acomp_09_nome": acomp_09_nome,
                        "acomp_09_rg": acomp_09_rg,
                        "acomp_09_cpf": acomp_09_cpf,
                        "acomp_09_idade": acomp_09_idade,
                        "acomp_09_parentesco": acomp_09_parentesco,
                        "acomp_10_nome": acomp_10_nome,
                        "acomp_10_rg": acomp_10_rg,
                        "acomp_10_cpf": acomp_10_cpf,
                        "acomp_10_idade": acomp_10_idade,
                        "acomp_10_parentesco": acomp_10_parentesco,
                    }
            )
            show_response_message(response)

    else:
        show_response_message(response)

with tab4:
    st.header('Deletar uma Ficha de Inquilino')
    delete_id = st.number_input(
        label="ID da Ficha de Inquilino para Deletar",
        min_value=1,
        format='%d',
        key=8149
    )
    if delete_id:
        response = requests.get(f'http://backend:8000/inquilinos/{delete_id}')
    if response.status_code == 200:
        ficha_viz = response.json()
        df = pd.DataFrame([ficha_viz])
        st.dataframe(df, hide_index=True)
    else:
        show_response_message(response)
    if st.button('Deletar Ficha'):
        response = requests.delete(f'http://backend:8000/inquilinos/{delete_id}')
        show_response_message(response)

with tab5:
    st.header('Listar todas as Fichas de Innquilino')
    if st.button("Exibir Todas as Fichas"):
        response = requests.get(f'http://backend:8000/inquilinos/')
        if response.status_code == 200:
            fichas = response.json()
            df = pd.DataFrame(fichas)
            st.dataframe(df, hide_index=True)
        else:
            show_response_message(response)