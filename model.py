from pydantic import BaseModel


class Info(BaseModel):
    user: str
    password: str

    class Config:
        orm_mode = True

class GhostInfo(BaseModel):
    lat: str
    lon: str
    time: str

    class Config:
        orm_mode = True

