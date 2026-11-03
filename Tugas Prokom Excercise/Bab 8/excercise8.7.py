def make_album(artist, title, songs=None):
    """Membuat dictionary yang menggambarkan sebuah album musik."""
    album = {"artist": artist, "title": title}
    if songs is not None:
        album["songs"] = songs
    return album

album_1 = make_album("Sheila on 7", "Kisah Klasik untuk Masa Depan")
album_2 = make_album("Dewa 19", "Pandawa Lima")
album_3 = make_album("Afgan", "Bukan Cinta Biasa")

print(album_1)
print(album_2)
print(album_3)

album_4 = make_album("One Direction", "Night Changes", songs=9)
print(album_4)