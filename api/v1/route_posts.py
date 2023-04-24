from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status
from database.session import get_db
from database.models.posts import Post
from schemas.posts import PostCreate, ShowPost
from database.repository.posts import create_new_post, retrieve_post, list_posts, update_post_by_id, delete_post_by_id
from typing import List

router = APIRouter()

@router.post("/create-post/", response_model=ShowPost)
def create_post(post: PostCreate, db: Session = Depends(get_db)):
    owner_id = 1
    post = create_new_post(post=post, db=db, owner_id=owner_id)
    return post

@router.get("/get/{id}", response_model=ShowPost)
def read_post(id: int, db: Session = Depends(get_db)):
    post = retrieve_post(id=id, db=db)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Post with the id {id} is not available")
    return post

@router.get("/all", response_model=List[ShowPost])
def read_posts(db: Session = Depends(get_db)):
    posts = db.query(Post).filter(Post.is_active == True).all()
    return [ShowPost.from_orm(post) for post in posts]

@router.put("/update/{id}")
def update_post(id: int, post: PostCreate, db: Session = Depends(get_db)):
    owner_id = 1
    message = update_post_by_id(id=id, post=post, db=db, owner_id=owner_id)
    if not message:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Post with the id {id} is not available")
    return {"msg": "Successfully updated data."}

@router.delete("/delete/{id}")
def delete_post(id: int, db: Session = Depends(get_db)):
    owner_id = 1
    message = delete_post_by_id(id=id, db=db, owner_id=owner_id)
    if not message:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Post with the id {id} is not available")
    return {"msg": "Successfully deleted data."}