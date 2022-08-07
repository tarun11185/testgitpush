import pymongo
client = pymongo.MongoClient("mongodb+srv://leosunny:Alstom15a@sunny.ay5bul8.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)


d = {
    "name":"leo",
    "email":"tarun@gmail.com",
    "surname": "united"
}