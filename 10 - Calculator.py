def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def calculator(operation,n1,n2):
    result=operations[operation](n1,n2)
    return result

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


logo = r"""
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""





while True:     #General loop
    print(logo)
    n1=float(input("What's the first number?: "))

    while True:  #This loops the operation and second number inputs in case you want to accumulate
        while True: # This checks if you enter a valid character
            operation=input("+\n-\n*\n/\nPick an operation: ")
            if operation in operations:
                break
        n2=float(input("What's the next number?: "))
        result = calculator(operation, n1, n2)
        print(n1, operation, n2, " = ", result)
        if input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")=="n":
            print("\n" * 20)
            break
        else:
            n1=result