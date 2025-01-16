from datetime import date, timedelta
import json
import pandas as pd
import requests
import streamlit as st
from src.fdate import str_to_date, calculate_diarias
from src.functions import merge_dictionaries, none_or_str, show_response_message, show_data_output


st.set_page_config(
    page_title='Ficha de Inquilinos',
    layout='wide'
)
st.title('Ficha de Inquilinos')

tab1, tab2, tab3, tab4, tab5 = st.tabs(['Registrar', 'Consultar', 'Modificar', 'Deletar', 'Listar'])

# Em registrar deve ser possível fazer upload de um arquivo ou forms essas coisas que o inquilino pode já ter preenchido em casa e enviado para nós (google forms ou sei lá)

# Em consultar, deve ser possível então exportar a ficha em pdf no modelo proposto pelo condomínio

# Ajeitar a validação dos dados, formato de envio para o banco de dados e formato de exibição.

with tab1:
    st.header('Registrar Ficha de Inquilino')
    with st.form('new_ficha'):
        apto = st.text_input(
            label='Apartamento',
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
            index=1,
            horizontal=True,
            key=8003
        )
        cidade = st.text_input(
            label='Naturalidade (cidade)',
            value=None,
            key=8004
        )
        cep = st.text_input(
            label='CEP',
            value=None,
            key=8005
        )
        uf = st.text_input(
            label='Estado (UF)',
            value=None,
            key=8006
        )
        pais = st.text_input(
            label='País',
            value=None,
            key=8007
        )
        tel = st.text_input(
            label='Telefone',
            value=None,
            key=8008
        )
        estado_civil = st.selectbox(
            label='Estado civíl',
            index=0,
            placeholder='Selecione opção',
            options=['Solteiro(a)', 'Casado(a)', 'Separado(a)', 'Divorciado(a)', 'Viúvo(a)'],
            key=8009
        )
        profissao = st.text_input(
            label='Profissão',
            value=None,
            key=8010
        )
        rg = st.text_input(
            label='Identidade',
            value=None,
            key=8011
        )
        cpf = st.text_input(
            label='CPF',
            value=None,
            key=8012
        )
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
            format='DD/MM/YYYY',
            key=8018,
            value=date.today()
        )
        checkout = st.date_input(
            label='Check-out',
            format='DD/MM/YYYY',
            key=8019,
            value=checkin + timedelta(days=1)
        )
        diarias: int = calculate_diarias(checkin, checkout)
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
            value=None,
            key=8022
        )
        st.markdown('**Acompanhante 01**')
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
        acomp_01_idade = st.text_input(
            label='Idade',
            value=None,
            key=8026
        )
        acomp_01_parentesco = st.text_input(
            label='Parentesco',
            value=None,
            key=8027
        )

        st.markdown('**Acompanhante 02**')
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
        acomp_02_idade = st.text_input(
            label='Idade',
            value=None,
            key=8031
        )
        acomp_02_parentesco = st.text_input(
            label='Parentesco',
            value=None,
            key=8032
        )

        st.markdown('**Acompanhante 03**')
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
        acomp_03_idade = st.text_input(
            label='Idade',
            value=None,
            key=8036
        )
        acomp_03_parentesco = st.text_input(
            label='Parentesco',
            value=None,
            key=8037
        )

        st.markdown('**Acompanhante 04**')
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
        acomp_04_idade = st.text_input(
            label='Idade',
            value=None,
            key=8041
        )
        acomp_04_parentesco = st.text_input(
            label='Parentesco',
            value=None,
            key=8042
        )

        st.markdown('**Acompanhante 05**')
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
        acomp_05_idade = st.text_input(
            label='Idade',
            value=None,
            key=8046
        )
        acomp_05_parentesco = st.text_input(
            label='Parentesco',
            value=None,
            key=8047
        )

        st.markdown('**Acompanhante 06**')
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
        acomp_06_idade = st.text_input(
            label='Idade',
            value=None,
            key=8051
        )
        acomp_06_parentesco = st.text_input(
            label='Parentesco',
            value=None,
            key=8052
        )

        st.markdown('**Acompanhante 07**')
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
        acomp_07_idade = st.text_input(
            label='Idade',
            value=None,
            key=8056
        )
        acomp_07_parentesco = st.text_input(
            label='Parentesco',
            value=None,
            key=8057
        )

        st.markdown('**Acompanhante 08**')
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
        acomp_08_idade = st.text_input(
            label='Idade',
            value=None,
            key=8061
        )
        acomp_08_parentesco = st.text_input(
            label='Parentesco',
            value=None,
            key=8062
        )

        st.markdown('**Acompanhante 09**')
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
        acomp_09_idade = st.text_input(
            label='Idade',
            value=None,
            key=8066
        )
        acomp_09_parentesco = st.text_input(
            label='Parentesco',
            value=None,
            key=8067
        )

        st.markdown('**Acompanhante 10**')
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
        acomp_10_idade = st.text_input(
            label='Idade',
            value=None,
            key=8071
        )
        acomp_10_parentesco = st.text_input(
            label='Parentesco',
            value=None,
            key=8072
        )

        submit_button = st.form_submit_button('Registrar')
        if submit_button:
            ficha_data = {
                "apto": apto,
                "nome": nome,
                "tipo_residencia": tipo_residencia,
                "cidade": cidade,
                "cep": cep,
                "uf": uf,
                "pais": pais,
                "tel": tel,
                "estado_civil": estado_civil,
                "profissao": profissao,
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
                "imob_fone": imob_fone
            }
            acomps_data = {}
            for i in range(1, 11):
                acomps_data[f"acomp_{i:02d}_nome"] = locals()[f"acomp_{i:02d}_nome"]
                acomps_data[f"acomp_{i:02d}_rg"] = locals()[f"acomp_{i:02d}_rg"]
                acomps_data[f"acomp_{i:02d}_cpf"] = locals()[f"acomp_{i:02d}_cpf"]
                acomps_data[f"acomp_{i:02d}_idade"] = locals()[f"acomp_{i:02d}_idade"]
                acomps_data[f"acomp_{i:02d}_parentesco"] = locals()[f"acomp_{i:02d}_parentesco"]
            submit_data = json.dumps(obj=merge_dictionaries(ficha_data, acomps_data), separators=(',',':'))

            try:
                post_response = requests.post("http://backend:8000/fichas/", submit_data)
                show_response_message(post_response)
                st.subheader('Dados inseridos:')
                show_data_output(merge_dictionaries(ficha_data, acomps_data))
            except Exception as e:
                show_response_message(post_response)
                st.subheader('Dados NÃO inseridos:')
                show_data_output(merge_dictionaries(ficha_data, acomps_data))
                print(e)

