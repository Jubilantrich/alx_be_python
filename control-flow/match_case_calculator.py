num1= float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
opr = input("Choose the operation (+, -, *, /): ")

match opr:
    case "+":
        result=num1+num2
    case "-":
        result = num1 - num2
        print("The result is", result)
    case "*":
        result = num1 * num2
        print("The result is", result)
    case "/":
        if  num2 == 0:
            print("Cannot divide by zero")
        else:
            result=num1/num2
            print("The result is", result)
    case _:
        print("Your input not in the required operations listed")



