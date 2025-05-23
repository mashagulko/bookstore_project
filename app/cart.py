def calculate_total_price(items):
    return sum(item['price'] * item['quantity'] for item in items)

def clear_cart(cart):
    cart.clear()
