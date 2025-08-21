from sqlalchemy import Column, Integer, String, Date
from database import Base

class Evento(Base):
    __tablename__ = "eventos"

    id = Column(Integer, primary_key=True, index=True)
    area = Column(String, index=True) # RH, Marketing ou IA
    evento = Column(String)
    data_inicio = Column(Date)
    data_fim = Column(Date)
    responsavel = Column(String)