class ValueTooHighError(Exception):
    pass

def check_number():
    try:
        num = int(input("Enter a number: "))
        if num > 100:
            raise ValueTooHighError("Error: The value is too high!")
        else:
            print(f"The number is {num}, which is within the allowed range.")
    except ValueTooHighError as e:
        print(e)
    except ValueError:
        print("Error: Invalid input. Please enter a number.")
    
check_number()