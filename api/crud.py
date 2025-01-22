from models import (
    Aluguel,
    Apartamento,
    Despesa,
    Ficha,
    Garagem,
    Pagamento,
    Proprietario,
)
from schemas import (
    AluguelCreate,
    AluguelUpdate,
    ApartamentoCreate,
    ApartamentoUpdate,
    DespesaCreate,
    DespesaUpdate,
    FichaCreate,
    FichaUpdate,
    GaragemCreate,
    GaragemUpdate,
    PagamentoCreate,
    PagamentoUpdate,
    ProprietarioCreate,
    ProprietarioUpdate,
)
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
from typing import List


def create_aluguel(db: Session, aluguel: AluguelCreate) -> Aluguel:
    """
    Creates a new aluguel record in the database.

    This function takes an `AluguelCreate` object containing the new aluguel data
    and persists it to the database.

    Args:
        db (Session): A SQLAlchemy session to interact with the database.
        aluguel (AluguelCreate): An object containing the new aluguel data.

    Returns:
        Aluguel: The newly created aluguel object.

    Raises:
        SQLAlchemyError: If an error occurs during the creation.
    """
    try:
        db_aluguel = Aluguel(**aluguel.model_dump())
        db.add(db_aluguel)
        db.commit()
        db.refresh(db_aluguel)
        return db_aluguel
    except SQLAlchemyError as e:
        print(f"Erro ao registrar aluguel: {e}")
        db.rollback()
        raise e


def read_alugueis(db: Session, offset: int = 0, limit: int = 100) -> List[Aluguel]:
    """
    Retrieves alugueis from the database with pagination.

    This function queries the 'alugueis' table in the database and returns the records,
    ordered by ID in descending order. It allows pagination of the results through
    the `offset` and `limit` parameters.

    Args:
        db (Session): A SQLAlchemy session to interact with the database.
        offset (int, optional): The starting index of the results. Defaults to 0.
        limit (int, optional): The maximum number of results to be returned. Defaults to 100.

    Returns:
        List[Aluguel]: A list of `Aluguel` objects from the database.

    Raises:
        SQLAlchemyError: If an error occurs during the database query.
    """
    try:
        return (
            db.query(Aluguel)
            .order_by(Aluguel.id.desc())
            .offset(offset)
            .limit(limit)
            .all()
        )
    except SQLAlchemyError as e:
        print(f"Erro ao buscar aluguéis: {e}")
        raise e


def read_aluguel(db: Session, aluguel_id: int) -> Aluguel:
    """
    Retrieves a specific aluguel from the database.

    This function queries the database for a aluguel with the given ID.

    Args:
        db (Session): A SQLAlchemy session to interact with the database.
        aluguel_id (int): The ID of the aluguel to retrieve.

    Returns:
        Aluguel: The aluguel object with the specified ID.

    Raises:
        SQLAlchemyError: If an error occurs during the query.
    """
    try:
        return db.query(Aluguel).filter(Aluguel.id == aluguel_id).first()
    except SQLAlchemyError as e:
        print(f"Erro ao buscar aluguel: {e}")
        raise e


def update_aluguel(db: Session, aluguel_id: int, aluguel: AluguelCreate) -> Aluguel:
    """
    Updates an existing aluguel in the database.

    This function takes the aluguel ID and an `AluguelUpdate` object containing the new
    data, and updates the corresponding record in the database.

    Args:
        db (Session): A SQLAlchemy session to interact with the database.
        aluguel_id (int): The ID of the aluguel to be updated.
        aluguel (AluguelUpdate): An object containing the updated aluguel data.

    Returns:
        Aluguel: The updated aluguel object.

    Raises:
        SQLAlchemyError: If an error occurs during the update.
    """
    try:
        db_aluguel = db.query(Aluguel).filter(Aluguel.id == aluguel_id).first()
        if db_aluguel is None:
            return None

        db.query(Aluguel).filter(Aluguel.id == aluguel_id).update(aluguel.model_dump())
        db.commit()
        db.refresh(db_aluguel)
        return db_aluguel
    except SQLAlchemyError as e:
        print(f"Erro ao atualizar aluguel: {e}")
        db.rollback()
        raise e


