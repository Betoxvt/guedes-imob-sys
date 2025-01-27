from datetime import date, datetime
import locale
import os
import pandas as pd
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph, SimpleDocTemplate, Table, TableStyle, Spacer
import requests
import streamlit as st
from utils.mydate import showbr_dfdate
from utils.myfunc import show_data_output, show_response_message
from utils.mystr import apto_input

st.title("Relatórios")
comissao = 0.15
locale.setlocale(locale.LC_ALL, "pt_BR.UTF-8")
tab1, tab2 = st.tabs(["Gerar Relatório", "Editar Relatório"])

with tab1:
    st.subheader("Gerar Relatório")
    st.markdown(
        '<p style="font-size: 12px;">Campos com * são obrigatórios</p>',
        unsafe_allow_html=True,
    )
    apto_id: str = apto_input(
        st.text_input(label="Apartamento *", key=8100, value=None)
    )
    if apto_id:
        apto_response = requests.get(f"http://api:8000/apartamentos/{apto_id}")
        if apto_response.status_code == 200:
            relatorios_response = requests.get("http://api:8000/relatorios/")
            if relatorios_response.status_code == 200:
                relatorios = relatorios_response.json()
                if relatorios:
                    df_rel = pd.DataFrame(relatorios)
                    df_rel = df_rel[df_rel["apto_id"] == apto_id]
                    if not df_rel.empty:
                        df_rel = df_rel.sort_values(by="data", ascending=False)
                        last_rel = df_rel.iloc[0]
                        from_day = last_rel.loc["data"]
                        value = last_rel.loc["valor"]
                        st.markdown(
                            f"Último relatório foi em **{datetime.strptime(from_day, "%Y-%m-%d").strftime("%d/%m/%Y")}**"
                        )
                        st.markdown(
                            f"E foi entregue ao proprietário, um montante de **{locale.currency(value)}**"
                        )
                        from_day = st.date_input(
                            label="Data de início *",
                            key=8101,
                            value=from_day,
                            format="DD/MM/YYYY",
                        )
                    else:
                        st.write("Não foi encontrada a data do último pagamento")
                        st.write("Insira a data de início do relatório")
                        from_day = st.date_input(
                            label="Data de início *",
                            key=8102,
                            value=None,
                            format="DD/MM/YYYY",
                        )
                else:
                    st.write("Não foi encontrada a data do último pagamento")
                    st.write("Insira a data de início do relatório")
                    from_day = st.date_input(
                        label="Data de início *",
                        key=8103,
                        value=None,
                        format="DD/MM/YYYY",
                    )
            else:
                show_response_message(relatorios_response)
            if from_day:
                despesas_response = requests.get("http://api:8000/despesas/")
                if despesas_response.status_code == 200:
                    despesas = despesas_response.json()
                    if despesas:
                        df_desp = pd.DataFrame(despesas)
                        df_desp = df_desp[df_desp["apto_id"] == apto_id]
                        df_desp = df_desp[df_desp["data"] > from_day.isoformat()]
                        if not df_desp.empty:
                            df_desp = df_desp.sort_values(by=["data"])
                            df_desp = df_desp.drop(
                                ["apto_id", "id", "criado_em", "modificado_em"], axis=1
                            )
                            desp_ord = ["data", "categoria", "descricao", "valor"]
                            despesas_tot = df_desp["valor"].sum()
                            df_desp = showbr_dfdate(df_desp.reindex(desp_ord, axis=1))
                            df_desp.columns = [
                                "Data",
                                "Categoria",
                                "Descrição",
                                "Valor",
                            ]
                            df_desp["Valor"] = df_desp["Valor"].apply(
                                lambda x: locale.currency(x, grouping=True)
                            )
                            st.markdown("#### Despesas")
                            st.dataframe(
                                df_desp, hide_index=True, use_container_width=True
                            )
                            st.markdown(
                                f":red[Valor das Despesas: {locale.currency(despesas_tot)}]"
                            )
                        else:
                            st.warning(
                                f"Não há despesas para o {apto_id} desde {from_day}"
                            )
                            despesas_tot = 0
                    else:
                        st.warning("Não há despesas")
                else:
                    show_response_message(despesas_response)

                alugueis_response = requests.get("http://api:8000/alugueis/")
                if alugueis_response.status_code == 200:
                    alugueis = alugueis_response.json()
                    if alugueis:
                        df_alug = pd.DataFrame(alugueis)
                        df_alug = df_alug[df_alug["apto_id"] == apto_id]
                        df_alug = df_alug[df_alug["checkin"] > from_day.isoformat()]
                        if not df_alug.empty:
                            df_alug["valor_final"] = df_alug["valor_total"] - (
                                df_alug["valor_total"] * 0.15
                            )
                            df_alug = df_alug.sort_values(by=["checkin"])
                            df_alug = df_alug.drop(
                                [
                                    "apto_id",
                                    "ficha_id",
                                    "nome",
                                    "contato",
                                    "id",
                                    "criado_em",
                                    "modificado_em",
                                ],
                                axis=1,
                            )
                            alug_ord = [
                                "checkin",
                                "checkout",
                                "diarias",
                                "valor_diaria",
                                "valor_total",
                                "valor_final",
                            ]
                            bruto = df_alug["valor_total"].sum()
                            comissao = bruto * 0.15
                            liquido = df_alug["valor_final"].sum()
                            df_alug = showbr_dfdate(df_alug.reindex(alug_ord, axis=1))
                            df_alug.columns = [
                                "Check-In",
                                "Check-Out",
                                "Qtd. Dias",
                                "Por Dia",
                                "Bruto",
                                "Líquido",
                            ]
                            curr_columns = ["Por Dia", "Bruto", "Líquido"]
                            for col in curr_columns:
                                df_alug[col] = df_alug[col].apply(
                                    lambda x: locale.currency(x, grouping=True)
                                )
                            st.markdown("#### Aluguéis")
                            st.dataframe(
                                df_alug, hide_index=True, use_container_width=True
                            )
                            st.write(
                                f"Valor bruto dos alugueis: {locale.currency(bruto)}"
                            )
                            st.write(
                                f"Valor da comissao a 15%: {locale.currency(comissao)}"
                            )
                            st.write(
                                f"Valor líquido dos alugueis: {locale.currency(liquido)}"
                            )
                        else:
                            st.warning(
                                f"Não há alugueis para o {apto_id} desde {from_day}"
                            )
                            liquido = 0
                        entregar = liquido - despesas_tot
                        if entregar > 0:
                            st.markdown(
                                f":blue[Valor a entregar: {locale.currency(entregar)}]"
                            )
                        else:
                            st.markdown(
                                f":red[Atenção. Apartamento devendo: {locale.currency(entregar)}]"
                            )
                    else:
                        st.warning("Não há alugueis")
                else:
                    show_response_message(alugueis_response)

            if from_day and not (df_desp.empty or df_alug.empty):
                gen_relatorio = st.button("Gerar relatório", key=8003)
                if gen_relatorio:
                    file_name = f"relatorio_{apto_id}_{from_day}.pdf"
                    doc = SimpleDocTemplate(file_name, pagesize=A4)
                    elements = []

                    df_desp_to_table = [
                        df_desp.columns.to_list()
                    ] + df_desp.values.tolist()
                    df_alug_to_table = [
                        df_alug.columns.to_list()
                    ] + df_alug.values.tolist()

                    despesas_table = Table(df_desp_to_table)
                    alugueis_table = Table(df_alug_to_table)

                    style_despesas = TableStyle(
                        [
                            ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
                            ("TEXTCOLOR", (0, 0), (-1, 0), colors.black),
                            ("ALIGN", (0, 0), (-1, -1), "CENTER"),
                            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                            ("BOTTOMPADDING", (0, 0), (-1, 0), 12),
                            ("BACKGROUND", (0, 1), (-1, -1), colors.beige),
                            ("GRID", (0, 0), (-1, -1), 1, colors.black),
                            ("TEXTCOLOR", (0, 1), (-1, -1), colors.red),
                        ]
                    )

                    style_alugueis = TableStyle(
                        [
                            ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
                            ("TEXTCOLOR", (0, 0), (-1, 0), colors.black),
                            ("ALIGN", (0, 0), (-1, -1), "CENTER"),
                            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                            ("BOTTOMPADDING", (0, 0), (-1, 0), 12),
                            ("BACKGROUND", (0, 1), (-1, -1), colors.beige),
                            ("GRID", (0, 0), (-1, -1), 1, colors.black),
                            ("TEXTCOLOR", (0, 1), (-1, -1), colors.darkblue),
                        ]
                    )

                    f_despesas_tot = locale.currency(despesas_tot)
                    f_liquido = locale.currency(liquido)
                    f_entregar = locale.currency(entregar)
                    f_from_day = from_day.strftime("%d/%m/%Y")

                    despesas_table.setStyle(style_despesas)
                    alugueis_table.setStyle(style_alugueis)

                    elements.append(
                        Paragraph(
                            f"Apartamento <b><u>{apto_id}</u></b> a partir de <b><u>{f_from_day}</u></b>",
                            style=ParagraphStyle(
                                name="APTO", fontSize=18, alignment=TA_CENTER
                            ),
                        )
                    )
                    elements.append(Spacer(1, 24))
                    elements.append(
                        Paragraph(
                            "Despesas",
                            style=ParagraphStyle(
                                name="TITLE", fontSize=14, alignment=TA_LEFT
                            ),
                        )
                    )
                    elements.append(Spacer(1, 16))
                    elements.append(despesas_table)
                    elements.append(Spacer(1, 12))
                    elements.append(
                        Paragraph(
                            f"Total de despesas: {f_despesas_tot}",
                            style=ParagraphStyle(
                                name="DESPESAS", fontSize=12, textColor=colors.red
                            ),
                        )
                    )
                    elements.append(Spacer(1, 24))
                    elements.append(
                        Paragraph(
                            "Aluguéis",
                            style=ParagraphStyle(
                                name="TITLE", fontSize=14, alignment=TA_LEFT
                            ),
                        )
                    )
                    elements.append(Spacer(1, 16))
                    elements.append(alugueis_table)
                    elements.append(Spacer(1, 12))
                    elements.append(
                        Paragraph(
                            f"Total Líquido: {f_liquido}",
                            style=ParagraphStyle(
                                name="ALUGUEIS", fontSize=12, textColor=colors.darkblue
                            ),
                        )
                    )
                    elements.append(Spacer(1, 12))
                    if entregar > 0:
                        elements.append(
                            Paragraph(
                                f"Valor a receber: {f_liquido}<font color='red'> - {f_despesas_tot}</font> = {f_entregar}",
                                style=ParagraphStyle(
                                    name="TOTAL_POS",
                                    fontSize=14,
                                    textColor=colors.darkblue,
                                ),
                            )
                        )
                    else:
                        elements.append(
                            Paragraph(
                                f"Valor está negativo: {f_liquido}<font color='red'> - {f_despesas_tot} = {f_entregar}</font>",
                                style=ParagraphStyle(
                                    name="TOTAL_NEG",
                                    fontSize=14,
                                    textColor=colors.darkblue,
                                ),
                            )
                        )
                    elements.append(Spacer(1, 24))
                    elements.append(
                        Paragraph(
                            f"Data de emissão: {date.today().strftime('%d/%m/%Y')}"
                        )
                    )

                    doc.build(elements)
                    with open(f"./{file_name}", "rb") as f:
                        st.download_button(
                            label="Download PDF",
                            data=f,
                            file_name=file_name,
                            mime="application/pdf",
                            key=8004,
                        )
                    os.remove(f"./{file_name}")

                    rel_reg = {
                        "apto_id": apto_id,
                        "data": date.today().isoformat(),
                        "valor": entregar,
                    }

                    post_rel_response = requests.post(
                        "http://api:8000/relatorios/", json=rel_reg
                    )
                    show_response_message(post_rel_response)
                    if post_rel_response.status_code == 200:
                        st.markdown("####Dados do relatório registrados com sucesso:")
                    else:
                        st.markdown("####NÃO foi possível registrar:")
                    show_data_output(rel_reg)
        else:
            st.error(f"Apartamento {apto_id} não encontrado em nossos registros")
            show_response_message(apto_response)

