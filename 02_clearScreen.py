import os
def clear_screen():
    # Windows
    if os.name == 'nt':
        os.system('cls')
    # Linux and macOS
    else:
        os.system('clear')

clear_screen()