def patch_aluguel(db: Session, aluguel_id: int, aluguel: AluguelUpdate) -> Aluguel:
    """
    Updates specific elements from an existing aluguel in the database.

    This function takes the aluguel ID and an `AluguelUpdate` object containing the new
    data, and updates the corresponding record in the database.

    Args:
        db (Session): SQLAlchemy database session.
        aluguel_id (int): ID of the aluguel record to update.
        aluguel (AluguelUpdate): Data to update.

    Returns:
        Aluguel: The updated aluguel record.
    """
    try:
        db_aluguel = db.query(Aluguel).filter(Aluguel.id == aluguel_id).first()
        if db_aluguel is None:
            return None

        for key, value in aluguel.model_dump(exclude_unset=True).items():
            setattr(db_aluguel, key, value)
        db.commit()
        db.refresh(db_aluguel)
        return db_aluguel
    except SQLAlchemyError as e:
        print(f"Erro ao atualizar aluguel: {e}")
        db.rollback()
        raise e


def delete_aluguel(db: Session, aluguel_id: int) -> Aluguel:
    """
    Deletes a aluguel from the database.

    This function deletes the aluguel with the given ID from the database.

    Args:
        db (Session): A SQLAlchemy session to interact with the database.
        aluguel_id (int): The ID of the aluguel to be deleted.

    Returns:
        Aluguel: The deleted aluguel record.

    Raises:
        SQLAlchemyError: If an error occurs during the deletion.
    """
    try:
        db_aluguel = db.query(Aluguel).filter(Aluguel.id == aluguel_id).first()
        db.delete(db_aluguel)
        db.commit()
        return db_aluguel
    except SQLAlchemyError as e:
        print(f"Erro ao deletar aluguel: {e}")
        db.rollback()
        raise e


def create_apartamento(db: Session, apartamento: ApartamentoCreate) -> Apartamento:
    """
    Creates a new element in database table apartamentos
    """
    try:
        db_apartamento = Apartamento(**apartamento.model_dump())
        db.add(db_apartamento)
        db.commit()
        db.refresh(db_apartamento)
        return db_apartamento
    except SQLAlchemyError as e:
        print(f"Erro ao registrar apartamento: {e}")
        db.rollback()
        raise e


def read_apartamentos(db: Session, offset: int = 0, limit: int = 100):
    """
    Returns all elements from database table apartamentos
    """
    try:
        return (
            db.query(Apartamento)
            .order_by(Apartamento.id.desc())
            .offset(offset)
            .limit(limit)
            .all()
        )
    except SQLAlchemyError as e:
        print(f"Erro ao buscar apartamentos: {e}")
        raise e


def read_apartamento(db: Session, apartamento_id: int):
    """
    Returns a specific element from database table apartamentos
    """
    try:
        return db.query(Apartamento).filter(Apartamento.id == apartamento_id).first()
    except SQLAlchemyError as e:
        print(f"Erro ao buscar apartamento: {e}")
        raise e


def update_apartamento(
    db: Session, apartamento_id: int, apartamento: ApartamentoCreate
):
    """
    Updates all elements from database table apartamentos
    """
    try:
        db_apartamento = (
            db.query(Apartamento).filter(Apartamento.id == apartamento_id).first()
        )
        if db_apartamento is None:
            return None

        db.query(Apartamento).filter(Apartamento.id == apartamento_id).update(
            apartamento.model_dump()
        )
        db.commit()
        db.refresh(db_apartamento)
        return db_apartamento
    except SQLAlchemyError as e:
        print(f"Erro ao atualizar apartamento: {e}")
        db.rollback()
        return e


def patch_apartamento(db: Session, apartamento_id: int, apartamento: ApartamentoUpdate):
    """
    Updates a specific element from database table apartamentos

    Args:
        db (Session): SQLAlchemy database session.
        apartamento_id (int): ID of the apartamento record to update.
        apartamento (ApartamentoUpdate): Data to update.

    Returns:
        Apartamento: The updated apartamento record.
    """
    try:
        db_apartamento = (
            db.query(Apartamento).filter(Apartamento.id == apartamento_id).first()
        )
        if db_apartamento is None:
            return None

        for key, value in apartamento.model_dump(exclude_unset=True).items():
            setattr(db_apartamento, key, value)
        db.commit()
        db.refresh(db_apartamento)
        return db_apartamento
    except SQLAlchemyError as e:
        print(f"Erro ao atualizar apartamento: {e}")
        db.rollback()
        raise e


