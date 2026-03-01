from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.todo import Todo


def create_todo(
    db: Session,
    title: str,
    user_id: int
):

    todo = Todo(
        title=title,
        owner_id=user_id
    )

    db.add(todo)
    db.commit()
    db.refresh(todo)

    return todo


def get_all_todos(
    db: Session,
    user_id: int
):

    return db.query(Todo)\
        .filter(Todo.owner_id == user_id)\
        .all()


def get_todo_by_id(
    db: Session,
    todo_id: int,
    user_id: int
):

    todo = db.query(Todo)\
        .filter(
            Todo.id == todo_id,
            Todo.owner_id == user_id
        )\
        .first()

    if not todo:
        raise HTTPException(
            status_code=404,
            detail="Todo not found"
        )

    return todo


def update_todo(
    db: Session,
    todo_id: int,
    title: str,
    user_id: int
):

    todo = get_todo_by_id(
        db,
        todo_id,
        user_id
    )

    todo.title = title

    db.commit()
    db.refresh(todo)

    return todo


def delete_todo(
    db: Session,
    todo_id: int,
    user_id: int
):

    todo = get_todo_by_id(
        db,
        todo_id,
        user_id
    )

    db.delete(todo)
    db.commit()

    return {"message": "Deleted"}