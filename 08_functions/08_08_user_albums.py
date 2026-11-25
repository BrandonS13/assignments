#I Learned how to use a while loop with a function.

def make_album(artist, title):
    album = {"artist": artist, "title": title}
    return album

while True:
    artist = input("Enter an artist (or 'q' to quit): ")

    if artist == "q":
        break

    title = input("Enter an album title (or 'q' to quit): ")

    if title == "q":
        break

    print(make_album(artist, title))