def delete_apartamento(db: Session, apartamento_id: int):
    """
    Deletes a specific element from database table apartamentos
    """
    try:
        db_apartamento = (
            db.query(Apartamento).filter(Apartamento.id == apartamento_id).first()
        )
        db.delete(db_apartamento)
        db.commit()
        return db_apartamento
    except SQLAlchemyError as e:
        print(f"Erro ao deletar apartamento: {e}")
        db.rollback()
        raise e


def create_despesa(db: Session, despesa: DespesaCreate) -> Despesa:
    """
    Creates a new element in database table despesas
    """
    try:
        db_despesa = Despesa(**despesa.model_dump())
        db.add(db_despesa)
        db.commit()
        db.refresh(db_despesa)
        return db_despesa
    except SQLAlchemyError as e:
        print(f"Erro ao registrar despesa: {e}")
        db.rollback()
        raise e


def read_despesas(db: Session, offset: int = 0, limit: int = 100):
    """
    Returns all elements from database table despesas
    """
    try:
        return (
            db.query(Despesa)
            .order_by(Despesa.id.desc())
            .offset(offset)
            .limit(limit)
            .all()
        )
    except SQLAlchemyError as e:
        print(f"Erro ao buscar despesas: {e}")
        raise e


def read_despesa(db: Session, despesa_id: int):
    """
    Returns a specific element from database table despesas
    """
    try:
        return db.query(Despesa).filter(Despesa.id == despesa_id).first()
    except SQLAlchemyError as e:
        print(f"Erro ao buscar despesa: {e}")
        raise e


def update_despesa(db: Session, despesa_id: int, despesa: DespesaCreate):
    """
    Updates all elements from database table despesas
    """
    try:
        db_despesa = db.query(Despesa).filter(Despesa.id == despesa_id).first()
        if db_despesa is None:
            return None

        db.query(Despesa).filter(Despesa.id == despesa_id).update(despesa.model_dump())
        db.commit()
        db.refresh(db_despesa)
        return db_despesa
    except SQLAlchemyError as e:
        print(f"Erro ao atualizar despesa: {e}")
        db.rollback()
        return e


def patch_despesa(db: Session, despesa_id: int, despesa: DespesaUpdate):
    """
    Updates a specific element from database table despesas

    Args:
        db (Session): SQLAlchemy database session.
        despesa_id (int): ID of the despesa record to update.
        despesa (DespesaUpdate): Data to update.

    Returns:
        Despesa: The updated despesa record.
    """
    try:
        db_despesa = db.query(Despesa).filter(Despesa.id == despesa_id).first()
        if db_despesa is None:
            return None

        for key, value in despesa.model_dump(exclude_unset=True).items():
            setattr(db_despesa, key, value)
        db.commit()
        db.refresh(db_despesa)
        return db_despesa
    except SQLAlchemyError as e:
        print(f"Erro ao atualizar despesa: {e}")
        db.rollback()
        raise e


def delete_despesa(db: Session, despesa_id: int):
    """
    Deletes a specific element from database table despesas
    """
    try:
        db_despesa = db.query(Despesa).filter(Despesa.id == despesa_id).first()
        db.delete(db_despesa)
        db.commit()
        return db_despesa
    except SQLAlchemyError as e:
        print(f"Erro ao deletar despesa: {e}")
        db.rollback()
        raise e


def create_garagem(db: Session, garagem: GaragemCreate) -> Garagem:
    """
    Creates a new element in database table garagens
    """
    try:
        db_garagem = Garagem(**garagem.model_dump())
        db.add(db_garagem)
        db.commit()
        db.refresh(db_garagem)
        return db_garagem
    except SQLAlchemyError as e:
        print(f"Erro ao registrar garagem: {e}")
        db.rollback()
        raise e


def read_garagens(db: Session, offset: int = 0, limit: int = 100):
    """
    Returns all elements from database table garagens
    """
    try:
        return (
            db.query(Garagem)
            .order_by(Garagem.id.desc())
            .offset(offset)
            .limit(limit)
            .all()
        )
    except SQLAlchemyError as e:
        print(f"Erro ao buscar garagens: {e}")
        raise e


def read_garagem(db: Session, garagem_id: int):
    """
    Returns a specific element from database table garagens
    """
    try:
        return db.query(Garagem).filter(Garagem.id == garagem_id).first()
    except SQLAlchemyError as e:
        print(f"Erro ao buscar garagem: {e}")
        raise e


