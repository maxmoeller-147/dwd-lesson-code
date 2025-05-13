# --- USE: Ternary Operator ---
age = 22
category = "Child" if age < 13 else "Adult or Teen" # The ternary operator
print(f"Age: {age}, Category: {category}")

if age >= 18:
    category = "Adult"
else:
    category = "Minor"
