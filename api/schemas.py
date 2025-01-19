from datetime import date
from enum import Enum
from pydantic import BaseModel
from typing import Optional


def convert_to_optional(schema):
    return {k: Optional[v] for k, v in schema.__annotations__.items()}

# Base schemas


class AluguelBase(BaseModel):
    apto_id: int
    ficha_id: Optional[int]
    checkin: date
    checkout: date
    diarias: int
    valor_diaria: float
    valor_total: float


class ApartamentoBase(BaseModel):
    apto: str
    proprietario_id: Optional[int]
    cod_celesc: Optional[str]
    cod_gas: Optional[str]
    prov_net: Optional[str]
    wifi: Optional[str]
    wifi_senha: Optional[str]
    lock_senha: Optional[str]


class DespesaCat(Enum):
    cat1 = 'IPTU'
    cat2 = 'CONDOMÍNIO'
    cat3 = 'LUZ'
    cat4 = 'GÁS'
    cat5 = 'INTERNET'
    cat6 = 'MANUTENÇÃO'
    cat7 = 'OUTROS'


class DespesaBase(BaseModel):
    apto_id: Optional[int]
    data_pagamento: date
    valor: float
    descricao: str


class GaragemBase(BaseModel):
    apto_origem_id: int
    apto_destino_id: int
    checkin: date
    checkout: date
    diarias: int
    valor_diaria: float
    valor_total: float


class ProprietarioBase(BaseModel):
    nome: str
    cpf: Optional[str]
    tel: Optional[str]
    email: Optional[str]


class FichaCat:
    cat1 = 'Anual'
    cat2 = 'Temporária'


class FichaBase(BaseModel):
    apto: str
    nome: str
    tipo_residencia: str
    cidade: str
    cep: str
    uf: str
    pais: str
    tel: str 
    estado_civil: str
    profissao: str
    rg: str
    cpf: str
    mae: str
    automovel: Optional[str]
    modelo_auto: Optional[str]
    placa_auto: Optional[str]
    cor_auto: Optional[str]
    checkin: date
    checkout: date
    observacoes: Optional[str]
    proprietario: Optional[str]
    imob_fone: Optional[str]
    a0: Optional[dict]
    a1: Optional[dict]
    a2: Optional[dict]
    a3: Optional[dict]
    a4: Optional[dict]
    a5: Optional[dict]
    a6: Optional[dict]
    a7: Optional[dict]
    a8: Optional[dict]
    a9: Optional[dict]


# Create schemas


class AluguelCreate(AluguelBase):
    pass


class ApartamentoCreate(ApartamentoBase):
    pass


class DespesaCreate(DespesaBase):
    pass


class GaragemCreate(GaragemBase):
    pass


class ProprietarioCreate(ProprietarioBase):
    pass


class FichaCreate(FichaBase):
    pass


# Response schemas


class AluguelResponse(AluguelBase):
    id: int
    criado_em: date
    modificado_em: date

    class Config:
        from_attributes = True


class ApartamentoResponse(ApartamentoBase):
    id: int
    criado_em: date
    modificado_em: date

    class Config:
        from_attributes = True


class DespesaResponse(DespesaBase):
    id: int
    criado_em: date
    modificado_em: date

    class Config:
        from_attributes = True


class GaragemResponse(GaragemBase):
    id: int
    criado_em: date
    modificado_em: date

    class Config:
        from_attributes = True


class ProprietarioResponse(ProprietarioBase):
    id: int
    criado_em: date
    modificado_em: date
    
    class Config:
        from_attributes = True


class FichaResponse(FichaBase):
    id: int
    criado_em: date
    modificado_em: date

    class Config:
        from_attributes = True


# Update schemas

class AluguelUpdate(AluguelCreate):
    __annotations__ = convert_to_optional(AluguelCreate)


class ApartamentoUpdate(ApartamentoCreate):
    __annotations__ = convert_to_optional(ApartamentoCreate)


class DespesaUpdate(DespesaCreate):
    __annotations__ = convert_to_optional(DespesaCreate)


class GaragemUpdate(GaragemCreate):
    __annotations__ = convert_to_optional(DespesaCreate)
    

class ProprietarioUpdate(ProprietarioCreate):
    __annotations__ = convert_to_optional(ProprietarioCreate)


class FichaUpdate(FichaCreate):
    __annotations__ = convert_to_optional(FichaCreate)
