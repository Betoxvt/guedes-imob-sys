from pydantic import BaseModel, PositiveFloat, EmailStr, PositiveInt
from datetime import date
from typing import Optional


# Base schemas

class AluguelBase(BaseModel):
    apartamento_id: PositiveInt
    inquilino_id: Optional[PositiveInt]
    checkin: date
    checkout: date
    diarias: PositiveInt
    valor_diaria: Optional[PositiveFloat]
    taxa_adm: PositiveFloat
    valor_total: PositiveFloat
    valor_imob: PositiveFloat
    valor_prop: PositiveFloat


class ApartamentoBase(BaseModel):
    apartamento: str
    edificio_id: PositiveInt
    proprietario_id: PositiveInt
    celesc: Optional[int]
    supergasbras: Optional[int]
    internet_provedor: Optional[str]
    wifiid: Optional[str]
    wifipass: Optional[str]
    lockpass: Optional[int]


class DespesaBase(BaseModel):
    apartamento_id: PositiveInt
    data_pagamento: date
    valor: PositiveFloat
    descricao: str


class EdificioBase(BaseModel):
    nome: str
    logradouro: Optional[str]
    numero: Optional[int]
    bairro: Optional[str]
    cidade: Optional[str]
    uf: Optional[str]
    pais: Optional[str]
    cep: Optional[int]

class GaragemBase(BaseModel):
    apto_origem_id: PositiveInt
    apto_destino_id: PositiveInt
    checkin: date
    checkout: date
    diarias: PositiveInt
    valor_diaria: Optional[PositiveFloat]
    taxa_adm: PositiveFloat
    valor_total: PositiveFloat
    valor_imob: PositiveFloat
    valor_prop: PositiveFloat


class GastoBase(BaseModel):
    apartamento_id: PositiveInt
    data_pagamento: date
    valor_material: Optional[PositiveFloat]
    valor_mo: Optional[PositiveFloat]
    valor_total: PositiveFloat
    descricao: str


class ProprietarioBase(BaseModel):
    nome: str
    cpf: Optional[int]
    telefone: Optional[int]
    email: Optional[EmailStr]


class InquilinoBase(BaseModel):
    apartamento: str
    nome: str
    tipo_residencia: str
    cidade: str
    cep: PositiveInt
    estado: str
    pais: str
    telefone: PositiveInt
    estado_civil: str
    profissao: str
    rg: PositiveInt
    cpf: PositiveInt
    mae: str
    automovel: str
    modelo_auto: str
    placa_auto: str
    cor_auto: str
    checkin: date
    checkout: date
    observacoes: Optional[str]
    proprietario: Optional[str]
    imob_fone: PositiveInt
    acomp_01_nome: Optional[str]
    acomp_01_rg: Optional[PositiveInt]
    acomp_01_cpf: Optional[PositiveInt]
    acomp_01_idade: Optional[int]
    acomp_01_parentesco: Optional[str]
    acomp_02_nome: Optional[str]
    acomp_02_rg: Optional[PositiveInt]
    acomp_02_cpf: Optional[PositiveInt]
    acomp_02_idade: Optional[int]
    acomp_02_parentesco: Optional[str]
    acomp_03_nome: Optional[str]
    acomp_03_rg: Optional[PositiveInt]
    acomp_03_cpf: Optional[PositiveInt]
    acomp_03_idade: Optional[int]
    acomp_03_parentesco: Optional[str]
    acomp_04_nome: Optional[str]
    acomp_04_rg: Optional[PositiveInt]
    acomp_04_cpf: Optional[PositiveInt]
    acomp_04_idade: Optional[int]
    acomp_04_parentesco: Optional[str]
    acomp_05_nome: Optional[str]
    acomp_05_rg: Optional[PositiveInt]
    acomp_05_cpf: Optional[PositiveInt]
    acomp_05_idade: Optional[int]
    acomp_05_parentesco: Optional[str]
    acomp_06_nome: Optional[str]
    acomp_06_rg: Optional[PositiveInt]
    acomp_06_cpf: Optional[PositiveInt]
    acomp_06_idade: Optional[int]
    acomp_06_parentesco: Optional[str]
    acomp_07_nome: Optional[str]    
    acomp_07_rg: Optional[PositiveInt]
    acomp_07_cpf: Optional[PositiveInt]
    acomp_07_idade: Optional[int]
    acomp_07_parentesco: Optional[str]
    acomp_08_nome: Optional[str]
    acomp_08_rg: Optional[PositiveInt]
    acomp_08_cpf: Optional[PositiveInt]
    acomp_08_idade: Optional[int]
    acomp_08_parentesco: Optional[str]
    acomp_09_nome: Optional[str]
    acomp_09_rg: Optional[PositiveInt]
    acomp_09_cpf: Optional[PositiveInt]
    acomp_09_idade: Optional[int]
    acomp_09_parentesco: Optional[str]
    acomp_10_nome: Optional[str]
    acomp_10_rg: Optional[PositiveInt]
    acomp_10_cpf: Optional[PositiveInt]
    acomp_10_idade: Optional[int]
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
    valor_diaria: Optional[PositiveFloat]
    taxa_adm: Optional[PositiveFloat]
    valor_total: Optional[PositiveFloat]
    valor_imob: Optional[PositiveFloat]
    valor_prop: Optional[PositiveFloat]


