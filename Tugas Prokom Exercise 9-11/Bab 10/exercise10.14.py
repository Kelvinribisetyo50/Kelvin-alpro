from pathlib import Path
import json


def get_stored_username(path):
    """Ambil username yang tersimpan, jika ada."""
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
        return None


def get_new_username(path):
    """Minta username baru dan simpan ke file."""
    username = input("Siapa namamu? ")
    contents = json.dumps(username)
    path.write_text(contents)
    return username


def greet_user():
    """Sapa pengguna, setelah memastikan username-nya benar."""
    path = Path(__file__).parent / 'username.json'
    username = get_stored_username(path)

    if username:
        answer = input(f"Apakah kamu {username}? (y/n) ")
        if answer.lower() == 'y':
            print(f"Selamat datang kembali, {username}!")
        else:
            username = get_new_username(path)
            print(f"Kami akan mengingatmu saat kamu kembali, {username}!")
    else:
        username = get_new_username(path)
        print(f"Kami akan mengingatmu saat kamu kembali, {username}!")


greet_user()