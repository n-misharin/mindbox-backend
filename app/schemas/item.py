from pydantic import BaseModel, UUID4


class ItemSchema(BaseModel):
    id: UUID4
    title: str

    class Config:
        orm_mode = True
