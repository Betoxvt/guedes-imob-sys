from datetime import date
from sqlalchemy import ForeignKey, func, Numeric, String, JSON
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class Aluguel(Base):
    __tablename__ = "alugueis"

    id: Mapped[int] = mapped_column(primary_key=True)
    apto_id: Mapped[str] = mapped_column(ForeignKey("apartamentos.id"), nullable=False)
    ficha_id: Mapped[int] = mapped_column(
        ForeignKey("fichas.id"), unique=True, nullable=True
    )
    checkin: Mapped[date] = mapped_column(nullable=False)
    checkout: Mapped[date] = mapped_column(nullable=False)
    diarias: Mapped[int] = mapped_column(nullable=False)
    valor_diaria: Mapped[float] = mapped_column(Numeric(10, 2), nullable=False)
    valor_total: Mapped[float] = mapped_column(Numeric(10, 2), nullable=False)
    nome: Mapped[str] = mapped_column(String, nullable=True)
    contato: Mapped[str] = mapped_column(String, nullable=True)
    criado_em: Mapped[date] = mapped_column(
        server_default=func.current_date(), nullable=False
    )
    modificado_em: Mapped[date] = mapped_column(
        server_default=func.current_date(), onupdate=func.current_date(), nullable=False
    )

    apartamento: Mapped["Apartamento"] = relationship(
        "Apartamento", foreign_keys=[apto_id], back_populates="alugueis"
    )
    ficha: Mapped["Ficha"] = relationship(
        "Ficha",
        foreign_keys="[Ficha.aluguel_id]",
        back_populates="aluguel",
        uselist=False,
    )
    pagamentos: Mapped[list["Pagamento"]] = relationship(back_populates="aluguel")


class Apartamento(Base):
    __tablename__ = "apartamentos"

    id: Mapped[str] = mapped_column(
        String, nullable=False, unique=True, primary_key=True
    )
    proprietario_id: Mapped[int] = mapped_column(
        ForeignKey("proprietarios.id"), nullable=True
    )
    cod_celesc: Mapped[str] = mapped_column(String, nullable=True)
    cod_gas: Mapped[str] = mapped_column(String, nullable=True)
    prov_net: Mapped[str] = mapped_column(String, nullable=True)
    wifi: Mapped[str] = mapped_column(String, nullable=True)
    wifi_senha: Mapped[str] = mapped_column(String, nullable=True)
    lock_senha: Mapped[str] = mapped_column(String, nullable=True)
    cod_imov: Mapped[str] = mapped_column(String, nullable=True)
    dic: Mapped[str] = mapped_column(String, nullable=True)
    ins_imob: Mapped[str] = mapped_column(String, nullable=True)
    matricula: Mapped[str] = mapped_column(String, nullable=True)
    rip: Mapped[str] = mapped_column(String, nullable=True)
    criado_em: Mapped[date] = mapped_column(
        server_default=func.current_date(), nullable=False
    )
    modificado_em: Mapped[date] = mapped_column(
        server_default=func.current_date(), onupdate=func.current_date(), nullable=False
    )

    proprietario: Mapped["Proprietario"] = relationship(
        "Proprietario", foreign_keys=[proprietario_id], back_populates="apartamentos"
    )
    alugueis: Mapped[list["Aluguel"]] = relationship(back_populates="apartamento")
    despesas: Mapped[list["Despesa"]] = relationship(back_populates="apartamento")
    garagens_origem: Mapped[list["Garagem"]] = relationship(
        back_populates="apartamento_origem", foreign_keys="[Garagem.apto_id_origem]"
    )
    garagens_destino: Mapped[list["Garagem"]] = relationship(
        back_populates="apartamento_destino", foreign_keys="[Garagem.apto_id_destino]"
    )
    fichas: Mapped[list["Ficha"]] = relationship(back_populates="apartamento")
    relatorios: Mapped[list["Relatorio"]] = relationship(back_populates="apartamento")


class Caixa(Base):
    __tablename__ = "caixa"

    id: Mapped[int] = mapped_column(primary_key=True)
    moeda: Mapped[str] = mapped_column(String, nullable=False)
    valor: Mapped[float] = mapped_column(Numeric(10, 2), nullable=False)
    criado_em: Mapped[date] = mapped_column(
        server_default=func.current_date(), nullable=False
    )
    modificado_em: Mapped[date] = mapped_column(
        server_default=func.current_date(), onupdate=func.current_date(), nullable=False
    )


class Despesa(Base):
    __tablename__ = "despesas"

    id: Mapped[int] = mapped_column(primary_key=True)
    apto_id: Mapped[str] = mapped_column(ForeignKey("apartamentos.id"), nullable=False)
    data: Mapped[date] = mapped_column(
        server_default=func.current_date(), nullable=False
    )
    valor: Mapped[float] = mapped_column(Numeric(10, 2), nullable=False)
    categoria: Mapped[str] = mapped_column(String, nullable=False)
    descricao: Mapped[str] = mapped_column(String, nullable=True)
    criado_em: Mapped[date] = mapped_column(
        server_default=func.current_date(), nullable=False
    )
    modificado_em: Mapped[date] = mapped_column(
        server_default=func.current_date(), onupdate=func.current_date(), nullable=False
    )

    apartamento: Mapped["Apartamento"] = relationship(back_populates="despesas")


