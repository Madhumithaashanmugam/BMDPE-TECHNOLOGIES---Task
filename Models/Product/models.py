from sqlalchemy import Column, String, Integer, Float, TIMESTAMP, text
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
import uuid
from config.db.session import Base

class Product(Base):
    __tablename__ = "product"
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()), index=True)    
    name = Column(String, nullable=False)
    category = Column(String, nullable=False)
    quantity = Column(Integer, default=0)
    price = Column(Float, nullable=False)
    created_datetime = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    updated_datetime = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("CURRENT_TIMESTAMP"), onupdate=datetime.utcnow)

    @property
    def low_stock(self) -> bool:
        return self.quantity < 10
