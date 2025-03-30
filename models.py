from pydantic import BaseModel, EmailStr
from typing import Optional

class User(BaseModel):
    username: str
    email: EmailStr
    password: str
    city: str
    state: str
    country: str
    

class Disaster(BaseModel):
    country: str
    description: str
    severity: str
    date: str
