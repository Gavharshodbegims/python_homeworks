#1

import requests

def get_weather(city_name, api_key):
    base_url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric'  # Use 'imperial' for Fahrenheit
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    if response.status_code == 200:
        print(f"Weather in {data['name']}, {data['sys']['country']}:")
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Humidity: {data['main']['humidity']}%")
        print(f"Weather: {data['weather'][0]['description'].capitalize()}")
        print(f"Wind Speed: {data['wind']['speed']} m/s")
    else:
        print(f"Error: {data.get('message', 'Unable to fetch weather data.')}")

# Replace 'your_api_key' with your actual OpenWeatherMap API key
api_key = 'your_api_key'
get_weather('Tashkent', api_key)

#2

import requests
import random

def get_genre_id(api_key, genre_name):
    url = 'https://api.themoviedb.org/3/genre/movie/list'
    params = {
        'api_key': api_key,
        'language': 'en-US'
    }
    response = requests.get(url, params=params)
    genres = response.json().get('genres', [])
    for genre in genres:
        if genre['name'].lower() == genre_name.lower():
            return genre['id']
    return None

def recommend_movie(api_key, genre_name):
    genre_id = get_genre_id(api_key, genre_name)
    if not genre_id:
        print(f"Genre '{genre_name}' not found.")
        return

    url = 'https://api.themoviedb.org/3/discover/movie'
    params = {
        'api_key': api_key,
        'with_genres': genre_id,
        'sort_by': 'popularity.desc',
        'language': 'en-US',
        'page': random.randint(1, 5)  # Random page for variety
    }
    response = requests.get(url, params=params)
    movies = response.json().get('results', [])
    if movies:
        movie = random.choice(movies)
        print(f"Recommended Movie: {movie['title']}")
        print(f"Overview: {movie['overview']}")
        print(f"Release Date: {movie['release_date']}")
        print(f"Rating: {movie['vote_average']}/10")
    else:
        print(f"No movies found for genre '{genre_name}'.")

# Replace 'your_tmdb_api_key' with your actual TMDB API key
api_key = 'your_tmdb_api_key'
genre = input("Enter a movie genre (e.g., Action, Comedy, Drama): ")
recommend_movie(api_key, genre)
