import time


def add(a, b):
    answer = a + b
    # Use ANSI escape codes to change text color
    print(f'\033[92m{a} + {b} = {answer}\033[0m')


def sub(a, b):
    answer = a - b
    # print('---------------')
    print(f'\033[92m{a} - {b} = {answer}\033[0m')


def mul(a, b):
    print("Multiplication in progress:")
    for i in range(1, 11):
        time.sleep(0.1)  # Simulate some work being done
        print("\r[" + "=" * i + " " * (10 - i) +
              f"] {i * 10}%", end='', flush=True)
    print()  # Print a new line to separate progress bar from result
    answer = a * b
    print(f'\033[92m{a} * {b} = {answer}\033[0m')


def div(a, b):
    answer = a / b
    print(f'\033[92m{a} / {b} = {answer}\033[0m')


while True:  # infinite loop
    print("""A. Addition
B. Subtraction
C. Multiplication
D. Division
E. Exit""")

    choice = input("Enter your choice: ")

    if choice.upper() == 'A':
        print("Addition")
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        add(a, b)
    elif choice.upper() == 'B':
        print("Subtraction")
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        sub(a, b)
    elif choice.upper() == 'C':
        print("Multiplication")
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        mul(a, b)
    elif choice.upper() == 'D':
        print("Division")
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        div(a, b)
    elif choice.upper() == 'E':
        print("Program Ended")
        break  # Exit the loop and end the program
        # quit()
    else:
        # \033[91m changes text color to red
        print(
            "\033[91mInvalid choice. Please select a valid option (A, B, C, D, or E).\033[0m")  # \033[0m reset the color
