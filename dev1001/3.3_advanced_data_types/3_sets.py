# Sets
#
# Sets are collections of **unique** items, and they are **unordered**
#   (you can't rely on index positions)."
# Key characteristics: **Mutable**, **Unordered**, **Unique Elements**.
# Syntax: Uses curly braces `{}` like dictionaries, but *only* values.
#         An empty set must be created using `set()`.
# Use cases: Removing duplicates, fast membership testing,
#            mathematical set operations (union, intersection).

# Creating sets
numbers = {1, 2, 3, 2, 4, 1} # Duplicates are automatically removed
print(f"Numbers set: {numbers}")

# TODO 1: Add "communication" to required_skills if it's not already there.
# TODO 2: Find out which skills the candidate has that are also required.
# TODO 3: Find out all unique skills possessed by either (required or candidate).
# TODO 4: Which skills are required but the candidate doesn't have?


required_skills.add('communication')
print(required_skills)

print(required_skills & candidate_skills)

print(required_skills | candidate_skills)

print(required_skills - candidate_skills)
