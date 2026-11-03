prompt = "\nMasukkan topping pizza yang Anda inginkan."
prompt += "\nKetik 'quit' jika sudah selesai: "

topping = ""
while topping != 'quit':
    topping = input(prompt)

    if topping != 'quit':
        print(f"Baik, topping {topping} akan kami tambahkan ke pizza Anda.")