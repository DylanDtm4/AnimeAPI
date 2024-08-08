from typing import List, Optional
from fastapi import APIRouter, Depends, Query
from models.models import Anime, Genre
from config.database import anime_collection, genre_collection
from schema.schemas import list_serial_animes, list_serial_genres
from bson import ObjectId
from utils.util import parse_genres

router = APIRouter()

# GET Request Method
@router.get("/")
async def root():
    return {"Hello": "World"}

# GET Request Method
@router.get("/animes")
async def get_animes(
    genres: Optional[List[int]] = Depends(parse_genres),
    page: int = Query(1, gt=0),
    size: int = Query(25, gt=0, le=100)
):
    animes = list(anime_collection.find()) 
    result = list_serial_animes(animes, page, size, genres)
    return result

# POST Request Method
@router.post("/create-animes")
async def post_anime(animes: List[Anime]):
    anime_dicts = [anime.model_dump() for anime in animes]
    anime_collection.insert_many(anime_dicts)
    return {"message": "Animes added"}

# GET Request Method
@router.get("/genres")
async def get_genres():
    genres = list_serial_genres(genre_collection.find())
    return genres

# POST Request Method
@router.post("/create-genres")
async def post_genres(genres: List[Genre]):
    genre_dicts = [genre.model_dump() for genre in genres]
    genre_collection.insert_many(genre_dicts)
    return {"message": "Genres added"}

# PUT Request Method
@router.put("/animes/{id}")
async def update_anime(id: str, anime: Anime):
    anime_collection.find_one_and_update(
        {"_id": ObjectId(id)}, {"$set": dict(anime)})

# DELETE Request Method
@router.delete("/animes/{id}")
async def delete_anime(id: str):
    anime_collection.find_one_and_delete({"_id": ObjectId(id)})

# PUT Request Method
@router.put("/genres/{id}")
async def update_anime(id: str, genre: Genre):
    genre_collection.find_one_and_update(
        {"_id": ObjectId(id)}, {"$set": dict(genre)})

# DELETE Request Method
@router.delete("/genres/{id}")
async def delete_anime(id: str):
    genre_collection.find_one_and_delete({"_id": ObjectId(id)})