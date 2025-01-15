from datetime import date
from sqlalchemy import CheckConstraint, ForeignKey, func, Numeric, String
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
    criado_em: Mapped[date] = mapped_column(server_default=func.current_date(), nullable=False)
    modificado_em: Mapped[date] = mapped_column(server_default=func.current_date(), onupdate=func.current_date(), nullable=False)


class Apartamento(Base):
    __tablename__ = 'apartamentos'

    id: Mapped[int] = mapped_column(primary_key=True)
    apto = mapped_column(String(5), nullable=False, unique=True)
    proprietario_id: Mapped[int] = mapped_column(ForeignKey('proprietarios.id'), nullable=True)
    cod_celesc = mapped_column(String(20), nullable=True)
    cod_gas = mapped_column(String(20), nullable=True)
    prov_net = mapped_column(String(20), nullable=True)
    wifi = mapped_column(String(20), nullable=True)
    wifi_senha = mapped_column(String(20), nullable=True)
    lock_senha = mapped_column(String(10), nullable=True)
    criado_em: Mapped[date] = mapped_column(server_default=func.current_date(), nullable=False)
    modificado_em: Mapped[date] = mapped_column(server_default=func.current_date(), onupdate=func.current_date(), nullable=False)
    

class Despesa(Base):
    __tablename__ = 'despesas'

    id: Mapped[int] = mapped_column(primary_key=True)
    apto_id: Mapped[int] = mapped_column(ForeignKey('apartamentos.id'), nullable=True)
    data_pagamento: Mapped[date] = mapped_column(server_default=func.current_date(), nullable=False)
    valor: Mapped[float] = mapped_column(Numeric(10, 2), nullable=False)
    descricao = mapped_column(String(200), nullable=False)
    criado_em: Mapped[date] = mapped_column(server_default=func.current_date(), nullable=False)
    modificado_em: Mapped[date] = mapped_column(server_default=func.current_date(), onupdate=func.current_date(), nullable=False)


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
    criado_em: Mapped[date] = mapped_column(server_default=func.current_date(), nullable=False)
    modificado_em: Mapped[date] = mapped_column(server_default=func.current_date(), onupdate=func.current_date(), nullable=False)

    # Constraints
    __table_args__ = (
            CheckConstraint("apto_origem_id != apto_destino_id", name='ck_apto_ids_not_equal'),
        )


class Proprietario(Base):
    __tablename__ = 'proprietarios'

    id: Mapped[int] = mapped_column(primary_key=True)
    nome = mapped_column(String(50), nullable=False)
    cpf = mapped_column(String(14), nullable=True)
    tel = mapped_column(String(20), nullable=True)
    email = mapped_column(String(50), nullable=True)
    criado_em: Mapped[date] = mapped_column(server_default=func.current_date(), nullable=False)
    modificado_em: Mapped[date] = mapped_column(server_default=func.current_date(), onupdate=func.current_date(), nullable=False)


class Ficha(Base):
    __tablename__ = 'fichas'

    id: Mapped[int] = mapped_column(primary_key=True)
    apto = mapped_column(String(5), nullable=False)
    nome = mapped_column(String(50), nullable=False)
    tipo_residencia = mapped_column(String(10), nullable=False)
    cidade = mapped_column(String(50), nullable=False)
    cep = mapped_column(String(9), nullable=False)
    uf = mapped_column(String(2), nullable=False)
    pais = mapped_column(String(10), nullable=False)
    tel = mapped_column(String(20), nullable=False)
    estado_civil = mapped_column(String(10), nullable=False)
    profissao = mapped_column(String(50), nullable=False)
    rg = mapped_column(String(15), nullable=True)
    cpf = mapped_column(String(14), nullable=False)
    mae = mapped_column(String(50), nullable=False)
    automovel = mapped_column(String(16), nullable=True)
    modelo_auto = mapped_column(String(16), nullable=True)
    placa_auto = mapped_column(String(8), nullable=True)
    cor_auto = mapped_column(String(10), nullable=True)
    checkin: Mapped[date] = mapped_column(nullable=False)
    checkout: Mapped[date] = mapped_column(nullable=False)
    observacoes = mapped_column(String(200), nullable=True)
    proprietario = mapped_column(String(50), nullable=True)
    imob_fone = mapped_column(String(20), nullable=True)
    acomp_id = Mapped[int] = mapped_column(ForeignKey('aacompanhantes.id'), nullable=False)
    criado_em: Mapped[date] = mapped_column(server_default=func.current_date(), nullable=False)
    modificado_em: Mapped[date] = mapped_column(server_default=func.current_date(), onupdate=func.current_date(), nullable=False)
    
    # Constraints
    __table_args__ = CheckConstraint("length(uf) = 2", name="ck_uf_length")


class Acompanhantes(Base):
    __tablename__ = 'acompanhantes'

    id: Mapped[int] = mapped_column(primary_key=True)
    ficha_id = Mapped[int] = mapped_column(ForeignKey('fichas.id'), nullable=False)
    for i in range(1, 11):
        locals()[f"acomp_{i:02d}_nome"] = mapped_column(String(50), nullable=True)
        locals()[f"acomp_{i:02d}_rg"] = mapped_column(String(15), nullable=True)
        locals()[f"acomp_{i:02d}_cpf"] = mapped_column(String(14), nullable=True)
        locals()[f"acomp_{i:02d}_idade"] = mapped_column(String(3), nullable=True)
        locals()[f"acomp_{i:02d}_parentesco"] = mapped_column(String(10), nullable=True)
    criado_em: Mapped[date] = mapped_column(server_default=func.current_date(), nullable=False)
    modificado_em: Mapped[date] = mapped_column(server_default=func.current_date(), onupdate=func.current_date(), nullable=False)
