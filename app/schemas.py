
from pydantic import BaseModel, EmailStr, Field
from typing import Annotated
from datetime import datetime
from typing import Optional


class Post_Base(BaseModel):
    title : str
    content : str
    published: bool = True

class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode = True

class Post_Created(Post_Base):
    pass

class Post(Post_Base):
    id : int
    created_at : datetime
    owner_id : int
    owner:UserOut
    class Config:
        orm_mode = True

class PostOut(BaseModel):
    Post:Post
    vote:int
    class Config:
        orm_mode = True
        
class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token : str
    token_type : str

class TokenData(BaseModel):
    id : Optional[int] = None

class Vote(BaseModel):
    post_id : int
    dir : Annotated[int, Field(ge=0, le=1)]
