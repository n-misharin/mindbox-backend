from sqlalchemy import Column, TEXT, Table, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from mindbox_backend.db import DeclarativeBase
from mindbox_backend.db.models.item_category import ItemCategory


class Category(DeclarativeBase):
    __tablename__ = "categories"

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
    )
    items = relationship(
        "Item",
        secondary="items_categories",
        backref="category",
        lazy="selectin",
        viewonly=True,
    )

