# define a function perform_operation
def perform_operation(num1, num2, operation):
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if  num2 == 0:
            return print("We can nor divide by zero")
        else: 
            return num1 / num2
    else:
        return print("No proper operation inputted")