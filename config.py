import pymongo
import certifi


developer = {
    "first": "Gigi",
    "last": "Bailey",
    "age": "46",
    "email": "tx2vabch@gmail.com",
    "hobbies": ["code", "fishing"],
    "address": {
        "num": "12244",
        "street": "homers",
        "city": "temecula"
    }
}





con_str ="mongodb+srv://tx2vabch:1Qazdr41!@server.dtaoehu.mongodb.net/?retryWrites=true&w=majority"
client = pymongo.MongoClient(con_str, tlsCAFile=certifi.where())
db = client.get_database("gigi")
