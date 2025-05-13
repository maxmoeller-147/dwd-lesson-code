# Shopping Cart
cart = ["apples", "bananas", "bread"]

# Solve the TODOs by writing code, NOT by changing the data structure by hand!

# TODO 1: Add "milk" to the end of the cart.
# TODO 2: "bananas" are out of stock. Remove them.
# TODO 3: You remembered you need "eggs" right after "apples". Insert it there.
# TODO 4: You bought 2 "apples". How many "apples" are in the cart now? (Assume it's still 1 for this example, but how would you check?)
# TODO 5: Sort the cart alphabetically.
# Print the final cart.


cart.append("milk")
cart.remove("bananas")
cart.insert(1,'eggs')
cart.extend(['apples','apples'])
print(f'number of apples:{cart.count('apples')}')

cart.sort()
print(cart[:2])
print(cart[1:])

print(cart)
print(f'total items: {len(cart)}')