from sqlalchemy import Column, Integer, String, ForeignKey
from app.core.database import Base

class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    owner_id = Column(
        Integer,
        ForeignKey("users.id")
    )