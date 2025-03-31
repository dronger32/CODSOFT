import random
import string

def generate_password():
    try:
        length = int(input("Enter the desired password length: "))
        if length < 4:
            print("Password length should be at least 4 characters for security.")
            return
        
        use_uppercase = input("Include uppercase letters? (yes/no): ").strip().lower() == "yes"
        use_digits = input("Include digits? (yes/no): ").strip().lower() == "yes"
        use_special = input("Include special characters? (yes/no): ").strip().lower() == "yes"
        
        characters = string.ascii_lowercase
        if use_uppercase:
            characters += string.ascii_uppercase
        if use_digits:
            characters += string.digits
        if use_special:
            characters += string.punctuation
        
        if not characters:
            print("You must include at least one type of character.")
            return
        
        password = ''.join(random.choice(characters) for _ in range(length))
        
        print("\nGenerated Password: ", password)
    except ValueError:
        print("Invalid input! Please enter a valid number.")

def main():
    print("Welcome to the Secure Password Generator!")
    while True:
        generate_password()
        again = input("\nWould you like to generate another password? (yes/no): ").strip().lower()
        if again != "yes":
            print("Goodbye! Stay safe.")
            break

if __name__ == "__main__":
    main()
