import dns.resolver
import dns.reversename
import socket
import subprocess
import time
import webbrowser


# DNS Footprinting Function
def dns_footprinting_menu():
    print("\nDNS Footprinting Options:")
    print("1. Perform DNS Query (A, MX, TXT, NS, CNAME, SDA, SRV, PTR, RP, HINFO, etc.)")
    print("   Example: Retrieve different types of DNS records for a domain.")
    print("   - A: IP address of the domain")
    print("   - MX: Mail exchange servers")
    print("   - TXT: Text records")
    print("   - NS: Nameservers")
    print("   - CNAME: Canonical names")
    print("   - SDA: Service Discovery Agent records")
    print("   - SRV: Service location records")
    print("   - PTR: Pointer records for reverse DNS lookups")
    print("   - RP: Responsible person records")
    print("   - HINFO: Host information records")
    print("2. Reverse DNS Lookup")
    print("   Example: Find the domain name associated with a given IP address.")
    print("3. DNS Zone Transfer")
    print("   Example: Attempt to retrieve the entire DNS zone file from a domain's nameserver (if misconfigured).")
    print("4. DNSSEC Verification")
    print("   Example: Check if a domain has DNSSEC enabled, which adds extra security to DNS lookups.")
    print("5. Subdomain Enumeration")
    print("   Example: Discover subdomains (e.g., blog.example.com, mail.example.com) of a given domain.")
    print("6. DNS History Lookup")
    print("   Example: View historical DNS records for a domain, including previous IP addresses and nameservers.")
    print("7. Get Extra Details")
    print("   Example: View additional details and tools for network analysis.")
    print("0. Exit")

    choice = input("\nSelect an option: ")

    if choice == "1":
        perform_dns_query()
    elif choice == "2":
        reverse_dns_lookup()
    elif choice == "3":
        dns_zone_transfer()
    elif choice == "4":
        dnssec_verification()
    elif choice == "5":
        subdomain_enumeration()
    elif choice == "6":
        dns_history_lookup()
    elif choice == "7":
        get_extra_details()
    elif choice == "0":
        print("Exiting DNS Footprinting...")
    else:
        print("Invalid choice, please select a valid option.")
        dns_footprinting_menu()


# Function to perform DNS query (A, MX, TXT, NS, CNAME, SDA, SRV, PTR, RP, HINFO records)
def perform_dns_query():
    domain = input("\nEnter the domain name: ")
    record_type = input("Enter the DNS record type (A, MX, TXT, NS, CNAME, SDA, SRV, PTR, RP, HINFO): ").upper()

    try:
        answers = dns.resolver.resolve(domain, record_type)
        for rdata in answers:
            print(f"{record_type} record for {domain}: {rdata}")
    except Exception as e:
        print(f"Error performing DNS query: {e}")


# Function to perform Reverse DNS lookup
def reverse_dns_lookup():
    ip_address = input("\nEnter the IP address: ")
    try:
        addr = dns.reversename.from_address(ip_address)
        reversed_name = dns.resolver.resolve(addr, "PTR")
        for rdata in reversed_name:
            print(f"Reverse DNS lookup result: {rdata}")
    except Exception as e:
        print(f"Error performing reverse DNS lookup: {e}")


# Function to attempt DNS Zone Transfer
def dns_zone_transfer():
    domain = input("\nEnter the domain name for zone transfer: ")
    try:
        ns_records = dns.resolver.resolve(domain, 'NS')
        for ns in ns_records:
            ns_ip = socket.gethostbyname(str(ns))
            print(f"Attempting zone transfer on nameserver {ns} ({ns_ip})")
            transfer = dns.query.xfr(ns_ip, domain)
            zone = dns.zone.from_xfr(transfer)
            for name, node in zone.nodes.items():
                print(zone[name].to_text(name))
    except Exception as e:
        print(f"Zone transfer failed or restricted: {e}")


# Function to check DNSSEC
def dnssec_verification():
    domain = input("\nEnter the domain name to check DNSSEC: ")
    try:
        dnssec_info = dns.resolver.resolve(domain, 'DNSKEY')
        if dnssec_info:
            print(f"DNSSEC is enabled for {domain}")
            for rdata in dnssec_info:
                print(f"DNSSEC key: {rdata}")
        else:
            print(f"DNSSEC is not enabled for {domain}")
    except Exception as e:
        print(f"Error checking DNSSEC: {e}")


# Function to enumerate subdomains with detailed process updates
def subdomain_enumeration():
    domain = input("\nEnter the domain name for subdomain enumeration: ")

    print(f"\nStarting subdomain enumeration for domain: {domain}")

    sublist3r_command = f"sublist3r -d {domain}"
    print(f"Running command: {sublist3r_command}")

    start_time = time.time()

    try:
        print("\nExecuting the subdomain enumeration command. This may take some time...")
        process = subprocess.Popen(sublist3r_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        while process.poll() is None:
            output = process.stdout.readline().decode('utf-8')
            if output:
                print(output.strip())
            time.sleep(1)

        result, _ = process.communicate()
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"\nTime taken for subdomain enumeration: {elapsed_time:.2f} seconds")

        if result:
            print(f"\nSubdomains found for {domain}:\n{result.decode('utf-8')}")
        else:
            print(f"\nNo subdomains found for {domain}.")

    except subprocess.CalledProcessError as e:
        print(f"Error during subdomain enumeration: {e}")

    except Exception as e:
        print(f"Unexpected error: {e}")


# Function to perform DNS history lookup
def dns_history_lookup():
    domain = input("\nEnter the domain name for DNS history lookup: ")
    url = f"https://securitytrails.com/domain/{domain}/dns"
    try:
        print(f"Fetching DNS history for {domain}...")
        print(f"Open this link to view DNS history: {url}")
        open_in_browser = input("Do you want to open this link in your browser? (yes/no): ")
        if open_in_browser.lower() == 'yes':
            webbrowser.open(url)
    except Exception as e:
        print(f"Error fetching DNS history: {e}")


# Function to get extra details from a link
def get_extra_details():
    link = "https://mxtoolbox.com/NetworkTools.aspx"
    print(f"\nTo get additional details and tools for network analysis, visit the following link: {link}")
    open_in_browser = input("Do you want to open this link in your browser? (yes/no): ")
    if open_in_browser.lower() == 'yes':
        webbrowser.open(link)
    else:
        print("Link not opened. Returning to the main menu.")


# Call the DNS footprinting menu
if __name__ == "__main__":
    dns_footprinting_menu()
