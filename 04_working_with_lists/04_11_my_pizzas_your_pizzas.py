my_pizzas = ["cheese", "pepperoni", "pineapple"]

friend_pizzas = my_pizzas[:]

my_pizzas.append("chicken")
friend_pizzas.append("bacon")

print("My favorite pizzas are:")
for pizza in my_pizzas:
    print(pizza)

print("My friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)
