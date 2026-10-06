cities = {"new york": {"country": "united states", "population": 8000000, "fact": "it is home to times square"}, "miami": {"country": "united states", "population": 450000, "fact": "it is known for its beaches"}, "london": {"country": "england", "population": 9000000, "fact": "big ben is located there"}}
for city, information in cities.items():
    print(city.title())
    print(information)