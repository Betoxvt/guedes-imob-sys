from pydantic import BaseModel, EmailStr, PositiveInt, NonNegativeInt, NonNegativeFloat
from datetime import date
from typing import Any, Optional

# Base schemas

class AluguelBase(BaseModel):
    apartamento_id: PositiveInt
    inquilino_id: Optional[PositiveInt]
    checkin: date
    checkout: date
    diarias: PositiveInt
    valor_diaria: Optional[NonNegativeInt]
    taxa_adm: NonNegativeFloat
    valor_total: NonNegativeFloat
    valor_imob: NonNegativeFloat
    valor_prop: NonNegativeFloat


class ApartamentoBase(BaseModel):
    apartamento: str
    edificio_id: PositiveInt
    proprietario_id: PositiveInt
    celesc: Optional[str]
    supergasbras: Optional[str]
    internet_provedor: Optional[str]
    wifiid: Optional[str]
    wifipass: Optional[str]
    lockpass: Optional[str]


class DespesaBase(BaseModel):
    apartamento_id: PositiveInt
    data_pagamento: date
    valor: NonNegativeFloat
    descricao: str


class EdificioBase(BaseModel):
    nome: str
    logradouro: Optional[str]
    numero: Optional[str]
    bairro: Optional[str]
    cidade: Optional[str]
    uf: Optional[str]
    pais: Optional[str]
    cep: Optional[str]


class GaragemBase(BaseModel):
    apto_origem_id: PositiveInt
    apto_destino_id: PositiveInt
    checkin: date
    checkout: date
    diarias: PositiveInt
    valor_diaria: Optional[NonNegativeInt]
    taxa_adm: NonNegativeFloat
    valor_total: NonNegativeFloat
    valor_imob: NonNegativeFloat
    valor_prop: NonNegativeFloat


class GastoBase(BaseModel):
    apartamento_id: PositiveInt
    data_pagamento: date
    valor_material: Optional[NonNegativeFloat]
    valor_mo: Optional[NonNegativeFloat]
    valor_total: NonNegativeFloat
    descricao: str


class ProprietarioBase(BaseModel):
    nome: str
    cpf: Optional[str]
    telefone: Optional[str]
    email: Optional[EmailStr]


class InquilinoBase(BaseModel):
    apartamento: str
    nome: str
    tipo_residencia: str
    cidade: str
    cep: str
    estado: str
    pais: str
    telefone: str
    estado_civil: str
    profissao: str
    rg: Optional[str]
    cpf: str
    mae: str
    check_automovel: Optional[int]
    automovel: Optional[str]
    modelo_auto: Optional[str]
    placa_auto: Optional[str]
    cor_auto: Optional[str]
    checkin: date
    checkout: date
    observacoes: Optional[str]
    proprietario: Optional[str]
    imob_fone: str
    qtd_acomp: Optional[int]
    acomp_01_nome: Optional[str]
    acomp_01_rg: Optional[str]
    acomp_01_cpf: Optional[str]
    acomp_01_idade: Optional[NonNegativeInt]
    acomp_01_parentesco: Optional[str]
    acomp_02_nome: Optional[str]
    acomp_02_rg: Optional[str]
    acomp_02_cpf: Optional[str]
    acomp_02_idade: Optional[NonNegativeInt]
    acomp_02_parentesco: Optional[str]
    acomp_03_nome: Optional[str]
    acomp_03_rg: Optional[str]
    acomp_03_cpf: Optional[str]
    acomp_03_idade: Optional[NonNegativeInt]
    acomp_03_parentesco: Optional[str]
    acomp_04_nome: Optional[str]
    acomp_04_rg: Optional[str]
    acomp_04_cpf: Optional[str]
    acomp_04_idade: Optional[NonNegativeInt]
    acomp_04_parentesco: Optional[str]
    acomp_05_nome: Optional[str]
    acomp_05_rg: Optional[str]
    acomp_05_cpf: Optional[str]
    acomp_05_idade: Optional[NonNegativeInt]
    acomp_05_parentesco: Optional[str]
    acomp_06_nome: Optional[str]
    acomp_06_rg: Optional[str]
    acomp_06_cpf: Optional[str]
    acomp_06_idade: Optional[NonNegativeInt]
    acomp_06_parentesco: Optional[str]
    acomp_07_nome: Optional[str]    
    acomp_07_rg: Optional[str]
    acomp_07_cpf: Optional[str]
    acomp_07_idade: Optional[NonNegativeInt]
    acomp_07_parentesco: Optional[str]
    acomp_08_nome: Optional[str]
    acomp_08_rg: Optional[str]
    acomp_08_cpf: Optional[str]
    acomp_08_idade: Optional[NonNegativeInt]
    acomp_08_parentesco: Optional[str]
    acomp_09_nome: Optional[str]
    acomp_09_rg: Optional[str]
    acomp_09_cpf: Optional[str]
    acomp_09_idade: Optional[NonNegativeInt]
    acomp_09_parentesco: Optional[str]
    acomp_10_nome: Optional[str]
    acomp_10_rg: Optional[str]
    acomp_10_cpf: Optional[str]
    acomp_10_idade: Optional[NonNegativeInt]
    acomp_10_parentesco: Optional[str]


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


