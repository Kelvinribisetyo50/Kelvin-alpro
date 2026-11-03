def send_messages(messages, sent_messages):
    """Mencetak setiap pesan dan memindahkannya ke daftar sent_messages."""
    while messages:
        current_message = messages.pop(0)
        print(f"Mengirim pesan: {current_message}")
        sent_messages.append(current_message)

pesan = [
    "Halo, apa kabar?",
    "Jangan lupa ada matkul Prokom jam 10.",
    "Terima kasih atas bantuannya!",
]
sent_messages = []

send_messages(pesan, sent_messages)

print("\nDaftar pesan:", pesan)
print("Daftar sent_messages:", sent_messages)