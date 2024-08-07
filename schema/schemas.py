from models.models import Anime, Pagination, AnimeResponse
from utils.pagination import paginate, contains_genres

def individual_serial(anime) -> dict:
    return {
        "id": str(anime["_id"]),
        "img": anime["img"],
        "title": anime["title"],
        "synopsis": anime["synopsis"],
        "genres": anime["genres"],
        "explicit_genres": anime["explicit_genres"],
        "themes": anime["themes"],
        "demographics": anime["demographics"],
    }

def list_serial(animes, page: int, size: int, genres: list) -> dict:
    filtered_animes = [anime for anime in animes if contains_genres(anime, genres)] if genres else animes
    serialized_animes = [individual_serial(anime) for anime in filtered_animes]
    pagination_info, paginated_animes = paginate(serialized_animes, page, size)

    return {
        "pagination": pagination_info,
        "data": paginated_animes
    }

