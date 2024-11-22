# Python program to swap three values

def swap_values(a, b, c):
    # Swapping the values
    a, b, c = b, c, a
    return a, b, c

# Example usage
x = input("Enter first value: ")
y = input("Enter second value: ")
z = input("Enter third value: ")

# Before swapping
print(f"Before swapping: x={x}, y={y}, z={z}")

# Swapping
x, y, z = swap_values(x, y, z)

# After swapping
print(f"After swapping: x={x}, y={y}, z={z}")
