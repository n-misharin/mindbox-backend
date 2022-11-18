from uuid import UUID

from sqlalchemy import select, update, delete
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.ext.asyncio import AsyncSession

from mindbox_backend.db.models import Item


async def get_item_by_id(session: AsyncSession, item_id: UUID) -> Item:
    query = select(Item).where(Item.id == item_id)
    item = await session.scalar(query)
    return item


async def insert_item(session: AsyncSession, title: str, cost: float) -> Item:
    query = insert(Item).values(title=title, cost=cost).returning(Item)
    item = await session.execute(query)
    await session.commit()
    return item.first()


async def update_item(session: AsyncSession, item_id: UUID, values: dict) -> Item:
    query = update(Item).where(Item.id == item_id).values(**values).returning(Item)
    item = await session.execute(query)
    await session.commit()
    return item.first()


async def delete_item_by_id(session: AsyncSession, item_id: UUID):
    query = delete(Item).where(Item.id == item_id)
    await session.execute(query)
    await session.commit()
