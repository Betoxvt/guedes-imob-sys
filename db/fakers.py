from datetime import date, timedelta
from faker import Faker
import locale
from modelscopy import (
    Aluguel,
    Apartamento,
    Despesa,
    Garagem,
    Pagamento,
    Proprietario,
    Relatorio,
)
import os
from pydantic import EmailStr
import random
from schemascopy import (
    AluguelBase,
    ApartamentoBase,
    DespesaBase,
    DespesaCat,
    GaragemBase,
    PagamentoBase,
    PagamentoCat,
    ProprietarioBase,
    RelatorioBase,
)
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from typing import Optional
from time import sleep


def gen_proprietario():
    data = {}
    for field, type in ProprietarioBase.__annotations__.items():
        if type == str:
            data[field] = fake.name() if field == "nome" else fake.text(max_nb_chars=20)
        elif type == Optional[str]:
            data[field] = fake.cpf() if field == "cpf" else fake.phone_number()
        elif type == Optional[EmailStr]:
            data[field] = fake.email()
    return data


def gen_apartamento():
    global proprietario_id
    data = {}
    for field, type in ApartamentoBase.__annotations__.items():
        if type == str and field == "id":
            while True:
                letter = str(random.choice(["A", "B", "C", "D"]))
                num1 = str(random.choice(["0", "1", "2"]))
                num2 = str(random.randint(0, 9))
                num3 = str(random.choice(["0", "1", "2"]))
                id = str(f"{letter}-{num1}{num2}{num3}")
                if id not in generated_apto_ids:
                    generated_apto_ids.append(id)
                    data[field] = str(id)
                    break
        elif type == Optional[int] and field == "proprietario_id":
            data[field] = proprietario_id
            proprietario_id += 1
            if proprietario_id > entries:
                proprietario_id = 1
        elif type == Optional[str]:
            data[field] = str(fake.random_number(digits=9, fix_len=True))
    return data


def gen_aluguel():
    data = {}
    for field, type in AluguelBase.__annotations__.items():
        if field == "apto_id":
            data[field] = random.choice(generated_apto_ids)
        elif field == "ficha_id":
            data[field] = None
        elif field == "checkin":
            data[field] = (
                fake.date_between(start_date=date.today(), end_date=date(2026, 4, 30))
            ).isoformat()
        elif field == "checkout":
            data[field] = (
                date.fromisoformat(data["checkin"])
                + timedelta(days=random.randint(4, 10))
            ).isoformat()
        elif field == "diarias":
            data[field] = (
                date.fromisoformat(data["checkout"])
                - date.fromisoformat(data["checkin"])
            ).days
        elif type == float:
            data[field] = (
                random.randint(100, 200)
                if field == "valor_diaria"
                else (data["diarias"] * data["valor_diaria"])
            )
        elif type == str:
            data[field] = fake.name() if field == "nome" else fake.cellphone_number()
    return data


def gen_despesa():
    data = {}
    for field in DespesaBase.__annotations__.keys():
        if field == "apto_id":
            data[field] = random.choice(generated_apto_ids)
        elif field == "data":
            data[field] = fake.date_between(
                start_date=date.today(), end_date=date(2026, 4, 30)
            ).isoformat()
        elif field == "valor":
            data[field] = random.randint(100, 200)
        elif field == "categoria":
            data[field] = random.choice([x.value for x in DespesaCat])
        else:
            data[field] = fake.text(max_nb_chars=100)
    return data


def gen_garagem():
    data = {}
    for field, type in GaragemBase.__annotations__.items():
        if field == "apto_id_origem":
            data[field] = random.choice(generated_apto_ids)
        elif field == "apto_id_destino":
            value = data["apto_id_origem"]
            while value == data["apto_id_origem"]:
                value = random.choice(generated_apto_ids)
            data[field] = value
        elif field == "checkin":
            data[field] = (
                fake.date_between(start_date=date.today(), end_date=date(2026, 4, 30))
            ).isoformat()
        elif field == "checkout":
            data[field] = (
                date.fromisoformat(data["checkin"])
                + timedelta(days=random.randint(4, 10))
            ).isoformat()
        elif field == "diarias":
            data[field] = (
                date.fromisoformat(data["checkout"])
                - date.fromisoformat(data["checkin"])
            ).days
        elif type == Optional[float]:
            data[field] = (
                random.randint(50, 80)
                if field == "valor_diaria"
                else (data["diarias"] * data["valor_diaria"])
            )
    return data


def gen_pagamento():
    data = {}
    global aluguel_id
    for field, value in PagamentoBase.__annotations__.items():
        if value == str:
            data[field] = random.choice([x.value for x in PagamentoCat])
        elif value == float:
            data[field] = random.randint(100, 200)
        elif value == int:
            data[field] = aluguel_id
            aluguel_id += 1
            if aluguel_id > entries:
                aluguel_id = 1
        elif field == "notas":
            data[field] = fake.text(max_nb_chars=60)
        elif field == "nome":
            data[field] = fake.name()
        elif field == "contato":
            data[field] = fake.cellphone_number()
        elif value == date:
            data[field] = fake.date_between(
                start_date=date(2024, 11, 20), end_date=date(2025, 10, 20)
            ).isoformat()
    return data


def gen_relatorio():
    data = {}
    for field in RelatorioBase.__annotations__.keys():
        if field == "apto_id":
            data[field] = random.choice(generated_apto_ids)
        elif field == "data":
            data[field] = fake.date_between(
                start_date=date(2024, 1, 1), end_date=date.today()
            ).isoformat()
        else:
            data[field] = random.randint(1000, 2000)
    return data


def insert_data(data_generator, Table):
    data = data_generator
    Session = sessionmaker(bind=engine)
    session = Session()
    try:
        new_registry = Table(**data)
        session.add(new_registry)
        session.commit()
        print("sucesso:", data)
    except Exception as e:
        print(e)
        session.rollback()
    finally:
        session.close()
        sleep(0.1)


if __name__ == "__main__":
    locale.setlocale(locale.LC_ALL, "pt_BR.UTF-8")
    fake = Faker("pt_BR")

    entries = 25
    generated_apto_ids = list()
    proprietario_id = 1
    aluguel_id = 1

    POSTGRES_USER = os.environ.get("POSTGRES_USER")
    POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD")
    POSTGRES_DB = os.environ.get("POSTGRES_DB")
    DB_PATH = f"postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@127.0.0.1:5432/{POSTGRES_DB}"
    engine = create_engine(DB_PATH)

    for _ in range(entries):
        insert_data(gen_proprietario(), Proprietario)

    for _ in range(entries):
        insert_data(gen_apartamento(), Apartamento)

    for _ in range(entries * 2):
        insert_data(gen_aluguel(), Aluguel)

    for _ in range(entries):
        insert_data(gen_despesa(), Despesa)

    for _ in range(entries):
        insert_data(gen_garagem(), Garagem)

    for _ in range(entries * 2):
        insert_data(gen_pagamento(), Pagamento)

    for _ in range(entries):
        insert_data(gen_relatorio(), Relatorio)
