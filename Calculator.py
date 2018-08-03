import operator
import sys


def retry():
    try:
        global num1, num2
        num1 = float(input("Please enter the first number: "))
        num2 = float(input("Now the second number: "))
    except ValueError:
        print("That is not a number, please retry.")
        retry()


while True:

    print("----------------------------------------------------")
    print("\'+\' for addition,\n"
          "\'-\' for subtraction,\n"
          "\'*\' for multiplication,\n"
          "\'/\' for division,\n"
          "\'powt\' for potency,\n"
          "\'//\' for floor division,\n"
          "and \'%\' for modulo.\n"
          "Type the symbol for the operation you want to do:\n"
          "(Type \'quit\' to end the program.)")
    print("----------------------------------------------------")
    user_input = input("Select the operator: ")
    if user_input == "quit":
        print("Bye!")
        sys.exit()

    try:
        num1 = float(input("Please enter the first number: "))
        num2 = float(input("Now the second number: "))
    except ValueError:
        print("That is not a number, please retry.")
        retry()

    if user_input == "+":
        result = str(operator.add(num1, num2))
        print(num1, "+", num2, "=", result)
    elif user_input == "-":
        result = str(operator.sub(num1, num2))
        print(num1, "-", num2, "=", result)
    elif user_input == "*":
        result = str(operator.mul(num1, num2))
        print(num1, "*", num2, "=", result)
    elif user_input == "/":
        result = str(operator.truediv(num1, num2))
        print(num1, "/", num2, "=", result)
    elif user_input == "powt":
        result = str(operator.pow(num1, num2))
        print(num1, "^", num2, "=", result)
    elif user_input == "//":
        result = str(operator.floordiv(num1, num2))
        print(num1, "//", num2, "=", result)
    elif user_input == "%":
        result = str(operator.mod(num1, num2))
        print(num1, "%", num2, "=", result)
    else:
        print("-----------------------------------------------------------")
        print("Unknown operator. Please select a listed type of operation.")
