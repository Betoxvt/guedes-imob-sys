from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Configurando o Banco de Dados
DATABASE_URL = "postgresql:///usuario:senha@localhost/imob"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()