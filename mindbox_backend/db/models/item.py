from sqlalchemy import Column, TEXT
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

from mindbox_backend.db import DeclarativeBase


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
    )
