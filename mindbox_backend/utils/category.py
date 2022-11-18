from uuid import UUID

from sqlalchemy import select, update, delete
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.ext.asyncio import AsyncSession

from mindbox_backend.db.models import Category


async def get_category_by_id(session: AsyncSession, item_id: UUID) -> Category:
    query = select(Category).where(Category.id == item_id)
    category = await session.scalar(query)
    return category


async def insert_category(session: AsyncSession, title: str) -> Category:
    query = insert(Category).values(title=title).returning(Category)
    category = await session.execute(query)
    await session.commit()
    return category.first()


async def update_category(session: AsyncSession, category_id: UUID, values: dict) -> Category:
    query = update(Category).where(Category.id == category_id).values(values).returning(Category)
    category = await session.execute(query)
    await session.commit()
    return category.first()


async def delete_category_by_id(session: AsyncSession, item_id: UUID):
    query = delete(Category).where(Category.id == item_id)
    await session.execute(query)
    await session.commit()
