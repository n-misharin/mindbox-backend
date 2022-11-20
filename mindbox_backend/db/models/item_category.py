from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from mindbox_backend.db import DeclarativeBase


class ItemCategory(DeclarativeBase):
    __tablename__ = "items_categories"

    item_id = Column(
        "item_id",
        UUID(as_uuid=True),
        ForeignKey("items.id", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
        primary_key=True,
        index=True,
    )

    category_id = Column(
        "category_id",
        UUID(as_uuid=True),
        ForeignKey("categories.id", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
        primary_key=True,
        index=True,
    )
    item = relationship(
        "Item",
        backref="item_category",
        lazy="selectin",
    )
    category = relationship(
        "Category",
        backref="category_item",
        lazy="selectin",
    )
