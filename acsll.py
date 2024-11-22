# Python program to find ASCII values of all alphabets

def print_ascii_values():
    # Printing ASCII values for uppercase alphabets
    for i in range(65, 91):
        print(f"{chr(i)}: {i}")
    
    # Printing ASCII values for lowercase alphabets
    for i in range(97, 123):
        print(f"{chr(i)}: {i}")

print("ASCII values of all uppercase and lowercase alphabets:")
print_ascii_values()
