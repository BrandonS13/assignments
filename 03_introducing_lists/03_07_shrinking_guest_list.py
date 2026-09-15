guests = ["danny", "lebron", "damien", "pat", "marty", "bob"]
print("I can only invite two people to dinner.")
del guests[5]
del guests[4]
del guests[3]
del guests[2]
print(guests)
print(f"Hey {guests[0].title()}, you are still invited to dinner.")
print(f"Hey {guests[1].title()}, you are still invited to dinner.")
del guests[1]
del guests[0]
print(guests)