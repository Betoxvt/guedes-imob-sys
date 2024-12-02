from sqlmodel import Field, SQLModel, create_engine, Relationship
from typing import Optional, List

# Tabela apartamentos
class Apartamento(SQLModel, table=True):
    __tablename__ = "apartamentos"
    apartamento: str = Field(primary_key=True)  # Primary Key
    edificio: str
    endereco: str
    celesc: Optional[int]
    supergasbras: Optional[int]
    internet: Optional[str]
    wifiid: Optional[str]
    wifipass: Optional[str]
    lockpass: Optional[int]
    proprietario: Optional[int] = Field(foreign_key="proprietarios.cpf")  # Foreign Key


# Tabela proprietarios
class Proprietario(SQLModel, table=True):
    __tablename__ = "proprietarios"
    cpf: int = Field(primary_key=True)  # Primary Key
    nome: str
    telefone: Optional[int]
    email: Optional[str]
    apto1: str = Field(foreign_key="apartamentos.apartamento")
    apto2: Optional[str] = Field(foreign_key="apartamentos.apartamento")
    apto3: Optional[str] = Field(foreign_key="apartamentos.apartamento")
    apto4: Optional[str] = Field(foreign_key="apartamentos.apartamento")


# Tabela despesas_fixas
class DespesaFixa(SQLModel, table=True):
    __tablename__ = "despesas_fixas"
    id: Optional[int] = Field(default=None, primary_key=True)  # Primary Key
    data_pagamento: str
    valor: float
    descricao: str
    apto: str = Field(foreign_key="apartamentos.apartamento")  # Foreign Key


# Tabela gastos_variaveis
class GastoVariavel(SQLModel, table=True):
    __tablename__ = "gastos_variaveis"
    id: Optional[int] = Field(default=None, primary_key=True)  # Primary Key
    data_pagamento: str
    valor_material: Optional[float]
    valor_mo: Optional[float]
    valor_total: float
    descricao: str
    apto: str = Field(foreign_key="apartamentos.apartamento")  # Foreign Key


# Tabela alugueis
class Aluguel(SQLModel, table=True):
    __tablename__ = "alugueis"
    id: Optional[int] = Field(default=None, primary_key=True)  # Primary Key
    checkin: str
    checkout: str
    diarias: int
    valor_diaria: float
    taxa_adm: float
    valor_total: float
    valor_imob: float
    valor_prop: float
    apto: str = Field(foreign_key="apartamentos.apartamento")  # Foreign Key


# Tabela garagens
class Garagem(SQLModel, table=True):
    __tablename__ = "garagens"
    id: Optional[int] = Field(default=None, primary_key=True)  # Primary Key
    checkin: str
    checkout: str
    diarias: int
    valor_diaria: float
    taxa_adm: float
    valor_total: float
    valor_imob: float
    valor_prop: float
    apto_destino: str = Field(foreign_key="apartamentos.apartamento")  # Foreign Key
    apto_origem: str = Field(foreign_key="apartamentos.apartamento")  # Foreign Key


# Configuração do banco de dados SQLite
DATABASE_URL = "sqlite:///imob.sqlite"
engine = create_engine(DATABASE_URL)

# Criar as tabelas no banco de dados
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

if __name__ == "__main__":
    create_db_and_tables()
