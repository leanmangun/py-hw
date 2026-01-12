password = input("Enter a password: ").strip()

# Flags to track requirements
has_letter = False
has_digit = False
has_special = False

# Check each character
for c in password:
    if c.isalpha():
        has_letter = True
    elif c.isdigit():
        has_digit = True
    elif c in "@#$%&":
        has_special = True

# Determine strength
if len(password) < 6:
    print("Weak password: Too short (must be at least 6 characters)")

elif password.isalpha() or password.isdigit():
    # Only letters OR only digits → weak (even if long)
    print("Weak password: Must contain both letters and digits")

elif len(password) >= 8 and has_letter and has_digit and has_special:
    print("Strong password")

elif len(password) >= 6 and has_letter and has_digit:
    print("Moderate password")

else:
    print("Moderate password")  # Covers cases like special chars but short length