from sqlalchemy import Column, Integer, String, Boolean,Date, ForeignKey
from sqlalchemy.orm import relationship
from database.base_db_class import Base


class Post(Base):
    id = Column(Integer,primary_key = True, index=True)
    title = Column(String,nullable= False)
    description = Column(String,nullable=False)
    date_posted = Column(Date)
    owner_id =  Column(Integer,ForeignKey("user.id"))
    owner = relationship("User",back_populates="posts")
    is_active = Column(Boolean, default=True)
