def replace_value(values, index, new_value):
    values[index] = new_value


def find_first(values, target):
    for i in range(len(values)):
        if values[i] == target:
            return i
    return -1


def summarize(values):
    return min(values), max(values), sum(values)


# Ask for the number of days
days = int(input("Enter the number of days: "))

# Store the original water usage values
original = []

for i in range(days):
    water = int(input("Enter water use in litres: "))
    original.append(water)

# Create a copy of the original list using slicing
updated = original[:]

# Correct a water usage value
index = int(input("Enter the index to correct: "))
new_value = int(input("Enter the new water use: "))
replace_value(updated, index, new_value)

# Search for a water usage value
target = int(input("Enter the water use to search for: "))

first_index = find_first(updated, target)
matching_values = updated.count(target)

# Calculate minimum, maximum, and total
minimum, maximum, total = summarize(updated)

# Create a sorted copy
sorted_values = sorted(updated)

# Display the results
print(f"Original: {original}")
print(f"Updated: {updated}")
print(f"Sorted: {sorted_values}")
print(f"Minimum water use: {minimum} litres")
print(f"Maximum water use: {maximum} litres")
print(f"Total water use: {total} litres")

if first_index == -1:
    print("Target not found")
else:
    print(f"First matching index: {first_index}")

print(f"Matching values: {matching_values}")