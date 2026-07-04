import requests

base_url = "https://pokeapi.co/api/v2"
stats = []


def get_pokemon_info(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)
    if response.status_code == 200:
        data_of_response = response.json()
        return data_of_response


pokemon_name = input("Enter The Name Of The Pokemon: ")
pokemon_info = get_pokemon_info(pokemon_name)
# stats = input("Enter the name of stats: ")
# stats_of_pokemon = print_stats(stats)
is_true = True


def print_stats(pokemon_stat):
    try:
        return pokemon_info[pokemon_stat]
    except KeyError:
        return "invalid stat name"


if pokemon_info:
    while is_true:
        pokemon_stats = input("Enter The Pokemon Stats you want to know: ")
        stat = print_stats(pokemon_stats)
        print(stat)
else:
    print("ERROR")
