from utils.util import paginate, contains_genres

def individual_serial_anime(anime) -> dict:
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

def list_serial_animes(animes, page: int, size: int, genres: list) -> dict:
    filtered_animes = [anime for anime in animes if contains_genres(
        anime, genres)] if genres else animes
    serialized_animes = [individual_serial_anime(
        anime) for anime in filtered_animes]
    pagination_info, paginated_animes = paginate(serialized_animes, page, size)

    return {
        "pagination": pagination_info,
        "data": paginated_animes
    }

def individual_serial_genre(genre) -> dict:
    return {
        "name": genre["name"]
    }

def list_serial_genres(genres) -> dict:
    return {
        "data": [individual_serial_genre(genre) for genre in genres]
    }