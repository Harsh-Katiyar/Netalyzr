# Importing each module from the modules folder

from modules import search_engine, google_hacking, social_networking
from modules import websites, email, competitive_intelligence
from modules import whois_lookup, dns_lookup, network, social_engineering, automated_tool

def display_menu():
    print("Welcome to Netalyzr!")
    print("Select a module to explore:")
    print("1) Search Engines")
    print("2) Advanced Google Hacking Techniques")
    print("3) Social Networking Sites")
    print("4) Websites")
    print("5) Email")
    print("6) Competitive Intelligence")
    print("7) WHOIS")
    print("8) DNS")
    print("9) Network")
    print("10) Social Engineering")
    print("11) Automated In-Build Tool")
    print("0) Exit")

def handle_choice(choice):
    if choice == '1':
        print("Launching Search Engines module...")
        search_engine.search_engines_module()
        # Add functionality here
    elif choice == '2':
        print("Launching Advanced Google Hacking Techniques module...")
        # Add functionality here
    elif choice == '3':
        print("Launching Social Networking Sites module...")
        # Add functionality here
    elif choice == '4':
        print("Launching Websites module...")
        # Add functionality here
    elif choice == '5':
        print("Launching Email module...")
        # Add functionality here
    elif choice == '6':
        print("Launching Competitive Intelligence module...")
        # Add functionality here
    elif choice == '7':
        print("Launching WHOIS module...")
        whois_lookup.whois_lookup()
        # Add functionality here
    elif choice == '8':
        print("Launching DNS module...")
        # Add functionality here
    elif choice == '9':
        print("Launching Network module...")
        # Add functionality here
    elif choice == '10':
        print("Launching Social Engineering module...")
        # Add functionality here
    elif choice == '11':
        print("Launching Automated In-Build Tool...")
        # Add functionality here
    elif choice == '0':
        print("Exiting...")
        exit()
    else:
        print("Invalid choice. Please select a number between 0 and 11.")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        handle_choice(choice)

if __name__ == "__main__":
    main()