class ApartamentoUpdate(BaseModel):
    apartamento: Optional[str]
    edificio_id: Optional[PositiveInt]
    proprietario_id: Optional[PositiveInt]
    celesc: Optional[int]
    supergasbras: Optional[int]
    internet_provedor: Optional[str]
    wifiid: Optional[str]
    wifipass: Optional[str]
    lockpass: Optional[int]


class DespesaUpdate(BaseModel):
    apartamento_id: Optional[PositiveInt]
    data_pagamento: Optional[date]
    valor: Optional[PositiveFloat]
    descricao: Optional[str]


class EdificioUpdate(BaseModel):
    nome: Optional[str]
    logradouro: Optional[str]
    numero: Optional[int]
    bairro: Optional[str]
    cidade: Optional[str]
    uf: Optional[str]
    pais: Optional[str]
    cep: Optional[int]


class GaragemUpdate(BaseModel):
    apto_origem_id: Optional[PositiveInt]
    apto_destino_id: Optional[PositiveInt]
    checkin: Optional[date]
    checkout: Optional[date]
    diarias: Optional[PositiveInt]
    valor_diaria: Optional[PositiveFloat]
    taxa_adm: Optional[PositiveFloat]
    valor_total: Optional[PositiveFloat]
    valor_imob: Optional[PositiveFloat]
    valor_prop: Optional[PositiveFloat]


class GastoUpdate(BaseModel):
    apartamento_id: Optional[PositiveInt]
    data_pagamento: Optional[date]
    valor_material: Optional[PositiveFloat]
    valor_mo: Optional[PositiveFloat]
    valor_total: Optional[PositiveFloat]
    descricao: Optional[str]


class ProprietarioUpdate(BaseModel):
    nome: Optional[str]
    cpf: Optional[int]
    telefone: Optional[int]
    email: Optional[EmailStr]


class InquilinoUpdate(BaseModel):
    apartamento: Optional[str]
    nome: Optional[str]
    tipo_residencia: Optional[str]
    cidade: Optional[str]
    cep: Optional[PositiveInt]
    estado: Optional[str]
    pais: Optional[str]
    telefone: Optional[PositiveInt]
    estado_civil: Optional[str]
    profissao: Optional[str]
    rg: Optional[PositiveInt]
    cpf: Optional[PositiveInt]
    mae: Optional[str]
    automovel: Optional[str]
    modelo_auto: Optional[str]
    placa_auto: Optional[str]
    cor_auto: Optional[str]
    checkin: Optional[date]
    checkout: Optional[date]
    observacoes: Optional[str]
    proprietario: Optional[str]
    imob_fone: Optional[PositiveInt]
    acomp_01_nome: Optional[str]
    acomp_01_rg: Optional[PositiveInt]
    acomp_01_cpf: Optional[PositiveInt]
    acomp_01_idade: Optional[int]
    acomp_01_parentesco: Optional[str]
    acomp_02_nome: Optional[str]
    acomp_02_rg: Optional[PositiveInt]
    acomp_02_cpf: Optional[PositiveInt]
    acomp_02_idade: Optional[int]
    acomp_02_parentesco: Optional[str]
    acomp_03_nome: Optional[str]
    acomp_03_rg: Optional[PositiveInt]
    acomp_03_cpf: Optional[PositiveInt]
    acomp_03_idade: Optional[int]
    acomp_03_parentesco: Optional[str]
    acomp_04_nome: Optional[str]
    acomp_04_rg: Optional[PositiveInt]
    acomp_04_cpf: Optional[PositiveInt]
    acomp_04_idade: Optional[int]
    acomp_04_parentesco: Optional[str]
    acomp_05_nome: Optional[str]
    acomp_05_rg: Optional[PositiveInt]
    acomp_05_cpf: Optional[PositiveInt]
    acomp_05_idade: Optional[int]
    acomp_05_parentesco: Optional[str]
    acomp_06_nome: Optional[str]
    acomp_06_rg: Optional[PositiveInt]
    acomp_06_cpf: Optional[PositiveInt]
    acomp_06_idade: Optional[int]
    acomp_06_parentesco: Optional[str]
    acomp_07_nome: Optional[str]
    acomp_07_rg: Optional[PositiveInt]
    acomp_07_cpf: Optional[PositiveInt]
    acomp_07_idade: Optional[int]
    acomp_07_parentesco: Optional[str]
    acomp_08_nome: Optional[str]
    acomp_08_rg: Optional[PositiveInt]
    acomp_08_cpf: Optional[PositiveInt]
    acomp_08_idade: Optional[int]
    acomp_08_parentesco: Optional[str]
    acomp_09_nome: Optional[str]
    acomp_09_rg: Optional[PositiveInt]
    acomp_09_cpf: Optional[PositiveInt]
    acomp_09_idade: Optional[int]
    acomp_09_parentesco: Optional[str]
    acomp_10_nome: Optional[str]
    acomp_10_rg: Optional[PositiveInt]
    acomp_10_cpf: Optional[PositiveInt]
    acomp_10_idade: Optional[int]
    acomp_10_parentesco: Optional[str]
