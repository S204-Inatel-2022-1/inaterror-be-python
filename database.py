import pymongo
from pymongo import MongoClient
from model import Info
client = pymongo.MongoClient("mongodb+srv://Leolang:3BXQylG45puUydBx@cluster0.mexdq.mongodb.net/InaTerror?retryWrites=true&w=majority")
db = client.InaTerror
Fantasmas = db.Fantasmas
Users = db.Users


async def fetch_all():
  userInfo = []
  cursor = Users.find({})
  async for document in cursor:
    userInfo.append(Info(**document))
  return userInfo


async def create(info):
  document = info
  result = await Users.insert_one(document)
  return document


async def update(user, password):
  await Users.update_one({"user": user}, {"$set": {"password": password}})
  document = await Users.find_one({"user": user})
  return document



async def fetch_one(user):
  document = await Users.find_one({"user": user})
  return document


async def remove(user):
  await Users.delete_one({"user": user})
  return True
