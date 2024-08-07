from pymongo import MongoClient

client = MongoClient("mongodb+srv://dylandtm4:Dylan404736@anime-api.kaosex9.mongodb.net/?retryWrites=true&w=majority&appName=Anime-API", connectTimeoutMS=10000, socketTimeoutMS=10000)

db = client.anime_db

collection_name = db["anime_collection"]