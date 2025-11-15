from pydantic import BaseModel


class OfferWallCreate(BaseModel):
    name: str
    url: str
    description: str | None = None


class OfferWallRead(OfferWallCreate):
    id: int
