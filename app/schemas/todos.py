from pydantic import BaseModel

class TodoCreate(BaseModel):
    title: str


class TodoResponse(BaseModel):
    id: int
    title: str

    class Config:
        orm_mode = True