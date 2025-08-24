from typing import Optional
from pydantic import BaseModel #garante que os dados recebidos e enviados pela API estejam no formato correto

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

#definindo esquema para atualização de eventos (tipos de dados)
class EventoUpdate(BaseModel):
    area: Optional[str] = None
    data: Optional[str] = None
    evento: Optional[str] = None
    descricao: Optional[str] = None
    status: Optional[str] = None
    engajamento: Optional[int] = None
