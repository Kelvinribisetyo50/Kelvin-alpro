prompt = "\nMasukkan topping pizza yang Anda inginkan."
prompt += "\nKetik 'quit' jika sudah selesai: "

aktif = True
while aktif:
    topping = input(prompt)

    if topping == 'quit':
        aktif = False
    else:
        print(f"Baik, topping {topping} akan kami tambahkan ke pizza Anda.")