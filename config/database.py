from pymongo import MongoClient

client = MongoClient("mongodb+srv://dylandtm4:Dylan404736@anime-api.kaosex9.mongodb.net/?retryWrites=true&w=majority&appName=Anime-API", connectTimeoutMS=10000, socketTimeoutMS=10000)

db = client.anime_db

anime_collection = db["animes"]
genre_collection = db["genres"]

# Dropping the 'animes' collection to fix corrupted api data
# anime_collection.drop()

# Dropping the 'genres' collection to fix corrupted api data
# genre_collection.drop()