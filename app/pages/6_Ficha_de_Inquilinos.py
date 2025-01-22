from datetime import date
import json
import os
import pandas as pd
import requests
import streamlit as st
from utils.mydate import calculate_diarias, str_to_date
from utils.myfunc import cat_index, show_data_output, show_response_message
from utils.mynum import cep_input, cpf_input, rg_input, tel_input_br
from utils.mypdf import fill_ficha
from utils.mystr import apto_input, csv_handler, empty_none_dict, none_or_str

st.set_page_config(page_title="Ficha de Inquilinos", layout="wide")
st.title("Ficha de Inquilinos")

tab1, tab2, tab3, tab4, tab5 = st.tabs(
    ["Registrar", "Consultar", "Modificar", "Deletar", "Listar"]
)

with tab1:
    st.header("Registrar Ficha de Inquilino")
    st.write("Registre uma ficha a partir de um arquivo .csv")
    uploaded_ficha = st.file_uploader(label="Enviar Arquivo", type="csv", key=6100)
    if uploaded_ficha is not None:
        with st.spinner("Processando arquivo..."):
            try:
                df = csv_handler(uploaded_ficha)
                st.dataframe(df, hide_index=True)
                if st.button("Registrar", key=61005):
                    for i, r in df.iterrows():
                        ficha_data = {
                            "apto_id": None,
                            "nome": df.nome[i],
                            "tipo_residencia": "Temporário",
                            "cidade": df.cidade[i],
                            "cep": cep_input(df.cep[i]),
                            "uf": df.uf[i],
                            "pais": df.pais[i],
                            "tel": tel_input_br(df.tel[i]),
                            "estado_civil": df.estado_civil[i],
                            "profissao": df.profissao[i],
                            "rg": rg_input(df.rg[i]),
                            "cpf": cpf_input(df.cpf[i]),
                            "mae": df.mae[i],
                            "automovel": df.automovel[i],
                            "modelo_auto": df.modelo_auto[i],
                            "placa_auto": df.placa_auto[i],
                            "cor_auto": df.cor_auto[i],
                            "checkin": str(str_to_date(df.checkin[i])),
                            "checkout": str(str_to_date(df.checkout[i])),
                            "observacoes": None,
                            "proprietario": None,
                            "imob_fone": None,
                            "a0": {
                                "nome": df.a0_nome[i],
                                "doc": df.a0_doc[i],
                                "idade": df.a0_idade[i],
                                "parentesco": df.a0_parentesco[i],
                            },
                            "a1": {
                                "nome": df.a1_nome[i],
                                "doc": df.a1_doc[i],
                                "idade": df.a1_idade[i],
                                "parentesco": df.a1_parentesco[i],
                            },
                            "a2": {
                                "nome": df.a2_nome[i],
                                "doc": df.a2_doc[i],
                                "idade": df.a2_idade[i],
                                "parentesco": df.a2_parentesco[i],
                            },
                            "a3": {
                                "nome": df.a3_nome[i],
                                "doc": df.a3_doc[i],
                                "idade": df.a3_idade[i],
                                "parentesco": df.a3_parentesco[i],
                            },
                            "a4": {
                                "nome": df.a4_nome[i],
                                "doc": df.a4_doc[i],
                                "idade": df.a4_idade[i],
                                "parentesco": df.a4_parentesco[i],
                            },
                            "a5": {
                                "nome": df.a5_nome[i],
                                "doc": df.a5_doc[i],
                                "idade": df.a5_idade[i],
                                "parentesco": df.a5_parentesco[i],
                            },
                            "a6": {
                                "nome": df.a6_nome[i],
                                "doc": df.a6_doc[i],
                                "idade": df.a6_idade[i],
                                "parentesco": df.a6_parentesco[i],
                            },
                            "a7": {
                                "nome": df.a7_nome[i],
                                "doc": df.a7_doc[i],
                                "idade": df.a7_idade[i],
                                "parentesco": df.a7_parentesco[i],
                            },
                            "a8": {
                                "nome": df.a8_nome[i],
                                "doc": df.a8_doc[i],
                                "idade": df.a8_idade[i],
                                "parentesco": df.a8_parentesco[i],
                            },
                            "a9": {
                                "nome": df.a9_nome[i],
                                "doc": df.a9_doc[i],
                                "idade": df.a9_idade[i],
                                "parentesco": df.a9_parentesco[i],
                            },
                        }
                        submit_data = json.dumps(obj=ficha_data, separators=(",", ":"))
                        try:
                            post_response = requests.post(
                                "http://api:8000/fichas/", submit_data
                            )
                            show_response_message(post_response)
                            if post_response.status_code == 200:
                                st.subheader("Dados inseridos, tudo OK:")
                            else:
                                st.subheader("Dados NÃO inseridos, favor revisar:")
                            show_data_output(ficha_data)
                        except Exception as e:
                            raise (e)
            except pd.errors.ParserError:
                st.error(
                    "Erro: O arquivo enviado não é um CSV válido ou está mal formatado."
                )
            except Exception as e:
                st.error(f"Ocorreu um erro ao processar o arquivo: {e}")
    st.write("Ou digite os dados abaixo:")
    st.markdown(
        '<p style="font-size: 12px;">Campos com * são obrigatórios</p>',
        unsafe_allow_html=True,
    )
    apto_id = st.text_input(label="Apartamento", value=None, key=6101)
    nome = st.text_input(label="Nome completo *", value=None, key=6102)
    tipo_residencia = st.radio(
        label="Tipo de residência *",
        options=["Anual", "Temporário"],
        index=1,
        horizontal=True,
        key=6103,
    )
    cidade = st.text_input(label="Naturalidade (cidade) *", value=None, key=6104)
    cep = st.text_input(label="CEP *", value=None, key=6105)
    uf = st.text_input(label="Estado (UF) *", value=None, key=6106)
    pais = st.text_input(label="País *", value=None, key=6107)
    tel = st.text_input(label="Telefone *", value=None, key=6108)
    estado_civil = st.selectbox(
        label="Estado civíl *",
        index=0,
        options=[
            "Casado(a)",
            "Divorciado(a)",
            "Separado(a)",
            "Solteiro(a)",
            "Viúvo(a)",
        ],
        key=6109,
    )
    profissao = st.text_input(label="Profissão *", value=None, key=6110)
    rg = st.text_input(label="Identidade *", value=None, key=6111)
    cpf = st.text_input(label="CPF *", value=None, key=6112)
    mae = st.text_input(label="Nome completo da mãe *", value=None, key=6113)
    with st.expander("Dados do Automóvel"):
        automovel = st.text_input(label="Automóvel", value=None, key=6114)
        modelo_auto = st.text_input(label="Modelo", value=None, key=6115)
        placa_auto = st.text_input(label="Placa", value=None, key=6116)
        cor_auto = st.text_input(label="Cor", value=None, key=6117)
    checkin: date = st.date_input(
        label="Check-in *", format="DD/MM/YYYY", key=6118, value=None
    )
    checkout: date = st.date_input(
        label="Check-out *", format="DD/MM/YYYY", key=6119, value=None
    )
    diarias: int = calculate_diarias(checkin, checkout)
    st.write(f"Diárias: {diarias}")
    observacoes = st.text_input(label="Observações", value=None, key=6120)
    proprietario = st.text_input(label="Proprietário", value=None, key=6121)
    imob_fone = st.text_input(label="Telefone Imobiliária", value=None, key=6122)
    with st.expander(label="Acompanhantes 1 a 5"):
        st.markdown("**Acompanhante 01**")
        a0_nome = st.text_input(label="Nome", value=None, key=6123)
        a0_doc = st.text_input(label="Documento (RG/CPF)", value=None, key=6124)
        a0_idade = st.text_input(label="Idade", value=None, key=6126)
        a0_parentesco = st.text_input(label="Parentesco", value=None, key=6127)

        st.markdown("**Acompanhante 02**")
        a1_nome = st.text_input(label="Nome", value=None, key=6128)
        a1_doc = st.text_input(label="Documento (RG/CPF)", value=None, key=6129)
        a1_idade = st.text_input(label="Idade", value=None, key=6131)
        a1_parentesco = st.text_input(label="Parentesco", value=None, key=6132)

        st.markdown("**Acompanhante 03**")
        a2_nome = st.text_input(label="Nome", value=None, key=6133)
        a2_doc = st.text_input(label="Documento (RG/CPF)", value=None, key=6134)
        a2_idade = st.text_input(label="Idade", value=None, key=6136)
        a2_parentesco = st.text_input(label="Parentesco", value=None, key=6137)

        st.markdown("**Acompanhante 04**")
        a3_nome = st.text_input(label="Nome", value=None, key=6138)
        a3_doc = st.text_input(label="Documento (RG/CPF)", value=None, key=6139)
        a3_idade = st.text_input(label="Idade", value=None, key=6141)
        a3_parentesco = st.text_input(label="Parentesco", value=None, key=6142)

        st.markdown("**Acompanhante 05**")
        a4_nome = st.text_input(label="Nome", value=None, key=6143)
        a4_doc = st.text_input(label="Documento (RG/CPF)", value=None, key=6144)
        a4_idade = st.text_input(label="Idade", value=None, key=6146)
        a4_parentesco = st.text_input(label="Parentesco", value=None, key=6147)
    with st.expander("Acompanhantes 6 a 10"):
        st.markdown("**Acompanhante 06**")
        a5_nome = st.text_input(label="Nome", value=None, key=6148)
        a5_doc = st.text_input(label="Documento (RG/CPF)", value=None, key=6149)
        a5_idade = st.text_input(label="Idade", value=None, key=6151)
        a5_parentesco = st.text_input(label="Parentesco", value=None, key=6152)

        st.markdown("**Acompanhante 07**")
        a6_nome = st.text_input(label="Nome", value=None, key=6153)
        a6_doc = st.text_input(label="Documento (RG/CPF)", value=None, key=6154)
        a6_idade = st.text_input(label="Idade", value=None, key=6156)
        a6_parentesco = st.text_input(label="Parentesco", value=None, key=6157)

        st.markdown("**Acompanhante 08**")
        a7_nome = st.text_input(label="Nome", value=None, key=6158)
        a7_doc = st.text_input(label="Documento (RG/CPF)", value=None, key=6159)
        a7_idade = st.text_input(label="Idade", value=None, key=6161)
        a7_parentesco = st.text_input(label="Parentesco", value=None, key=6162)

        st.markdown("**Acompanhante 09**")
        a8_nome = st.text_input(label="Nome", value=None, key=6163)
        a8_doc = st.text_input(label="Documento (RG/CPF)", value=None, key=6164)
        a8_idade = st.text_input(label="Idade", value=None, key=6166)
        a8_parentesco = st.text_input(label="Parentesco", value=None, key=6167)

        st.markdown("**Acompanhante 10**")
        a9_nome = st.text_input(label="Nome", value=None, key=6168)
        a9_doc = st.text_input(label="Documento (RG/CPF)", value=None, key=6169)
        a9_idade = st.text_input(label="Idade", value=None, key=6171)
        a9_parentesco = st.text_input(label="Parentesco", value=None, key=6172)
    if st.button("Registrar", key=6173):
        ficha_data = {
            "apto_id": apto_input(apto_id),
            "nome": nome,
            "tipo_residencia": tipo_residencia,
            "cidade": cidade,
            "cep": cep_input(cep),
            "uf": uf,
            "pais": pais,
            "tel": tel_input_br(tel),
            "estado_civil": estado_civil,
            "profissao": profissao,
            "rg": rg_input(rg),
            "cpf": cpf_input(cpf),
            "mae": mae,
            "automovel": automovel,
            "modelo_auto": modelo_auto,
            "placa_auto": placa_auto,
            "cor_auto": cor_auto,
            "checkin": checkin.isoformat(),
            "checkout": checkout.isoformat(),
            "observacoes": observacoes,
            "proprietario": proprietario,
            "imob_fone": tel_input_br(imob_fone),
            "a0": {
                "nome": a0_nome,
                "doc": a0_doc,
                "idade": a0_idade,
                "parentesco": a0_parentesco,
            },
            "a1": {
                "nome": a1_nome,
                "doc": a1_doc,
                "idade": a1_idade,
                "parentesco": a1_parentesco,
            },
            "a2": {
                "nome": a2_nome,
                "doc": a2_doc,
                "idade": a2_idade,
                "parentesco": a2_parentesco,
            },
            "a3": {
                "nome": a3_nome,
                "doc": a3_doc,
                "idade": a3_idade,
                "parentesco": a3_parentesco,
            },
            "a4": {
                "nome": a4_nome,
                "doc": a4_doc,
                "idade": a4_idade,
                "parentesco": a4_parentesco,
            },
            "a5": {
                "nome": a5_nome,
                "doc": a5_doc,
                "idade": a5_idade,
                "parentesco": a5_parentesco,
            },
            "a6": {
                "nome": a6_nome,
                "doc": a6_doc,
                "idade": a6_idade,
                "parentesco": a6_parentesco,
            },
            "a7": {
                "nome": a7_nome,
                "doc": a7_doc,
                "idade": a7_idade,
                "parentesco": a7_parentesco,
            },
            "a8": {
                "nome": a8_nome,
                "doc": a8_doc,
                "idade": a8_idade,
                "parentesco": a8_parentesco,
            },
            "a9": {
                "nome": a9_nome,
                "doc": a9_doc,
                "idade": a9_idade,
                "parentesco": a9_parentesco,
            },
        }
        submit_data = json.dumps(obj=empty_none_dict(ficha_data), separators=(",", ":"))

        try:
            post_response = requests.post("http://api:8000/fichas/", submit_data)
            show_response_message(post_response)
            if post_response.status_code == 200:
                st.subheader("Dados inseridos, tudo OK:")
            else:
                st.subheader("Dados NÃO inseridos, favor revisar:")
            show_data_output(ficha_data)
        except Exception as e:
            raise (e)

