from typing import Optional
from pydantic import BaseModel
from datetime import datetime, date

class PostBase(BaseModel):
    title: str
    description: str
    date_posted: Optional[date] = datetime.now().date()

class PostCreate(PostBase):
    title: str
    description: str

class ShowPost(PostBase):
    title: str
    description: Optional[str]
    date_posted: date

    class Config():
        orm_mode = True
