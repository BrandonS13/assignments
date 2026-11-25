#I learned how to use a * to allow the function to have unlimited arguements rather then having to define a fixed amount


def make_sandwich(*ingredients):
    """Display the ingredients in a sandwich."""
    print("Your sandwich contains:")
    for ingredient in ingredients:
        print(ingredient)

make_sandwich("Peanut Butter", "Jelly")
make_sandwich("Turkey", "Lettuce", "Tomato")
make_sandwich("Ham")