with tab2:
    st.header('Consultar Ficha de Inquilino')
    get_id = st.number_input(
        'ID da Ficha de Inquilino',
        min_value=1,
        format='%d',
        key=8150
    )
    if get_id:
        get_response = requests.get(f'http://backend:8000/fichas/{get_id}')
        if get_response.status_code == 200:
            ficha = get_response.json()
            df_get = pd.DataFrame([ficha])
            st.dataframe(df_get, hide_index=True)
        else:
            show_response_message(get_response)

with tab3:
    st.header('Modificar Ficha de Inquilino')
    update_id = st.number_input(
        'ID da Ficha',
        min_value=1,
        format='%d',
        key=8151
    )
    if update_id:
        update_response = requests.get(f'http://backend:8000/fichas/{update_id}')
        if update_response.status_code == 200:
            ficha_up = update_response.json()
            df_up = pd.DataFrame([ficha_up])
            st.dataframe(df_up, hide_index=True)
            st.subheader(f"Ficha de Inquilino nº: {update_id}")
            with st.form('update_ficha'):
                apto = st.text_input(
                    label='Apartamento',
                    value=str(df_up.apto[0]),
                    key=8073
                )
                nome = st.text_input(
                    label='Nome completo',
                    value=str(df_up.nome[0]),
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
                    value=str(df_up.cidade[0]),
                    key=8076
                )
                cep = st.text_input(
                    label='CEP',
                    value=str(df_up.cep[0]),
                    key=8077
                )
                uf = st.text_input(
                    label='Estado (UF)',
                    value=str(df_up.uf[0]),
                    key=8078
                )
                pais = st.text_input(
                    label='País',
                    value=str(df_up.pais[0]),
                    key=8079
                )
                tel = st.text_input(
                    label='Telefone',
                    value=str(df_up.tel[0]),
                    key=8080
                )
                estado_civil = st.selectbox(
                    label='Estado civíl',
                    options=['Solteiro', 'Casado', 'Separado', 'Divorciado', 'Viúvo'],
                    placeholder=str(df_up.estado_civil[0]),
                    key=8081
                )
                profissao = st.text_input(
                    label='Profissão',
                    value=str(df_up.profissao[0]),
                    key=8082
                )
                rg = st.text_input(
                    label='Identidade (RG)',
                    value=none_or_str(df_up.rg[0]),
                    key=8083
                )
                cpf = st.text_input(
                    label='CPF',
                    value=str(df_up.cpf[0]),
                    help='Somente números',
                    key=8084
                )
                mae = st.text_input(
                    label='Nome completo da mãe',
                    value=str(df_up.mae[0]),
                    key=8085
                )
                automovel = st.text_input(
                    label='Automóvel',
                    value=none_or_str(df_up.automovel[0]),
                    key=8087
                )
                modelo_auto = st.text_input(
                    label='Modelo',
                    value=none_or_str(df_up.modelo_auto[0]),
                    key=8089
                )
                placa_auto = st.text_input(
                    label='Placa',
                    value=none_or_str(df_up.placa_auto[0]),
                    key=8091
                )
                cor_auto = st.text_input(
                    label='Cor',
                    value=none_or_str(df_up.cor_auto[0]),
                    key=8093
                )
                checkin = st.date_input(
                    label='Check-in',
                    value=str_to_date(df_up.checkin[0]),
                    format='DD/MM/YYYY',
                    key=8094
                )
                checkout = st.date_input(
                    label='Check-out',
                    value=str_to_date(df_up.checkout[0]),
                    format='DD/MM/YYYY',
                    key=8095
                )
                diarias: int = calculate_diarias(checkin, checkout)
                observacoes = st.text_area(
                    label='Observações',
                    value=none_or_str(df_up.loc[0, 'observacoes']),
                    key=8096
                )
                proprietario = st.text_input(
                    label='Proprietário',
                    value=none_or_str(df_up.proprietario[0]),
                    key=8097
                )
                imob_fone = st.text_input(
                    label='Telefone Imobiliária',
                    value=none_or_str(df_up.imob_fone[0]),
                    key=8098
                )

                st.markdown('**Acompanhante 01**')
                acomp_01_nome = st.text_input(
                    label='Nome',
                    value=none_or_str(df_up.acomp_01_nome[0]),
                    key=8099
                )
                acomp_01_rg = st.text_input(
                    label='RG',
                    value=none_or_str(df_up.acomp_01_rg[0]),
                    key=8100
                )
                acomp_01_cpf = st.text_input(
                    label='CPF',
                    value=none_or_str(df_up.acomp_01_cpf[0]),
                    key=8101
                )
                acomp_01_idade = st.text_input(
                    label='Idade',
                    value=none_or_str(df_up.loc[0, 'acomp_01_idade']),
                    key=8102
                )
                acomp_01_parentesco = st.text_input(
                    label='Parentesco',
                    value=none_or_str(df_up.acomp_01_parentesco[0]),
                    key=8103
                )

                st.markdown('**Acompanhante 02**')
                acomp_02_nome = st.text_input(
                    label='Nome',
                    value=none_or_str(df_up.acomp_02_nome[0]),
                    key=8104
                )
                acomp_02_rg = st.text_input(
                    label='RG',
                    value=none_or_str(df_up.acomp_02_rg[0]),
                    key=8105
                )
                acomp_02_cpf = st.text_input(
                    label='CPF',
                    value=none_or_str(df_up.acomp_02_cpf[0]),
                    key=8106
                )
                acomp_02_idade = st.text_input(
                    label='Idade',
                    value=none_or_str(df_up.loc[0, 'acomp_02_idade']),
                    key=8107
                )
                acomp_02_parentesco = st.text_input(
                    label='Parentesco',
                    value=none_or_str(df_up.acomp_02_parentesco[0]),
                    key=8108
                )

                st.markdown('**Acompanhante 03**')
                acomp_03_nome = st.text_input(
                    label='Nome',
                    value=none_or_str(df_up.acomp_03_nome[0]),
                    key=8109
                )
                acomp_03_rg = st.text_input(
                    label='RG',
                    value=none_or_str(df_up.acomp_03_rg[0]),
                    key=8110
                )
                acomp_03_cpf = st.text_input(
                    label='CPF',
                    value=none_or_str(df_up.acomp_03_cpf[0]),
                    key=8111
                )
                acomp_03_idade = st.text_input(
                    label='Idade',
                    value=none_or_str(df_up.loc[0, 'acomp_03_idade']),
                    key=8112
                )
                acomp_03_parentesco = st.text_input(
                    label='Parentesco',
                    value=none_or_str(df_up.acomp_03_parentesco[0]),
                    key=8113
                )

                st.markdown('**Acompanhante 04**')
                acomp_04_nome = st.text_input(
                    label='Nome',
                    value=none_or_str(df_up.acomp_04_nome[0]),
                    key=8114
                )
                acomp_04_rg = st.text_input(
                    label='RG',
                    value=none_or_str(df_up.acomp_04_rg[0]),
                    key=8115
                )
                acomp_04_cpf = st.text_input(
                    label='CPF',
                    value=none_or_str(df_up.acomp_04_cpf[0]),
                    key=8116
                )
                acomp_04_idade = st.text_input(
                    label='Idade',
                    value=none_or_str(df_up.loc[0, 'acomp_04_idade']),
                    key=8117
                )
                acomp_04_parentesco = st.text_input(
                    label='Parentesco',
                    value=none_or_str(df_up.acomp_04_parentesco[0]),
                    key=8118
                )

                st.markdown('**Acompanhante 05**')
                acomp_05_nome = st.text_input(
                    label='Nome',
                    value=none_or_str(df_up.acomp_05_nome[0]),
                    key=8119
                )
                acomp_05_rg = st.text_input(
                    label='RG',
                    value=none_or_str(df_up.acomp_05_rg[0]),
                    key=8120
                )
                acomp_05_cpf = st.text_input(
                    label='CPF',
                    value=none_or_str(df_up.acomp_05_cpf[0]),
                    key=8121
                )
                acomp_05_idade = st.text_input(
                    label='Idade',
                    value=none_or_str(df_up.loc[0, 'acomp_05_idade']),
                    key=8122
                )
                acomp_05_parentesco = st.text_input(
                    label='Parentesco',
                    value=none_or_str(df_up.acomp_05_parentesco[0]),
                    key=8123
                )

                st.markdown('**Acompanhante 06**')
                acomp_06_nome = st.text_input(
                    label='Nome',
                    value=none_or_str(df_up.acomp_06_nome[0]),
                    key=8124
                )
                acomp_06_rg = st.text_input(
                    label='RG',
                    value=none_or_str(df_up.acomp_06_rg[0]),
                    key=8125
                )
                acomp_06_cpf = st.text_input(
                    label='CPF',
                    value=none_or_str(df_up.acomp_06_cpf[0]),
                    key=8126
                )
                acomp_06_idade = st.text_input(
                    label='Idade',
                    value=none_or_str(df_up.loc[0, 'acomp_06_idade']),
                    key=8127
                )
                acomp_06_parentesco = st.text_input(
                    label='Parentesco',
                    value=none_or_str(df_up.acomp_06_parentesco[0]),
                    key=8128
                )

                st.markdown('**Acompanhante 07**')
                acomp_07_nome = st.text_input(
                    label='Nome',
                    value=none_or_str(df_up.acomp_07_nome[0]),
                    key=8129
                )
                acomp_07_rg = st.text_input(
                    label='RG',
                    value=none_or_str(df_up.acomp_07_rg[0]),
                    key=8130
                )
                acomp_07_cpf = st.text_input(
                    label='CPF',
                    value=none_or_str(df_up.acomp_07_cpf[0]),
                    key=8131
                )
                acomp_07_idade = st.text_input(
                    label='Idade',
                    value=none_or_str(df_up.loc[0, 'acomp_07_idade']),
                    key=8132
                )
                acomp_07_parentesco = st.text_input(
                    label='Parentesco',
                    value=none_or_str(df_up.acomp_07_parentesco[0]),
                    key=8133
                )

                st.markdown('**Acompanhante 08**')
                acomp_08_nome = st.text_input(
                    label='Nome',
                    value=none_or_str(df_up.acomp_08_nome[0]),
                    key=8134
                )
                acomp_08_rg = st.text_input(
                    label='RG',
                    value=none_or_str(df_up.acomp_08_rg[0]),
                    key=8135
                )
                acomp_08_cpf = st.text_input(
                    label='CPF',
                    value=none_or_str(df_up.acomp_08_cpf[0]),
                    key=8136
                )
                acomp_08_idade = st.text_input(
                    label='Idade',
                    value=none_or_str(df_up.loc[0, 'acomp_08_idade']),
                    key=8137
                )
                acomp_08_parentesco = st.text_input(
                    label='Parentesco',
                    value=none_or_str(df_up.acomp_08_parentesco[0]),
                    key=8138
                )

                st.markdown('**Acompanhante 09**')
                acomp_09_nome = st.text_input(
                    label='Nome',
                    value=none_or_str(df_up.acomp_09_nome[0]),
                    key=8139
                )
                acomp_09_rg = st.text_input(
                    label='RG',
                    value=none_or_str(df_up.acomp_09_rg[0]),
                    key=8140
                )
                acomp_09_cpf = st.text_input(
                    label='CPF',
                    value=none_or_str(df_up.acomp_09_cpf[0]),
                    key=8141
                )
                acomp_09_idade = st.text_input(
                    label='Idade',
                    value=none_or_str(df_up.loc[0, 'acomp_09_idade']),
                    key=8142
                )
                acomp_09_parentesco = st.text_input(
                    label='Parentesco',
                    value=none_or_str(df_up.acomp_09_parentesco[0]),
                    key=8143
                )

                st.markdown('**Acompanhante 10**')
                acomp_10_nome = st.text_input(
                    label='Nome',
                    value=none_or_str(df_up.acomp_10_nome[0]),
                    key=8144
                )
                acomp_10_rg = st.text_input(
                    label='RG',
                    value=none_or_str(df_up.acomp_10_rg[0]),
                    key=8145
                )
                acomp_10_cpf = st.text_input(
                    label='CPF',
                    value=none_or_str(df_up.acomp_10_cpf[0]),
                    key=8146
                )
                acomp_10_idade = st.text_input(
                    label='Idade',
                    value=none_or_str(df_up.loc[0, 'acomp_10_idade']),
                    key=8147
                )
                acomp_10_parentesco = st.text_input(
                    label='Parentesco',
                    value=none_or_str(df_up.acomp_10_parentesco[0]),
                    key=8148
                )

                update_button = st.form_submit_button('Modificar')
                if update_button:
                    ficha_up_data = {
                        "apto": apto,
                        "nome": nome,
                        "tipo_residencia": tipo_residencia,
                        "cidade": cidade,
                        "cep": cep,
                        "uf": uf,
                        "pais": pais,
                        "tel": tel,
                        "estado_civil": estado_civil,
                        "profissao": profissao,
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
                        "imob_fone": imob_fone
                    }
                    acomps_up_data = {}
                    for i in range(1, 11):
                        acomps_up_data[f"acomp_{i:02d}_nome"] = locals()[f"acomp_{i:02d}_nome"]
                        acomps_up_data[f"acomp_{i:02d}_rg"] = locals()[f"acomp_{i:02d}_rg"]
                        acomps_up_data[f"acomp_{i:02d}_cpf"] = locals()[f"acomp_{i:02d}_cpf"]
                        acomps_up_data[f"acomp_{i:02d}_idade"] = locals()[f"acomp_{i:02d}_idade"]
                        acomps_up_data[f"acomp_{i:02d}_parentesco"] = locals()[f"acomp_{i:02d}_parentesco"]

                    update_data = json.dumps(obj=merge_dictionaries(ficha_up_data, acomps_up_data), separators=(',',':'))

                    try:
                        put_response = requests.put(f"http://backend:8000/fichas/{update_id}", update_data)
                        show_response_message(put_response)
                        st.subheader('Dados inseridos:')
                        show_data_output(merge_dictionaries(ficha_up_data, acomps_up_data))
                    except Exception as e:
                        show_response_message(put_response)
                        st.subheader('Dados NÃO inseridos:')
                        show_data_output(merge_dictionaries(ficha_up_data, acomps_up_data))
                        print(e) 

        else:
            show_response_message(update_response)

with tab4:
    st.header('Deletar Ficha de Inquilino')
    delete_id = st.number_input(
        label="ID Ficha",
        min_value=1,
        format='%d',
        step=1,
        key=8149
    )
    if delete_id:
        show_delete_response = requests.get(f'http://backend:8000/fichas/{delete_id}')
    if show_delete_response.status_code == 200:
        ficha_delete = show_delete_response.json()
        df_delete = pd.DataFrame([ficha_delete])
        st.dataframe(df_delete, hide_index=True)
    else:
        show_response_message(show_delete_response)
    if st.button(
        'Deletar',
        key=6400
    ):
        try:
            delete_response = requests.delete(f'http://backend:8000/fichas/{delete_id}')
        except Exception as e:
            print(e)
        finally:
            show_response_message(delete_response)

with tab5:
    st.header('Listar Fichas de Inquilino')
    if st.button(
        "Mostrar",
        key=6500
    ):
        get_list_response = requests.get(f'http://backend:8000/fichas/')
        if get_list_response.status_code == 200:
            list_fichas = get_list_response.json()
            df_list = pd.DataFrame(list_fichas)
            st.dataframe(df_list, hide_index=True)
            st.write(df_list.isna())
        else:
            show_response_message(get_list_response)
