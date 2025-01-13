from pydantic import BaseModel

# Base schemas

class AluguelBase(BaseModel):
    apartamento_id: int
    inquilino_id: int | None = None
    checkin: str
    checkout: str
    diarias: int
    valor_diaria: int | None = None
    taxa_adm: float
    valor_total: float
    valor_imob: float
    valor_prop: float


class ApartamentoBase(BaseModel):
    apartamento: str
    edificio_id: int
    proprietario_id: int
    celesc: str | None = None
    supergasbras: str | None = None
    internet_provedor: str | None = None
    wifiid: str | None = None
    wifipass: str | None = None
    lockpass: str | None = None


class DespesaBase(BaseModel):
    apartamento_id: int
    data_pagamento: str
    valor: float
    descricao: str


class EdificioBase(BaseModel):
    nome: str
    logradouro: str | None = None
    numero: str | None = None
    bairro: str | None = None
    cidade: str | None = None
    uf: str | None = None
    pais: str | None = None
    cep: str | None = None


class GaragemBase(BaseModel):
    apto_origem_id: int
    apto_destino_id: int
    checkin: str
    checkout: str
    diarias: int
    valor_diaria: int | None = None
    taxa_adm: float
    valor_total: float
    valor_imob: float
    valor_prop: float


class GastoBase(BaseModel):
    apartamento_id: int
    data_pagamento: str
    valor_material: float | None = None
    valor_mo: float | None = None
    valor_total: float
    descricao: str


class ProprietarioBase(BaseModel):
    nome: str
    cpf: str | None = None
    telefone: str | None = None
    email: str | None = None


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
    rg: str | None = None
    cpf: str
    mae: str
    automovel: str | None = None
    modelo_auto: str | None = None
    placa_auto: str | None = None
    cor_auto: str | None = None
    checkin: str
    checkout: str
    observacoes: str | None = None
    proprietario: str | None = None
    imob_fone: str | None = None
    acomp_01_nome: str | None = None
    acomp_01_rg: str | None = None
    acomp_01_cpf: str | None = None
    acomp_01_idade: int | None = None
    acomp_01_parentesco: str | None = None
    acomp_02_nome: str | None = None
    acomp_02_rg: str | None = None
    acomp_02_cpf: str | None = None
    acomp_02_idade: int | None = None
    acomp_02_parentesco: str | None = None
    acomp_03_nome: str | None = None
    acomp_03_rg: str | None = None
    acomp_03_cpf: str | None = None
    acomp_03_idade: int | None = None
    acomp_03_parentesco: str | None = None
    acomp_04_nome: str | None = None
    acomp_04_rg: str | None = None
    acomp_04_cpf: str | None = None
    acomp_04_idade: int | None = None
    acomp_04_parentesco: str | None = None
    acomp_05_nome: str | None = None
    acomp_05_rg: str | None = None
    acomp_05_cpf: str | None = None
    acomp_05_idade: int | None = None
    acomp_05_parentesco: str | None = None
    acomp_06_nome: str | None = None
    acomp_06_rg: str | None = None
    acomp_06_cpf: str | None = None
    acomp_06_idade: int | None = None
    acomp_06_parentesco: str | None = None
    acomp_07_nome: str | None = None    
    acomp_07_rg: str | None = None
    acomp_07_cpf: str | None = None
    acomp_07_idade: int | None = None
    acomp_07_parentesco: str | None = None
    acomp_08_nome: str | None = None
    acomp_08_rg: str | None = None
    acomp_08_cpf: str | None = None
    acomp_08_idade: int | None = None
    acomp_08_parentesco: str | None = None
    acomp_09_nome: str | None = None
    acomp_09_rg: str | None = None
    acomp_09_cpf: str | None = None
    acomp_09_idade: int | None = None
    acomp_09_parentesco: str | None = None
    acomp_10_nome: str | None = None
    acomp_10_rg: str | None = None
    acomp_10_cpf: str | None = None
    acomp_10_idade: int | None = None
    acomp_10_parentesco: str | None = None


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
    id: int
    criado_em: str
    modificado_em: str

    class Config:
        from_attributes = True


class ApartamentoResponse(ApartamentoBase):
    id: int
    criado_em: str
    modificado_em: str


    class Config:
        from_attributes = True


class DespesaResponse(DespesaBase):
    id: int
    criado_em: str
    modificado_em: str


    class Config:
        from_attributes = True


class EdificioResponse(EdificioBase):
    id: int
    criado_em: str
    modificado_em: str


    class Config:
        from_attributes = True


class GaragemResponse(GaragemBase):
    id: int
    criado_em: str
    modificado_em: str


    class Config:
        from_attributes = True


class GastoResponse(GastoBase):
    id: int
    criado_em: str
    modificado_em: str


    class Config:
        from_attributes = True


class ProprietarioResponse(ProprietarioBase):
    id: int
    criado_em: str
    modificado_em: str
    

    class Config:
        from_attributes = True


