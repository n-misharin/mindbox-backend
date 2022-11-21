from sqlalchemy import Column, TEXT, Float, ForeignKey, Table
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from mindbox_backend.db import DeclarativeBase
from mindbox_backend.db.models.item_category import ItemCategory


class Item(DeclarativeBase):
    __tablename__ = "items"
    id = Column(
        "id",
        UUID(as_uuid=True),
        primary_key=True,
        server_default=func.gen_random_uuid(),
    )
    title = Column(
        "title",
        TEXT,
        nullable=False,
        index=True,
        unique=True,
    )
    cost = Column(
        "cost",
        Float,
        nullable=False,
    )
    categories = relationship(
        "Category",
        secondary="items_categories",
        backref="item",
        lazy="selectin",
        viewonly=True,
    )
