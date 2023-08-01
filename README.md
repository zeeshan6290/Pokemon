# Pokemon
It is a mini project. It is a simple project to take CSV data and put it into a flask or fast api app with a paginated API.

- Please find a requirements.txt file inside pokemon/flaskProject
- Install it
- Run flask project on 8000 port



{
	"info": {
		"_postman_id": "d7a86891-5325-484f-b93c-7696d6f86538",
		"name": "Pokemon",
		"schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json",
		"_exporter_id": "7014971"
	},
	"item": [
		{
			"name": "get pokemon",
			"request": {
				"method": "GET",
				"header": [],
				"url": {
					"raw": "http://localhost:8000/pokemons?sort_by=weight",
					"protocol": "http",
					"host": [
						"localhost"
					],
					"port": "8000",
					"path": [
						"pokemons"
					],
					"query": [
						{
							"key": "page",
							"value": "1",
							"disabled": true
						},
						{
							"key": "per_page",
							"value": "3",
							"disabled": true
						},
						{
							"key": "filter_by",
							"value": "weight",
							"disabled": true
						},
						{
							"key": "filter_value",
							"value": "69",
							"disabled": true
						},
						{
							"key": "keyword",
							"value": "b",
							"disabled": true
						},
						{
							"key": "sort_by",
							"value": "weight"
						}
					]
				}
			},
			"response": []
		},
		{
			"name": "import from csv",
			"request": {
				"method": "GET",
				"header": [],
				"url": {
					"raw": "http://localhost:8000/import_csv",
					"protocol": "http",
					"host": [
						"localhost"
					],
					"port": "8000",
					"path": [
						"import_csv"
					]
				}
			},
			"response": []
		},
		{
			"name": "export csv",
			"request": {
				"method": "GET",
				"header": [],
				"url": {
					"raw": "http://localhost:8000/import_csv",
					"protocol": "http",
					"host": [
						"localhost"
					],
					"port": "8000",
					"path": [
						"import_csv"
					]
				}
			},
			"response": []
		}
	]
}
