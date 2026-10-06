favorite_places = {"brandon": ["new jersey", "florida"], "cris": ["new york", "california"], "liam": ["pennsylvania", "florida"]}
for person, places in favorite_places.items():
    print(person.title())
    for place in places:
        print(place.title())