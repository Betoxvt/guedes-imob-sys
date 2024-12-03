from pydantic import BaseModel

class AluguelSchema(BaseModel):
    id: int
    checkin: str
    checkout: str
    diarias: int
    valor_diaria: float
    taxa_adm: float
    valor_total: float
    valor_imob: float
    valor_prop: float
    apto: str

    class Config:
        from_attributes = True

class ApartamentoSchema(BaseModel):
    apartamento: str
    edificio: str
    endereco: str
    celesc: int
    supergasbras: int
    internet: str
    wifiid: str
    wifipass: str
    lockpass: int
    proprietario: int

    class Config:
        from_attributes = True

class DespesaFixaSchema(BaseModel):
    id: int
    data_pagamento: str
    valor: float
    descricao: str
    apto: str

    class Config:
        from_attributes = True

class GaragemSchema(BaseModel):
    id: int
    checkin: str
    checkout: str
    diarias: int
    valor_diaria: float
    taxa_adm: float
    valor_total: float
    valor_imob: float
    valor_prop: float
    apto_destino: str
    apto_origem: str

    class Config:
        from_attributes = True

class GastoVariavelSchema(BaseModel):
    id: int
    data_pagamento: str
    valor_material: float
    valor_mo: float
    valor_total: float
    descricao: str
    apto: str

    class Config:
        from_attributes = True

class ProprietarioSchema(BaseModel):
    cpf: int
    nome: str
    telefone: int
    email: str

    class Config:
        from_attributes = True
        