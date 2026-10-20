#in this i use .items(), .keys(), and .values() to print out the information in the dictionary

rivers = {"nile": "egypt", "amazon": "brazil", "mississippi": "united states"}
for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")
for river in rivers.keys():
    print(river.title())
for country in rivers.values():
    print(country.title())
