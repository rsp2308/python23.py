def display_menu():
    print("Menu:")
    print("1. Display a message")
    print("2. Perform a calculation")
    print("3. Exit")

def display_message():
    print("Hello! This is a simple message.")

def perform_calculation():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter an operation (+, -, *, /): ")

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 != 0:
            result = num1 /num2
        else:
            result = "Error: Division by zero"
    else:
        result = "Invalid operation"

    print(f"The result is: {result}")

def main():
    while True:
        display_menu()
        choice = input("Choose an option (1, 2, or 3): ")

        if choice == '1':
            display_message()
        elif choice == '2':
            perform_calculation()
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
