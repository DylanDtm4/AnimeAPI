import requests
import json

def clean_string(s):
    return json.dumps(s)

def parse_json_string(s):
    return json.loads(s)
    
def fetch_paginated_data(base_url, pageNum): # (, pageNum)
    all_data = []    
    url = f"{base_url}?page={pageNum}" # ?page={pageNum}"

    try:
        response = requests.get(url)
        data = response.json()
        all_data.extend(data.get('data', []))

    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 429:
            return -1
        else:
            raise

    return all_data

def extract_genre_data(genres):
    genre_data = []
    for genre in genres:
        genre_data.append({"ord_id": genre['mal_id'], "name": genre['name']})
    return genre_data

def extract_anime_data(data):
    anime_data = []
    for anime in data:
        ord_id = anime["mal_id"]
        img = anime["images"]["jpg"]["image_url"]
        title = clean_string(anime["title"])
        title = parse_json_string(title)
        synopsis = clean_string(anime["synopsis"])
        synopsis = parse_json_string(synopsis)
        if synopsis == None:
            synopsis = "None"
        genres = extract_genre_data(anime["genres"])
        explicit_genres = extract_genre_data(anime["explicit_genres"])
        themes = extract_genre_data(anime["themes"])
        demographics = extract_genre_data(anime["demographics"])

        anime_data.append({
            "ord_id": ord_id,
            "img": img,
            "title": title,
            "synopsis": synopsis,
            "genres": genres,
            "explicit_genres": explicit_genres,
            "themes": themes,
            "demographics": demographics
        })
    return anime_data

    # return json.dumps(anime_data, indent=2)

def main(pageNum): # (pageNum) for anime input
    
    # inputting anime data
    URL = 'https://api.jikan.moe/v4/anime'
    data = fetch_paginated_data(URL, pageNum)
    anime_data = extract_anime_data(data)    
    
    api_url = "http://127.0.0.1:8000/create-animes"
    response = requests.post(api_url, json=anime_data)
    
    '''
    # inputting genre data
    URL = 'https://api.jikan.moe/v4/genres/anime'
    data = fetch_paginated_data(URL)
    genre_data = extract_genre_data(data)
    api_url = "http://127.0.0.1:8000/create-genres"
    response = requests.post(api_url, json=genre_data)
    '''
    
    if response.status_code == 200:
        return 0
    else:
        return -1
    
if __name__ == "__main__":
    import sys
    page_num = int(sys.argv[1]) # for anime input
    exit_code = main(page_num) # (page_num) for anime input
    sys.exit(exit_code)
