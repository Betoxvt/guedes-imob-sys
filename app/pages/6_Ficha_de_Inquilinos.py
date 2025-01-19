from datetime import date
import json
import os
import pandas as pd
import requests
import streamlit as st
from utils.mydate import calculate_diarias, str_to_date
from utils.myfunc import show_data_output, show_response_message
from utils.mystr import empty_none_dict, none_or_str
from utils.mypdf import fill_ficha

st.set_page_config(
    page_title='Ficha de Inquilinos',
    layout='wide'
)
st.title('Ficha de Inquilinos')

tab1, tab2, tab3, tab4, tab5 = st.tabs(['Registrar', 'Consultar', 'Modificar', 'Deletar', 'Listar'])

# Em registrar deve ser possível fazer upload de um arquivo ou forms essas coisas que o inquilino pode já ter preenchido em casa e enviado para nós (google forms ou sei lá)

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
            options=['Casado(a)', 'Divorciado(a)', 'Separado(a)', 'Solteiro(a)', 'Viúvo(a)'],
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
        checkin: date = st.date_input(
            label='Check-in',
            format='DD/MM/YYYY',
            key=8018,
            value=None
        )
        checkout: date = st.date_input(
            label='Check-out',
            format='DD/MM/YYYY',
            key=8019,
            value=None
        )
        diarias: int = calculate_diarias(checkin, checkout)
        st.write(f'Diárias: {diarias}')
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
        a0_nome = st.text_input(
            label='Nome',
            value=None,
            key=8023
        )
        a0_doc = st.text_input(
            label='Documento (RG/CPF)',
            value=None,
            key=8024
        )
        a0_idade = st.text_input(
            label='Idade',
            value=None,
            key=8026
        )
        a0_parentesco = st.text_input(
            label='Parentesco',
            value=None,
            key=8027
        )

        st.markdown('**Acompanhante 02**')
        a1_nome = st.text_input(
            label='Nome',
            value=None,
            key=8028
        )
        a1_doc = st.text_input(
            label='Documento (RG/CPF)',
            value=None,
            key=8029
        )
        a1_idade = st.text_input(
            label='Idade',
            value=None,
            key=8031
        )
        a1_parentesco = st.text_input(
            label='Parentesco',
            value=None,
            key=8032
        )

        st.markdown('**Acompanhante 03**')
        a2_nome = st.text_input(
            label='Nome',
            value=None,
            key=8033
        )
        a2_doc = st.text_input(
            label='Documento (RG/CPF)',
            value=None,
            key=8034
        )
        a2_idade = st.text_input(
            label='Idade',
            value=None,
            key=8036
        )
        a2_parentesco = st.text_input(
            label='Parentesco',
            value=None,
            key=8037
        )

        st.markdown('**Acompanhante 04**')
        a3_nome = st.text_input(
            label='Nome',
            value=None,
            key=8038
        )
        a3_doc = st.text_input(
            label='Documento (RG/CPF)',
            value=None,
            key=8039
        )
        a3_idade = st.text_input(
            label='Idade',
            value=None,
            key=8041
        )
        a3_parentesco = st.text_input(
            label='Parentesco',
            value=None,
            key=8042
        )

        st.markdown('**Acompanhante 05**')
        a4_nome = st.text_input(
            label='Nome',
            value=None,
            key=8043
        )
        a4_doc = st.text_input(
            label='Documento (RG/CPF)',
            value=None,
            key=8044
        )
        a4_idade = st.text_input(
            label='Idade',
            value=None,
            key=8046
        )
        a4_parentesco = st.text_input(
            label='Parentesco',
            value=None,
            key=8047
        )

        st.markdown('**Acompanhante 06**')
        a5_nome = st.text_input(
            label='Nome',
            value=None,
            key=8048
        )
        a5_doc = st.text_input(
            label='Documento (RG/CPF)',
            value=None,
            key=8049
        )
        a5_idade = st.text_input(
            label='Idade',
            value=None,
            key=8051
        )
        a5_parentesco = st.text_input(
            label='Parentesco',
            value=None,
            key=8052
        )

        st.markdown('**Acompanhante 07**')
        a6_nome = st.text_input(
            label='Nome',
            value=None,
            key=8053
        )
        a6_doc = st.text_input(
            label='Documento (RG/CPF)',
            value=None,
            key=8054
        )
        a6_idade = st.text_input(
            label='Idade',
            value=None,
            key=8056
        )
        a6_parentesco = st.text_input(
            label='Parentesco',
            value=None,
            key=8057
        )

        st.markdown('**Acompanhante 08**')
        a7_nome = st.text_input(
            label='Nome',
            value=None,
            key=8058
        )
        a7_doc = st.text_input(
            label='Documento (RG/CPF)',
            value=None,
            key=8059
        )
        a7_idade = st.text_input(
            label='Idade',
            value=None,
            key=8061
        )
        a7_parentesco = st.text_input(
            label='Parentesco',
            value=None,
            key=8062
        )

        st.markdown('**Acompanhante 09**')
        a8_nome = st.text_input(
            label='Nome',
            value=None,
            key=8063
        )
        a8_doc = st.text_input(
            label='Documento (RG/CPF)',
            value=None,
            key=8064
        )
        a8_idade = st.text_input(
            label='Idade',
            value=None,
            key=8066
        )
        a8_parentesco = st.text_input(
            label='Parentesco',
            value=None,
            key=8067
        )

        st.markdown('**Acompanhante 10**')
        a9_nome = st.text_input(
            label='Nome',
            value=None,
            key=8068
        )
        a9_doc = st.text_input(
            label='Documento (RG/CPF)',
            value=None,
            key=8069
        )
        a9_idade = st.text_input(
            label='Idade',
            value=None,
            key=8071
        )
        a9_parentesco = st.text_input(
            label='Parentesco',
            value=None,
            key=8072
        )

        submit_button = st.form_submit_button('Registrar')
        if submit_button:
            ficha_data = {
                'apto': apto,
                'nome': nome,
                'tipo_residencia': tipo_residencia,
                'cidade': cidade,
                'cep': cep,
                'uf': uf,
                'pais': pais,
                'tel': tel,
                'estado_civil': estado_civil,
                'profissao': profissao,
                'rg': rg,
                'cpf': cpf,
                'mae': mae,
                'automovel': automovel,
                'modelo_auto': modelo_auto,
                'placa_auto': placa_auto,
                'cor_auto': cor_auto,
                'checkin': checkin.isoformat(),
                'checkout': checkout.isoformat(),
                'observacoes': observacoes,
                'proprietario': proprietario,
                'imob_fone': imob_fone,
                'a0': {'nome': a0_nome, 'doc': a0_doc, 'idade': a0_idade, 'parentesco': a0_parentesco},
                'a1': {'nome': a1_nome, 'doc': a1_doc, 'idade': a1_idade, 'parentesco': a1_parentesco},
                'a2': {'nome': a2_nome, 'doc': a2_doc, 'idade': a2_idade, 'parentesco': a2_parentesco},
                'a3': {'nome': a3_nome, 'doc': a3_doc, 'idade': a3_idade, 'parentesco': a3_parentesco},
                'a4': {'nome': a4_nome, 'doc': a4_doc, 'idade': a4_idade, 'parentesco': a4_parentesco},
                'a5': {'nome': a5_nome, 'doc': a5_doc, 'idade': a5_idade, 'parentesco': a5_parentesco},
                'a6': {'nome': a6_nome, 'doc': a6_doc, 'idade': a6_idade, 'parentesco': a6_parentesco},
                'a7': {'nome': a7_nome, 'doc': a7_doc, 'idade': a7_idade, 'parentesco': a7_parentesco},
                'a8': {'nome': a8_nome, 'doc': a8_doc, 'idade': a8_idade, 'parentesco': a8_parentesco},
                'a9': {'nome': a9_nome, 'doc': a9_doc, 'idade': a9_idade, 'parentesco': a9_parentesco}
            }
            submit_data = json.dumps(obj=empty_none_dict(ficha_data), separators=(',',':'))

            try:
                post_response = requests.post('http://backend:8000/fichas/', submit_data)
                show_response_message(post_response)
                if post_response.status_code == 200:
                    st.subheader('Dados inseridos, tudo OK:')
                else:
                    st.subheader('Dados NÃO inseridos, favor revisar:')
                show_data_output(ficha_data)
            except Exception as e:
                print(e)

