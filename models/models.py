from typing import List, Optional
from pydantic import BaseModel

class Genre(BaseModel):
    ord_id: int
    name: str

class Anime(BaseModel):
    ord_id: int
    img: str
    title: str
    synopsis: str
    genres: Optional[List[Genre]] = None
    explicit_genres: Optional[List[Genre]] = None
    themes: Optional[List[Genre]] = None
    demographics: Optional[List[Genre]] = None

class Pagination(BaseModel):
    last_visible_page: int
    has_next_page: bool
    current_page: int
    items: dict

class AnimeResponse(BaseModel):
    pagination: Pagination
    data: List[dict]