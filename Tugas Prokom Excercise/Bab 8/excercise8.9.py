def show_messages(messages):
    """Mencetak setiap pesan teks dalam daftar."""
    for message in messages:
        print(message)

pesan = [
    "Halo, apa kabar?",
    "Jangan lupa ada matkul Prokom jam 10.",
    "Terima kasih atas bantuannya!",
]

show_messages(pesan)