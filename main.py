import os
import json
import requests
from geopy import distance
from dotenv import load_dotenv
import folium
from flask import Flask, render_template


def site():
    return render_template('index.html')


def fetch_coordinates(apikey, address):
    base_url = "https://geocode-maps.yandex.ru/1.x"
    response = requests.get(base_url, params={
        "geocode": address,
        "apikey": apikey,
        "format": "json",
    })
    response.raise_for_status()
    found_places = response.json()['response']['GeoObjectCollection']['featureMember']

    if not found_places:
        return None

    most_relevant = found_places[0]
    lon, lat = most_relevant['GeoObject']['Point']['pos'].split(" ")
    return lon, lat


def map(location_of_person, nearest_places):
    m = folium.Map(location_of_person, zoom_start=15, tiles="Stamen Terrain")
    for place in nearest_places:
        folium.Marker(
            location=[place['geoData']['coordinates'][1], place['geoData']['coordinates'][0]],
            popup=place["Name"],
            icon=folium.Icon(icon="cloud"),
        ).add_to(m)
    os.makedirs('templates', exist_ok=False)
    m.save("templates/index.html")


def get_distance(coffee_house_info):
    return coffee_house_info['distance']


def main():
    load_dotenv()
    point_a = list(fetch_coordinates(os.environ['YANDEX_APIKEY'], input("В каком городе Вы находитесь: ")))
    point_a.append(point_a.pop(0))
    with open('coffee.json', "r", encoding="CP1251") as file:
        file_content = json.load(file)
    for coffee_house in file_content:
        coffee_house['distance'] = distance.distance(point_a, (coffee_house['geoData']['coordinates'][1], coffee_house['geoData']['coordinates'][0])).km
    map(point_a, sorted(file_content, key=get_distance, reverse=False)[:5])


if __name__ == "__main__":
    main()
    app = Flask(__name__)
    app.add_url_rule('/', 'site', site)
    app.run('0.0.0.0')
