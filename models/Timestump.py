from sqlalchemy import Column, DateTime, func
from db.db_base import Base

# Modelo da tabela de times_tump
class Timestump:
    __tablename__ = "times_tump"
    created_at = Column(DateTime(timezone=True), server_default=func.now()) 
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
