import csv

import requests
from sqlalchemy.exc import IntegrityError

from schema import Pokemon, db


class PokemonData:
    @staticmethod
    def parse_csv_and_store_pokemon_data():
        db.create_all()
        with open('data.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for pokemon_data in reader:
                pokemon = Pokemon(
                    name=pokemon_data['Name'],
                    base_experience=pokemon_data['Base Experience'],
                    height=pokemon_data['Height'],
                    weight=pokemon_data['Weight'],
                    image_url=pokemon_data['Image URL']
                )
                db.session.add(pokemon)
            try:
                db.session.commit()
            except IntegrityError:
                pass

    @staticmethod
    def fetch_data_and_store_pokemon_data():
        response = requests.get('https://pokeapi.co/api/v2/pokemon/')
        data = response.json()['results']
        fieldnames = ['Name', 'Base Experience', 'Height', 'Weight', 'Image URL']

        with open('data.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(fieldnames)
            for item in data:
                pokemon_data = requests.get(item['url']).json()
                writer.writerow([pokemon_data['name'],
                                 pokemon_data['base_experience'],
                                 pokemon_data['height'],
                                 pokemon_data['weight'],
                                 pokemon_data['sprites']['front_default']
                                 ])
