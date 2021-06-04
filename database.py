import pymongo
from pymongo import MongoClient
from model import Info
client = pymongo.MongoClient("mongodb+srv://Leolang:3BXQylG45puUydBx@cluster0.mexdq.mongodb.net/InaTerror?retryWrites=true&w=majority")
db = client.InaTerror
Fantasmas = db.Fantasmas
Users = db.Alpha


def fetch_all():
  userInfo = []
  cursor = Users.find({})
  for document in cursor:
    userInfo.append(Info(**document))
  return userInfo


def create(info):
  document = info
  result = Users.insert_one(document)
  return document


def update(user, password):
  Users.update_one({"user": user}, {"$set": {"password": password}})
  document = Users.find_one({"user": user})
  return document


def fetch_one(user,password):
  document =  Users.find_one({ "user": user, "password": password })
  if document == None:
    return bool(False)
  return document


def remove(user):
  Users.delete_one({"user": user})
  return True

