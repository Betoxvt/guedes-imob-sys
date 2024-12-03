from sqlalchemy import (
    Column, String, Integer, BigInteger, Numeric, ForeignKey, Date, DateTime, Text
)
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from db import Base

# Tabela alugueis
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
    apto = Column(String(10), ForeignKey('apartamentos.apartamento'))

    apartamento = relationship("Apartamento", back_populates="aluguel_rel")

# Tabela apartamentos
class Apartamento(Base):
    __tablename__ = 'apartamentos'

    apartamento = Column(String(10), primary_key=True)
    edificio = Column(Text, nullable=False)
    endereco = Column(Text, nullable=False)
    celesc = Column(Integer)
    supergasbras = Column(Integer)
    internet = Column(Text)
    wifiid = Column(Text)
    wifipass = Column(Text)
    lockpass = Column(Integer)
    proprietario = Column(BigInteger, ForeignKey('proprietarios.cpf'))
    
    proprietario_rel = relationship("Proprietario", back_populates="apartamentos")
    aluguels = relationship("Aluguel", back_populates="apartamento")
    despesas_fixas = relationship("DespesaFixa", back_populates="apartamento")
    gastos_variaveis = relationship("GastoVariavel", back_populates="apartamento")
    garagens_destino = relationship("Garagem", foreign_keys="[Garagem.apto_destino]")
    garagens_origem = relationship("Garagem", foreign_keys="[Garagem.apto_origem]")

# Tabela despesas_fixas
class DespesaFixa(Base):
    __tablename__ = 'despesas_fixas'

    id = Column(Integer, primary_key=True, autoincrement=True)
    data_pagamento = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    valor = Column(Numeric(10, 2), nullable=False)
    descricao = Column(Text, nullable=False)
    apto = Column(String(10), ForeignKey('apartamentos.apartamento'))

    apartamento = relationship("Apartamento", back_populates="despesas_fixas")

# Tabela garagens
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
    apto_destino = Column(String(10), ForeignKey('apartamentos.apartamento'))
    apto_origem = Column(String(10), ForeignKey('apartamentos.apartamento'))

# Tabela gastos_variaveis
class GastoVariavel(Base):
    __tablename__ = 'gastos_variaveis'

    id = Column(Integer, primary_key=True, autoincrement=True)
    data_pagamento = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    valor_material = Column(Numeric(10, 2))
    valor_mo = Column(Numeric(10, 2))
    valor_total = Column(Numeric(10, 2), nullable=False)
    descricao = Column(Text, nullable=False)
    apto = Column(String(10), ForeignKey('apartamentos.apartamento'))

    apartamento = relationship("Apartamento", back_populates="gastos_variaveis")

# Tabela proprietarios
class Proprietario(Base):
    __tablename__ = 'proprietarios'

    cpf = Column(BigInteger, primary_key=True)
    nome = Column(Text, nullable=False)
    telefone = Column(BigInteger)
    email = Column(Text)

    apartamentos = relationship("Apartamento", back_populates="proprietario_rel")
