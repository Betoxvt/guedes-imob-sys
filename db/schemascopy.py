from datetime import date
from enum import Enum
from pydantic import BaseModel, EmailStr, field_validator
from typing import Optional


def convert_to_optional(schema):
    return {k: Optional[v] for k, v in schema.__annotations__.items()}


# Base schemas


class AluguelBase(BaseModel):
    apto_id: str
    ficha_id: Optional[int]
    checkin: date
    checkout: date
    diarias: int
    valor_diaria: float
    valor_total: float
    nome: str
    contato: str


class ApartamentoBase(BaseModel):
    id: str
    proprietario_id: Optional[int]
    cod_celesc: Optional[str]
    cod_gas: Optional[str]
    prov_net: Optional[str]
    wifi: Optional[str]
    wifi_senha: Optional[str]
    lock_senha: Optional[str]
    cod_imov: Optional[str]
    dic: Optional[str]
    ins_imob: Optional[str]
    matricula: Optional[str]
    rip: Optional[str]


class DespesaCat(Enum):
    cat1 = "IPTU"
    cat2 = "Condomínio"
    cat3 = "Ambiental"
    cat4 = "Luz"
    cat5 = "Gás"
    cat6 = "Internet"
    cat7 = "Manutenção"
    cat8 = "Adiantamento"
    cat9 = "Outros"


class DespesaBase(BaseModel):
    apto_id: str
    data: date
    valor: float
    categoria: str
    descricao: Optional[str]

    @field_validator("categoria")
    def check_categoria_despesa_base(cls, v):
        if v in [item.value for item in DespesaCat]:
            return v
        raise ValueError("Categoria inválida")


class FichaTipoCat(Enum):
    cat1 = "Anual"
    cat2 = "Temporário"


class FichaCivilCat(Enum):
    cat1 = "Casado(a)"
    cat2 = "Divorciado(a)"
    cat3 = "Separado(a)"
    cat4 = "Solteiro(a)"
    cat5 = "Viúvo(a)"


class FichaBase(BaseModel):
    apto_id: Optional[str]
    aluguel_id: Optional[int]
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

    @field_validator("estado_civil")
    def check_categoria_estado_civil_base(cls, v):
        if v in [item.value for item in FichaCivilCat]:
            return v
        raise ValueError("Categoria inválida")

    @field_validator("tipo_residencia")
    def check_categoria_tipo_residencia_base(cls, v):
        if v in [item.value for item in FichaTipoCat]:
            return v
        raise ValueError("Categoria inválida")


class GaragemBase(BaseModel):
    apto_id_origem: str
    apto_id_destino: str
    checkin: Optional[date]
    checkout: Optional[date]
    diarias: Optional[int]
    valor_diaria: Optional[float]
    valor_total: Optional[float]


class PagamentoCat(Enum):
    categoria1 = "Reserva"
    categoria2 = "Parcela"
    categoria3 = "Integral"
    categoria4 = "Quitação"
    categoria5 = "Garagem"


class PagamentoBase(BaseModel):
    tipo: str
    valor: float
    aluguel_id: int
    notas: Optional[str]
    nome: Optional[str]
    contato: Optional[str]
    data: date

    @field_validator("tipo")
    def check_categoria_pagamento_base(cls, v):
        if v in [item.value for item in PagamentoCat]:
            return v
        raise ValueError("Categoria inválida")


class ProprietarioBase(BaseModel):
    nome: str
    cpf: Optional[str]
    tel: Optional[str]
    email: Optional[EmailStr]


class RelatorioBase(BaseModel):
    apto_id: str
    data: date
    valor: float


# Create schemas


class AluguelCreate(AluguelBase):
    pass


class ApartamentoCreate(ApartamentoBase):
    pass


class DespesaCreate(DespesaBase):
    pass


class FichaCreate(FichaBase):
    pass


class GaragemCreate(GaragemBase):
    pass


class PagamentoCreate(PagamentoBase):
    pass


class ProprietarioCreate(ProprietarioBase):
    pass


class RelatorioCreate(RelatorioBase):
    pass


# Response schemas


class AluguelResponse(AluguelBase):
    id: int
    criado_em: date
    modificado_em: date

    class Config:
        from_attributes = True


class ApartamentoResponse(ApartamentoBase):
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


class FichaResponse(FichaBase):
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


class PagamentoResponse(PagamentoBase):
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


class RelatorioResponse(RelatorioBase):
    id: int
    criado_em: date
    modificado_em: date


# Update schemas


class AluguelUpdate(AluguelCreate):
    __annotations__ = convert_to_optional(AluguelCreate)


class ApartamentoUpdate(ApartamentoCreate):
    __annotations__ = convert_to_optional(ApartamentoCreate)


class DespesaUpdate(DespesaCreate):
    __annotations__ = convert_to_optional(DespesaCreate)

    @field_validator("categoria")
    def check_categoria_despesa_up(cls, v):
        if v is None:
            return v
        if v in [item.value for item in DespesaCat]:
            return v
        raise ValueError("Categoria inválida")


class FichaUpdate(FichaCreate):
    __annotations__ = convert_to_optional(FichaCreate)

    @field_validator("estado_civil")
    def check_categoria_estado_civil_up(cls, v):
        if v is None:
            return v
        if v in [item.value for item in FichaCivilCat]:
            return v
        raise ValueError("Categoria inválida")

    @field_validator("tipo_residencia")
    def check_categoria_tipo_residencia_up(cls, v):
        if v is None:
            return v
        if v in [item.value for item in FichaTipoCat]:
            return v
        raise ValueError("Categoria inválida")


class GaragemUpdate(GaragemCreate):
    __annotations__ = convert_to_optional(GaragemCreate)


class PagamentoUpdate(PagamentoCreate):
    __annotations__ = convert_to_optional(PagamentoCreate)

    @field_validator("tipo")
    def check_categoria_pagamento_up(cls, v):
        if v is None:
            return v
        if v in [item.value for item in PagamentoCat]:
            return v
        raise ValueError("Categoria inválida")


class ProprietarioUpdate(ProprietarioCreate):
    __annotations__ = convert_to_optional(ProprietarioCreate)


class RelatorioUpdate(RelatorioCreate):
    __annotations__ = convert_to_optional(RelatorioCreate)
