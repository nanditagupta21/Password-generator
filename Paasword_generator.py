import random
import string

def generate_password(length, complexity):
    # Define the character sets based on complexity
    char_sets = {
        'low': string.ascii_lowercase,
        'medium': string.ascii_letters,
        'high': string.ascii_letters + string.digits,
        'very_high': string.ascii_letters + string.digits + string.punctuation
    }
    
    if complexity not in char_sets:
        raise ValueError("Invalid complexity level. Choose from 'low', 'medium', 'high', 'very_high'.")
    
    # Get the appropriate character set
    chars = char_sets[complexity]
    
    # Generate the password
    password = ''.join(random.choice(chars) for _ in range(length))
    
    return password

def main():
    print("Welcome to the Password Generator!")
    
    # Get user input for password length
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length <= 0:
                raise ValueError("Length must be a positive integer.")
            break
        except ValueError as ve:
            print(f"Invalid input: {ve}. Please enter a positive integer.")
    
    # Get user input for password complexity
    while True:
        complexity = input("Enter the complexity level ('low', 'medium', 'high', 'very_high'): ").strip().lower()
        if complexity in {'low', 'medium', 'high', 'very_high'}:
            break
        else:
            print("Invalid complexity level. Please choose from 'low', 'medium', 'high', 'very_high'.")
    
    # Generate and display the password
    password = generate_password(length, complexity)
    print(f"Generated password: {password}")

if __name__ == "__main__":
    main()
