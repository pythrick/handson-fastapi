from fastapi import Depends, FastAPI
from pydantic import BaseModel
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from handson_fastapi import service
from handson_fastapi.db.base import get_session
from handson_fastapi.exceptions import DuplicatedEntryError

app = FastAPI()


class CitySchema(BaseModel):
    name: str
    population: int

    class Config:
        orm_mode = True


@app.post("/cities/")
async def add_city(
        city: CitySchema,
        session: AsyncSession = Depends(get_session)
):
    city = service.add_city(session, city.name, city.population)
    try:
        await session.commit()
        return city
    except IntegrityError as exc:
        await session.rollback()
        raise DuplicatedEntryError(
            "This city already exists on database."
        ) from exc


@app.get("/cities/")
async def list_cities(session: AsyncSession = Depends(get_session)):
    cities = await service.get_biggest_cities(session)
    return [CitySchema.from_orm(c) for c in cities]


@app.get("/")
async def index():
    return {"Hello": "World"}
