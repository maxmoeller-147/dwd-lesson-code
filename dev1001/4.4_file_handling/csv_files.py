import csv

# --- Reading from CSV ---
print("\n--- Reading grades.csv ---")
with open("grades.csv", mode='r', newline='') as f: # newline='' is important for csv
    csv_reader = csv.reader(f)
    header = next(csv_reader) # Skip/read header row
    print(f"Header: {header}")
    for row in csv_reader:
        # Each row is a list of strings
        name, subject, grade = row
        print(f"{name} scored {grade} in {subject}")