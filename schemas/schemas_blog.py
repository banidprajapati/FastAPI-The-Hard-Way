from typing import Optional
from pydantic import BaseModel, root_validator
from datetime import datetime


class CreateBlog(BaseModel):
    title: str
    slug: Optional[str] = None
    content: Optional[str] = None

    @root_validator(pre=True)
    def generate_slug(cls, values):
        if "title" in values and not values.get("slug"):
            values["slug"] = values["title"].replace(" ", "-").lower()
        return values


class ShowBlog(BaseModel):
    title: str
    content: Optional[str]
    created_at: datetime

    model_config = {"from_attributes": True}


class UpdateBlog(CreateBlog):
    pass
