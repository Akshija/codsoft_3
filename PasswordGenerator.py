import random
import string

def generate_password(length, complexity):
    char_sets = {
        1: string.ascii_lowercase,                          
        2: string.ascii_lowercase + string.ascii_uppercase, 
        3: string.ascii_letters + string.digits,
        4: string.ascii_letters + string.digits + string.punctuation
    }
    
    if complexity not in char_sets:
        raise ValueError("Invalid complexity level. Please choose a level between 1 and 4.")

    password = ''.join(random.choice(char_sets[complexity]) for _ in range(length))
    return password

def main():
    try:
        length = int(input("Enter the desired length of the password: "))
        
        print("\nSelect the complexity level of the password:")
        print("1: Lowercase letters")
        print("2: Lowercase and uppercase letters")
        print("3: Letters and digits")
        print("4: Letters, digits, and special characters")
        complexity = int(input("\nEnter the complexity level (1-4): "))
        
        password = generate_password(length, complexity)
        print("\nGenerated password:", password)
    
    except ValueError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
