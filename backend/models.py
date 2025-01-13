from sqlalchemy import (
    Column, String, Integer, Numeric, ForeignKey, Text,
    CheckConstraint, UniqueConstraint,
    func
)
from database import Base


class Aluguel(Base):
    __tablename__ = 'alugueis'

    id = Column(Integer, primary_key=True)
    apartamento_id = Column(Integer, ForeignKey('apartamentos.id'), nullable=False)
    ficha_id = Column(Integer, ForeignKey('fichas.id'))
    checkin = Column(Text, nullable=False)
    checkout = Column(Text, nullable=False)
    diarias = Column(Integer, nullable=False)
    valor_diaria = Column(Numeric(10, 2))
    taxa_adm = Column(Numeric(5, 2), nullable=False)
    valor_total = Column(Numeric(10, 2), nullable=False)
    valor_imob = Column(Numeric(10, 2), nullable=False)
    valor_prop = Column(Numeric(10, 2), nullable=False)
    criado_em = Column(Text, server_default=func.now(), nullable=False)
    modificado_em = Column(Text, server_default=func.now(), onupdate=func.now(), nullable=False)

    # Constraints
    __table_args__ = (
        CheckConstraint('taxa_adm >= 0 AND taxa_adm <= 1', name='check_taxa_adm_range'),
        CheckConstraint('valor_diaria >= 0', name='check_valor_diaria_nonnegative'),
        CheckConstraint('valor_total >= 0', name='check_valor_total_nonnegative'),
    )


class Apartamento(Base):
    __tablename__ = 'apartamentos'

    id = Column(Integer, primary_key=True)
    apartamento = Column(Text, nullable=False)
    edificio_id = Column(Integer, ForeignKey('edificios.id'), nullable=False)
    proprietario_id = Column(Integer, ForeignKey('proprietarios.id'), nullable=False)
    celesc = Column(Text)
    supergasbras = Column(Text)
    internet_provedor = Column(Text)
    wifiid = Column(Text)
    wifipass = Column(Text)
    lockpass = Column(Text)
    criado_em = Column(Text, server_default=func.now(), nullable=False)
    modificado_em = Column(Text, server_default=func.now(), onupdate=func.now(), nullable=False)

    # Constraints
    __table_args__ = (
        UniqueConstraint('apartamento', 'edificio_id', name='unique_apartamento_edificio'),
    )
    

class Despesa(Base):
    __tablename__ = 'despesas'

    id = Column(Integer, primary_key=True)
    apartamento_id = Column(Integer, ForeignKey('apartamentos.id'), nullable=False)
    data_pagamento = Column(Text, server_default=func.now(), nullable=False)
    valor = Column(Numeric(10, 2), nullable=False)
    descricao = Column(Text, nullable=False)
    criado_em = Column(Text, server_default=func.now(), nullable=False)
    modificado_em = Column(Text, server_default=func.now(), onupdate=func.now(), nullable=False)


class Edificio(Base):
    __tablename__ = 'edificios'

    id = Column(Integer, primary_key=True)
    nome = Column(Text, nullable=False)
    logradouro = Column(Text)
    numero = Column(Integer)
    bairro = Column(Text)
    cidade = Column(Text)
    uf = Column(Text)
    pais = Column(Text)
    cep = Column(Text)
    criado_em = Column(Text, server_default=func.now(), nullable=False)
    modificado_em = Column(Text, server_default=func.now(), onupdate=func.now(), nullable=False)

    # Constraints
    __table_args__ = (
        CheckConstraint("char_length(uf) = 2", name="check_uf_length"),
    )


class Garagem(Base):
    __tablename__ = 'garagens'

    id = Column(Integer, primary_key=True)
    apto_origem_id = Column(Integer, ForeignKey('apartamentos.id'), nullable=False)
    apto_destino_id = Column(Integer, ForeignKey('apartamentos.id'), nullable=False)
    checkin = Column(Text, nullable=False)
    checkout = Column(Text, nullable=False)
    diarias = Column(Integer, nullable=False)
    valor_diaria = Column(Numeric(10, 2))
    taxa_adm = Column(Numeric(5, 2), nullable=False)
    valor_total = Column(Numeric(10, 2), nullable=False)
    valor_imob = Column(Numeric(10, 2), nullable=False)
    valor_prop = Column(Numeric(10, 2), nullable=False)
    criado_em = Column(Text, server_default=func.now(), nullable=False)
    modificado_em = Column(Text, server_default=func.now(), onupdate=func.now(), nullable=False)

    # Constraints
    __table_args__ = (
            CheckConstraint('apto_origem_id != apto_destino_id', name='check_apto_ids_not_equal'),
        )


