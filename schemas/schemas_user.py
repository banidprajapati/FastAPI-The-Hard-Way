from pydantic import BaseModel, EmailStr, Field

# properties required during user creation
class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=4)


# new
class ShowUser(BaseModel):
    id: int
    email: EmailStr
    is_active: bool

    model_config = {"from_attributes": True}
