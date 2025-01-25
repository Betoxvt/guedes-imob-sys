from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker


DATABASE_URL = "postgresql://user:password@db:5432/mydatabase"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


verify_trigger = text(
    """
        SELECT 1
        FROM pg_trigger
        WHERE tgname = 'tr_block_aluguel_conflict';
    """
)


trigger_aluguel = text(
    """
CREATE OR REPLACE FUNCTION check_aluguel_conflict()
RETURNS TRIGGER AS $$
DECLARE
    conflito_id INTEGER;
BEGIN
    SELECT a.id INTO conflito_id
    FROM alugueis a
    WHERE a.apto_id = NEW.apto_id
      AND NOT (a.checkout <= NEW.checkin OR a.checkin >= NEW.checkout);

    IF FOUND THEN
        RAISE EXCEPTION 'Apartamento já reservado para este período. Conflito com o Aluguel ID %.', conflito_id;
    END IF;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER tr_block_aluguel_conflict
BEFORE INSERT ON alugueis
FOR EACH ROW EXECUTE PROCEDURE check_aluguel_conflict();
"""
)
