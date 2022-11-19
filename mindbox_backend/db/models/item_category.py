from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from mindbox_backend.db import DeclarativeBase


class ItemCategory(DeclarativeBase):
    __tablename__ = "items_categories"

    id = Column(
        "id",
        Integer,
        primary_key=True,
        autoincrement=True,
    )

    item_id = Column(
        "item_id",
        UUID(as_uuid=True),
        ForeignKey("items.id", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
    )

    category_id = Column(
        "category_id",
        UUID(as_uuid=True),
        ForeignKey("categories.id", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
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
