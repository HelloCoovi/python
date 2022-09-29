from art import logo

print(logo)

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,    
}

def calculator():
    should_continue = True
    num1 = float(input("What's the first number?: "))
    
    for i in operations:
        print(i)
    
    while should_continue:
        operation = input("Pick an operation: ")
        num2 = float(input("What's the second number?: "))
        
        calculation_function = operations[operation]
        reslut = calculation_function(num1, num2)
        
        print(f"{num1} {operation} {num2} = {reslut}")
    
        if input("Type 'y' to continue calculating with {reslut}, or type 'n' to exit.: ") == "y":
            num1 = reslut
        else:
            should_continue = False
            calculator()


calculator()