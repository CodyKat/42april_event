# PokeAPI를 사용
import requests

pokeName = input('Enter the name of a Pokemon: : ')

pokemon_url = 'https://pokeapi.co/api/v2/pokemon/' + pokeName.lower() + '/'
pokemon_response = requests.get(pokemon_url)
if pokemon_response.status_code == 200:
	pokemon_info = pokemon_response.json()
	print("Name: " + pokemon_info['name'])
	print("Abilities:")
	for i in pokemon_info['abilities']:
		print("- " + i['ability']['name'])
else:
	print("Pokemon not found.")
