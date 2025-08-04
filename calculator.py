def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero."
    return a / b

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main():
    print("📟 Welcome to the CLI Calculator!")

    while True:
        print("\nChoose an operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Dividison (/)")
        print("5. Exit")

        choice = input("Enter choice (1/2/3/4/5): ").strip()

        if choice == '5':
            print("👋 Exiting calculator. Thank you!")
            break

        if choice in ['1', '2', '3', '4']:
            num1 = get_number("Enter first number: ")
            num2 = get_number("Enter second number: ")

            if choice == '1':
                result = add(num1, num2)
            elif choice == '2':
                result = subtract(num1, num2)
            elif choice == '3':
                result = multiply(num1, num2)
            elif choice == '4':
                result = divide(num1, num2)

            print(f"✅ Result: {result}")
        else:
            print("❌ Invalid choice. Please select from 1 to 5.")

if __name__ == "__main__":
    main()
