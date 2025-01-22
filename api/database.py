from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


DATABASE_URL = "postgresql://user:password@postgres/mydatabase"

# Connect to the database
engine = create_engine(DATABASE_URL)

# Create a session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a base class
Base = declarative_base()


# Manage the database conections
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
