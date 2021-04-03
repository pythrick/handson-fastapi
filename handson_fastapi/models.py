from sqlalchemy import Column, Integer, String

from handson_fastapi.db.base import Base


class City(Base):
    __tablename__ = "cities"

    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    name = Column(String, unique=True)
    population = Column(Integer)
