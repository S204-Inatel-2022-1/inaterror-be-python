from fastapi import FastAPI, HTTPException
from typing import Optional, List
from model import Info
from database import (
    create,
    fetch_all,
    update,
    fetch_one,
    remove,
)
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/info")
def get_info():
    response =  fetch_all()
    return response


@app.post("/api/info/", response_model=Info)
def post_info(info: Info):
    response =  create(info.dict())
    if response:
        return response
    raise HTTPException(400, "Erro")


@app.put("/api/info/{user}/", response_model=Info)
def put_info(user: str, password: str):
    response = update(user, password)
    if response:
        return response
    raise HTTPException(404, f" {user}not found")


@app.get("/api/info/{user}", response_model=Info)
def get_info_by_title(user):
    response =  fetch_one(user)
    if response:
        return response
    raise HTTPException(404, f"There is no info with the title {user}")


@app.delete("/api/info/{user}")
def delete_info(user):
    response =  remove(user)
    if response:
        return "Successfully deleted info"
    raise HTTPException(404, f"There is no info with the title {user}")