from pydantic import BaseModel


class Info(BaseModel):
    user: str
    password: str

    class Config:
        orm_mode = True

class GhostInfo(BaseModel):
    id: int
    lat: str
    lon: str
    time: str

    class Config:
        orm_mode = True