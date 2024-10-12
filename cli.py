import argparse
from monitor import monitor_blockchain
from colorama import Fore

def print_title():
    # Create a star pattern for the title
    star_title = [
        "  *************   **       **          ****          *************   ****       **   *************   **       **   *************  ",
        "  *************   **       **         **  **         *************   ** **      **   *************    **     **    *************  ",
        "  **              **       **        **    **             ***        **  **     **   **                **   **     **  ",
        "  **              ***********       **      **            ***        **   **    **   ********           ** **      ********  ",
        "  **              ***********      ************           ***        **    **   **   ********            ***       ********  ",
        "  **              **       **     **          **          ***        **     **  **   **                  ***       **  ",
        "  *************   **       **    **            **    *************   **      ** **   *************       ***       *************  ",
        "  *************   **       **   **              **   *************   **       ****   *************       ***       *************  ",
    ]
    
    # Print the star title
    for line in star_title:
        print(Fore.RED + line)
    
    print(Fore.CYAN + "Made by: Harsh Dev\n")

def main():
    # Print the title
    print_title()

    # Prompt user to start or stop
    while True:
        command = input(Fore.BLUE + "Type 'start' to begin monitoring or 'stop' to exit: ").strip().lower()
        if command == 'start':
            blockchain_name = input(Fore.GREEN + "Enter the blockchain name (e.g., bitcoin): ").strip().lower()
            monitor_blockchain(blockchain_name)
        elif command == 'stop':
            print(Fore.RED + "Exiting the program. Goodbye!")
            break
        else:
            print(Fore.RED + "Invalid command! Please type 'start' or 'stop'.")

if __name__ == "__main__":
    main()