from datetime import date
from sqlalchemy import CheckConstraint, Date, ForeignKey, func, Numeric, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class Aluguel(Base):
    __tablename__ = 'alugueis'

    id: Mapped[int] = mapped_column(primary_key=True)
    apto_id: Mapped[int] = mapped_column(ForeignKey('apartamentos.id'), nullable=False)
    ficha_id: Mapped[int] = mapped_column(ForeignKey('fichas.id'), nullable=True)
    checkin: Mapped[date] = mapped_column(nullable=False)
    checkout: Mapped[date] = mapped_column(nullable=False)
    diarias: Mapped[int] = mapped_column(nullable=False)
    valor_diaria: Mapped[float] = mapped_column(Numeric(10, 2), nullable=False)
    valor_total: Mapped[float] = mapped_column(Numeric(10, 2), nullable=False)
    criado_em: Mapped[date] = mapped_column(Date, server_default=func.current_date(), nullable=False)
    modificado_em: Mapped[date] = mapped_column(Date, server_default=func.current_date(), onupdate=func.current_date(), nullable=False)


class Apartamento(Base):
    __tablename__ = 'apartamentos'

    id: Mapped[int] = mapped_column(primary_key=True)
    apto: Mapped[str] = mapped_column(String(5), nullable=False, unique=True)
    proprietario_id: Mapped[int] = mapped_column(ForeignKey('proprietarios.id'), nullable=True)
    cod_celesc = Mapped[str] = mapped_column(String(20), nullable=True)
    cod_gas = Mapped[str] = mapped_column(String(20), nullable=True)
    prov_net = Mapped[str] = mapped_column(String(20), nullable=True)
    wifi = Mapped[str] = mapped_column(String(20), nullable=True)
    wifi_senha = Mapped[str] = mapped_column(String(20), nullable=True)
    lock_senha = Mapped[str] = mapped_column(String(10), nullable=True)
    criado_em: Mapped[date] = mapped_column(Date, server_default=func.current_date(), nullable=False)
    modificado_em: Mapped[date] = mapped_column(Date, server_default=func.current_date(), onupdate=func.current_date(), nullable=False)
    

class Despesa(Base):
    __tablename__ = 'despesas'

    id: Mapped[int] = mapped_column(primary_key=True)
    apto_id: Mapped[int] = mapped_column(ForeignKey('apartamentos.id'), nullable=True)
    data_pagamento: Mapped[date] = mapped_column(server_default=func.current_date(), nullable=False)
    valor: Mapped[float] = mapped_column(Numeric(10, 2), nullable=False)
    descricao: Mapped[str] = mapped_column(String(200), nullable=False)
    criado_em: Mapped[date] = mapped_column(Date, server_default=func.current_date(), nullable=False)
    modificado_em: Mapped[date] = mapped_column(Date, server_default=func.current_date(), onupdate=func.current_date(), nullable=False)


class Garagem(Base):
    __tablename__ = 'garagens'

    id: Mapped[int] = mapped_column(primary_key=True)
    apto_origem_id: Mapped[int] = mapped_column(ForeignKey('apartamentos.id'), nullable=False)
    apto_destino_id: Mapped[int] = mapped_column(ForeignKey('apartamentos.id'), nullable=False)
    checkin: Mapped[date] = mapped_column(nullable=False)
    checkout: Mapped[date] = mapped_column(nullable=False)
    diarias: Mapped[int] = mapped_column(nullable=False)
    valor_diaria: Mapped[float] = mapped_column(Numeric(10, 2), nullable=False)
    valor_total: Mapped[float] = mapped_column(Numeric(10, 2), nullable=False)
    criado_em: Mapped[date] = mapped_column(Date, server_default=func.current_date(), nullable=False)
    modificado_em: Mapped[date] = mapped_column(Date, server_default=func.current_date(), onupdate=func.current_date(), nullable=False)

    # Constraints
    __table_args__ = (
            CheckConstraint("apto_origem_id != apto_destino_id", name='ck_apto_ids_not_equal'),
        )


class Proprietario(Base):
    __tablename__ = 'proprietarios'

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(50), nullable=False)
    cpf: Mapped[str] = mapped_column(String(14), nullable=True)
    tel: Mapped[str] = mapped_column(String(20), nullable=True)
    email: Mapped[str] = mapped_column(String(50), nullable=True)
    criado_em: Mapped[date] = mapped_column(Date, server_default=func.current_date(), nullable=False)
    modificado_em: Mapped[date] = mapped_column(Date, server_default=func.current_date(), onupdate=func.current_date(), nullable=False)


class Ficha(Base):
    __tablename__ = 'fichas'

    id: Mapped[int] = mapped_column(primary_key=True)
    apartamento: Mapped[str] = mapped_column(String, nullable=False)
    nome: Mapped[str] = mapped_column(String, nullable=False)
    tipo_residencia: Mapped[str] = mapped_column(String, nullable=False)
    cidade: Mapped[str] = mapped_column(String, nullable=False)
    cep: Mapped[str] = mapped_column(String, nullable=False)
    uf: Mapped[str] = mapped_column(String(2), nullable=False)
    pais: Mapped[str] = mapped_column(String, nullable=False)
    tel: Mapped[str] = mapped_column(String, nullable=False)
    estado_civil: Mapped[str] = mapped_column(String, nullable=False)
    profissao: Mapped[str] = mapped_column(String, nullable=False)
    rg: Mapped[str] = mapped_column(String, nullable=True)
    cpf: Mapped[str] = mapped_column(String, nullable=False)
    mae: Mapped[str] = mapped_column(String, nullable=False)
    automovel: Mapped[str] = mapped_column(String, nullable=True)
    modelo_auto: Mapped[str] = mapped_column(String, nullable=True)
    placa_auto: Mapped[str] = mapped_column(String, nullable=True)
    cor_auto: Mapped[str] = mapped_column(String, nullable=True)
    checkin: Mapped[date] = mapped_column(nullable=False)
    checkout: Mapped[date] = mapped_column(nullable=False)
    observacoes: Mapped[str] = mapped_column(String, nullable=True)
    proprietario: Mapped[str] = mapped_column(String, nullable=True)
    imob_fone: Mapped[str] = mapped_column(String, nullable=True)

    for i in range(1, 11):
        locals()[f"acomp_{i:02d}_nome"] = Mapped[str] = mapped_column(String, nullable=True)
        locals()[f"acomp_{i:02d}_rg"] = Mapped[str] = mapped_column(String, nullable=True)
        locals()[f"acomp_{i:02d}_cpf"] = Mapped[str] = mapped_column(String, nullable=True)
        locals()[f"acomp_{i:02d}_idade"] = Mapped[str] = mapped_column(String, nullable=True)
        locals()[f"acomp_{i:02d}_parentesco"] = Mapped[str] = mapped_column(String, nullable=True)
    criado_em: Mapped[date] = mapped_column(Date, server_default=func.current_date(), nullable=False)
    modificado_em: Mapped[date] = mapped_column(Date, server_default=func.current_date(), onupdate=func.current_date(), nullable=False)

    # Constraints
    __table_args__ = (
        CheckConstraint("length(uf) = 2", name="ck_uf_length"),
    )