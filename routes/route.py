from typing import List, Optional
from fastapi import APIRouter, Depends, Query
from models.models import Anime, Pagination, AnimeResponse
from config.database import collection_name
from schema.schemas import list_serial
from bson import ObjectId
from utils.pagination import paginate, parse_genres, contains_genres

router = APIRouter()

# GET Request Method
@router.get("/")
async def root():
    return {"Hello": "World"}

# Test DB Connection
@router.get("/test-db-connection")
async def test_db_connection():
    try:
        collections = collection_name.database.list_collection_names()
        return {"status": "success", "collections": collections}
    except Exception as e:
        return {"status": "failed", "message": str(e)}

# GET Request Method
@router.get("/animes")
async def get_animes(
    genres: Optional[List[int]] = Depends(parse_genres),
    page: int = Query(1, gt=0),
    size: int = Query(25, gt=0, le=100)
):
    animes = list_serial(collection_name.find(), page, size, genres)
    return animes

# POST Request Method
@router.post("/create-animes")
async def post_anime(animes: List[Anime]):
    anime_dicts = [anime.model_dump() for anime in animes]
    collection_name.insert_many(anime_dicts)
    return {"message": "Animes added"}

# PUT Request Method
@router.put("/animes/{id}")    
async def update_anime(id: str, anime: Anime):
    collection_name.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(anime)})

# DELETE Request Method
@router.delete("/animes/{id}")
async def delete_anime(id: str):
    collection_name.find_one_and_delete({"_id": ObjectId(id)})