from sqlalchemy import Column, Integer, String, DateTime
from database.db_setup import Base
from utils.time_utils import current_time

class User(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(50), nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    senha = Column(String)
    criado_em = Column(DateTime, default=current_time)  # Campo de data e hora de criação com valor padrão
    

    # addresses = relationship("Address", back_populates="user")

    def __repr__(self):
        return f"<User(name='{self.nome}', email='{self.email}')>"