class Ficha(Base):
    __tablename__ = "fichas"

    id: Mapped[int] = mapped_column(primary_key=True)
    apto_id: Mapped[str] = mapped_column(ForeignKey("apartamentos.id"), nullable=True)
    aluguel_id: Mapped[int] = mapped_column(
        ForeignKey("alugueis.id"), unique=True, nullable=True
    )
    nome: Mapped[str] = mapped_column(String, nullable=False)
    tipo_residencia: Mapped[str] = mapped_column(String, nullable=False)
    cidade: Mapped[str] = mapped_column(String, nullable=False)
    cep: Mapped[str] = mapped_column(String, nullable=False)
    uf: Mapped[str] = mapped_column(String, nullable=False)
    pais: Mapped[str] = mapped_column(String, nullable=False)
    tel: Mapped[str] = mapped_column(String, nullable=False)
    estado_civil: Mapped[str] = mapped_column(String, nullable=False)
    profissao: Mapped[str] = mapped_column(String, nullable=False)
    rg: Mapped[str] = mapped_column(String, nullable=False)
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
    a0: Mapped[dict] = mapped_column(JSON, nullable=True)
    a1: Mapped[dict] = mapped_column(JSON, nullable=True)
    a2: Mapped[dict] = mapped_column(JSON, nullable=True)
    a3: Mapped[dict] = mapped_column(JSON, nullable=True)
    a4: Mapped[dict] = mapped_column(JSON, nullable=True)
    a5: Mapped[dict] = mapped_column(JSON, nullable=True)
    a6: Mapped[dict] = mapped_column(JSON, nullable=True)
    a7: Mapped[dict] = mapped_column(JSON, nullable=True)
    a8: Mapped[dict] = mapped_column(JSON, nullable=True)
    a9: Mapped[dict] = mapped_column(JSON, nullable=True)
    criado_em: Mapped[date] = mapped_column(
        server_default=func.current_date(), nullable=False
    )
    modificado_em: Mapped[date] = mapped_column(
        server_default=func.current_date(), onupdate=func.current_date(), nullable=False
    )

    apartamento: Mapped["Apartamento"] = relationship(
        "Apartamento", foreign_keys=[apto_id], back_populates="fichas"
    )
    aluguel: Mapped["Aluguel"] = relationship(
        "Aluguel",
        # remote_side=[aluguel_id],
        foreign_keys=[aluguel_id],
        back_populates="ficha",
    )


class Garagem(Base):
    __tablename__ = "garagens"

    id: Mapped[int] = mapped_column(primary_key=True)
    apto_id_origem: Mapped[str] = mapped_column(
        ForeignKey("apartamentos.id"), nullable=False, name="fk_apto_origem"
    )
    apto_id_destino: Mapped[str] = mapped_column(
        ForeignKey("apartamentos.id"), nullable=False, name="fk_apto_destino"
    )
    checkin: Mapped[date] = mapped_column(nullable=False)
    checkout: Mapped[date] = mapped_column(nullable=False)
    diarias: Mapped[int] = mapped_column(nullable=False)
    valor_diaria: Mapped[float] = mapped_column(Numeric(10, 2), nullable=False)
    valor_total: Mapped[float] = mapped_column(Numeric(10, 2), nullable=False)
    criado_em: Mapped[date] = mapped_column(
        server_default=func.current_date(), nullable=False
    )
    modificado_em: Mapped[date] = mapped_column(
        server_default=func.current_date(), onupdate=func.current_date(), nullable=False
    )

    apartamento_origem: Mapped["Apartamento"] = relationship(
        back_populates="garagens_origem", foreign_keys=[apto_id_origem]
    )
    apartamento_destino: Mapped["Apartamento"] = relationship(
        back_populates="garagens_destino", foreign_keys=[apto_id_destino]
    )


class Pagamento(Base):
    __tablename__ = "pagamentos"

    id: Mapped[int] = mapped_column(primary_key=True)
    tipo: Mapped[str] = mapped_column(String, nullable=False)
    valor: Mapped[float] = mapped_column(Numeric(10, 2), nullable=False)
    aluguel_id: Mapped[int] = mapped_column(ForeignKey("alugueis.id"), nullable=True)
    notas: Mapped[str] = mapped_column(String, nullable=True)
    nome: Mapped[str] = mapped_column(String, nullable=True)
    contato: Mapped[str] = mapped_column(String, nullable=True)
    data: Mapped[date] = mapped_column(
        server_default=func.current_date(), nullable=False
    )
    criado_em: Mapped[date] = mapped_column(
        server_default=func.current_date(), nullable=False
    )
    modificado_em: Mapped[date] = mapped_column(
        server_default=func.current_date(), onupdate=func.current_date(), nullable=False
    )

    aluguel: Mapped["Aluguel"] = relationship(back_populates="pagamentos")


class Proprietario(Base):
    __tablename__ = "proprietarios"

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String, nullable=False)
    cpf: Mapped[str] = mapped_column(String, nullable=True)
    tel: Mapped[str] = mapped_column(String, nullable=True)
    email: Mapped[str] = mapped_column(String, nullable=True)
    criado_em: Mapped[date] = mapped_column(
        server_default=func.current_date(), nullable=False
    )
    modificado_em: Mapped[date] = mapped_column(
        server_default=func.current_date(), onupdate=func.current_date(), nullable=False
    )

    apartamentos: Mapped[list["Apartamento"]] = relationship(
        back_populates="proprietario"
    )


class Relatorio(Base):
    __tablename__ = "relatorios"

    id: Mapped[int] = mapped_column(primary_key=True)
    apto_id: Mapped[str] = mapped_column(ForeignKey("apartamentos.id"), nullable=False)
    data: Mapped[date] = mapped_column(nullable=False)
    valor: Mapped[float] = mapped_column(Numeric(10, 2), nullable=False)
    criado_em: Mapped[date] = mapped_column(
        server_default=func.current_date(), nullable=False
    )
    modificado_em: Mapped[date] = mapped_column(
        server_default=func.current_date(), onupdate=func.current_date(), nullable=False
    )

    apartamento: Mapped["Apartamento"] = relationship(back_populates="relatorios")
