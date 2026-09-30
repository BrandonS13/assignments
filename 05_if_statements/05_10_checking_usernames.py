# Checks if a new username is already being used

current_users = ["brandon", "jake", "mike", "alex", "chris"]
new_users = ["james", "mike", "ryan", "alex", "david"]

for new_user in new_users:
    if new_user in current_users:
        print("You need to enter a new username")
    else:
        print("This username is available")