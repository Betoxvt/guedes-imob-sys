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
from utils.myfunc import show_response_message
from utils.mystr import apto_input

st.title("Relatórios")
comissao = 0.15
locale.setlocale(locale.LC_ALL, "pt_BR.UTF-8")
st.header("Gerar Relatório")
st.markdown(
    '<p style="font-size: 12px;">Campos com * são obrigatórios</p>',
    unsafe_allow_html=True,
)
apto: str = apto_input(st.text_input(label="Apartamento *", key=8000, value=None))
if apto:

    pagamentos_response = requests.get("http://api:8000/pagamentos/")
    if pagamentos_response.status_code == 200:
        pagamentos = pagamentos_response.json()
        if pagamentos:
            df_pag = pd.DataFrame(pagamentos)
            df_pag = df_pag[df_pag["apto_id"] == apto]
            df_pag = df_pag[df_pag["tipo"] == "Saída"]
            df_pag = df_pag.sort_values(by="data", ascending=False)
            last_pag = df_pag.iloc[0]
            from_day = last_pag.loc["data"]
            pago = last_pag.loc["valor"]
            st.write(
                f"Última entrega de valores foi em {datetime.strptime(from_day, "%Y-%m-%d").strftime("%d/%m/%Y")}, um total de {locale.currency(pago)}"
            )
            from_day = st.date_input(label="Data de início *", key=8001, value=from_day)
        else:
            st.write("Não foi encontrada a data do último pagamento")
            st.write("Insira a data de início do relatório")
            from_day = st.date_input(label="Data de início *", key=8002, value=None)
    else:
        show_response_message(pagamentos_response)

    despesas_response = requests.get("http://api:8000/despesas/")
    if despesas_response.status_code == 200:
        despesas = despesas_response.json()
        if despesas:
            df_desp = pd.DataFrame(despesas)
            df_desp = df_desp[df_desp["apto_id"] == apto]
            df_desp = df_desp[df_desp["data"] > from_day]
            df_desp = df_desp.sort_values(by=["data"])
            df_desp = df_desp.drop(
                ["apto_id", "id", "criado_em", "modificado_em"], axis=1
            )
            desp_ord = ["data", "categoria", "descricao", "valor"]
            despesas = df_desp["valor"].sum()
            df_desp = showbr_dfdate(df_desp.reindex(desp_ord, axis=1))
            df_desp["valor"] = df_desp["valor"].apply(
                lambda x: locale.currency(x, grouping=True)
            )
            st.subheader("Despesas")
            st.dataframe(df_desp, hide_index=True)
            st.write(f"Valor das Despesas: {locale.currency(despesas)}")
        else:
            st.warning("Não há despesas")
    else:
        show_response_message(despesas_response)

    alugueis_response = requests.get("http://api:8000/alugueis/")
    if alugueis_response.status_code == 200:
        alugueis = alugueis_response.json()
        if alugueis:
            df_alug = pd.DataFrame(alugueis)
            df_alug = df_alug[df_alug["apto_id"] == apto]
            df_alug = df_alug[df_alug["checkin"] > from_day]
            df_alug["valor_final"] = df_alug["valor_total"] - (
                df_alug["valor_total"] * 0.15
            )
            df_alug = df_alug.sort_values(by=["checkin"])
            df_alug = df_alug.drop(
                [
                    "apto_id",
                    "ficha",
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
            curr_columns = ["valor_diaria", "valor_total", "valor_final"]
            for col in curr_columns:
                df_alug[col] = df_alug[col].apply(
                    lambda x: locale.currency(x, grouping=True)
                )
            st.subheader("Aluguéis")
            st.dataframe(df_alug, hide_index=True)
            st.write(f"Valor bruto dos alugueis: {locale.currency(bruto)}")
            st.write(f"Valor da comissao: {locale.currency(comissao)}")
            st.write(f"Valor líquido dos alugueis: {locale.currency(liquido)}")
            entregar = liquido - despesas
            st.write(f"Valor a entregar: {locale.currency(entregar)}")
        else:
            st.warning("Não há alugueis")
    else:
        show_response_message(pagamentos_response)

    # Editar os campos do relatório

    if from_day and (despesas or pagamentos):
        gerar_relatorio = st.button("Gerar relatório", key=8003)
        if gerar_relatorio:
            file_name = f"{apto}_{from_day}.pdf"
            doc = SimpleDocTemplate(file_name, pagesize=A4)
            elements = []
            despesas_columns = ["Data", "Categoria", "Descrição", "Valor"]
            alugueis_columns = [
                "Check-In",
                "Check-Out",
                "Qtd. Dias",
                "R$ / Dia",
                "Bruto",
                "Líquido",
            ]
            df_desp_to_table = [despesas_columns] + df_desp.values.tolist()
            df_alug_to_table = [alugueis_columns] + df_alug.values.tolist()

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

            despesas = locale.currency(despesas)
            liquido = locale.currency(liquido)
            entregar = locale.currency(entregar)
            from_day = datetime.strptime(from_day, "%Y-%m-%d")
            from_day = from_day.strftime("%d/%m/%Y")

            despesas_table.setStyle(style_despesas)
            alugueis_table.setStyle(style_alugueis)

            elements.append(
                Paragraph(
                    f"Apartamento {apto} a partir de {from_day}",
                    style=ParagraphStyle(name="APTO", fontSize=14, alignment=TA_CENTER),
                )
            )
            elements.append(Spacer(1, 24))
            elements.append(
                Paragraph(
                    "Despesas",
                    style=ParagraphStyle(name="TITLE", fontSize=14, alignment=TA_LEFT),
                )
            )
            elements.append(Spacer(1, 16))
            elements.append(despesas_table)
            elements.append(Spacer(1, 12))
            elements.append(
                Paragraph(
                    f"Total de despesas: {despesas}",
                    style=ParagraphStyle(
                        name="DESPESAS", fontSize=12, textColor=colors.red
                    ),
                )
            )
            elements.append(Spacer(1, 24))
            elements.append(
                Paragraph(
                    "Aluguéis",
                    style=ParagraphStyle(name="TITLE", fontSize=14, alignment=TA_LEFT),
                )
            )
            elements.append(Spacer(1, 16))
            elements.append(alugueis_table)
            elements.append(Spacer(1, 12))
            elements.append(
                Paragraph(
                    f"Total Líquido: {liquido}",
                    style=ParagraphStyle(
                        name="ALUGUEIS", fontSize=12, textColor=colors.darkblue
                    ),
                )
            )
            elements.append(Spacer(1, 12))
            elements.append(
                Paragraph(
                    f"Valor a receber: {liquido} - <font color='red'>{despesas}</font> = {entregar}",
                    style=ParagraphStyle(
                        name="TOTAL", fontSize=14, textColor=colors.darkblue
                    ),
                )
            )
            elements.append(Spacer(1, 24))
            elements.append(
                Paragraph(f"Data de emissão: {date.today().strftime('%d/%m/%Y')}")
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