with tab2:
    st.header("Consultar Ficha de Inquilino")
    get_id = st.number_input(
        "ID da Ficha de Inquilino",
        min_value=1,
        value=None,
        format="%d",
        step=1,
        key=6200,
    )
    if get_id:
        get_response = requests.get(f"http://api:8000/fichas/{get_id}")
        if get_response.status_code == 200:
            ficha = get_response.json()
            df_get = pd.DataFrame([ficha])
            st.dataframe(df_get.set_index("id"))
        else:
            show_response_message(get_response)
        if st.button("Gerar PDF", key=6201):
            pdf = fill_ficha(ficha)
            if pdf:
                st.success(f"PDF gerado com sucesso")
                with open(pdf, "rb") as f:
                    st.download_button(
                        label="Download PDF",
                        data=f,
                        file_name=pdf[26:],
                        mime="application/pdf",
                        key=6203,
                    )
                os.remove(pdf)
            else:
                st.error(f"Não foi possível gerar o PDF")

with tab3:
    civil_cats = [
        "Casado(a)",
        "Divorciado(a)",
        "Separado(a)",
        "Solteiro(a)",
        "Viúvo(a)",
    ]
    st.header("Modificar Ficha de Inquilino")
    st.markdown(
        '<p style="font-size: 12px;">Campos com * são obrigatórios</p>',
        unsafe_allow_html=True,
    )
    update_id = st.number_input(
        "ID da Ficha", min_value=1, value=None, format="%d", step=1, key=6300
    )
    if update_id:
        update_response = requests.get(f"http://api:8000/fichas/{update_id}")
        if update_response.status_code == 200:
            ficha_up = update_response.json()
            df_up = pd.DataFrame([ficha_up])
            st.dataframe(df_up.set_index("id"))
            st.subheader(f"Ficha de Inquilino nº: {update_id}")
            apto_id = st.text_input(
                label="Apartamento", value=str(df_up.apto_id[0]), key=6301
            )
            nome = st.text_input(
                label="Nome completo *", value=str(df_up.nome[0]), key=6302
            )
            tipo_residencia = st.radio(
                label="Tipo de residência *",
                options=["Anual", "Temporário"],
                index=cat_index(df_up, "tipo_residencia", ["Anual", "Temporário"]),
                horizontal=True,
                key=6303,
            )
            cidade = st.text_input(
                label="Naturalidade (cidade) *", value=str(df_up.cidade[0]), key=6304
            )
            cep = st.text_input(label="CEP *", value=str(df_up.cep[0]), key=6305)
            uf = st.text_input(label="Estado (UF) *", value=str(df_up.uf[0]), key=6306)
            pais = st.text_input(label="País *", value=str(df_up.pais[0]), key=6307)
            tel = st.text_input(label="Telefone *", value=str(df_up.tel[0]), key=6308)
            estado_civil = st.selectbox(
                label="Estado civíl *",
                options=[
                    "Casado(a)",
                    "Divorciado(a)",
                    "Separado(a)",
                    "Solteiro(a)",
                    "Viúvo(a)",
                ],
                index=cat_index(df_up, "estado_civil", civil_cats),
                key=6309,
            )
            profissao = st.text_input(
                label="Profissão *", value=str(df_up.profissao[0]), key=6310
            )
            rg = st.text_input(
                label="Identidade (RG) *", value=none_or_str(df_up.rg[0]), key=6311
            )
            cpf = st.text_input(
                label="CPF *", value=str(df_up.cpf[0]), help="Somente números", key=6312
            )
            mae = st.text_input(
                label="Nome completo da mãe *", value=str(df_up.mae[0]), key=6313
            )
            with st.expander("Dados do Automóvel"):
                automovel = st.text_input(
                    label="Automóvel", value=none_or_str(df_up.automovel[0]), key=6314
                )
                modelo_auto = st.text_input(
                    label="Modelo", value=none_or_str(df_up.modelo_auto[0]), key=6315
                )
                placa_auto = st.text_input(
                    label="Placa", value=none_or_str(df_up.placa_auto[0]), key=6316
                )
                cor_auto = st.text_input(
                    label="Cor", value=none_or_str(df_up.cor_auto[0]), key=6317
                )
            checkin: date = st.date_input(
                label="Check-in *",
                value=str_to_date(df_up.checkin[0]),
                format="DD/MM/YYYY",
                key=6318,
            )
            checkout: date = st.date_input(
                label="Check-out *",
                value=str_to_date(df_up.checkout[0]),
                format="DD/MM/YYYY",
                key=6319,
            )
            diarias: int = calculate_diarias(checkin, checkout)
            st.write(f"Diárias: {diarias}")
            observacoes = st.text_input(
                label="Observações",
                value=none_or_str(df_up.loc[0, "observacoes"]),
                key=6320,
            )
            proprietario = st.text_input(
                label="Proprietário", value=none_or_str(df_up.proprietario[0]), key=6321
            )
            imob_fone = st.text_input(
                label="Telefone Imobiliária",
                value=none_or_str(df_up.imob_fone[0]),
                key=6322,
            )
            with st.expander("Acompanhantes 1 a 5"):
                st.markdown("**Acompanhante 01**")
                a0_nome = st.text_input(
                    label="Nome",
                    value=none_or_str(df_up["a0"].iloc[0].get("nome")),
                    key=6323,
                )
                a0_doc = st.text_input(
                    label="Documento (RG/CPF)",
                    value=none_or_str(df_up["a0"].iloc[0].get("doc")),
                    key=6324,
                )
                a0_idade = st.text_input(
                    label="Idade",
                    value=none_or_str(df_up["a0"].iloc[0].get("idade")),
                    key=6325,
                )
                a0_parentesco = st.text_input(
                    label="Parentesco",
                    value=none_or_str(df_up["a0"].iloc[0].get("parentesco")),
                    key=6326,
                )

                st.markdown("**Acompanhante 02**")
                a1_nome = st.text_input(
                    label="Nome",
                    value=none_or_str(df_up["a1"].iloc[0].get("nome")),
                    key=6327,
                )
                a1_doc = st.text_input(
                    label="Documento (RG/CPF)",
                    value=none_or_str(df_up["a1"].iloc[0].get("doc")),
                    key=6328,
                )
                a1_idade = st.text_input(
                    label="Idade",
                    value=none_or_str(df_up["a1"].iloc[0].get("idade")),
                    key=6329,
                )
                a1_parentesco = st.text_input(
                    label="Parentesco",
                    value=none_or_str(df_up["a1"].iloc[0].get("parentesco")),
                    key=6330,
                )

                st.markdown("**Acompanhante 03**")
                a2_nome = st.text_input(
                    label="Nome",
                    value=none_or_str(df_up["a2"].iloc[0].get("nome")),
                    key=6331,
                )
                a2_doc = st.text_input(
                    label="Documento (RG/CPF)",
                    value=none_or_str(df_up["a2"].iloc[0].get("doc")),
                    key=6332,
                )
                a2_idade = st.text_input(
                    label="Idade",
                    value=none_or_str(df_up["a2"].iloc[0].get("idade")),
                    key=6333,
                )
                a2_parentesco = st.text_input(
                    label="Parentesco",
                    value=none_or_str(df_up["a2"].iloc[0].get("parentesco")),
                    key=6334,
                )

                st.markdown("**Acompanhante 04**")
                a3_nome = st.text_input(
                    label="Nome",
                    value=none_or_str(df_up["a3"].iloc[0].get("nome")),
                    key=6335,
                )
                a3_doc = st.text_input(
                    label="Documento (RG/CPF)",
                    value=none_or_str(df_up["a3"].iloc[0].get("doc")),
                    key=6336,
                )
                a3_idade = st.text_input(
                    label="Idade",
                    value=none_or_str(df_up["a3"].iloc[0].get("idade")),
                    key=6337,
                )
                a3_parentesco = st.text_input(
                    label="Parentesco",
                    value=none_or_str(df_up["a3"].iloc[0].get("parentesco")),
                    key=6338,
                )

                st.markdown("**Acompanhante 05**")
                a4_nome = st.text_input(
                    label="Nome",
                    value=none_or_str(df_up["a4"].iloc[0].get("nome")),
                    key=6339,
                )
                a4_doc = st.text_input(
                    label="Documento (RG/CPF)",
                    value=none_or_str(df_up["a4"].iloc[0].get("doc")),
                    key=6340,
                )
                a4_idade = st.text_input(
                    label="Idade",
                    value=none_or_str(df_up["a4"].iloc[0].get("idade")),
                    key=6341,
                )
                a4_parentesco = st.text_input(
                    label="Parentesco",
                    value=none_or_str(df_up["a4"].iloc[0].get("parentesco")),
                    key=6342,
                )
            with st.expander("Acompanhantes 6 a 10"):
                st.markdown("**Acompanhante 06**")
                a5_nome = st.text_input(
                    label="Nome",
                    value=none_or_str(df_up["a5"].iloc[0].get("nome")),
                    key=6343,
                )
                a5_doc = st.text_input(
                    label="Documento (RG/CPF)",
                    value=none_or_str(df_up["a5"].iloc[0].get("doc")),
                    key=6344,
                )
                a5_idade = st.text_input(
                    label="Idade",
                    value=none_or_str(df_up["a5"].iloc[0].get("idade")),
                    key=6345,
                )
                a5_parentesco = st.text_input(
                    label="Parentesco",
                    value=none_or_str(df_up["a5"].iloc[0].get("parentesco")),
                    key=6346,
                )

                st.markdown("**Acompanhante 07**")
                a6_nome = st.text_input(
                    label="Nome",
                    value=none_or_str(df_up["a6"].iloc[0].get("nome")),
                    key=6347,
                )
                a6_doc = st.text_input(
                    label="Documento (RG/CPF)",
                    value=none_or_str(df_up["a6"].iloc[0].get("doc")),
                    key=6348,
                )
                a6_idade = st.text_input(
                    label="Idade",
                    value=none_or_str(df_up["a6"].iloc[0].get("idade")),
                    key=6349,
                )
                a6_parentesco = st.text_input(
                    label="Parentesco",
                    value=none_or_str(df_up["a6"].iloc[0].get("parentesco")),
                    key=6350,
                )

                st.markdown("**Acompanhante 08**")
                a7_nome = st.text_input(
                    label="Nome",
                    value=none_or_str(df_up["a7"].iloc[0].get("nome")),
                    key=6351,
                )
                a7_doc = st.text_input(
                    label="Documento (RG/CPF)",
                    value=none_or_str(df_up["a7"].iloc[0].get("doc")),
                    key=6352,
                )
                a7_idade = st.text_input(
                    label="Idade",
                    value=none_or_str(df_up["a7"].iloc[0].get("idade")),
                    key=6353,
                )
                a7_parentesco = st.text_input(
                    label="Parentesco",
                    value=none_or_str(df_up["a7"].iloc[0].get("parentesco")),
                    key=6354,
                )

                st.markdown("**Acompanhante 09**")
                a8_nome = st.text_input(
                    label="Nome",
                    value=none_or_str(df_up["a8"].iloc[0].get("nome")),
                    key=6355,
                )
                a8_doc = st.text_input(
                    label="Documento (RG/CPF)",
                    value=none_or_str(df_up["a8"].iloc[0].get("doc")),
                    key=6356,
                )
                a8_idade = st.text_input(
                    label="Idade",
                    value=none_or_str(df_up["a8"].iloc[0].get("idade")),
                    key=6357,
                )
                a8_parentesco = st.text_input(
                    label="Parentesco",
                    value=none_or_str(df_up["a8"].iloc[0].get("parentesco")),
                    key=6358,
                )

                st.markdown("**Acompanhante 10**")
                a9_nome = st.text_input(
                    label="Nome",
                    value=none_or_str(df_up["a9"].iloc[0].get("nome")),
                    key=6359,
                )
                a9_doc = st.text_input(
                    label="Documento (RG/CPF)",
                    value=none_or_str(df_up["a9"].iloc[0].get("doc")),
                    key=6360,
                )
                a9_idade = st.text_input(
                    label="Idade",
                    value=none_or_str(df_up["a9"].iloc[0].get("idade")),
                    key=6361,
                )
                a9_parentesco = st.text_input(
                    label="Parentesco",
                    value=none_or_str(df_up["a9"].iloc[0].get("parentesco")),
                    key=6362,
                )
            if st.button("Modificar"):
                ficha_up_data = {
                    "apto_id": apto_input(apto_id),
                    "nome": nome,
                    "tipo_residencia": tipo_residencia,
                    "cidade": cidade,
                    "cep": cep_input(cep),
                    "uf": uf,
                    "pais": pais,
                    "tel": tel_input_br(tel),
                    "estado_civil": estado_civil,
                    "profissao": profissao,
                    "rg": rg_input(rg),
                    "cpf": cpf_input(cpf),
                    "mae": mae,
                    "automovel": automovel,
                    "modelo_auto": modelo_auto,
                    "placa_auto": placa_auto,
                    "cor_auto": cor_auto,
                    "checkin": checkin.isoformat(),
                    "checkout": checkout.isoformat(),
                    "observacoes": observacoes,
                    "proprietario": proprietario,
                    "imob_fone": tel_input_br(imob_fone),
                    "a0": {
                        "nome": a0_nome,
                        "doc": a0_doc,
                        "idade": a0_idade,
                        "parentesco": a0_parentesco,
                    },
                    "a1": {
                        "nome": a1_nome,
                        "doc": a1_doc,
                        "idade": a1_idade,
                        "parentesco": a1_parentesco,
                    },
                    "a2": {
                        "nome": a2_nome,
                        "doc": a2_doc,
                        "idade": a2_idade,
                        "parentesco": a2_parentesco,
                    },
                    "a3": {
                        "nome": a3_nome,
                        "doc": a3_doc,
                        "idade": a3_idade,
                        "parentesco": a3_parentesco,
                    },
                    "a4": {
                        "nome": a4_nome,
                        "doc": a4_doc,
                        "idade": a4_idade,
                        "parentesco": a4_parentesco,
                    },
                    "a5": {
                        "nome": a5_nome,
                        "doc": a5_doc,
                        "idade": a5_idade,
                        "parentesco": a5_parentesco,
                    },
                    "a6": {
                        "nome": a6_nome,
                        "doc": a6_doc,
                        "idade": a6_idade,
                        "parentesco": a6_parentesco,
                    },
                    "a7": {
                        "nome": a7_nome,
                        "doc": a7_doc,
                        "idade": a7_idade,
                        "parentesco": a7_parentesco,
                    },
                    "a8": {
                        "nome": a8_nome,
                        "doc": a8_doc,
                        "idade": a8_idade,
                        "parentesco": a8_parentesco,
                    },
                    "a9": {
                        "nome": a9_nome,
                        "doc": a9_doc,
                        "idade": a9_idade,
                        "parentesco": a9_parentesco,
                    },
                }
                update_data = json.dumps(
                    obj=empty_none_dict(ficha_up_data), separators=(",", ":")
                )

                try:
                    put_response = requests.put(
                        f"http://api:8000/fichas/{update_id}", update_data
                    )
                    show_response_message(put_response)
                    if put_response.status_code == 200:
                        st.subheader("Dados inseridos, tudo OK:")
                    else:
                        st.subheader("Dados NÃO inseridos, favor revisar:")
                    show_data_output(ficha_up_data)
                except Exception as e:
                    raise (e)

        else:
            show_response_message(update_response)

