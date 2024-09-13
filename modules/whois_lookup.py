import re
import whois
import webbrowser


def display_whois_in_terminal(domain):
    """Gather WHOIS data for a domain and display it in the terminal."""
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
    except Exception as e:
        print(f"An error occurred while fetching WHOIS data: {e}")


def whois_lookup():
    """Main function to handle WHOIS lookup for domain or IP and user choices."""

    # Ask the user whether they want to look up a domain or an IP
    print("Do you want to perform a WHOIS lookup for:")
    print("1) Domain")
    print("2) IP Address")
    choice = input("Enter 1 for Domain or 2 for IP: ").strip()

    if choice == '1':
        # WHOIS lookup for domain
        domain = input("Enter domain: ").strip()

        print("\nSelect an option:")
        print("1) Gather WHOIS data in the terminal.")
        print("2) WHOIS lookup links for your browser.")

        option = input("Enter your choice (1 or 2): ").strip()

        if option == '1':
            display_whois_in_terminal(domain)
        elif option == '2':
            print("\nHere are the WHOIS lookup services for the domain:")
            print(f"1) https://www.whois.com/whois/{domain}")
            print(f"2) https://whois.domaintools.com/{domain}")

            open_links = input("Do you want to open these links in your browser? (yes/no): ").strip().lower()

            if open_links == 'yes':
                webbrowser.open(f"https://www.whois.com/whois/{domain}")
                webbrowser.open(f"https://whois.domaintools.com/{domain}")
                print("Opening links in your browser...")
            else:
                print("Links not opened. Exiting...")
        else:
            print("Invalid choice. Please enter 1 or 2.")

    elif choice == '2':
        # WHOIS lookup for IP
        ip = input("Enter IP address: ").strip()

        # Validate the IP address using regex
        ip_pattern = re.compile(
            r"^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$")
        if ip_pattern.match(ip):
            ip_whois_url = f"https://whois.urih.com/record/{ip}"
            print(f"\nHere is the WHOIS lookup link for the IP address: {ip}")
            print(f"URIH WHOIS Lookup: {ip_whois_url}")

            # Ask if the user wants to open the IP WHOIS link in the browser
            open_ip_in_browser = input(
                "Do you want to open the IP WHOIS link in your browser? (yes/no): ").strip().lower()

            if open_ip_in_browser == 'yes':
                webbrowser.open(ip_whois_url)
                print("Opening IP WHOIS link in your browser...")
            else:
                print("Link not opened. Exiting...")
        else:
            print("Invalid IP address format. Please try again.")
    else:
        print("Invalid choice. Please enter 1 for Domain or 2 for IP.")


if __name__ == "__main__":
    whois_lookup()
