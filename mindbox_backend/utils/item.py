from uuid import UUID

from sqlalchemy import select, update, delete
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.ext.asyncio import AsyncSession

from mindbox_backend.db.models import Item, ItemCategory


async def get_item_by_id(session: AsyncSession, item_id: UUID) -> Item:
    query = select(Item).where(Item.id == item_id)
    item = await session.scalar(query)
    return item


async def insert_item(
        session: AsyncSession,
        title: str,
        cost: float,
        categories_ids: list[UUID] | None = None,
) -> Item:
    item = Item(title=title, cost=cost)
    session.add(item)
    await session.commit()
    await session.refresh(item)
    if categories_ids is not None:
        ins_values = []
        for _id in categories_ids:
            ins_values.append({
                "category_id": _id,
                "item_id": item.id
            })
        query = insert(ItemCategory).values(ins_values)
        await session.execute(query)
    return item


async def update_item(session: AsyncSession, item_id: UUID, values: dict) -> Item:
    query = update(Item).where(Item.id == item_id).values(**values).returning(Item)
    item = await session.execute(query)
    await session.commit()
    return item.first()


async def delete_item_by_id(session: AsyncSession, item_id: UUID):
    query = delete(Item).where(Item.id == item_id)
    await session.execute(query)
    await session.commit()
