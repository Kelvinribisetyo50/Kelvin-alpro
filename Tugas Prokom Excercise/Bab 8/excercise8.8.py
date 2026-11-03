def make_album(artist, title, songs=None):
    """Membuat dictionary yang menggambarkan sebuah album musik."""
    album = {"artist": artist, "title": title}
    if songs is not None:
        album["songs"] = songs
    return album

while True:
    print("\nMasukkan informasi album (ketik 'q' kapan saja untuk keluar)")

    artist = input("Nama artis: ")
    if artist == "q":
        break

    title = input("Judul album: ")
    if title == "q":
        break

    album = make_album(artist, title)
    print(album)

print("\nTerima kasih, program selesai.")