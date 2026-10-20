favorite_languages = {"brandon": "python", "cris": "java"}
people = ["brandon", "cris", "liam", "alexis"]
for person in people:
    if person in favorite_languages:
        print(f"Thank you for responding, {person.title()}!")
    else:
        print(f"{person.title()}, please take the poll!")