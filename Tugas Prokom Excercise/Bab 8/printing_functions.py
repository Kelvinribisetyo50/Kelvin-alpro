def print_models(unprinted_designs, completed_models):
    """
    Simulasi mencetak setiap desain sampai tidak ada yang tersisa.
    Pindahkan setiap desain ke completed_models setelah dicetak.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Mencetak model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Tampilkan semua model yang sudah dicetak."""
    print("\nModel berikut telah dicetak:")
    for completed_model in completed_models:
        print(completed_model)