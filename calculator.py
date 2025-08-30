def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a*b


def devide(a, b):
    if b != 0:
        return a / b
    else:
        return "Division by 0 is not allowed"


while True:
    print("\nMenu:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "5":
        print("Exiting...")
        break

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    if choice == "1":
        print("Result: ", add(num1, num2))

    elif choice == "2":
        print("Result: ", subtract(num1, num2))

    elif choice == "3":
        print("Result: ", multiply(num1, num2))

    elif choice == "4":
        print("Result: ", devide(num1, num2))

    else:
        print("Invalid choice, please try again.")
