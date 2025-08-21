from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

import models
import schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="API de Agendas")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/eventos/", response_model=schemas.Evento)
def create_evento(evento: schemas.EventoCreate, db: Session = Depends(get_db)):
    # Cria um objeto SQLAlchemy a partir dos dados do Pydantic
    db_evento = models.Evento(**evento.model_dump())
    db.add(db_evento)
    db.commit()
    db.refresh(db_evento)
    return db_evento

@app.get("/eventos/", response_model=List[schemas.Evento])
def read_eventos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    eventos = db.query(models.Evento).offset(skip).limit(limit).all()
    return eventos