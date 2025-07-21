import random
import string

# Step 1: User Input
length = int(input("Enter the desired password length: "))

# Step 2: Generate Password
characters = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(characters) for _ in range(length))

# Step 3: Display the Password
print("Generated Password:", password)
