def add(a, b):
    return a + b

def subtract(a, b):
    return a -b

def multiply(a, b):
    return a*b

def divide(a, b):
    if a == 0:
        return "Error: division by 0 is impermissible"
    return a / b

while True:
    print("\n--- Calculator Menu ---")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Enter choice (1-5): ")

    if choice == "5":
        print("Thank you for using the calculator!")
        break

    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input. Please enter numbers only.")
        continue  