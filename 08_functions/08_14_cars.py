def make_car(manufacturer, model, **car_info):
    """Build a dictionary containing car information."""
    car_info["manufacturer"] = manufacturer
    car_info["model"] = model
    return car_info
car = make_car("Jeep", "Wrangler", color="Green", year=2013)
print(car)