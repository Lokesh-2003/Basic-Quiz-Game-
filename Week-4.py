import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    try:
        password_length = int(input("Enter the desired password length: "))
        num_passwords = int(input("Enter the number of passwords to generate: "))

        for _ in range(num_passwords):
            password = generate_password(password_length)
            print(password)

    except ValueError:
        print("Please enter valid numeric values.")

if __name__ == "__main__":
    main()