class InquilinoResponse(InquilinoBase):
    id: int
    criado_em: str
    modificado_em: str


    class Config:
        from_attributes = True


# Update schemas

class AluguelUpdate(BaseModel):
    apartamento_id: int | None = None
    inquilino_id: int | None = None
    checkin: str | None = None
    checkout: str | None = None
    diarias: int | None = None
    valor_diaria: int | None = None
    taxa_adm: float | None = None
    valor_total: float | None = None
    valor_imob: float | None = None
    valor_prop: float | None = None


class ApartamentoUpdate(BaseModel):
    apartamento: str | None = None
    edificio_id: int | None = None
    proprietario_id: int | None = None
    celesc: str | None = None
    supergasbras: str | None = None
    internet_provedor: str | None = None
    wifiid: str | None = None
    wifipass: str | None = None
    lockpass: str | None = None


class DespesaUpdate(BaseModel):
    apartamento_id: int | None = None
    data_pagamento: str | None = None
    valor: float | None = None
    descricao: str | None = None


class EdificioUpdate(BaseModel):
    nome: str | None = None
    logradouro: str | None = None
    numero: str | None = None
    bairro: str | None = None
    cidade: str | None = None
    uf: str | None = None
    pais: str | None = None
    cep: str | None = None


class GaragemUpdate(BaseModel):
    apto_origem_id: int | None = None
    apto_destino_id: int | None = None
    checkin: str | None = None
    checkout: str | None = None
    diarias: int | None = None
    valor_diaria: int | None = None
    taxa_adm: float | None = None
    valor_total: float | None = None
    valor_imob: float | None = None
    valor_prop: float | None = None


class GastoUpdate(BaseModel):
    apartamento_id: int | None = None
    data_pagamento: str | None = None
    valor_material: float | None = None
    valor_mo: float | None = None
    valor_total: float | None = None
    descricao: str | None = None


class ProprietarioUpdate(BaseModel):
    nome: str | None = None
    cpf: str | None = None
    telefone: str | None = None
    email: str | None = None


class InquilinoUpdate(BaseModel):
    apartamento: str | None = None
    nome: str | None = None
    tipo_residencia: str | None = None
    cidade: str | None = None
    cep: str | None = None
    estado: str | None = None
    pais: str | None = None
    telefone: str | None = None
    estado_civil: str | None = None
    profissao: str | None = None
    rg: str | None = None
    cpf: str | None = None
    mae: str | None = None
    automovel: str | None = None
    modelo_auto: str | None = None
    placa_auto: str | None = None
    cor_auto: str | None = None
    checkin: str | None = None
    checkout: str | None = None
    observacoes: str | None = None
    proprietario: str | None = None
    imob_fone: str | None = None
    acomp_01_nome: str | None = None
    acomp_01_rg: str | None = None
    acomp_01_cpf: str | None = None
    acomp_01_idade: int | None = None
    acomp_01_parentesco: str | None = None
    acomp_02_nome: str | None = None
    acomp_02_rg: str | None = None
    acomp_02_cpf: str | None = None
    acomp_02_idade: int | None = None
    acomp_02_parentesco: str | None = None
    acomp_03_nome: str | None = None
    acomp_03_rg: str | None = None
    acomp_03_cpf: str | None = None
    acomp_03_idade: int | None = None
    acomp_03_parentesco: str | None = None
    acomp_04_nome: str | None = None
    acomp_04_rg: str | None = None
    acomp_04_cpf: str | None = None
    acomp_04_idade: int | None = None
    acomp_04_parentesco: str | None = None
    acomp_05_nome: str | None = None
    acomp_05_rg: str | None = None
    acomp_05_cpf: str | None = None
    acomp_05_idade: int | None = None
    acomp_05_parentesco: str | None = None
    acomp_06_nome: str | None = None
    acomp_06_rg: str | None = None
    acomp_06_cpf: str | None = None
    acomp_06_idade: int | None = None
    acomp_06_parentesco: str | None = None
    acomp_07_nome: str | None = None
    acomp_07_rg: str | None = None
    acomp_07_cpf: str | None = None
    acomp_07_idade: int | None = None
    acomp_07_parentesco: str | None = None
    acomp_08_nome: str | None = None
    acomp_08_rg: str | None = None
    acomp_08_cpf: str | None = None
    acomp_08_idade: int | None = None
    acomp_08_parentesco: str | None = None
    acomp_09_nome: str | None = None
    acomp_09_rg: str | None = None
    acomp_09_cpf: str | None = None
    acomp_09_idade: int | None = None
    acomp_09_parentesco: str | None = None
    acomp_10_nome: str | None = None
    acomp_10_rg: str | None = None
    acomp_10_cpf: str | None = None
    acomp_10_idade: int | None = None
    acomp_10_parentesco: str | None = None
