full_name = input("Enter your full name: ").strip()

# Remove extra spaces and split into parts
parts = full_name.split()

# Basic validation: ensure at least two names are provided
if len(parts) < 2:
    print("Error: Please enter at least a first and last name.")
else:
    first_initial = parts[0][0].upper()
    last_initial = parts[-1][0].upper()
    print("Your initials are:", f"{first_initial}.{last_initial}.")