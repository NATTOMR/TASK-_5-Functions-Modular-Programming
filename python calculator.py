"""
Modular Calculator Program
TASK 5: Functions & Modular Programming
"""

def add(a=0, b=0):
    """
    Returns the sum of two numbers.
    """
    return a + b


def subtract(a=0, b=0):
    """
    Returns the difference between two numbers.
    """
    return a - b


def multiply(a=0, b=0):
    """
    Returns the product of two numbers.
    """
    return a * b


def divide(a=0, b=1):
    """
    Returns the division of two numbers.
    Handles division by zero.
    """
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b


def get_numbers():
    """
    Prompts the user to enter two numbers.
    """
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    return a, b


def show_menu():
    """
    Displays calculator options.
    """
    print("\nCalculator Menu")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")


def main():
    """
    Main function to run the calculator.
    """
    while True:
        show_menu()
        choice = input("Choose an option (1-5): ")

        if choice == "5":
            print("Exiting calculator. Goodbye!")
            break

        if choice not in ["1", "2", "3", "4"]:
            print("Invalid choice. Please try again.")
            continue

        num1, num2 = get_numbers()

        if choice == "1":
            result = add(num1, num2)
        elif choice == "2":
            result = subtract(num1, num2)
        elif choice == "3":
            result = multiply(num1, num2)
        elif choice == "4":
            result = divide(num1, num2)

        print("Result:", result)


# Run the program
if __name__ == "__main__":
    main()
