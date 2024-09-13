# Main Netalyzr file

from modules import search_engine, social_networking
from modules import websites, email, competitive_intelligence
from modules import whois_lookup, dns_lookup, network, social_engineering, automated_tool
from modules import google_hacking  # Import the Google hacking module

def display_menu():
    """Display the main menu for the Netalyzr tool."""
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
    """Handle the user's choice by running the appropriate module."""
    if choice == '1':
        print("Launching Search Engines module...")
        search_engine.search_engines_module()
    elif choice == '2':
        print("Launching Advanced Google Hacking Techniques module...")
        google_hacking.main()  # Call the main function from google_hacking module
    elif choice == '3':
        print("Launching Social Networking Sites module...")
        social_networking.social_networking_module()
    elif choice == '4':
        print("Launching Websites module...")
        websites.websites_module()
    elif choice == '5':
        print("Launching Email module...")
        email.email_module()
    elif choice == '6':
        print("Launching Competitive Intelligence module...")
        competitive_intelligence.competitive_intelligence_module()
    elif choice == '7':
        print("Launching WHOIS module...")
        whois_lookup.whois_lookup()  # Call the WHOIS module function
    elif choice == '8':
        print("Launching DNS module...")
        dns_lookup.dns_lookup_module()
    elif choice == '9':
        print("Launching Network module...")
        network.network_module()
    elif choice == '10':
        print("Launching Social Engineering module...")
        social_engineering.social_engineering_module()
    elif choice == '11':
        print("Launching Automated In-Build Tool...")
        automated_tool.automated_tool_module()
    elif choice == '0':
        print("Exiting...")
        exit()
    else:
        print("Invalid choice. Please select a number between 0 and 11.")

def main():
    """Main function to display the menu and handle user inputs."""
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        handle_choice(choice)

if __name__ == "__main__":
    main()
