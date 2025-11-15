from sqlalchemy import Column, Integer, String
from app.db import Base


class OfferWall(Base):
    __tablename__ = "offer_walls"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    url = Column(String, nullable=False)
    description = Column(String, nullable=True)
