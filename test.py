import certifi
from pymongo import MongoClient
from urllib.parse import quote_plus

username = quote_plus('hamedsedaghatgit83')
password = quote_plus('Hitlerwashero2050')

# MongoDB bağlantı dizesini oluştur
MONGO_URI = f"mongodb+srv://{username}:{password}@cluster0.kpry90i.mongodb.net/?retryWrites=true&w=majority"


client = MongoClient(
    MONGO_URI,
    tlsCAFile=certifi.where()
)