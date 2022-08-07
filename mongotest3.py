import pymongo

client = pymongo.MongoClient("mongodb+srv://leosunny:Alstom15a@sunny.ay5bul8.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

database = client['myinfo']
collection = database["sun"]

record = collection.find()



#data = collection.find({"companyName": "iNeuron"})

data = collection.find({"courseOffered":{"$lt":"E"}})
for i in data:
    print(i)