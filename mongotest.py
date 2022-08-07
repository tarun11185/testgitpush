import pymongo
client = pymongo.MongoClient("mongodb+srv://leosunny:Alstom15a@sunny.ay5bul8.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)


d = {
    "name":"tarun",
    "email":"sunny@gmail.com",
    "surname": "kumar"
}

db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)
