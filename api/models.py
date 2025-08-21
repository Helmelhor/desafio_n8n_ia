from sqlalchemy import Column, Integer, String
from database import Base

#determinando tabela
class Evento(Base):
    __tablename__ = "eventos"

    id = Column(Integer, primary_key=True, index=True)
    area = Column(String, index=True)
    data = Column(String)
    evento = Column(String)
    descricao = Column(String)
    status = Column(String)
    engajamento = Column(Integer)