from fastapi import APIRouter, status, HTTPException
from sqlalchemy.orm import Session
from fastapi import Depends

from db.session import get_db
from schemas.schemas_blog import ShowBlog, CreateBlog, UpdateBlog
from backend.db.repository.repository_blog import (
    create_new_blog,
    retreive_blog,
    list_blogs,
)
from backend.db.repository.repository_blog import update_blog, delete_blog

from typing import List


router = APIRouter()


@router.post("/blogs", response_model=ShowBlog, status_code=status.HTTP_201_CREATED)
def create_blog(blog: CreateBlog, db: Session = Depends(get_db)):
    blog = create_new_blog(blog=blog, db=db, author_id=1)
    return blog


@router.get("/blog/{id}", response_model=ShowBlog)
def get_blog(id: int, db: Session = Depends(get_db)):
    blog = retreive_blog(id=id, db=db)
    if not blog:
        raise HTTPException(
            detail=f"Blog with ID {id} does not exist.",
            status_code=status.HTTP_404_NOT_FOUND,
        )
    return blog


@router.get("/blogs", response_model=List[ShowBlog])
def get_all_blogs(db: Session = Depends(get_db)):
    blogs = list_blogs(db=db)
    return blogs


@router.put("/blog/{id}", response_model=ShowBlog)
def update_a_blog(id: int, blog: UpdateBlog, db: Session = Depends(get_db)):
    blog = update_blog(id=id, blog=blog, author_id=1, db=db)
    if not blog:
        raise HTTPException(detail=f"Blog with id {id} does not exist")
    return blog


@router.delete("/blog/{id}", response_model=ShowBlog)
def delete_a_blog(id: int, db: Session = Depends(get_db)):
    message = delete_blog(id=id, author_id=1, db=db)
    if message.get("error"):
        raise HTTPException(
            detail=message.get("error"), status_code=status.HTTP_400_BAD_REQUEST
        )
    return {"msg": f"Successfully deleted blog with id {id}"}
