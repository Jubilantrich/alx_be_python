def divide_number():

    
    try:
        num1= float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result=num1/num2
        print(f"Result: {result}")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except ValueError:
         print("Error: Invalid input. Please enter numbers.")
    
divide_number()