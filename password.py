import random
import string
def generate_password(length, strength):
    if strength == 'weak':
        characters = string.ascii_lowercase
    elif strength == 'medium':
        characters = string.ascii_letters + string.digits
    else:
        characters = string.ascii_letters + string.digits + string.punctuation
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# User input
length = int(input("Enter password length: "))
strength = input("Choose strength (weak/medium/strong): ").lower()

# Generate and print password
password = generate_password(length, strength)
print("Generated Password:", password)
