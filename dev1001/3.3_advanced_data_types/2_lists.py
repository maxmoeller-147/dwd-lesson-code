# Lists
#
# Like tuples, lists are also ordered sequences, but the key difference is
# they are **Mutable** - you *can* change them after creation.
# Syntax: Uses square brackets: []
# Use cases: Storing collections where items might be added, removed, or changed
#               (e.g., a list of tasks, scores, user names).

# Creating lists
shopping_list = ["apples", "bananas", "milk"]
scores = [88, 92, 75, 100]
mixed_list = [1, "hello", True, 3.14]
empty_list = []

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
