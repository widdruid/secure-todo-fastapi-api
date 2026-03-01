from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.todos import TodoCreate, TodoResponse
from app.core.database import get_db
from app.core.security import get_current_user
from app.models.user import User

from app.services.todo_service import (
    create_todo,
    get_all_todos,
    get_todo_by_id,
    update_todo,
    delete_todo,
)

router = APIRouter(
    prefix="/todos",
    tags=["Todos"]
)


@router.post("", response_model=TodoResponse)
def create(
    data: TodoCreate,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):
    return create_todo(db, data.title, user.id)


@router.get("", response_model=list[TodoResponse])
def get_all(
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):
    return get_all_todos(db, user.id)


@router.get("/{todo_id}", response_model=TodoResponse)
def get_by_id(
    todo_id: int,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):
    return get_todo_by_id(db, todo_id, user.id)


@router.put("/{todo_id}", response_model=TodoResponse)
def update(
    todo_id: int,
    data: TodoCreate,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):
    return update_todo(db, todo_id, data.title, user.id)


@router.delete("/{todo_id}")
def delete(
    todo_id: int,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):
    return delete_todo(db, todo_id, user.id)