class Gasto(Base):
    __tablename__ = 'gastos'

    id = Column(Integer, primary_key=True)
    apartamento_id = Column(Integer, ForeignKey('apartamentos.id'), nullable=False)
    data_pagamento = Column(Text, server_default=func.now(), nullable=False)
    valor_material = Column(Numeric(10, 2))
    valor_mo = Column(Numeric(10, 2))
    valor_total = Column(Numeric(10, 2), nullable=False)
    descricao = Column(Text, nullable=False)
    criado_em = Column(Text, server_default=func.now(), nullable=False)
    modificado_em = Column(Text, server_default=func.now(), onupdate=func.now(), nullable=False)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if 'valor_total' not in kwargs:
            self.valor_total = (self.valor_material + self.valor_mo)


class Proprietario(Base):
    __tablename__ = 'proprietarios'

    id = Column(Integer, primary_key=True)
    nome = Column(Text, nullable=False)
    cpf = Column(Text)
    telefone = Column(Text)
    email = Column(Text)
    criado_em = Column(Text, server_default=func.now(), nullable=False)
    modificado_em = Column(Text, server_default=func.now(), onupdate=func.now(), nullable=False)


class Ficha(Base):
    __tablename__ = 'fichas'

    id = Column(Integer, primary_key=True)
    apartamento = Column(Text, nullable=False)
    nome = Column(Text, nullable=False)
    tipo_residencia = Column(Text, nullable=False)
    cidade = Column(Text, nullable=False)
    cep = Column(Text, nullable=False)
    estado = Column(Text, nullable=False)
    pais = Column(Text, nullable=False)
    telefone = Column(Text, nullable=False)
    estado_civil = Column(Text, nullable=False)
    profissao = Column(Text, nullable=False)
    rg = Column(Text)
    cpf = Column(Text, nullable=False)
    mae = Column(Text, nullable=False)
    automovel = Column(Text)
    modelo_auto = Column(Text)
    placa_auto = Column(Text)
    cor_auto = Column(Text)
    checkin = Column(Text, nullable=False)
    checkout = Column(Text, nullable=False)
    observacoes = Column(Text)
    proprietario = Column(Text)
    imob_fone = Column(Text)
    acomp_01_nome = Column(Text)
    acomp_01_rg = Column(Text)
    acomp_01_cpf = Column(Text)
    acomp_01_idade = Column(Text)
    acomp_01_parentesco = Column(Text)
    acomp_02_nome = Column(Text)
    acomp_02_rg = Column(Text)
    acomp_02_cpf = Column(Text)
    acomp_02_idade = Column(Text)
    acomp_02_parentesco = Column(Text)
    acomp_03_nome = Column(Text)
    acomp_03_rg = Column(Text)
    acomp_03_cpf = Column(Text)
    acomp_03_idade = Column(Text)
    acomp_03_parentesco = Column(Text)
    acomp_04_nome = Column(Text)
    acomp_04_rg = Column(Text)
    acomp_04_cpf = Column(Text)
    acomp_04_idade = Column(Text)
    acomp_04_parentesco = Column(Text)
    acomp_05_nome = Column(Text)
    acomp_05_rg = Column(Text)
    acomp_05_cpf = Column(Text)
    acomp_05_idade = Column(Text)
    acomp_05_parentesco = Column(Text)
    acomp_06_nome = Column(Text)
    acomp_06_rg = Column(Text)
    acomp_06_cpf = Column(Text)
    acomp_06_idade = Column(Text)
    acomp_06_parentesco = Column(Text)
    acomp_07_nome = Column(Text)
    acomp_07_rg = Column(Text)
    acomp_07_cpf = Column(Text)
    acomp_07_idade = Column(Text)
    acomp_07_parentesco = Column(Text)
    acomp_08_nome = Column(Text)
    acomp_08_rg = Column(Text)
    acomp_08_cpf = Column(Text)
    acomp_08_idade = Column(Text)
    acomp_08_parentesco = Column(Text)
    acomp_09_nome = Column(Text)
    acomp_09_rg = Column(Text)
    acomp_09_cpf = Column(Text)
    acomp_09_idade = Column(Text)
    acomp_09_parentesco = Column(Text)
    acomp_10_nome = Column(Text)
    acomp_10_rg = Column(Text)
    acomp_10_cpf = Column(Text)
    acomp_10_idade = Column(Text)
    acomp_10_parentesco = Column(Text)
    criado_em = Column(Text, server_default=func.now(), nullable=False)
    modificado_em = Column(Text, server_default=func.now(), onupdate=func.now(), nullable=False)

    # Constraints
    __table_args__ = (
        CheckConstraint("char_length(estado) = 2", name="check_estado_length"),
    )