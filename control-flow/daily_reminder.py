task = str(input("Enter your task: "))
priority = input("Priority (high/medium/low): ")
time_bound = bool(input("Is it time-bound? (yes/no): "))

match priority:
    case "high":
        if time_bound == "yes":
            print("Reminder: 'Finish project report' is a high priority task that requires immediate attention today!")
        elif time_bound =="no":
            print("Reminder: 'Finish project report' is a high priority Consider completing it when you have free time.")
    case "Meduim":
        if time_bound == "yes":
            print("Reminder: 'Finish project report' is a low priority task that requires immediate attention today!")
        elif time_bound =="no":
            print("Note: 'Read a book' is a low priority task. Consider completing it when you have free time.")
    case "low":
        if time_bound == "yes":
            print("Reminder: 'Finish project report' is a low priority task that requires immediate attention today!")
        elif time_bound =="no":
            print("Note: 'Read a book' is a low priority task. Consider completing it when you have free time.")
    case _:
       print("we dont understand your request") 