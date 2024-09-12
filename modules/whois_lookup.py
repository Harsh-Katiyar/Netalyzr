import webbrowser
import whois


def display_whois_in_terminal(domain):
    """Gather WHOIS data and display it in the terminal."""
    try:
        w = whois.whois(domain)
        print("\nWHOIS Data:")
        print(f"Domain: {w.domain_name}")
        print(f"Registrar: {w.registrar}")
        print(f"Creation Date: {w.creation_date}")
        print(f"Expiration Date: {w.expiration_date}")
        print(f"Updated Date: {w.updated_date}")
        print(f"Name Servers: {w.name_servers}")
        print(f"Status: {w.status}")
        # Display more details if needed
    except Exception as e:
        print(f"An error occurred while fetching WHOIS data: {e}")


def whois_lookup():
    """Main function to handle WHOIS lookup and user choices."""
    # Prompt user for domain and IP address
    domain = input("Enter domain: ")


    # Provide user options
    print("\nSelect an option:")
    print("1) Gather WHOIS data in the terminal.")
    print("2) WHOIS lookup links for your browser.")

    option = input("Enter your choice (1 or 2): ")

    if option == '1':
        # Gather WHOIS data in the terminal
        display_whois_in_terminal(domain)
    elif option == '2':
        # Provide WHOIS lookup service links
        print("\nHere are the WHOIS lookup services for the domain:")
        print(f"1) https://www.whois.com/whois/{domain}")
        print(f"2) https://whois.domaintools.com/{domain}")

        # Ask user if they want to open these links
        open_links = input("Do you want to open these links in your browser? (yes/no): ")

        if open_links.lower() == 'yes':
            # Open the links in the default web browser
            webbrowser.open(f"https://www.whois.com/whois/{domain}")
            webbrowser.open(f"https://whois.domaintools.com/{domain}")
            print("Opening links in your browser...")
        else:
            print("Links not opened. Exiting...")
    else:
        print("Invalid choice. Please enter 1 or 2.")


if __name__ == "__main__":
    whois_lookup()
