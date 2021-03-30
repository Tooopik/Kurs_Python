"""

json.loads(jsonstring) - przetwarza jsonstring na dane typu Python

json.load(filePointer) - wczytuje json z pliku i zwraca jako wynik metody
                        dane typu Python

load z ang. wczytać
"""

import json
import pprint

film = {
    "title": "Ale ja nie będę tego robił!",
    "release_year": 1969,
    "won_oscar": True,
    "actors": ("Arkadiusz Włodarczyk", "Wiolleta Włodarczyk"),
    "budget": None,
    "credits": {
        "director": "Arkadiusz Włodarczyk",
        "writer": "Alan Burger",
        "animator": "Anime Animatrix"
    }
}

encodedFilm = json.dumps(film, ensure_ascii=False, indent=4, sort_keys=True)
print('Zakodowane do JSON :', encodedFilm)
print()

decodedMovie = json.loads(encodedFilm)
print('Odkodowane do PYTHON :', decodedMovie)

with open("sample.json", encoding="UTF-8") as file:
    wynik = json.load(file)

pprint.pprint(wynik)
