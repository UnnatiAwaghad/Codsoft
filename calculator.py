# Design a simple calculator with basic arithmetic operations.Prompt the user to input two numbers and an operation choice.
# Perform the calculation and display the result.

def calculator():
    n1 = int(input("Enter the number: "))
    n2 = int(input("Enter the number: "))

    print("\nSelect operation:")
    print("1) Addition(+)")
    print("2) Subtraction(-)")
    print("3) Multiplication(*)")
    print("4) Division (/)")

    choice = input("\nEnter your choice (1/2/3/4): ")

    if choice == '1':
        sum = n1 + n2
        print(f"\n{n1} + {n2} = {sum}")

    elif choice == '2':
        sub = n1 - n2
        print(f"\n{n1} - {n2} = {sub}")

    elif choice == '3':
        multiply = n1 * n2
        print(f"\n{n1} * {n2} = {multiply}")

    elif choice == '4':
        if n2 != 0: 
            result = n1 / n2
            print(f"\n{n1} / {n2} = {result}")
        else:
            print("\nError: Division by zero is not allowed.")
    else:
        print("\nInvalid input. Please choose a valid operation.")

calculator()
