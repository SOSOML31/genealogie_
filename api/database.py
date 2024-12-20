from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Configuration de la base de données PostgreSQL
DATABASE_URL = "postgresql://postgres:931752@localhost:5432/genealogie"

# Création du moteur SQLAlchemy
engine = create_engine(DATABASE_URL)

# Création de la session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)