class InquilinoCreate(InquilinoBase):
    pass

# Response schemas

class AluguelResponse(AluguelBase):
    id: PositiveInt
    criado_em: date
    modificado_em: date

    class Config:
        from_attributes = True


class ApartamentoResponse(ApartamentoBase):
    id: PositiveInt
    criado_em: date
    modificado_em: date


    class Config:
        from_attributes = True


class DespesaResponse(DespesaBase):
    id: PositiveInt
    criado_em: date
    modificado_em: date


    class Config:
        from_attributes = True


class EdificioResponse(EdificioBase):
    id: PositiveInt
    criado_em: date
    modificado_em: date


    class Config:
        from_attributes = True


class GaragemResponse(GaragemBase):
    id: PositiveInt
    criado_em: date
    modificado_em: date


    class Config:
        from_attributes = True


class GastoResponse(GastoBase):
    id: PositiveInt
    criado_em: date
    modificado_em: date


    class Config:
        from_attributes = True


class ProprietarioResponse(ProprietarioBase):
    id: PositiveInt
    criado_em: date
    modificado_em: date
    

    class Config:
        from_attributes = True


class InquilinoResponse(InquilinoBase):
    id: PositiveInt
    criado_em: date
    modificado_em: date


    class Config:
        from_attributes = True


# Update schemas

class AluguelUpdate(BaseModel):
    apartamento_id: Optional[PositiveInt]
    inquilino_id: Optional[PositiveInt]
    checkin: Optional[date]
    checkout: Optional[date]
    diarias: Optional[PositiveInt]
    valor_diaria: Optional[NonNegativeInt]
    taxa_adm: Optional[NonNegativeFloat]
    valor_total: Optional[NonNegativeFloat]
    valor_imob: Optional[NonNegativeFloat]
    valor_prop: Optional[NonNegativeFloat]


class ApartamentoUpdate(BaseModel):
    apartamento: Optional[str]
    edificio_id: Optional[PositiveInt]
    proprietario_id: Optional[PositiveInt]
    celesc: Optional[str]
    supergasbras: Optional[str]
    internet_provedor: Optional[str]
    wifiid: Optional[str]
    wifipass: Optional[str]
    lockpass: Optional[str]


class DespesaUpdate(BaseModel):
    apartamento_id: Optional[PositiveInt]
    data_pagamento: Optional[date]
    valor: Optional[NonNegativeFloat]
    descricao: Optional[str]


class EdificioUpdate(BaseModel):
    nome: Optional[str]
    logradouro: Optional[str]
    numero: Optional[str]
    bairro: Optional[str]
    cidade: Optional[str]
    uf: Optional[str]
    pais: Optional[str]
    cep: Optional[str]


