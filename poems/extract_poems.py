import pymongo
from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017/')
poems_beta = client["poems-beta"]
poems = poems_beta["poems"]
with open("qilu.txt", "w") as f:
  for poem in poems.find({"type":"七言律詩"}):
    if(len(poem["content"]) == 64):
      f.write(poem["content"] + "\n")
