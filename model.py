from pydantic import BaseModel


class Info(BaseModel):
    user: str
    password: str

