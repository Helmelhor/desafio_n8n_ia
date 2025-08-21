from pydantic import BaseModel

class EventoBase(BaseModel):
    #campos
    area: str 
    data: str
    evento: str
    descricao: str
    status: str
    engajamento: int

class EventoCreate(EventoBase):
    pass

class Evento(EventoBase):
    id: int

    class Config:
        from_attributes = True