def update_garagem(db: Session, garagem_id: int, garagem: GaragemCreate):
    """
    Updates all elements from database table garagens
    """
    try:
        db_garagem = db.query(Garagem).filter(Garagem.id == garagem_id).first()
        if db_garagem is None:
            return None

        db.query(Garagem).filter(Garagem.id == garagem_id).update(garagem.model_dump())
        db.commit()
        db.refresh(db_garagem)
        return db_garagem
    except SQLAlchemyError as e:
        print(f"Erro ao atualizar garagem: {e}")
        db.rollback()
        return e


def patch_garagem(db: Session, garagem_id: int, garagem: GaragemUpdate):
    """
    Updates a specific element from database table garagens

    Args:
        db (Session): SQLAlchemy database session.
        garagem_id (int): ID of the garagem record to update.
        garagem (GaragemUpdate): Data to update.

    Returns:
        Garagem: The updated garagem record.
    """
    try:
        db_garagem = db.query(Garagem).filter(Garagem.id == garagem_id).first()
        if db_garagem is None:
            return None

        for key, value in garagem.model_dump(exclude_unset=True).items():
            setattr(db_garagem, key, value)
        db.commit()
        db.refresh(db_garagem)
        return db_garagem
    except SQLAlchemyError as e:
        print(f"Erro ao atualizar garagem: {e}")
        db.rollback()
        raise e


def delete_garagem(db: Session, garagem_id: int):
    """
    Deletes a specific element from database table garagens
    """
    try:
        db_garagem = db.query(Garagem).filter(Garagem.id == garagem_id).first()
        db.delete(db_garagem)
        db.commit()
        return db_garagem
    except SQLAlchemyError as e:
        print(f"Erro ao deletar garagem: {e}")
        db.rollback()
        raise e


def create_proprietario(db: Session, proprietario: ProprietarioCreate) -> Proprietario:
    """
    Creates a new element in database table proprietarios
    """
    try:
        db_proprietario = Proprietario(**proprietario.model_dump())
        db.add(db_proprietario)
        db.commit()
        db.refresh(db_proprietario)
        return db_proprietario
    except SQLAlchemyError as e:
        print(f"Erro ao registrar proprietario: {e}")
        db.rollback()
        raise e


def read_proprietarios(db: Session, offset: int = 0, limit: int = 100):
    """
    Returns all elements from database table proprietarios
    """
    try:
        return (
            db.query(Proprietario)
            .order_by(Proprietario.id.desc())
            .offset(offset)
            .limit(limit)
            .all()
        )
    except SQLAlchemyError as e:
        print(f"Erro ao buscar proprietarios: {e}")
        raise e


def read_proprietario(db: Session, proprietario_id: int):
    """
    Returns a specific element from database table proprietarios
    """
    try:
        return db.query(Proprietario).filter(Proprietario.id == proprietario_id).first()
    except SQLAlchemyError as e:
        print(f"Erro ao buscar proprietario: {e}")
        raise e


def update_proprietario(
    db: Session, proprietario_id: int, proprietario: ProprietarioCreate
):
    """
    Updates all elements from database table proprietarios
    """
    try:
        db_proprietario = (
            db.query(Proprietario).filter(Proprietario.id == proprietario_id).first()
        )
        if db_proprietario is None:
            return None

        db.query(Proprietario).filter(Proprietario.id == proprietario_id).update(
            proprietario.model_dump()
        )
        db.commit()
        db.refresh(db_proprietario)
        return db_proprietario
    except SQLAlchemyError as e:
        print(f"Erro ao atualizar proprietario: {e}")
        db.rollback()
        raise e


def patch_proprietario(
    db: Session, proprietario_id: int, proprietario: ProprietarioUpdate
):
    """
    Updates a specific element from database table proprietarios

    Args:
        db (Session): SQLAlchemy database session.
        proprietario_id (int): ID of the proprietario record to update.
        proprietario (ProprietarioUpdate): Data to update.

    Returns:
        Proprietario: The updated proprietario record.
    """
    try:
        db_proprietario = (
            db.query(Proprietario).filter(Proprietario.id == proprietario_id).first()
        )
        if db_proprietario is None:
            return None

        proprietario_patch = proprietario.model_dump(exclude_unset=True)
        for key, value in proprietario_patch.items():
            setattr(db_proprietario, key, value)
        db.commit()
        db.refresh(db_proprietario)
        return db_proprietario
    except SQLAlchemyError as e:
        print(f"Erro ao atualizar proprietario: {e}")
        db.rollback()
        raise e


