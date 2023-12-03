import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_multiple_passwords(num_passwords, length=12):
    passwords = [generate_password(length) for _ in range(num_passwords)]
    return passwords

def main():
    print("Welcome to the Password Generator!")
    print("Pro Tip: Make sure to store generated passwords in a secure location.")

    try:
        length = int(input("Enter the desired length for the password(s): "))
        num_passwords = int(input("Enter the number of passwords to generate: "))
    except ValueError:
        print("Please enter valid numeric values.")
        return

    if length <= 0 or num_passwords <= 0:
        print("Length and number of passwords should be greater than zero.")
        return

    passwords = generate_multiple_passwords(num_passwords, length)

    print("\nGenerated Passwords:")
    for i, password in enumerate(passwords, start=1):
        print(f"Password {i}: {password}")

if __name__ == "__main__":
    main()
