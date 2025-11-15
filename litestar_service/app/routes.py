from litestar import Router, get, post, put, delete
from sqlalchemy.future import select
from app.db import async_session
from app.models import OfferWall
from app.schemas import OfferWallRead, OfferWallCreate


@get("/offerwalls", tags=["OfferWalls"])
async def list_offerwalls() -> list[OfferWallRead]:
    async with async_session() as session:
        result = await session.execute(select(OfferWall))
        offers = result.scalars().all()
        return [OfferWallRead.from_orm(o) for o in offers]


@get("/offerwalls/{offer_id:int}", tags=["OfferWalls"])
async def get_offerwall(offer_id: int) -> OfferWallRead:
    async with async_session() as session:
        result = await session.execute(select(OfferWall).filter_by(id=offer_id))
        offer = result.scalar_one_or_none()
        if not offer:
            raise ValueError("Offer not found")
        return OfferWallRead.from_orm(offer)


@post("/offerwalls", tags=["OfferWalls"])
async def create_offerwall(data: OfferWallCreate) -> OfferWallRead:
    async with async_session() as session:
        offer = OfferWall(**data.dict())
        session.add(offer)
        await session.commit()
        await session.refresh(offer)
        return OfferWallRead.from_orm(offer)


@put("/offerwalls/{offer_id:int}", tags=["OfferWalls"])
async def update_offerwall(offer_id: int, data: OfferWallCreate) -> OfferWallRead:
    async with async_session() as session:
        result = await session.execute(select(OfferWall).filter_by(id=offer_id))
        offer = result.scalar_one_or_none()
        if not offer:
            raise ValueError("Offer not found")
        for k, v in data.dict().items():
            setattr(offer, k, v)
        await session.commit()
        await session.refresh(offer)
        return OfferWallRead.from_orm(offer)


@delete("/offerwalls/{offer_id:int}", tags=["OfferWalls"], status_code=200)
async def delete_offerwall(offer_id: int) -> dict:
    async with async_session() as session:
        result = await session.execute(select(OfferWall).filter_by(id=offer_id))
        offer = result.scalar_one_or_none()
        if not offer:
            raise ValueError("Offer not found")
        await session.delete(offer)
        await session.commit()
        return {"status": "deleted"}


router = Router(path="/api", route_handlers=[list_offerwalls, get_offerwall, create_offerwall, update_offerwall, delete_offerwall])