def delete_proprietario(db: Session, proprietario_id: int):
    """
    Deletes a specific element from database table proprietario
    """
    try:
        db_proprietario = (
            db.query(Proprietario).filter(Proprietario.id == proprietario_id).first()
        )
        db.delete(db_proprietario)
        db.commit()
        return db_proprietario
    except SQLAlchemyError as e:
        print(f"Erro ao deletar proprietario: {e}")
        db.rollback()
        raise e


def create_ficha(db: Session, ficha: FichaCreate) -> Ficha:
    """
    Creates a new element in database table fichas
    """
    try:
        db_ficha = Ficha(**ficha.model_dump())
        db.add(db_ficha)
        db.commit()
        db.refresh(db_ficha)
        return db_ficha
    except SQLAlchemyError as e:
        print(f"Erro ao registrar ficha: {e}")
        db.rollback()
        raise e


def read_fichas(db: Session, offset: int = 0, limit: int = 100):
    """
    Returns all elements from database table fichas
    """
    try:
        return (
            db.query(Ficha).order_by(Ficha.id.desc()).offset(offset).limit(limit).all()
        )
    except SQLAlchemyError as e:
        print(f"Erro ao buscar fichas: {e}")
        raise e


def read_ficha(db: Session, ficha_id: int):
    """
    Returns a specific element from database table fichas
    """
    try:
        return db.query(Ficha).filter(Ficha.id == ficha_id).first()
    except SQLAlchemyError as e:
        print(f"Erro ao buscar ficha: {e}")
        raise e


def update_ficha(db: Session, ficha_id: int, ficha: FichaCreate):
    """
    Updates all elements from database table fichas

    """
    try:
        db_ficha = db.query(Ficha).filter(Ficha.id == ficha_id).first()
        if db_ficha is None:
            return None

        db.query(Ficha).filter(Ficha.id == ficha_id).update(ficha.model_dump())
        db.commit()
        db.refresh(db_ficha)
        return db_ficha
    except SQLAlchemyError as e:
        print(f"Erro ao atualizar ficha: {e}")
        db.rollback()
        return e


def patch_ficha(db: Session, ficha_id: int, ficha: FichaUpdate):
    """
    Updates a specific element from database table fichas

    Args:
        db (Session): SQLAlchemy database session.
        ficha_id (int): ID of the ficha record to update.
        ficha (FichaUpdate): Data to update.

    Returns:
        Ficha: The updated ficha record.
    """
    try:
        db_ficha = db.query(Ficha).filter(Ficha.id == ficha_id).first()
        if db_ficha is None:
            return None

        for key, value in ficha.model_dump(exclude_unset=True).items():
            setattr(db_ficha, key, value)
        db.commit()
        db.refresh(db_ficha)
        return db_ficha
    except SQLAlchemyError as e:
        print(f"Erro ao atualizar ficha: {e}")
        db.rollback()
        raise e


def delete_ficha(db: Session, ficha_id: int):
    """
    Deletes a specific element from database table fichas
    """
    try:
        db_ficha = db.query(Ficha).filter(Ficha.id == ficha_id).first()
        db.delete(db_ficha)
        db.commit()
        return db_ficha
    except SQLAlchemyError as e:
        print(f"Erro ao deletar ficha: {e}")
        db.rollback()
        raise e


def create_pagamento(db: Session, pagamento: PagamentoCreate) -> Pagamento:
    """
    Creates a new pagamento record in the database.

    This function takes an `PagamentoCreate` object containing the new pagamento data
    and persists it to the database.

    Args:
        db (Session): A SQLAlchemy session to interact with the database.
        pagamento (PagamentoCreate): An object containing the new pagamento data.

    Returns:
        Pagamento: The newly created pagamento object.

    Raises:
        SQLAlchemyError: If an error occurs during the creation.
    """
    try:
        db_pagamento = Pagamento(**pagamento.model_dump())
        db.add(db_pagamento)
        db.commit()
        db.refresh(db_pagamento)
        return db_pagamento
    except SQLAlchemyError as e:
        print(f"Erro ao registrar pagamento: {e}")
        db.rollback()
        raise e