with tab4:
    st.header("Deletar Ficha de Inquilino")
    delete_id = st.number_input(
        label="ID Ficha", min_value=1, value=None, format="%d", step=1, key=6400
    )
    if delete_id:
        show_delete_response = requests.get(f"http://api:8000/fichas/{delete_id}")
        if show_delete_response.status_code == 200:
            ficha_delete = show_delete_response.json()
            df_delete = pd.DataFrame([ficha_delete])
            st.dataframe(df_delete.set_index("id"))
            delete_confirm = st.checkbox("Confirma que deseja deletar o registro?")
            delete_button = st.button("Deletar", key=1401)
            if delete_button and delete_confirm:
                delete_response = requests.delete(f"http://api:8000/fichas/{delete_id}")
                show_response_message(delete_response)
            elif delete_button and not delete_confirm:
                st.warning("Você deve confirmar primeiro para deletar o registro")
        else:
            show_response_message(show_delete_response)

with tab5:
    st.header("Listar Fichas de Inquilino")
    if st.button("Mostrar", key=6500):
        get_list_response = requests.get(f"http://api:8000/fichas/")
        if get_list_response.status_code == 200:
            fichas = get_list_response.json()
            if fichas:
                df_list = pd.DataFrame(fichas)
                st.dataframe(df_list.set_index("id"))
            else:
                st.warning("Não há fichas para listar")
        else:
            show_response_message(get_list_response)
