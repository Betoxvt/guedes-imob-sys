from pydantic import BaseModel, PositiveFloat, EmailStr, PositiveInt
from datetime import datetime
from typing import Optional


# BaseModel schemas
class AluguelBase(BaseModel):
    checkin: datetime
    checkout: datetime
    diarias: PositiveInt
    valor_diaria: PositiveFloat
    taxa_adm: PositiveFloat
    valor_total: PositiveFloat
    valor_imob: PositiveFloat
    valor_prop: PositiveFloat
    apto: str


class ApartamentoBase(BaseModel):
    apartamento: str
    edificio: str
    endereco: Optional[str]
    celesc: Optional[PositiveInt]
    supergasbras: Optional[PositiveInt]
    internet: Optional[str]
    wifiid: Optional[str]
    wifipass: Optional[str]
    lockpass: Optional[int]
    proprietario: PositiveInt


class DespesaFixaBase(BaseModel):
    data_pagamento: datetime
    valor: PositiveFloat
    descricao: str
    apto: str


class GaragemBase(BaseModel):
    checkin: datetime
    checkout: datetime
    diarias: PositiveInt
    valor_diaria: PositiveFloat
    taxa_adm: PositiveFloat
    valor_total: PositiveFloat
    valor_imob: PositiveFloat
    valor_prop: PositiveFloat
    apto_origem: str
    apto_destino: str


class GastoVariavelBase(BaseModel):
    data_pagamento: datetime
    valor_material: Optional[PositiveFloat]
    valor_mo: Optional[PositiveFloat]
    valor_total: PositiveFloat
    descricao: str
    apto: str


class ProprietarioBase(BaseModel):
    cpf: Optional[PositiveInt]
    nome: str
    telefone: Optional[int]
    email: Optional[EmailStr]


#