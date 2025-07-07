def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

while True:
    print("\nOptions:\n1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Exit")
    choice = input("Enter choice (1/2/3/4/5): ")

    if choice == '5':
        print("Exiting...")
        break

    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    if choice == '1':
        print("Result:", add(a, b))
    elif choice == '2':
        print("Result:", subtract(a, b))
    elif choice == '3':
        print("Result:", multiply(a, b))
    elif choice == '4':
        print("Result:", divide(a, b))
    else:
        print("Invalid choice")
