from datetime import datetime
from datetime import date
import locale
import os
from reportlab.lib.enums import TA_LEFT, TA_RIGHT, TA_CENTER, TA_JUSTIFY
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph, SimpleDocTemplate, Table, TableStyle, Spacer
from reportlab.lib import colors
from reportlab.lib.styles import (
    ParagraphStyle,
)
import pandas as pd
import requests
import streamlit as st

# from utils.mydate import showbr_dfdate


def showbr_dfdate(df: pd.DataFrame) -> pd.DataFrame:
    """Converts specific DataFrame columns containing datetime.date objects to
    Brazilian date format (DD/MM/YYYY).

    Args:
        df: The input DataFrame.

    Returns:
        A new DataFrame with converted date columns, or the original DataFrame
        if no conversions were possible. Only columns specified for this project are converted.
        Returns None if input is not a DataFrame.
    """
    if not isinstance(df, pd.DataFrame):
        st.warning("Input must be a Pandas DataFrame.")
        return None
    df_new = df.copy()
    date_columns = [
        "checkin",
        "checkout",
        "criado_em",
        "modificado_em",
        "data_pagamento",
    ]
    for col in df_new.columns:
        if col in date_columns:
            try:
                if isinstance(df_new[col].iloc[0], date):
                    df_new[col] = df_new[col].apply(
                        lambda x: x.strftime("%d/%m/%Y") if isinstance(x, date) else x
                    )
                else:
                    df_new[col] = pd.to_datetime(
                        df_new[col], errors="coerce"
                    ).dt.strftime("%d/%m/%Y")
            except (ValueError, TypeError) as e:
                st.warning(
                    f"Warning: Column '{col}' could not be converted to date: {e}"
                )
                pass
    return df_new


# st.title("Relatórios")

