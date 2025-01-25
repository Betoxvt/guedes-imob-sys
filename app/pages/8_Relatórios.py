from datetime import date
import pandas as pd
import requests
import streamlit as st

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
        "descrição": "A/C",
    },
    {
        "apto_id": "A-111",
        "data_pagamento": "2024-01-20",
        "valor": 150,
        "categoria": "OUTROS",
        "descrição": "Dedetização",
    },
    {
        "apto_id": "A-111",
        "data_pagamento": "2025-01-30",
        "valor": 600,
        "categoria": "INTERNET",
        "descrição": "Anual",
    },
    {
        "apto_id": "B-222",
        "data_pagamento": "2025-01-30",
        "valor": 600,
        "categoria": "INTERNET",
        "descrição": "Anual",
    },
]
pagamentos = [
    {"tipo": "Saída", "valor": 4000, "apto_id": "A-111", "data": "202-01-30"},
    {"tipo": "Saída", "valor": 8800, "apto_id": "A-111", "data": "2024-12-01"},
    {"tipo": "Saída", "valor": 6000, "apto_id": "A-111", "data": "2024-01-30"},
    {"tipo": "Saída", "valor": 6000, "apto_id": "B-222", "data": "2024-01-30"},
]
comissao = 0.15

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
df_desp = df_desp.sort_values(by=["categoria", "data_pagamento"])
# print(df_desp)
desp_total = df_desp["valor"].sum()
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
# print(df_alug)
alug_total = df_alug["valor_final"].sum()
# print(alug_total)


# Finalmente mostrar o valor total a ser entregue, subtraindo o total das despesas e mostrando o resultado final
entregar = alug_total - desp_total
print(entregar)

# Mostrar a data em que foi gerado o relatório
print(date.today())
