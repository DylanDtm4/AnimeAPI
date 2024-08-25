from typing import List, Optional
from fastapi import Query

GENRES = ['Action', 'Adventure', 'Avant Garde', 'Award Winning', 'Boys Love', 'Comedy', 'Drama', 'Fantasy', 'Girls Love', 
          'Gourmet', 'Horror', 'Mystery', 'Romance', 'Sci-Fi', 'Slice of Life', 'Sports', 'Supernatural', 'Suspense', 'Ecchi', 
          'Erotica', 'Hentai', 'Adult Cast', 'Anthropomorphic', 'CGDCT', 'Childcare', 'Combat Sports', 'Crossdressing', 
          'Delinquents', 'Detective', 'Educational', 'Gag Humor', 'Gore', 'Harem', 'High Stakes Game', 'Historical', 
          'Idols (Female)', 'Idols (Male)', 'Isekai', 'Iyashikei', 'Love Polygon', 'Magical Sex Shift', 'Mahou Shoujo', 
          'Martial Arts', 'Mecha', 'Medical', 'Military', 'Music', 'Mythology', 'Organized Crime', 'Otaku Culture', 'Parody', 
          'Performing Arts', 'Pets', 'Psychological', 'Racing', 'Reincarnation', 'Reverse Harem', 'Romantic Subtext', 'Samurai', 
          'School', 'Showbiz', 'Space', 'Strategy Game', 'Super Power', 'Survival', 'Team Sports', 'Time Travel', 'Vampire', 
          'Video Game', 'Visual Arts', 'Workplace', 'Josei', 'Kids', 'Seinen', 'Shoujo', 'Shounen']

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
    combined_genre_ids = [
    genre["ord_id"]
    for category in ["genres", "explicit_genres", "themes", "demographics"]
    for genre in anime.get(category, [])
    ]
    return all(genre_id in combined_genre_ids for genre_id in genre_ids)


def parse_genres(genres: Optional[str] = Query(None)) -> Optional[List[int]]:
    if genres:
        return [int(g) for g in genres.split(',')]
    return None