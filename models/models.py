from typing import List, Optional
from pydantic import BaseModel

class Anime(BaseModel):
    img: str
    title: str
    synopsis: str
    genres: Optional[List[str]] = None
    explicit_genres: Optional[List[str]] = None
    themes: Optional[List[str]] = None
    demographics: Optional[List[str]] = None

class Pagination(BaseModel):
    last_visible_page: int
    has_next_page: bool
    current_page: int
    items: dict

class AnimeResponse(BaseModel):
    pagination: Pagination
    data: List[dict]