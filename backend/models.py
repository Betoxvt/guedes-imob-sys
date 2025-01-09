from sqlalchemy import (
    Column, String, Integer, BigInteger, Numeric, ForeignKey, Date, DateTime, Text
)
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from sqlalchemy.schema import CheckConstraint, UniqueConstraint
from database import Base

# Tabela para registros de aluguéis
class Aluguel(Base):
    __tablename__ = 'alugueis'

    id = Column(Integer, primary_key=True, autoincrement=True)
    checkin = Column(Date, nullable=False)
    checkout = Column(Date, nullable=False)
    diarias = Column(Integer, nullable=False)
    valor_diaria = Column(Numeric(10, 2), nullable=False)
    taxa_adm = Column(Numeric(5, 2), nullable=False)
    valor_total = Column(Numeric(10, 2), nullable=False)
    valor_imob = Column(Numeric(10, 2), nullable=False)
    valor_prop = Column(Numeric(10, 2), nullable=False)
    apartamento_id = Column(Integer, ForeignKey('apartamentos.id'))

    # Relationships
    apartamento = relationship('Apartamento', back_populates='alugueis')

    # Constraints
    __table_args__ = (
        CheckConstraint('taxa_adm >= 0 AND taxa_adm <= 100', name='ck_taxa_adm_range'),
        CheckConstraint('valor_diaria >= 0', name='ck_valor_diaria_nonnegative'),
        CheckConstraint('valor_total >= 0', name='ck_valor_total_nonnegative'),
    )

# Tabela para cadastro de apartamentos
class Apartamento(Base):
    __tablename__ = 'apartamentos'

    id = Column(Integer, primary_key=True, autoincrement=True)
    apartamento = Column(String(10), nullable=False)
    celesc = Column(Integer)
    supergasbras = Column(Integer)
    internet_provedor = Column(Text)
    wifiid = Column(Text)
    wifipass = Column(Text)
    lockpass = Column(Integer)
    edificio_id = Column(Integer, ForeignKey('edificios.id'))
    proprietario_id = Column(Integer, ForeignKey('proprietarios.id'))

    # Relationships
    alugueis = relationship('Aluguel', back_populates='apartamento')
    edificio = relationship('EnderecoEdificio', back_populates='apartamentos')
    proprietario = relationship('Proprietario', back_populates='apartamentos')
    despesas = relationship('Despesa', back_populates='apartamentos')
    gastos = relationship('Gasto', back_populates='apartamentos')
    garagens = relationship('Garagem', back_populates='apartamentos')
    garagens_destino = relationship('Garagem', foreign_keys='Garagem.apto_destino_id', back_populates='apto_destino_obj')
    garagens_origem = relationship('Garagem', foreign_keys='Garagem.apto_origem_id', back_populates='apto_origem_obj')


    # Constraints
    __table_args__ = (
        UniqueConstraint('apartamento', 'edificio_id', name='uq_apartamento_edificio'),
    )
    
# Tabela para registros de despesas fixas
class Despesa(Base):
    __tablename__ = 'despesas'

    id = Column(Integer, primary_key=True, autoincrement=True)
    data_pagamento = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    valor = Column(Numeric(10, 2), nullable=False)
    descricao = Column(Text, nullable=False)
    apartamento_id = Column(Integer, ForeignKey('apartamentos.id'))

    # Relationships
    apartamento = relationship('Apartamento', back_populates='despesas')

# Tabela para cadastro de edifícios
class EnderecoEdificio(Base):
    __tablename__ = 'edificios'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(Text, nullable=False)
    endereco = Column(Text)
    numero = Column(Integer)
    bairro = Column(Text)
    cidade = Column(Text)
    estado = Column(String(2))
    cep = Column(Integer)

    # Relationships
    apartamentos = relationship('Apartamento', back_populates='edificio')

    # Constraints
    __table_args__ = (
        CheckConstraint("char_length(estado) = 2", name="ck_estado_length"),
    )

# Tabela para registro de aluguéis de garagens e controle de vagas
class Garagem(Base):
    __tablename__ = 'garagens'

    id = Column(Integer, primary_key=True, autoincrement=True)
    checkin = Column(Date, nullable=False)
    checkout = Column(Date, nullable=False)
    diarias = Column(Integer, nullable=False)
    valor_diaria = Column(Numeric(10, 2), nullable=False)
    taxa_adm = Column(Numeric(5, 2), nullable=False)
    valor_total = Column(Numeric(10, 2), nullable=False)
    valor_imob = Column(Numeric(10, 2), nullable=False)
    valor_prop = Column(Numeric(10, 2), nullable=False)
    apto_destino_id = Column(Integer, ForeignKey('apartamentos.id'))
    apto_origem_id = Column(Integer, ForeignKey('apartamentos.id'))

    # Relationships
    apto_destino_obj = relationship('Apartamento', foreign_keys=[apto_destino_id], back_populates='garagens_destino')
    apto_origem_obj = relationship('Apartamento', foreign_keys=[apto_origem_id], back_populates='garagens_origem')

# Tabela para registros de gastos variáveis
class Gasto(Base):
    __tablename__ = 'gastos'

    id = Column(Integer, primary_key=True, autoincrement=True)
    data_pagamento = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    valor_material = Column(Numeric(10, 2))
    valor_mo = Column(Numeric(10, 2))
    valor_total = Column(Numeric(10, 2), nullable=False)
    descricao = Column(Text, nullable=False)
    apartamento_id = Column(Integer, ForeignKey('apartamentos.id'))

    # Relationships
    apartamento = relationship('Apartamento', back_populates='gastos')

# Tabela para cadastro dos proprietários (ou responsáveis) dos apartamentos
class Proprietario(Base):
    __tablename__ = 'proprietarios'

    id = Column(Integer, primary_key=True, autoincrement=True)
    cpf = Column(BigInteger, unique=True)
    nome = Column(Text, nullable=False)
    telefone = Column(BigInteger)
    email = Column(Text, unique=True)

    # Relationships
    apartamentos = relationship('Apartamento', back_populates='proprietario')
