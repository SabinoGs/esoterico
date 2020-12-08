from pydantic import BaseModel, AnyHttpUrl, EmailStr
from typing import Optional


class UserInModel(BaseModel):
    name: str
    nickname: str
    email: Optional[EmailStr]
    linkedin_profile_url: Optional[AnyHttpUrl]
    github_profile_url: Optional[AnyHttpUrl]
