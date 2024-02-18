# Calculator
from art import logo
# Add
def add(n1, n2):
    return n1 + n2

# Subtract
def subtract(n1,n2):
    return n1 - n2

# Multiply
def multiply(n1,n2):
    return n1 * n2

# Divide
def divide(n1,n2):
    return n1 / n2

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
}

def calculator():
    print(logo)
    num1 = float(input("What's the first number?: "))
    for operator in operations:
        print(operator)
    to_continue = True

    while to_continue == True:
        operation_operator = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        calculation_function = operations[operation_operator]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_operator} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation.: ") == "y":
            num1 = answer
        else:
            to_continue = False
            calculator()

calculator()