apto = {"id": "A-111", "proprietario_id": 1}
alugueis = [
    {
        "apto_id": "B-222",
        "valor_total": 8800,
        "checkin": "2025-10-20",
        "checkout": "2025-10-31",
        "diarias": 11,
        "valor_diaria": 800,
    },
    {
        "apto_id": "A-111",
        "valor_total": 8800,
        "checkin": "2024-10-20",
        "checkout": "2024-10-31",
        "diarias": 11,
        "valor_diaria": 800,
    },
    {
        "apto_id": "A-111",
        "valor_total": 8000,
        "checkin": "2025-01-20",
        "checkout": "2025-01-30",
        "diarias": 10,
        "valor_diaria": 800,
    },
    {
        "apto_id": "A-111",
        "valor_total": 8000,
        "checkin": "2025-01-20",
        "checkout": "2025-01-30",
        "diarias": 10,
        "valor_diaria": 800,
    },
    {
        "apto_id": "A-111",
        "valor_total": 8000,
        "checkin": "2025-01-20",
        "checkout": "2025-01-30",
        "diarias": 10,
        "valor_diaria": 800,
    },
    {
        "apto_id": "A-111",
        "valor_total": 8000,
        "checkin": "2025-01-20",
        "checkout": "2025-01-30",
        "diarias": 10,
        "valor_diaria": 800,
    },
    {
        "apto_id": "A-111",
        "valor_total": 8000,
        "checkin": "2025-01-20",
        "checkout": "2025-01-30",
        "diarias": 10,
        "valor_diaria": 800,
    },
    {
        "apto_id": "A-111",
        "valor_total": 8000,
        "checkin": "2025-01-20",
        "checkout": "2025-01-30",
        "diarias": 10,
        "valor_diaria": 800,
    },
    {
        "apto_id": "A-111",
        "valor_total": 8000,
        "checkin": "2025-01-20",
        "checkout": "2025-01-30",
        "diarias": 10,
        "valor_diaria": 800,
    },
    {
        "apto_id": "A-111",
        "valor_total": 8000,
        "checkin": "2025-01-20",
        "checkout": "2025-01-30",
        "diarias": 10,
        "valor_diaria": 800,
    },
    {
        "apto_id": "A-111",
        "valor_total": 5600,
        "checkin": "2025-01-13",
        "checkout": "2025-01-20",
        "diarias": 10,
        "valor_diaria": 800,
    },
]
despesas = [
    {
        "apto_id": "A-111",
        "data_pagamento": "2025-01-10",
        "valor": 350,
        "categoria": "MANUTENÇÃO",
        "descricao": "Referoma geral, blablabla, mais isso e aquilo",
    },
    {
        "apto_id": "A-111",
        "data_pagamento": "2025-01-10",
        "valor": 350,
        "categoria": "MANUTENÇÃO",
        "descricao": "Referoma geral, blablabla, mais isso e aquilo",
    },
    {
        "apto_id": "A-111",
        "data_pagamento": "2025-01-10",
        "valor": 350,
        "categoria": "MANUTENÇÃO",
        "descricao": "Referoma geral, blablabla, mais isso e aquilo",
    },
    {
        "apto_id": "A-111",
        "data_pagamento": "2025-01-10",
        "valor": 350,
        "categoria": "MANUTENÇÃO",
        "descricao": "Referoma geral, blablabla, mais isso e aquilo",
    },
    {
        "apto_id": "A-111",
        "data_pagamento": "2025-01-10",
        "valor": 350,
        "categoria": "MANUTENÇÃO",
        "descricao": "Referoma geral, blablabla, mais isso e aquilo",
    },
    {
        "apto_id": "A-111",
        "data_pagamento": "2025-01-10",
        "valor": 350,
        "categoria": "MANUTENÇÃO",
        "descricao": "Referoma geral, blablabla, mais isso e aquilo",
    },
    {
        "apto_id": "A-111",
        "data_pagamento": "2025-01-10",
        "valor": 350,
        "categoria": "MANUTENÇÃO",
        "descricao": "Referoma geral, blablabla, mais isso e aquilo",
    },
    {
        "apto_id": "A-111",
        "data_pagamento": "2025-01-10",
        "valor": 350,
        "categoria": "MANUTENÇÃO",
        "descricao": "Referoma geral, blablabla, mais isso e aquilo",
    },
    {
        "apto_id": "A-111",
        "data_pagamento": "2025-01-10",
        "valor": 350,
        "categoria": "MANUTENÇÃO",
        "descricao": "Referoma geral, blablabla, mais isso e aquilo",
    },
    {
        "apto_id": "A-111",
        "data_pagamento": "2025-01-10",
        "valor": 350,
        "categoria": "MANUTENÇÃO",
        "descricao": "Referoma geral, blablabla, mais isso e aquilo",
    },
    {
        "apto_id": "A-111",
        "data_pagamento": "2025-01-10",
        "valor": 350,
        "categoria": "MANUTENÇÃO",
        "descricao": "Referoma geral, blablabla, mais isso e aquilo",
    },
    {
        "apto_id": "A-111",
        "data_pagamento": "2024-01-20",
        "valor": 150,
        "categoria": "OUTROS",
        "descricao": "Dedetização",
    },
    {
        "apto_id": "A-111",
        "data_pagamento": "2025-01-30",
        "valor": 600,
        "categoria": "INTERNET",
        "descricao": "Anual",
    },
    {
        "apto_id": "B-222",
        "data_pagamento": "2025-01-30",
        "valor": 600,
        "categoria": "INTERNET",
        "descricao": "Anual",
    },
]
pagamentos = [
    {"tipo": "Saída", "valor": 4000, "apto_id": "A-111", "data": "202-01-30"},
    {"tipo": "Saída", "valor": 8800, "apto_id": "A-111", "data": "2024-12-01"},
    {"tipo": "Saída", "valor": 6000, "apto_id": "A-111", "data": "2024-01-30"},
    {"tipo": "Saída", "valor": 6000, "apto_id": "B-222", "data": "2024-01-30"},
]
comissao = 0.15
locale.setlocale(locale.LC_ALL, "pt_BR.UTF-8")

# Definir o apartamento e a data inicial do relatório ou pegar automático de acordo com o último pagamento tipo Saída registrado ao apartamento
apto = apto["id"]
from_day = "2025-01-01"
df_pag = pd.DataFrame(pagamentos)
# print(df_pag)
df_pag = df_pag[df_pag["apto_id"] == apto]
# print(df_pag)
df_pag = df_pag.sort_values(by="data", ascending=False)
# print(df_pag)
last_pag = df_pag.iloc[0]
# print(last_pag)
from_day = last_pag.loc["data"]
# print(from_day)