def read_pagamentos(db: Session, offset: int = 0, limit: int = 100) -> List[Pagamento]:
    """
    Retrieves pagamentos from the database with pagination.

    This function queries the 'pagamentos' table in the database and returns the records,
    ordered by ID in descending order. It allows pagination of the results through
    the `offset` and `limit` parameters.

    Args:
        db (Session): A SQLAlchemy session to interact with the database.
        offset (int, optional): The starting index of the results. Defaults to 0.
        limit (int, optional): The maximum number of results to be returned. Defaults to 100.

    Returns:
        List[Pagamento]: A list of `Pagamento` objects from the database.

    Raises:
        SQLAlchemyError: If an error occurs during the database query.
    """
    try:
        return (
            db.query(Pagamento)
            .order_by(Pagamento.id.desc())
            .offset(offset)
            .limit(limit)
            .all()
        )
    except SQLAlchemyError as e:
        print(f"Erro ao buscar aluguéis: {e}")
        raise e


def read_pagamento(db: Session, pagamento_id: int) -> Pagamento:
    """
    Retrieves a specific pagamento from the database.

    This function queries the database for a pagamento with the given ID.

    Args:
        db (Session): A SQLAlchemy session to interact with the database.
        pagamento_id (int): The ID of the pagamento to retrieve.

    Returns:
        Pagamento: The pagamento object with the specified ID.

    Raises:
        SQLAlchemyError: If an error occurs during the query.
    """
    try:
        return db.query(Pagamento).filter(Pagamento.id == pagamento_id).first()
    except SQLAlchemyError as e:
        print(f"Erro ao buscar pagamento: {e}")
        raise e


def update_pagamento(
    db: Session, pagamento_id: int, pagamento: PagamentoCreate
) -> Pagamento:
    """
    Updates an existing pagamento in the database.

    This function takes the pagamento ID and an `PagamentoUpdate` object containing the new
    data, and updates the corresponding record in the database.

    Args:
        db (Session): A SQLAlchemy session to interact with the database.
        pagamento_id (int): The ID of the pagamento to be updated.
        pagamento (PagamentoUpdate): An object containing the updated pagamento data.

    Returns:
        Pagamento: The updated pagamento object.

    Raises:
        SQLAlchemyError: If an error occurs during the update.
    """
    try:
        db_pagamento = db.query(Pagamento).filter(Pagamento.id == pagamento_id).first()
        if db_pagamento is None:
            return None

        db.query(Pagamento).filter(Pagamento.id == pagamento_id).update(
            pagamento.model_dump()
        )
        db.commit()
        db.refresh(db_pagamento)
        return db_pagamento
    except SQLAlchemyError as e:
        print(f"Erro ao atualizar pagamento: {e}")
        db.rollback()
        raise e


def patch_pagamento(
    db: Session, pagamento_id: int, pagamento: PagamentoUpdate
) -> Pagamento:
    """
    Updates specific elements from an existing pagamento in the database.

    This function takes the pagamento ID and an `PagamentoUpdate` object containing the new
    data, and updates the corresponding record in the database.

    Args:
        db (Session): SQLAlchemy database session.
        pagamento_id (int): ID of the pagamento record to update.
        pagamento (PagamentoUpdate): Data to update.

    Returns:
        Pagamento: The updated pagamento record.
    """
    try:
        db_pagamento = db.query(Pagamento).filter(Pagamento.id == pagamento_id).first()
        if db_pagamento is None:
            return None

        for key, value in pagamento.model_dump(exclude_unset=True).items():
            setattr(db_pagamento, key, value)
        db.commit()
        db.refresh(db_pagamento)
        return db_pagamento
    except SQLAlchemyError as e:
        print(f"Erro ao atualizar pagamento: {e}")
        db.rollback()
        raise e


def delete_pagamento(db: Session, pagamento_id: int) -> Pagamento:
    """
    Deletes a pagamento from the database.

    This function deletes the pagamento with the given ID from the database.

    Args:
        db (Session): A SQLAlchemy session to interact with the database.
        pagamento_id (int): The ID of the pagamento to be deleted.

    Returns:
        Pagamento: The deleted pagamento record.

    Raises:
        SQLAlchemyError: If an error occurs during the deletion.
    """
    try:
        db_pagamento = db.query(Pagamento).filter(Pagamento.id == pagamento_id).first()
        db.delete(db_pagamento)
        db.commit()
        return db_pagamento
    except SQLAlchemyError as e:
        print(f"Erro ao deletar pagamento: {e}")
        db.rollback()
        raise e
