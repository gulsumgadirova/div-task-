def calculate_total(cart, discount_limiit=10):
    total = 0

    for product in cart:
        price = cart[product][0]
        quantity = cart[product][1]

        total += price * quantity

    if total >= discount_limiit:
        discounted = total * 0.9
    else:
        discounted = total
    return total, discounted

cart = {
    "alma": [1.5, 6],
    "corek":[0.8,2],
    "sud": [2.2, 1]              
}
total, discounted = calculate_total(cart)

for product in cart:
    price = cart[product][0]
    quantity = cart[product][1]

    print(product, quantity,"x", price, "=", price * quantity)
print("Umumi mebleg:", total)
print("Endirimli mebleg:", discounted)
    