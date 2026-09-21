full_name = input("Enter a name (First Last): ")

# 2. Split the name into a list of words using space as a separator
name_parts = full_name.split()

first_name = name_parts[0]
last_name = name_parts[-1] # Gets the last element


format_one = f"{first_name}, {last_name}"
format_two = f"{last_name.upper()}, {first_name}"


print("Format 1 (first,last):", format_one)
print("Format 2 (LAST, First):", format_two)
