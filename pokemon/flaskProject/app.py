from flask import request, jsonify, render_template

from pagination import paginate
from schema import Pokemon, app
from schema import PokemonSchema
from store_pokemon_data import PokemonData


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/import_csv', methods=['GET'])
def import_csv():
    PokemonData.parse_csv_and_store_pokemon_data()
    return jsonify({'message': 'Csv imported Successfully'}), 200


@app.route('/export_csv', methods=['GET'])
def export_csv():
    PokemonData.fetch_data_and_store_pokemon_data()
    return jsonify({'message': 'Csv exported Successfully'}), 200


@app.route('/pokemons', methods=['GET'])
@paginate
def get_pokemons():
    query = Pokemon.query

    # Sorting
    sort_by = request.args.get('sort_by')
    if sort_by:
        if sort_by in ['name', 'base_experience', 'height', 'weight']:
            query = query.order_by(getattr(Pokemon, sort_by))
        else:
            return jsonify({'message': 'Invalid sort property'}), 400

    # Filtering
    filter_by = request.args.get('filter_by')
    filter_value = request.args.get('filter_value')
    if filter_by and filter_value:
        if filter_by in ['name', 'base_experience', 'height', 'weight']:
            query = query.filter(getattr(Pokemon, filter_by) == filter_value)
        else:
            return jsonify({'message': 'Invalid filter property'}), 400
    # Search
    keyword = request.args.get('keyword', '')
    if keyword:
        pokemon = query.filter(Pokemon.name.contains(keyword)).all()
    else:
        pokemon = query.all()
    pokemon_schema = PokemonSchema(many=True)
    return pokemon_schema.dump(pokemon)


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8000)