with tab2:
    st.header('Consultar Ficha de Inquilino')
    get_id = st.number_input(
        'ID da Ficha de Inquilino',
        min_value=1,
        value=None,
        format='%d',
        step=1,
        key=8250
    )
    if get_id:
        get_response = requests.get(f'http://backend:8000/fichas/{get_id}')
        if get_response.status_code == 200:
            ficha = get_response.json()
            df_get = pd.DataFrame([ficha])
            st.dataframe(df_get.set_index('id'))
        else:
            show_response_message(get_response)
        if st.button('Gerar PDF',key=8251):
            pdf = fill_ficha(ficha)
            if pdf:
                st.success(f'PDF gerado com sucesso')
                with open(pdf, 'rb') as f:
                    st.download_button(
                        label='Download PDF',
                        data=f,
                        file_name=pdf[26:],
                        mime='application/pdf',
                        key=8252
                    )
                os.remove(pdf)
            else:
                st.error(f'Não foi possível gerar o PDF')

with tab3:
    st.header('Modificar Ficha de Inquilino')
    update_id = st.number_input(
        'ID da Ficha',
        min_value=1,
        value=None,
        format='%d',
        step=1,
        key=8151
    )
    if update_id:
        update_response = requests.get(f'http://backend:8000/fichas/{update_id}')
        if update_response.status_code == 200:
            ficha_up = update_response.json()
            df_up = pd.DataFrame([ficha_up])
            st.dataframe(df_up.set_index('id'))
            st.subheader(f'Ficha de Inquilino nº: {update_id}')
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
                    options=['Casado(a)', 'Divorciado(a)', 'Separado(a)', 'Solteiro(a)', 'Viúvo(a)'],
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
                checkin: date = st.date_input(
                    label='Check-in',
                    value=str_to_date(df_up.checkin[0]),
                    format='DD/MM/YYYY',
                    key=8094
                )
                checkout: date = st.date_input(
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
                a0_nome = st.text_input(
                    label='Nome',
                    value=none_or_str(df_up['a0'].iloc[0].get('nome')),
                    key=8099
                )
                a0_doc = st.text_input(
                    label='Documento (RG/CPF)',
                    value=none_or_str(df_up['a0'].iloc[0].get('doc')),
                    key=8100
                )
                a0_idade = st.text_input(
                    label='Idade',
                    value=none_or_str(df_up['a0'].iloc[0].get('idade')),
                    key=8102
                )
                a0_parentesco = st.text_input(
                    label='Parentesco',
                    value=none_or_str(df_up['a0'].iloc[0].get('parentesco')),
                    key=8103
                )

                st.markdown('**Acompanhante 02**')
                a1_nome = st.text_input(
                    label='Nome',
                    value=none_or_str(df_up['a1'].iloc[0].get('nome')),
                    key=8104
                )
                a1_doc = st.text_input(
                    label='Documento (RG/CPF)',
                    value=none_or_str(df_up['a1'].iloc[0].get('doc')),
                    key=8105
                )
                a1_idade = st.text_input(
                    label='Idade',
                    value=none_or_str(df_up['a1'].iloc[0].get('idade')),
                    key=8107
                )
                a1_parentesco = st.text_input(
                    label='Parentesco',
                    value=none_or_str(df_up['a1'].iloc[0].get('parentesco')),
                    key=8108
                )

                st.markdown('**Acompanhante 03**')
                a2_nome = st.text_input(
                    label='Nome',
                    value=none_or_str(df_up['a2'].iloc[0].get('nome')),
                    key=8109
                )
                a2_doc = st.text_input(
                    label='Documento (RG/CPF)',
                    value=none_or_str(df_up['a2'].iloc[0].get('doc')),
                    key=8110
                )
                a2_idade = st.text_input(
                    label='Idade',
                    value=none_or_str(df_up['a2'].iloc[0].get('idade')),
                    key=8112
                )
                a2_parentesco = st.text_input(
                    label='Parentesco',
                    value=none_or_str(df_up['a2'].iloc[0].get('parentesco')),
                    key=8113
                )

                st.markdown('**Acompanhante 04**')
                a3_nome = st.text_input(
                    label='Nome',
                    value=none_or_str(df_up['a3'].iloc[0].get('nome')),
                    key=8114
                )
                a3_doc = st.text_input(
                    label='Documento (RG/CPF)',
                    value=none_or_str(df_up['a3'].iloc[0].get('doc')),
                    key=8115
                )
                a3_idade = st.text_input(
                    label='Idade',
                    value=none_or_str(df_up['a3'].iloc[0].get('idade')),
                    key=8117
                )
                a3_parentesco = st.text_input(
                    label='Parentesco',
                    value=none_or_str(df_up['a3'].iloc[0].get('parentesco')),
                    key=8118
                )

                st.markdown('**Acompanhante 05**')
                a4_nome = st.text_input(
                    label='Nome',
                    value=none_or_str(df_up['a4'].iloc[0].get('nome')),
                    key=8119
                )
                a4_doc = st.text_input(
                    label='Documento (RG/CPF)',
                    value=none_or_str(df_up['a4'].iloc[0].get('doc')),
                    key=8120
                )
                a4_idade = st.text_input(
                    label='Idade',
                    value=none_or_str(df_up['a4'].iloc[0].get('idade')),
                    key=8122
                )
                a4_parentesco = st.text_input(
                    label='Parentesco',
                    value=none_or_str(df_up['a4'].iloc[0].get('parentesco')),
                    key=8123
                )

                st.markdown('**Acompanhante 06**')
                a5_nome = st.text_input(
                    label='Nome',
                    value=none_or_str(df_up['a5'].iloc[0].get('nome')),
                    key=8124
                )
                a5_doc = st.text_input(
                    label='Documento (RG/CPF)',
                    value=none_or_str(df_up['a5'].iloc[0].get('doc')),
                    key=8125
                )
                a5_idade = st.text_input(
                    label='Idade',
                    value=none_or_str(df_up['a5'].iloc[0].get('idade')),
                    key=8127
                )
                a5_parentesco = st.text_input(
                    label='Parentesco',
                    value=none_or_str(df_up['a5'].iloc[0].get('parentesco')),
                    key=8128
                )

                st.markdown('**Acompanhante 07**')
                a6_nome = st.text_input(
                    label='Nome',
                    value=none_or_str(df_up['a6'].iloc[0].get('nome')),
                    key=8129
                )
                a6_doc = st.text_input(
                    label='Documento (RG/CPF)',
                    value=none_or_str(df_up['a6'].iloc[0].get('doc')),
                    key=8130
                )
                a6_idade = st.text_input(
                    label='Idade',
                    value=none_or_str(df_up['a6'].iloc[0].get('idade')),
                    key=8132
                )
                a6_parentesco = st.text_input(
                    label='Parentesco',
                    value=none_or_str(df_up['a6'].iloc[0].get('parentesco')),
                    key=8133
                )

                st.markdown('**Acompanhante 08**')
                a7_nome = st.text_input(
                    label='Nome',
                    value=none_or_str(df_up['a7'].iloc[0].get('nome')),
                    key=8134
                )
                a7_doc = st.text_input(
                    label='Documento (RG/CPF)',
                    value=none_or_str(df_up['a7'].iloc[0].get('doc')),
                    key=8135
                )
                a7_idade = st.text_input(
                    label='Idade',
                    value=none_or_str(df_up['a7'].iloc[0].get('idade')),
                    key=8137
                )
                a7_parentesco = st.text_input(
                    label='Parentesco',
                    value=none_or_str(df_up['a7'].iloc[0].get('parentesco')),
                    key=8138
                )

                st.markdown('**Acompanhante 09**')
                a8_nome = st.text_input(
                    label='Nome',
                    value=none_or_str(df_up['a8'].iloc[0].get('nome')),
                    key=8139
                )
                a8_doc = st.text_input(
                    label='Documento (RG/CPF)',
                    value=none_or_str(df_up['a8'].iloc[0].get('doc')),
                    key=8140
                )
                a8_idade = st.text_input(
                    label='Idade',
                    value=none_or_str(df_up['a8'].iloc[0].get('idade')),
                    key=8142
                )
                a8_parentesco = st.text_input(
                    label='Parentesco',
                    value=none_or_str(df_up['a8'].iloc[0].get('parentesco')),
                    key=8143
                )

                st.markdown('**Acompanhante 10**')
                a9_nome = st.text_input(
                    label='Nome',
                    value=none_or_str(df_up['a9'].iloc[0].get('nome')),
                    key=8144
                )
                a9_doc = st.text_input(
                    label='Documento (RG/CPF)',
                    value=none_or_str(df_up['a9'].iloc[0].get('doc')),
                    key=8145
                )
                a9_idade = st.text_input(
                    label='Idade',
                    value=none_or_str(df_up['a9'].iloc[0].get('idade')),
                    key=8147
                )
                a9_parentesco = st.text_input(
                    label='Parentesco',
                    value=none_or_str(df_up['a9'].iloc[0].get('parentesco')),
                    key=8148
                )

                update_button = st.form_submit_button('Modificar')
                if update_button:
                    ficha_up_data = {
                        'apto': apto,
                        'nome': nome,
                        'tipo_residencia': tipo_residencia,
                        'cidade': cidade,
                        'cep': cep,
                        'uf': uf,
                        'pais': pais,
                        'tel': tel,
                        'estado_civil': estado_civil,
                        'profissao': profissao,
                        'rg': rg,
                        'cpf': cpf,
                        'mae': mae,
                        'automovel': automovel,
                        'modelo_auto': modelo_auto,
                        'placa_auto': placa_auto,
                        'cor_auto': cor_auto,
                        'checkin': checkin.isoformat(),
                        'checkout': checkout.isoformat(),
                        'observacoes': observacoes,
                        'proprietario': proprietario,
                        'imob_fone': imob_fone,
                        'a0': {'nome': a0_nome, 'doc': a0_doc, 'idade': a0_idade, 'parentesco': a0_parentesco},
                        'a1': {'nome': a1_nome, 'doc': a1_doc, 'idade': a1_idade, 'parentesco': a1_parentesco},
                        'a2': {'nome': a2_nome, 'doc': a2_doc, 'idade': a2_idade, 'parentesco': a2_parentesco},
                        'a3': {'nome': a3_nome, 'doc': a3_doc, 'idade': a3_idade, 'parentesco': a3_parentesco},
                        'a4': {'nome': a4_nome, 'doc': a4_doc, 'idade': a4_idade, 'parentesco': a4_parentesco},
                        'a5': {'nome': a5_nome, 'doc': a5_doc, 'idade': a5_idade, 'parentesco': a5_parentesco},
                        'a6': {'nome': a6_nome, 'doc': a6_doc, 'idade': a6_idade, 'parentesco': a6_parentesco},
                        'a7': {'nome': a7_nome, 'doc': a7_doc, 'idade': a7_idade, 'parentesco': a7_parentesco},
                        'a8': {'nome': a8_nome, 'doc': a8_doc, 'idade': a8_idade, 'parentesco': a8_parentesco},
                        'a9': {'nome': a9_nome, 'doc': a9_doc, 'idade': a9_idade, 'parentesco': a9_parentesco}
                    }
                    update_data = json.dumps(obj=empty_none_dict(ficha_up_data), separators=(',',':'))

                    try:
                        put_response = requests.put(f'http://backend:8000/fichas/{update_id}', update_data)
                        show_response_message(put_response)
                        if put_response.status_code == 200:
                            st.subheader('Dados inseridos, tudo OK:')
                        else:
                            st.subheader('Dados NÃO inseridos, favor revisar:')
                        show_data_output(ficha_up_data)
                    except Exception as e:
                        print(e)

        else:
            show_response_message(update_response)

with tab4:
    st.header('Deletar Ficha de Inquilino')
    delete_id = st.number_input(
        label='ID Ficha',
        min_value=1,
        value=None,
        format='%d',
        step=1,
        key=8149
    )
    if delete_id:
        show_delete_response = requests.get(f'http://backend:8000/fichas/{delete_id}')
        if show_delete_response.status_code == 200:
            ficha_delete = show_delete_response.json()
            df_delete = pd.DataFrame([ficha_delete])
            st.dataframe(df_delete.set_index('id'))
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
        'Mostrar',
        key=6500
    ):
        get_list_response = requests.get(f'http://backend:8000/fichas/')
        if get_list_response.status_code == 200:
            fichas = get_list_response.json()
            if fichas:
                df_list = pd.DataFrame(fichas)
                if df_list['id']:
                    st.dataframe(df_list.set_index('id'))
                else:
                    st.dataframe(df_list, hide_index=True)
            else:
                st.warning('Não há fichas para listar')
        else:
            show_response_message(get_list_response)