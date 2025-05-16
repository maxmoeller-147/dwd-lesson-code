# --- USE: Loop Examples ---
print("--- LOOPS: USE PHASE ---")

# 1. `while` loop: Simple countdown
print("--- While Loop ---")
countdown = 3
while countdown > 0:
    print(f"T-minus {countdown}...")
    countdown -= 1 # Crucial: update the condition variable
print("Lift off!")
print("-" * 20)

# 2. `for...in range()`: Processing a fixed number of times
print("--- For...in range() Loop ---")
num_students = 4
for i in range(num_students):
    print(f"Processing data for student #{i + 1}") # i is 0-indexed
print("-" * 20)

# 3. `for...in iterable` (list): Processing items in a collection
print("--- For...in iterable (List) ---")
shopping_list = ["apples", "bananas", "milk", "bread"]
for item in shopping_list:
    print(f"Need to buy: {item.capitalize()}")
print("-" * 20)

# 4. `for...in iterable` (dictionary items): Accessing keys and values
# (Re-using product_prices from dictionary section for context)
product_prices = {"laptop_stand": 25, "usb_c_hub": 30, "ergonomic_keyboard": 75}
print("--- For...in iterable (Dictionary items) ---")
print("Product Pricelist:")
for product, price in product_prices.items():
    print(f"- {product.replace('_', ' ').title()}: ${price}")
print("-" * 20)

# 5. `enumerate()`: Getting item and its index
print("--- Enumerate Loop ---")
tasks_today = ["Reply to emails", "Attend meeting", "Code feature X"]
print("Today's Tasks:")
for index, task in enumerate(tasks_today):
    print(f"{index + 1}. {task}") # User-friendly 1-based indexing
print("-" * 30 + "\n")


#  while` Loop Temperature Check:**
#       *   Imagine a sensor reading. Start with `current_temp = 18`.
current_temp = 18

#      *   Write a `while` loop that keeps printing "Temperature ({current_temp}°C) is cool, increasing..." and increments `current_temp` by 1, as long as `current_temp` is less than 22.
while current_temp < 22
print(f"temperature {current_temp} is cool, increasing...")
current_temp += 1


#     *   Once it reaches 22 or more, print "Temperature ({current_temp}°C) is optimal."
while current_temp .= 22
    for i in range(current_temp):print("-" * 20)
    
