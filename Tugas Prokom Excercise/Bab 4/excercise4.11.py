pizzas = ['pepperoni', 'margherita', 'hawaiian']
pizza_teman = pizzas[:]

pizzas.append('BBQ ayam')
pizza_teman.append('keju empat rasa')

print("Pizza favoritku adalah:")
for pizza in pizzas:
    print(pizza)

print("\nPizza favorit temanku adalah:")
for pizza in pizza_teman:
    print(pizza)