from guess_the_number import *
from interface_system import show_information

def main():
    # Show information about the user
    show_information()
    menu()

    # Select option
    select_option()

try:
    main()
except KeyboardInterrupt:
    print('\nGood bye, I hope you will come soon')