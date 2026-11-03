def make_sandwich(*items):
    """Mencetak ringkasan sandwich yang dipesan."""
    print("\nMembuat sandwich dengan isian:")
    for item in items:
        print(f"- {item}")

make_sandwich("daging asap")
make_sandwich("telur", "keju", "tomat")
make_sandwich("ayam", "selada", "mayones", "timun", "saus sambal")