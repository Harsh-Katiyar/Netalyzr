import os
import time
import hashlib
import requests
import webbrowser
from bs4 import BeautifulSoup


# Function to fetch website content
def get_website_content(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            print(f"Failed to fetch the website content. Status code: {response.status_code}")
            return None
    except Exception as e:
        print(f"Error fetching the website: {e}")
        return None


# Function to monitor entire website content
def monitor_website(url, interval=60):
    print(f"\nMonitoring entire website: {url}")
    previous_hash = None

    while True:
        content = get_website_content(url)
        if content:
            current_hash = hashlib.md5(content.encode('utf-8')).hexdigest()

            if previous_hash and current_hash != previous_hash:
                print(f"Website content updated at {time.ctime()}")
                print(f"Change detected on: {url}")
            else:
                print(f"No changes detected at {time.ctime()}")

            previous_hash = current_hash
        else:
            print("No content fetched.")

        time.sleep(interval)  # Wait for the next check


# Function to extract specific elements from a website
def extract_element(content, element, class_name=None, id_name=None):
    soup = BeautifulSoup(content, 'html.parser')

    if id_name:
        element_content = soup.find(element, id=id_name)
    elif class_name:
        element_content = soup.find(element, class_=class_name)
    else:
        element_content = soup.find(element)

    return element_content.get_text() if element_content else None


# Function to monitor specific elements on a website
def monitor_website_element(url, element, class_name=None, id_name=None, interval=60):
    print(f"\nMonitoring website element: {element} (class: {class_name}, id: {id_name}) on {url}")
    previous_hash = None

    while True:
        content = get_website_content(url)
        if content:
            extracted_content = extract_element(content, element, class_name, id_name)

            if extracted_content:
                current_hash = hashlib.md5(extracted_content.encode('utf-8')).hexdigest()

                if previous_hash and current_hash != previous_hash:
                    print(f"Website element updated at {time.ctime()}")
                    print(f"Change detected in {element} on: {url}")
                else:
                    print(f"No changes detected in {element} at {time.ctime()}")

                previous_hash = current_hash
            else:
                print(f"Element {element} not found.")
        else:
            print("No content fetched.")

        time.sleep(interval)


# Function to perform WHOIS lookup
def whois_lookup():
    print("\n=== WHOIS Lookup ===")

    # Ask for domain or IP input
    lookup_type = input("\nDo you want to lookup a domain or an IP address? (Enter 'domain' or 'IP'): ").strip().lower()

    if lookup_type == 'domain':
        domain = input("\nEnter the domain name for WHOIS lookup (e.g., example.com): ")
    elif lookup_type == 'ip':
        domain = input("\nEnter the IP address for WHOIS lookup (e.g., 8.8.8.8): ")
    else:
        print("Invalid input. Please enter 'domain' or 'IP'.")
        return

    print("\nChoose WHOIS service to gather domain/IP registration details:")
    print("1. whois.com")
    print("2. domaintools.com (with extended info)")

    choice = input("\nEnter your choice (1 or 2): ").strip()

    # Perform the basic WHOIS lookup
    if choice == '1':
        if lookup_type == 'domain':
            webbrowser.open(f"https://www.whois.com/whois/{domain}")
        else:
            webbrowser.open(f"https://www.whois.com/whois-ip/{domain}")

    elif choice == '2':
        api_key = input("\nDo you have a DomainTools API key? (yes/no): ").strip().lower()

        if api_key == 'yes':
            key = input("\nEnter your DomainTools API key: ").strip()
            use_domaintools_api(domain, key, lookup_type)
        else:
            print("\nOpening basic WHOIS lookup in DomainTools...")
            webbrowser.open(f"https://whois.domaintools.com/{domain}")

    else:
        print("Invalid choice!")


# Function to use DomainTools API for extended WHOIS information
def use_domaintools_api(domain, api_key, lookup_type):
    print("\nFetching extended WHOIS information using DomainTools API...")

    base_url = "https://api.domaintools.com/v1"
    if lookup_type == 'domain':
        endpoint = f"/whois/{domain}"
    else:
        endpoint = f"/whois/{domain}"

    url = base_url + endpoint
    params = {'api_username': 'your_username', 'api_key': api_key}

    try:
        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()
            print("\nWHOIS Data:")
            print(f"Domain: {data.get('domain', 'N/A')}")
            print(f"Registrar: {data.get('registrar', 'N/A')}")
            print(f"Created Date: {data.get('create_date', 'N/A')}")
            print(f"Updated Date: {data.get('update_date', 'N/A')}")
            print(f"Expiration Date: {data.get('expiration_date', 'N/A')}")
            print(f"Registrant: {data.get('registrant', 'N/A')}")
            print(f"Country: {data.get('registrant_country', 'N/A')}")
            print(f"Status: {data.get('status', 'N/A')}")
        else:
            print(f"Failed to fetch WHOIS data. Status code: {response.status_code}")
    except Exception as e:
        print(f"Error fetching data: {e}")


# Function to view WHOIS history
def whois_history():
    domain = input("\nEnter the domain name to view WHOIS history (e.g., example.com): ")
    print("\nOpening WHOIS history in DomainTools...")
    webbrowser.open(f"https://whois.domaintools.com/{domain}")


# Updated function for DNS information gathering
def dns_info():
    print("\n=== DNS Information Lookup ===")

    # Ask for domain input with a clear prompt
    domain = input("\nPlease enter the domain name for DNS lookup (e.g., example.com): ").strip()

    # Validate if the input is not empty
    if not domain:
        print("Invalid input! Domain name cannot be empty.")
        return

    print("\nChoose a DNS service to fetch DNS information:")
    print("1. DNS Watch")
    print("2. DNS Queries")

    # Ask user to choose a DNS lookup service
    choice = input("\nEnter your choice (1 or 2): ").strip()

    if choice == '1':
        dns_url = f"https://www.dnswatch.info/dns/dnslookup?la=en&host={domain}"
    elif choice == '2':
        dns_url = f"https://www.dnsqueries.com/en/dns_lookup.php?query={domain}"
    else:
        print("Invalid choice! Please select either option 1 or 2.")
        return

    # Ask user if they want to open the result in a browser
    open_browser = input("\nDo you want to open the DNS lookup result in your browser? (yes/no): ").strip().lower()

    if open_browser == 'yes':
        webbrowser.open(dns_url)
        print(f"\nOpening DNS information for {domain} in your browser...")
    else:
        print(f"\nYou can manually visit: {dns_url}")


# Function to gather information from Netcraft and Shodan
def netcraft_shodan_info():
    domain = input("\nEnter the domain name to search in Netcraft & Shodan (e.g., example.com): ").strip()
    netcraft_url = f"https://sitereport.netcraft.com/?url={domain}"
    shodan_url = f"https://www.shodan.io/search?query={domain}"

    print(f"\nNetcraft URL: {netcraft_url}")
    print(f"Shodan URL: {shodan_url}")

    open_links = input("\nDo you want to open these links in the browser? (yes/no): ").strip().lower()
    if open_links == 'yes':
        webbrowser.open(netcraft_url)
        webbrowser.open(shodan_url)
    else:
        print("Links not opened.")


# Main menu to select features
def main_menu():
    print("\n=== Website Footprinting Tool ===")
    print("1. Perform WHOIS Lookup")
    print("2. View WHOIS History")
    print("3. DNS Information Gathering")
    print("4. Gather Information from Netcraft & Shodan")
    print("5. Monitor Website for Updates")
    print("6. Monitor Specific Website Element for Updates")
    print("7. Exit")


# Main function to handle user input
def main():
    while True:
        main_menu()
        choice = input("\nEnter your choice: ").strip()

        if choice == '1':
            whois_lookup()
        elif choice == '2':
            whois_history()
        elif choice == '3':
            dns_info()
        elif choice == '4':
            netcraft_shodan_info()
        elif choice == '5':
            url = input("\nEnter the URL of the website to monitor (e.g., http://example.com): ").strip()
            interval = int(input("\nEnter the interval in seconds for checking updates (e.g., 60): ").strip())
            monitor_website(url, interval)
        elif choice == '6':
            url = input("\nEnter the URL of the website to monitor (e.g., http://example.com): ").strip()
            element = input("\nEnter the HTML element to monitor (e.g., p): ").strip()
            class_name = input("\nEnter the class name of the element (or leave empty): ").strip()
            id_name = input("\nEnter the id name of the element (or leave empty): ").strip()
            interval = int(input("\nEnter the interval in seconds for checking updates (e.g., 60): ").strip())
            monitor_website_element(url, element, class_name, id_name, interval)
        elif choice == '7':
            print("\nExiting...")
            break
        else:
            print("\nInvalid choice! Please try again.")


# Running the main function
if __name__ == "__main__":
    main()
