prompt = "\nMasukkan topping pizza yang Anda inginkan."
prompt += "\nKetik 'quit' jika sudah selesai: "

while True:
    topping = input(prompt)

    if topping == 'quit':
        break
    else:
        print(f"Baik, topping {topping} akan kami tambahkan ke pizza Anda.")