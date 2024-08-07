from typing import List, Optional
from fastapi import Query


def paginate(items, page: int, size: int):
    start = (page - 1) * size
    end = start + size
    total_items = len(items)
    last_visible_page = (total_items + size - 1) // size
    has_next_page = end < total_items

    paginated_items = items[start:end]

    pagination_info = {
        "last_visible_page": last_visible_page,
        "has_next_page": has_next_page,
        "current_page": page,
        "items": {
            "count": len(paginated_items),
            "total": total_items,
        }
    }

    return pagination_info, paginated_items

def contains_genres(anime, genre_ids):
    return all(genre_id in anime["genre_ids"] for genre_id in genre_ids)

def parse_genres(genres: Optional[str] = Query(None)) -> Optional[List[int]]:
    if genres:
        return [int(g) for g in genres.split(',')]
    return None