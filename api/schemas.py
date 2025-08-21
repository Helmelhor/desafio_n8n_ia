from pydantic import BaseModel
from datetime import date
from typing import Optional

class EventoBase(BaseModel):
    area: str
    evento: str
    data_inicio: date
    data_fim: date
    responsavel: str

class EventoCreate(EventoBase):
    pass

class Evento(EventoBase):
    id: int

    class Config:
        from_attributes = True