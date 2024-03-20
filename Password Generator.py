import random
import string

def generate_password(length=12, complexity="medium"):
    if complexity == "low":
        characters = string.ascii_letters + string.digits
    elif complexity == "medium":
        characters = string.ascii_letters + string.digits + string.punctuation
    elif complexity == "high":
        characters = string.ascii_letters + string.digits + string.punctuation + string.ascii_uppercase
    else:
        print("Invalid complexity level. Using medium complexity.")
        characters = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    length = int(input("Enter the length of the password: "))
    complexity = input("Enter the complexity level (low/medium/high): ").lower()
    password = generate_password(length, complexity)
    print("Generated password:", password)