class GaragemUpdate(BaseModel):
    apto_origem_id: Optional[PositiveInt]
    apto_destino_id: Optional[PositiveInt]
    checkin: Optional[date]
    checkout: Optional[date]
    diarias: Optional[PositiveInt]
    valor_diaria: Optional[NonNegativeInt]
    taxa_adm: Optional[NonNegativeFloat]
    valor_total: Optional[NonNegativeFloat]
    valor_imob: Optional[NonNegativeFloat]
    valor_prop: Optional[NonNegativeFloat]


class GastoUpdate(BaseModel):
    apartamento_id: Optional[PositiveInt]
    data_pagamento: Optional[date]
    valor_material: Optional[NonNegativeFloat]
    valor_mo: Optional[NonNegativeFloat]
    valor_total: Optional[NonNegativeFloat]
    descricao: Optional[str]


class ProprietarioUpdate(BaseModel):
    nome: Optional[str]
    cpf: Optional[str]
    telefone: Optional[str]
    email: Optional[EmailStr]


class InquilinoUpdate(BaseModel):
    apartamento: Optional[str]
    nome: Optional[str]
    tipo_residencia: Optional[str]
    cidade: Optional[str]
    cep: Optional[str]
    estado: Optional[str]
    pais: Optional[str]
    telefone: Optional[str]
    estado_civil: Optional[str]
    profissao: Optional[str]
    rg: Optional[str]
    cpf: Optional[str]
    mae: Optional[str]
    check_automovel: Optional[int]
    automovel: Optional[str]
    modelo_auto: Optional[str]
    placa_auto: Optional[str]
    cor_auto: Optional[str]
    checkin: Optional[date]
    checkout: Optional[date]
    observacoes: Optional[str]
    proprietario: Optional[str]
    imob_fone: Optional[str]
    qtd_acomp: Optional[int]
    acomp_01_nome: Optional[str]
    acomp_01_rg: Optional[str]
    acomp_01_cpf: Optional[str]
    acomp_01_idade: Optional[NonNegativeInt]
    acomp_01_parentesco: Optional[str]
    acomp_02_nome: Optional[str]
    acomp_02_rg: Optional[str]
    acomp_02_cpf: Optional[str]
    acomp_02_idade: Optional[NonNegativeInt]
    acomp_02_parentesco: Optional[str]
    acomp_03_nome: Optional[str]
    acomp_03_rg: Optional[str]
    acomp_03_cpf: Optional[str]
    acomp_03_idade: Optional[NonNegativeInt]
    acomp_03_parentesco: Optional[str]
    acomp_04_nome: Optional[str]
    acomp_04_rg: Optional[str]
    acomp_04_cpf: Optional[str]
    acomp_04_idade: Optional[NonNegativeInt]
    acomp_04_parentesco: Optional[str]
    acomp_05_nome: Optional[str]
    acomp_05_rg: Optional[str]
    acomp_05_cpf: Optional[str]
    acomp_05_idade: Optional[NonNegativeInt]
    acomp_05_parentesco: Optional[str]
    acomp_06_nome: Optional[str]
    acomp_06_rg: Optional[str]
    acomp_06_cpf: Optional[str]
    acomp_06_idade: Optional[NonNegativeInt]
    acomp_06_parentesco: Optional[str]
    acomp_07_nome: Optional[str]
    acomp_07_rg: Optional[str]
    acomp_07_cpf: Optional[str]
    acomp_07_idade: Optional[NonNegativeInt]
    acomp_07_parentesco: Optional[str]
    acomp_08_nome: Optional[str]
    acomp_08_rg: Optional[str]
    acomp_08_cpf: Optional[str]
    acomp_08_idade: Optional[NonNegativeInt]
    acomp_08_parentesco: Optional[str]
    acomp_09_nome: Optional[str]
    acomp_09_rg: Optional[str]
    acomp_09_cpf: Optional[str]
    acomp_09_idade: Optional[NonNegativeInt]
    acomp_09_parentesco: Optional[str]
    acomp_10_nome: Optional[str]
    acomp_10_rg: Optional[str]
    acomp_10_cpf: Optional[str]
    acomp_10_idade: Optional[NonNegativeInt]
    acomp_10_parentesco: Optional[str]
