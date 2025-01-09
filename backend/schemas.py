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
    logradouro: Optional[str]
    numero: Optional[PositiveInt]
    bairro: Optional[str]
    cidade: Optional[str]
    uf: Optional[str]
    pais: Optional[str]
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


class DespesaCreate(DespesaBase):
    pass


class EdificioCreate(EdificioBase):
    pass


class GaragemCreate(GaragemBase):
    pass


class GastoCreate(GastoBase):
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


class DespesaFixaResponse(DespesaBase):
    id: PositiveInt
    data_pagamento: datetime
    apartamendo_id: PositiveInt

    class Config:
        from_attributes = True


class EdificioResponse(EdificioBase):
    id: PositiveInt
    nome: str

    class Config:
        from_attributes = True


class GaragemResponse(GaragemBase):
    id: PositiveInt
    apto_origem_id: PositiveInt
    apto_destino_id: PositiveInt

    class Config:
        from_attributes = True


class GastoResponse(GastoBase):
    id: PositiveInt
    apartamento_id: PositiveInt
    data_pagamento: datetime

    class Config:
        from_attributes = True


class ProprietarioResponse(ProprietarioBase):
    id: PositiveInt
    nome: str

    class Config:
        from_attributes = True


# Update schemas

class AluguelUpdate(BaseModel):
    apartamento_id: Optional[PositiveInt]
    checkin: Optional[datetime]
    checkout: Optional[datetime]
    diarias: Optional[PositiveInt]
    valor_diaria: Optional[PositiveFloat]
    taxa_adm: Optional[PositiveFloat]
    valor_total: Optional[PositiveFloat]
    valor_imob: Optional[PositiveFloat]
    valor_prop: Optional[PositiveFloat]


class ApartamentoUpdate(BaseModel):
    apartamento: Optional[str]
    edificio_id: Optional[PositiveInt]
    proprietario_id: Optional[PositiveInt]
    celesc: Optional[PositiveInt]
    supergasbras: Optional[PositiveInt]
    internet_provedor: Optional[str]
    wifiid: Optional[str]
    wifipass: Optional[str]
    lockpass: Optional[int]


class DespesaUpdate(BaseModel):
    apartamento_id: Optional[str]
    data_pagamento: Optional[datetime]
    valor: Optional[PositiveFloat]
    descricao: Optional[str]


class EdificioUpdate(BaseModel):
    nome: Optional[str]
    logradouro: Optional[str]
    numero: Optional[PositiveInt]
    bairro: Optional[str]
    cidade: Optional[str]
    uf: Optional[str]
    pais: Optional[str]
    cep: Optional[PositiveInt]


class GaragemUpdate(BaseModel):
    apto_origem_id: Optional[str]
    apto_destino_id: Optional[str]
    checkin: Optional[datetime]
    checkout: Optional[datetime]
    diarias: Optional[PositiveInt]
    valor_diaria: Optional[PositiveFloat]
    taxa_adm: Optional[PositiveFloat]
    valor_total: Optional[PositiveFloat]
    valor_imob: Optional[PositiveFloat]
    valor_prop: Optional[PositiveFloat]


class GastoUpdate(BaseModel):
    apartamento_id: Optional[str]
    data_pagamento: Optional[datetime]
    valor_material: Optional[PositiveFloat]
    valor_mo: Optional[PositiveFloat]
    valor_total: Optional[PositiveFloat]
    descricao: Optional[str]


class ProprietarioUpdate(BaseModel):
    nome: Optional[str]
    cpf: Optional[PositiveInt]
    telefone: Optional[int]
    email: Optional[EmailStr]
