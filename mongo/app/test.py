import pymongo

client = pymongo.MongoClient("localhost",27017)
db = client.test
print db.name
print db.my_collection

