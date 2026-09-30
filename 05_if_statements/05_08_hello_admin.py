# Greets each user and gives the admin a special message

usernames = ["brandon", "jake", "admin", "mike", "alex"]

for username in usernames:
    if username == "admin":
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {username}, thank you for logging in again")