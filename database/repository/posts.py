from sqlalchemy.orm import Session
from schemas.posts import PostCreate
from database.models.posts import Post

def create_new_post(post: PostCreate, db: Session, owner_id: int):
    post_object = Post(**post.dict(), owner_id=owner_id)
    db.add(post_object)
    db.commit()
    db.refresh(post_object)
    return post_object

def retrieve_post(id: int, db: Session):
    post = db.query(Post).filter(Post.id == id).first()
    return post

def list_posts(db : Session):    #new
    posts = db.query(Post).filter(Post.is_active == True)
    return posts

def update_post_by_id(id: int, post: PostCreate, db: Session, owner_id: int):
    existing_post = db.query(Post).filter(Post.id == id)
    if not existing_post.first():
        return False
    existing_post.update(post.__dict__)
    db.commit()
    return True

def delete_post_by_id(id: int, db: Session, owner_id: int):
    existing_post = db.query(Post).filter(Post.id == id)
    if not existing_post.first():
        return False
    existing_post.delete(synchronize_session=False)
    db.commit()
    return True