from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from .database import engine, SessionLocal
from .models import Base, Individu, Relations
from .schemas import IndividuSchema, RelationSchema
from fastapi import FastAPI
from . import models
from .database import engine

# Initialisation de l'application FastAPI
app = FastAPI()

# Création des tables SQLAlchemy
models.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/individus/")
def create_individu(individu: IndividuSchema, db: Session = Depends(get_db)):
    db_individu = Individu(**individu.dict())
    db.add(db_individu)
    try:
        db.commit()
        db.refresh(db_individu)
        return db_individu
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/relations/")
def create_relation(relation: RelationSchema, db: Session = Depends(get_db)):
    db_relation = Relations(**relation.dict())
    db.add(db_relation)
    try:
        db.commit()
        db.refresh(db_relation)
        return db_relation
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))