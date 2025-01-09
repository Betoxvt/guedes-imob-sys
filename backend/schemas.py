from pydantic import BaseModel, PositiveFloat, EmailStr, PositiveInt
from datetime import datetime
from typing import Optional


# Base schemas
class AluguelBase(BaseModel):
    apartamento_id: PositiveInt
    checkin: datetime
    checkout: datetime
    diarias: PositiveInt
    valor_diaria: PositiveFloat
    taxa_adm: PositiveFloat
    valor_total: PositiveFloat
    valor_imob: PositiveFloat
    valor_prop: PositiveFloat


class ApartamentoBase(BaseModel):
    apartamento: str
    edificio_id: PositiveInt
    proprietario_id: PositiveInt
    celesc: Optional[PositiveInt]
    supergasbras: Optional[PositiveInt]
    internet_provedor: Optional[str]
    wifiid: Optional[str]
    wifipass: Optional[str]
    lockpass: Optional[int]


class DespesaBase(BaseModel):
    apartamento_id: str
    data_pagamento: datetime
    valor: PositiveFloat
    descricao: str


class EdificioBase(BaseModel):
    nome: str
    endereco: Optional[str]
    numero: Optional[PositiveInt]
    bairro: Optional[str]
    cidade: Optional[str]
    uf: Optional[str]
    cep: Optional[PositiveInt]

class GaragemBase(BaseModel):
    apto_origem_id: str
    apto_destino_id: str
    checkin: datetime
    checkout: datetime
    diarias: PositiveInt
    valor_diaria: PositiveFloat
    taxa_adm: PositiveFloat
    valor_total: PositiveFloat
    valor_imob: PositiveFloat
    valor_prop: PositiveFloat


class GastoBase(BaseModel):
    apartamento_id: str
    data_pagamento: datetime
    valor_material: Optional[PositiveFloat]
    valor_mo: Optional[PositiveFloat]
    valor_total: PositiveFloat
    descricao: str


class ProprietarioBase(BaseModel):
    nome: str
    cpf: Optional[PositiveInt]
    telefone: Optional[int]
    email: Optional[EmailStr]


# Create schemas
class AluguelCreate(AluguelBase):
    pass


class ApartamentoCreate(ApartamentoBase):
    pass


class DespesaFixaCreate(DespesaFixaBase):
    pass


class GaragemCreate(GaragemBase):
    pass


class GastoVariavelCreate(GastoVariavelBase):
    pass


class ProprietarioCreate(ProprietarioBase):
    pass


# Response schemas
class AluguelResponse(AluguelBase):
    id: PositiveInt
    checkin: datetime
    checkout: datetime

    class Config:
        from_attributes = True


class ApartamentoResponse(ApartamentoBase):
    id: PositiveInt
    apartamento: str
    edificio_id: PositiveInt

    class Config:
        from_attributes = True


class DespesaFixaResponse(DespesaFixaBase):
    id: PositiveInt
    data_pagamento: datetime
    apartamendo_id: PositiveInt

    class Config:
        from_attributes = True


class GaragemResponse(GaragemBase):