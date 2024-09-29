def display_menu():
    print("Shopping list manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()

        choice = int(input("Enter your choice: "))

        if choice == 1:
            # Prompt for and add an item

            itermname = input ("Enter the item to add: \n")

            shopping_list.append(itermname)
            
        elif choice == 2:
            # Prompt for and remove an item

            itermname = input("Enter the item to remove: ")

            if itermname in shopping_list:
                shopping_list.remove(itermname)
            else: print("Item can not be found in the list")

            
        elif choice == 3:
            # Display the shopping list
            print(shopping_list) 
            
        elif choice == 4:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()  