from datetime import datetime, timedelta

def display_current_datetime():
    # Get the current date and time
    current_date = datetime.now()

     # Format the date and time as "YYYY-MM-DD HH:MM:SS"
    date_formatted = current_date.strftime("%Y-%m-%d %H:%M:%S")
    
    # Print the formatted date and time
    print("Current Date and Time:", date_formatted)

# Call the function to display the current date and time
display_current_datetime()

def calculate_future_date():
    # Get the current date and time
    current_date = datetime.now()
    
    # Prompt the user to enter a number of days
    number_of_days = int(input("Enter the number of days to add to the current date: "))
    
    # Calculate the future date by adding the number of days to the current date
    future_date = current_date + timedelta(days=number_of_days)
    
    # Format the future date as "YYYY-MM-DD"
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    
    # Print the future date
    print("Future Date:", formatted_future_date)

# Call the function to calculate and display the future date
calculate_future_date()