from sqlmodel import Field, SQLModel, create_engine, Relationship
from typing import Optional

# Tabelas do banco de dados

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


# Tabela apartamentos
class Apartamento(SQLModel, table=True):
    __tablename__ = "apartamentos"
    apartamento: str = Field(primary_key=True)  # Primary Key
    edificio: str = "Imperatriz"
    endereco: str = "Av. Atlântica, 2554, Balneário Camboriú - SC"
    celesc: Optional[int]
    supergasbras: Optional[int]
    internet: Optional[str]
    wifiid: Optional[str]
    wifipass: Optional[str]
    lockpass: Optional[int]
    proprietario: Optional[int] = Field(foreign_key="proprietarios.cpf")  # Foreign Key


# Tabela despesas_fixas
class DespesaFixa(SQLModel, table=True):
    __tablename__ = "despesas_fixas"
    id: Optional[int] = Field(default=None, primary_key=True)  # Primary Key
    data_pagamento: str
    valor: float
    descricao: str
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

# Patch - Atualizar tabelas, permite alterações parciais

class AluguelPatch(SQLModel):
    checkin: Optional[str]
    checkout: Optional[str]
    diarias: Optional[int]
    valor_diaria: Optional[float]
    taxa_adm: Optional[float]
    valor_total: Optional[float]
    valor_imob: Optional[float]
    valor_prop: Optional[float]
    apto: Optional[str]

class ApartamentoPatch(SQLModel):
    edificio: Optional[str]
    endereco: Optional[str]
    celesc: Optional[int]
    supergasbras: Optional[int]
    internet: Optional[str]
    wifiid: Optional[str]
    wifipass: Optional[str]
    lockpass: Optional[int]
    proprietario: Optional[int]

class DespesaFixaPatch(SQLModel):
    data_pagamento: Optional[str]
    valor: Optional[float]
    descricao: Optional[str]
    apto: Optional[str]

class GaragemPatch(SQLModel):
    checkin: Optional[str]
    checkout: Optional[str]
    diarias: Optional[int]
    valor_diaria: Optional[float]
    taxa_adm: Optional[float]
    valor_total: Optional[float]
    valor_imob: Optional[float]
    valor_prop: Optional[float]
    apto_destino: Optional[str]
    apto_origem: Optional[str]

class GastoVariavelPatch(SQLModel):
    data_pagamento: Optional[str]
    valor_material: Optional[float]
    valor_mo: Optional[float]
    valor_total: Optional[float]
    descricao: Optional[str]
    apto: Optional[str]

class ProprietarioPatch(SQLModel):
    nome: Optional[str]
    telefone: Optional[int]
    email: Optional[str]
    apto1: Optional[str]
    apto2: Optional[str]
    apto3: Optional[str]
    apto4: Optional[str]
