from sqlalchemy import (
    Column, String, Integer, BigInteger, Numeric, ForeignKey, Date, Text,
    CheckConstraint, UniqueConstraint,
    func
)
from database import Base

DEFAULT_TAXA_ADM = 0.15
DEFAULT_EDIFICIO_ID = 1


class Aluguel(Base):
    __tablename__ = 'alugueis'

    id = Column(Integer, primary_key=True)
    apartamento_id = Column(Integer, ForeignKey('apartamentos.id'), nullable=False)
    checkin = Column(Date(), nullable=False)
    checkout = Column(Date(), nullable=False)
    diarias = Column(Integer, nullable=False)
    valor_diaria = Column(Numeric(10, 2), nullable=False)
    taxa_adm = Column(Numeric(5, 2), server_default=DEFAULT_TAXA_ADM, nullable=False)
    valor_total = Column(Numeric(10, 2), nullable=False)
    valor_imob = Column(Numeric(10, 2), nullable=False)
    valor_prop = Column(Numeric(10, 2), nullable=False)
    criado_em = Column(Date(), server_default=func.now(), nullable=False)
    modificado_em = Column(Date(), server_default=func.now(), onupdate=func.now(), nullable=False)

    # Constraints
    __table_args__ = (
        CheckConstraint('taxa_adm >= 0 AND taxa_adm <= 1', name='check_taxa_adm_range'),
        CheckConstraint('valor_diaria >= 0', name='check_valor_diaria_nonnegative'),
        CheckConstraint('valor_total >= 0', name='check_valor_total_nonnegative'),
    )

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if 'diarias' not in kwargs:
            self.diarias = (self.checkout - self.checkin).days
        if 'valor_total' not in kwargs:
            self.valor_total = self.diarias * self.valor_diaria
        if 'valor_imob' not in kwargs:
            self.valor_imob = self.valor_total * self.taxa_adm
        if 'valor_prop' not in kwargs:
            self.valor_prop = self.valor_total - self.valor_imob


class Apartamento(Base):
    __tablename__ = 'apartamentos'

    id = Column(Integer, primary_key=True)
    apartamento = Column(String(10), nullable=False)
    edificio_id = Column(Integer, ForeignKey('edificios.id'),server_default=DEFAULT_EDIFICIO_ID, nullable=False)
    proprietario_id = Column(Integer, ForeignKey('proprietarios.id'), nullable=False)
    celesc = Column(Integer)
    supergasbras = Column(Integer)
    internet_provedor = Column(Text)
    wifiid = Column(Text)
    wifipass = Column(Text)
    lockpass = Column(Integer)
    criado_em = Column(Date(), server_default=func.now(), nullable=False)
    modificado_em = Column(Date(), server_default=func.now(), onupdate=func.now(), nullable=False)

    # Constraints
    __table_args__ = (
        UniqueConstraint('apartamento', 'edificio_id', name='unique_apartamento_edificio'),
    )
    

class Despesa(Base):
    __tablename__ = 'despesas'

    id = Column(Integer, primary_key=True)
    apartamento_id = Column(Integer, ForeignKey('apartamentos.id'))
    data_pagamento = Column(Date(), server_default=func.now(), nullable=False)
    valor = Column(Numeric(10, 2), nullable=False)
    descricao = Column(Text, nullable=False)
    criado_em = Column(Date(), server_default=func.now(), nullable=False)
    modificado_em = Column(Date(), server_default=func.now(), onupdate=func.now(), nullable=False)


class Edificio(Base):
    __tablename__ = 'edificios'

    id = Column(Integer, primary_key=True)
    nome = Column(Text, nullable=False)
    logradouro = Column(Text)
    numero = Column(Integer)
    bairro = Column(Text)
    cidade = Column(Text)
    uf = Column(String(2))
    pais = Column(Text)
    cep = Column(Integer)
    criado_em = Column(Date(), server_default=func.now(), nullable=False)
    modificado_em = Column(Date(), server_default=func.now(), onupdate=func.now(), nullable=False)

    # Constraints
    __table_args__ = (
        CheckConstraint("char_length(uf) = 2", name="check_uf_length"),
    )


class Garagem(Base):
    __tablename__ = 'garagens'

    id = Column(Integer, primary_key=True)
    apto_origem_id = Column(Integer, ForeignKey('apartamentos.id'), nullable=False)
    apto_destino_id = Column(Integer, ForeignKey('apartamentos.id'), nullable=False)
    checkin = Column(Date(), nullable=False)
    checkout = Column(Date(), nullable=False)
    diarias = Column(Integer, nullable=False)
    valor_diaria = Column(Numeric(10, 2), nullable=False)
    taxa_adm = Column(Numeric(5, 2), nullable=False)
    valor_total = Column(Numeric(10, 2), nullable=False)
    valor_imob = Column(Numeric(10, 2), nullable=False)
    valor_prop = Column(Numeric(10, 2), nullable=False)
    criado_em = Column(Date(), server_default=func.now(), nullable=False)
    modificado_em = Column(Date(), server_default=func.now(), onupdate=func.now(), nullable=False)

    # Constraints
    __table_args__ = (
            CheckConstraint('apto_origem_id != apto_destino_id', name='check_apto_ids_not_equal'),
        )
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if 'diarias' not in kwargs:
            self.diarias = (self.checkout - self.checkin).days
        if 'valor_total' not in kwargs:
            self.valor_total = self.diarias * self.valor_diaria
        if 'valor_imob' not in kwargs:
            self.valor_imob = self.valor_total * self.taxa_adm
        if 'valor_prop' not in kwargs:
            self.valor_prop = self.valor_total - self.valor_imob


class Gasto(Base):
    __tablename__ = 'gastos'

    id = Column(Integer, primary_key=True)
    apartamento_id = Column(Integer, ForeignKey('apartamentos.id'), nullable=False)
    data_pagamento = Column(Date(), server_default=func.now(), nullable=False)
    valor_material = Column(Numeric(10, 2))
    valor_mo = Column(Numeric(10, 2))
    valor_total = Column(Numeric(10, 2), nullable=False)
    descricao = Column(Text, nullable=False)
    criado_em = Column(Date(), server_default=func.now(), nullable=False)
    modificado_em = Column(Date(), server_default=func.now(), onupdate=func.now(), nullable=False)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if 'valor_total' not in kwargs:
            self.valor_total = (self.valor_material + self.valor_mo)


class Proprietario(Base):
    __tablename__ = 'proprietarios'

    id = Column(Integer, primary_key=True)
    nome = Column(Text, nullable=False)
    cpf = Column(BigInteger, unique=True)
    telefone = Column(BigInteger, unique=True)
    email = Column(Text, unique=True)
    criado_em = Column(Date(), server_default=func.now(), nullable=False)
    modificado_em = Column(Date(), server_default=func.now(), onupdate=func.now(), nullable=False)
