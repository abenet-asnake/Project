"""
Positional arguments are the most basic way to pass data to functions in a specific order. 
The values you pass are assigned to parameters based on their position.
    the syntax for defining a function with positional parameters is:
def function_name(param1, param2, ...): 
    # function body
    return value        
    
"""

def create_order(product_name, quantity, unit_price,discount=0):
    """Create an order with product details."""
    total_price = quantity * unit_price * (1 - discount)
    return {
        'product_name': product_name,
        'quantity': quantity,
        'unit_price': unit_price,   
        'discount': discount,
        'total_price': total_price
    }
# Calling the function with default values
order1 = create_order('Laptop', 2, 1500)
print(order1)  # Output: {'product_name': 'Laptop', 'quantity': 2, 'unit_price': 1500, 'discount': 0, 'total_price': 3000.0}