# Listar os gastos de acordo com sua categoria, tipo uma tabela, as linhas são as datas, as colunas são descrição e valor
# Mostrar o total das despesas
df_desp = pd.DataFrame(despesas)
# print(df_desp)
df_desp = df_desp[df_desp["apto_id"] == apto]
# print(df_desp)
df_desp = df_desp[df_desp["data_pagamento"] > from_day]
# print(df_desp)
df_desp = df_desp.sort_values(by=["data_pagamento"])
df_desp = df_desp.drop("apto_id", axis=1)
desp_ord = ["data_pagamento", "categoria", "descricao", "valor"]
despesas = df_desp["valor"].sum()
df_desp = showbr_dfdate(df_desp.reindex(desp_ord, axis=1))
df_desp["valor"] = df_desp["valor"].apply(lambda x: locale.currency(x, grouping=True))
# print(df_desp)
# print(desp_total)

# listar os alugueis checkin - checkout - diarias - valor_diaria - valor_total - (valor_total-comissao)
# Abaixo mostrar o valor total dos alugueis já descontando a comissão
df_alug = pd.DataFrame(alugueis)
# print(df_alug)
df_alug = df_alug[df_alug["apto_id"] == apto]
# print(df_alug)
df_alug = df_alug[df_alug["checkin"] > from_day]
# print(df_alug)
df_alug["valor_final"] = df_alug["valor_total"] - (df_alug["valor_total"] * 0.15)
df_alug = df_alug.sort_values(by=["checkin"])
df_alug = df_alug.drop("apto_id", axis=1)
alug_ord = [
    "checkin",
    "checkout",
    "diarias",
    "valor_diaria",
    "valor_total",
    "valor_final",
]
liquido = df_alug["valor_final"].sum()
df_alug = showbr_dfdate(df_alug.reindex(alug_ord, axis=1))
curr_columns = ["valor_diaria", "valor_total", "valor_final"]
for col in curr_columns:
    df_alug[col] = df_alug[col].apply(lambda x: locale.currency(x, grouping=True))
# print(df_alug)
# print(alug_total)


# Finalmente mostrar o valor total a ser entregue, subtraindo o total das despesas e mostrando o resultado final
# print(entregar)
entregar = liquido - despesas

# Mostrar a data em que foi gerado o relatório
# print(date.today())

# Editar os campos do relatório

# Gerar o pdf do relatório
doc = SimpleDocTemplate("relatorio.pdf", pagesize=A4)
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
        "Despesas", style=ParagraphStyle(name="TITLE", fontSize=14, alignment=TA_LEFT)
    )
)
elements.append(Spacer(1, 16))
elements.append(despesas_table)
elements.append(Spacer(1, 12))
elements.append(
    Paragraph(
        f"Total de despesas: {despesas}",
        style=ParagraphStyle(name="DESPESAS", fontSize=12, textColor=colors.red),
    )
)
elements.append(Spacer(1, 24))
elements.append(
    Paragraph(
        "Aluguéis", style=ParagraphStyle(name="TITLE", fontSize=14, alignment=TA_LEFT)
    )
)
elements.append(Spacer(1, 16))
elements.append(alugueis_table)
elements.append(Spacer(1, 12))
elements.append(
    Paragraph(
        f"Total Líquido: {liquido}",
        style=ParagraphStyle(name="ALUGUEIS", fontSize=12, textColor=colors.darkblue),
    )
)
elements.append(Spacer(1, 12))
elements.append(
    Paragraph(
        f"Valor a receber: {liquido} - <font color='red'>{despesas}</font> = {entregar}",
        style=ParagraphStyle(name="TOTAL", fontSize=14, textColor=colors.darkblue),
    )
)
elements.append(Spacer(1, 24))
elements.append(Paragraph(f"Data de emissão: {date.today().strftime('%d/%m/%Y')}"))

doc.build(elements)
