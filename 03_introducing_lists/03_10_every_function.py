foods = ["pizza", "burger", "hotdog"]
foods.append("tacos")

foods.insert(1, "chicken nugget")

del foods[2]

removed_food = foods.pop()

print(removed_food)
foods.remove("hotdog")

foods.sort()

foods.reverse()
print(len(foods))