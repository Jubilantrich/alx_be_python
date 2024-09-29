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
        choice = input("Enter your choice: ")

        if choice == '1':
            itermname = input("Enter your itermn to add: ")
            shopping_list.append(itermname)
            pass
        elif choice == '2':
            # Prompt for and remove an item
            itermname = input("Enter your iterm to remove: ")
            if itermname in shopping_list:
                shopping_list.remove(itermname)
            else: print("Item can not be found in the list")

            pass
        elif choice == '3':
            # Display the shopping list
            print(shopping_list) 
            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()  