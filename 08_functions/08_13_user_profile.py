#I learned how to use ** in this. ** allows me to still have unlimited arguments but allows me to add a label to each value (a key) 

def build_profile(first, last, **user_info):
    """Build a dictionary containing user information."""
    user_info["first_name"] = first
    user_info["last_name"] = last
    return user_info

profile = build_profile("Brandon", "Smith",
                        sport="Soccer",
                        major="Cybersecurity",
                        college="Albright")

print(profile)