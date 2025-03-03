# Function to add two numbers
def add(x, y):
    return x + y

# Function to subtract two numbers
def subtract(x, y):
    return x - y

# Function to multiply two numbers
def multiply(x, y):
    return x * y

# Function to divide two numbers
def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

# Function to display the menu of operations
def display_menu():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

# Function to run the calculator
def calculator():
    while True:
        display_menu()

        # Get user choice
        choice = input("Enter choice (1/2/3/4/5): ")

        # Check if the user wants to exit
        if choice == '5':
            print("Exiting calculator. Goodbye!")
            break

        # Ensure the user input is a valid number
        if choice not in ['1', '2', '3', '4']:
            print("Invalid input! Please select a valid option.")
            continue

        # Get user input for numbers
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid number input. Please enter numeric values.")
            continue

        # Perform the selected operation
        if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        elif choice == '3':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        elif choice == '4':
            print(f"{num1} / {num2} = {divide(num1, num2)}")
        else:
            print("Invalid choice, please try again.")

# Run the calculator program
calculator()
