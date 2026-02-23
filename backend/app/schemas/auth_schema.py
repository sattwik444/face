from pydantic import BaseModel, EmailStr

class RegisterRequest(BaseModel):
    email: EmailStr
    password: str
    username: str
    class_name: str

class LoginRequest(BaseModel):
    email: EmailStr
    password: str
