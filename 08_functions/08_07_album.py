#I Learned how to return a dictionary from a function.

def make_album(artist, title):
    album = {"artist": artist, "title": title}
    return album

print(make_album("Drake", "Scorpion"))
print(make_album("Travis Scott", "Astroworld"))
print(make_album("The Weeknd", "After Hours"))