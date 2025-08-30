def get_factorial(num):
    result = 1
    for i in range(int(num)):
        result *= (i+1)

    return result


while True:
    print("\nMenu:")
    print("1. Enter the number you want to calculate factorial of:")
    print("2. Press to 'q' to exit")

    num = input("Enter your choice: ")

    if num == 'q' or num == 'Q':
        break
    else:
        print(get_factorial(num))
