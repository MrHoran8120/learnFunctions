import os
def clear_screen():
    # Windows
    if os.name == 'nt':
        os.system('cls')
    # Linux and macOS
    else:
        os.system('clear')

def printMenu():
    clear_screen()
    print("1. Option One")
    print("2. Option Two")
    print("3. Exit")


while True:
    printMenu()
    choice = input("Select an option (1-3): ")
    if choice == '1':
        print("You selected Option One.")
        input("Press Enter to continue...")
    elif choice == '2':
        print("You selected Option Two.")
        input("Press Enter to continue...")
    elif choice == '3':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
        input("Press Enter to continue...")
