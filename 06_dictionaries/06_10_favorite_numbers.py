favorite_numbers = {"brandon": [9, 13], "cris": [7, 10], "liam": [4, 18], "alexis": [3, 12]}
for person, numbers in favorite_numbers.items():
    print(person.title())
    for number in numbers:
        print(number)