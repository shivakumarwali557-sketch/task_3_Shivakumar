import random
import string

# Ask the user for password length
length = int(input("Enter password length: "))

# Check minimum password length
if length < 4:
    print("Password length should be at least 4.")
else:
    # Characters that can be used
    letters = string.ascii_letters
    numbers = string.digits
    special_characters = "@#$%&*!"

    all_characters = letters + numbers + special_characters

    # Make sure the password contains at least one number
    password = random.choice(numbers)

    # Generate the remaining characters
    for i in range(length - 1):
        password += random.choice(all_characters)

    # Shuffle the password
    password = list(password)
    random.shuffle(password)

    # Convert list back to string
    password = "".join(password)

    # Display the password
    print("Generated password:", password)