with tab2:
    st.subheader("Editar Relatório")
    if apto_id:
        if apto_response.status_code == 200:
            st.markdown("#### Despesas")
            try:
                if not df_desp.empty:
                    df_desp_edit = df_desp.copy()
                    df_desp_edit["Valor"] = df_desp_edit["Valor"].apply(
                        lambda x: float(
                            x.replace("R$", "")
                            .replace(".", "")
                            .strip()
                            .replace(",", ".")
                        )
                    )
                    edited_df_desp = st.data_editor(
                        df_desp_edit, hide_index=True, use_container_width=True
                    )
                    edited_despesas_tot = edited_df_desp["Valor"].sum()
                    st.markdown(
                        f":red[Valor das Despesas: {locale.currency(edited_despesas_tot)}]"
                    )
            except:
                st.warning("Nada para editar")

            st.markdown("#### Aluguéis")
            try:
                if not df_alug.empty:
                    df_alug_edit = df_alug.copy()
                    for col in curr_columns:
                        df_alug_edit[col] = df_alug_edit[col].apply(
                            lambda x: float(
                                x.replace("R$", "")
                                .replace(".", "")
                                .strip()
                                .replace(",", ".")
                            )
                        )
                    edited_df_alug = st.data_editor(
                        df_alug_edit, hide_index=True, use_container_width=True
                    )
                    edited_bruto = edited_df_alug["Bruto"].sum()
                    edited_comissao = edited_bruto * 0.15
                    edited_liquido = edited_df_alug["Líquido"].sum()
                    nova_taxa = 1 - (edited_liquido / edited_bruto)
                    st.write(
                        f"Valor bruto dos alugueis: {locale.currency(edited_bruto)}"
                    )
                    st.write(
                        f"Valor da comissao a 15%: {locale.currency(edited_comissao)}"
                    )
                    st.write(
                        f"Valor líquido dos alugueis: {locale.currency(edited_liquido)}"
                    )
                    edited_entregar = edited_liquido - edited_despesas_tot
                    st.markdown(
                        f":blue[Valor a entregar: {locale.currency(edited_entregar)}]"
                    )
                    if round(nova_taxa, 3) != 0.150:
                        st.warning(
                            f"Atenção: Os valores alterados indicam que a taxa de comissão é de {nova_taxa * 100}%. E o valor da comissão com esta alteração é {locale.currency(edited_bruto * nova_taxa)}"
                        )
            except:
                st.warning("Nada para editar")
            try:
                if from_day and not (edited_df_desp.empty or edited_df_alug.empty):
                    gen_edit_relatorio = st.button("Gerar relatório", key=8200)
                    if gen_edit_relatorio:
                        file_name = f"relatorio_{apto_id}_{from_day}.pdf"
                        doc = SimpleDocTemplate(file_name, pagesize=A4)
                        elements = []

                        edited_df_desp_to_table = [
                            edited_df_desp.columns.to_list()
                        ] + edited_df_desp.values.tolist()
                        edited_df_alug_to_table = [
                            edited_df_alug.columns.to_list()
                        ] + edited_df_alug.values.tolist()

                        edited_despesas_table = Table(edited_df_desp_to_table)
                        edited_alugueis_table = Table(edited_df_alug_to_table)

                        style_despesas = TableStyle(
                            [
                                ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
                                ("TEXTCOLOR", (0, 0), (-1, 0), colors.black),
                                ("ALIGN", (0, 0), (-1, -1), "CENTER"),
                                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                                ("BOTTOMPADDING", (0, 0), (-1, 0), 12),
                                ("BACKGROUND", (0, 1), (-1, -1), colors.beige),
                                ("GRID", (0, 0), (-1, -1), 1, colors.black),
                                ("TEXTCOLOR", (0, 1), (-1, -1), colors.red),
                            ]
                        )

                        style_alugueis = TableStyle(
                            [
                                ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
                                ("TEXTCOLOR", (0, 0), (-1, 0), colors.black),
                                ("ALIGN", (0, 0), (-1, -1), "CENTER"),
                                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                                ("BOTTOMPADDING", (0, 0), (-1, 0), 12),
                                ("BACKGROUND", (0, 1), (-1, -1), colors.beige),
                                ("GRID", (0, 0), (-1, -1), 1, colors.black),
                                ("TEXTCOLOR", (0, 1), (-1, -1), colors.darkblue),
                            ]
                        )

                        f_edited_despesas_tot = locale.currency(edited_despesas_tot)
                        f_edited_liquido = locale.currency(edited_liquido)
                        f_edited_entregar = locale.currency(edited_entregar)
                        f_from_day = from_day.strftime("%d/%m/%Y")

                        edited_despesas_table.setStyle(style_despesas)
                        edited_alugueis_table.setStyle(style_alugueis)

                        elements.append(
                            Paragraph(
                                f"Apartamento <b><u>{apto_id}</u></b> a partir de <b><u>{f_from_day}</u></b>",
                                style=ParagraphStyle(
                                    name="APTO", fontSize=18, alignment=TA_CENTER
                                ),
                            )
                        )
                        elements.append(Spacer(1, 24))
                        elements.append(
                            Paragraph(
                                "Despesas",
                                style=ParagraphStyle(
                                    name="TITLE", fontSize=14, alignment=TA_LEFT
                                ),
                            )
                        )
                        elements.append(Spacer(1, 16))
                        elements.append(edited_despesas_table)
                        elements.append(Spacer(1, 12))
                        elements.append(
                            Paragraph(
                                f"Total de despesas: {f_edited_despesas_tot}",
                                style=ParagraphStyle(
                                    name="DESPESAS", fontSize=12, textColor=colors.red
                                ),
                            )
                        )
                        elements.append(Spacer(1, 24))
                        elements.append(
                            Paragraph(
                                "Aluguéis",
                                style=ParagraphStyle(
                                    name="TITLE", fontSize=14, alignment=TA_LEFT
                                ),
                            )
                        )
                        elements.append(Spacer(1, 16))
                        elements.append(edited_alugueis_table)
                        elements.append(Spacer(1, 12))
                        elements.append(
                            Paragraph(
                                f"Total Líquido: {f_edited_liquido}",
                                style=ParagraphStyle(
                                    name="ALUGUEIS",
                                    fontSize=12,
                                    textColor=colors.darkblue,
                                ),
                            )
                        )
                        elements.append(Spacer(1, 12))
                        elements.append(
                            Paragraph(
                                f"Valor a receber: {f_edited_liquido} - <font color='red'>{f_edited_despesas_tot}</font> = {f_edited_entregar}",
                                style=ParagraphStyle(
                                    name="TOTAL", fontSize=14, textColor=colors.darkblue
                                ),
                            )
                        )
                        elements.append(Spacer(1, 24))
                        elements.append(
                            Paragraph(
                                f"Data de emissão: {date.today().strftime('%d/%m/%Y')}"
                            )
                        )

                        doc.build(elements)
                        with open(f"./{file_name}", "rb") as f:
                            st.download_button(
                                label="Download PDF",
                                data=f,
                                file_name=file_name,
                                mime="application/pdf",
                                key=8201,
                            )
                        os.remove(f"./{file_name}")

                        rel_reg = {
                            "apto_id": apto_id,
                            "data": date.today().isoformat(),
                            "valor": edited_entregar,
                        }

                        post_rel_response = requests.post(
                            "http://api:8000/relatorios/", json=rel_reg
                        )
                        show_response_message(post_rel_response)
                        if post_rel_response.status_code == 200:
                            st.markdown(
                                "####Dados do relatório registrados com sucesso:"
                            )
                        else:
                            st.markdown("####NÃO foi possível registrar:")
                        show_data_output(rel_reg)
            except:
                None
        else:
            st.error(f"Apartamento {apto_id} não encontrado em nossos registros")
            show_response_message(apto_response)
    else:
        st.markdown(
            "Volte para a aba de **Registrar** antes de editar um **Relatório**"
        )
