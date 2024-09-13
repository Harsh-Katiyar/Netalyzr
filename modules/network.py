import requests
import nmap
import socket
import ipaddress
import subprocess
import platform
import whois

def is_ip(address):
    """Check if the address is an IP address."""
    try:
        ipaddress.ip_address(address)
        return True
    except ValueError:
        return False

def ip_lookup():
    """Perform IP address lookup using ipinfo.io."""
    ip = input("Enter IP address: ")
    if not is_ip(ip):
        print("Invalid IP address format.")
        return
    try:
        response = requests.get(f"https://ipinfo.io/{ip}/json")
        print("IP Lookup Result:")
        print(response.json())
    except Exception as e:
        print(f"Error: {e}")

def domain_lookup():
    """Perform domain lookup using WHOIS."""
    domain = input("Enter domain name: ")
    try:
        domain_info = whois.whois(domain)
        print("Domain Lookup Result:")
        print(domain_info)
    except Exception as e:
        print(f"Error: {e}")

def subnet_scan():
    """Scan a subnet to find active hosts."""
    subnet = input("Enter subnet (e.g., 192.168.1.0/24): ")
    try:
        nm = nmap.PortScanner()
        nm.scan(hosts=subnet, arguments='-sn')
        print("Active hosts in subnet:")
        print(nm.all_hosts())
    except Exception as e:
        print(f"Error: {e}")

def port_scan():
    """Scan all ports of a given IP address or domain."""
    target = input("Enter IP address or domain name: ")
    if is_ip(target):
        try:
            nm = nmap.PortScanner()
            nm.scan(target, arguments='-p-')
            print("Open ports on the target:")
            print(nm[target]['tcp'].keys())
        except Exception as e:
            print(f"Error: {e}")
    else:
        print("Invalid IP address format.")

def service_enum():
    """Enumerate services running on open ports of a given IP address or domain."""
    target = input("Enter IP address or domain name: ")
    if is_ip(target):
        try:
            nm = nmap.PortScanner()
            nm.scan(target, arguments='-sV')
            print("Services running on the target:")
            print(nm[target]['tcp'])
        except Exception as e:
            print(f"Error: {e}")
    else:
        print("Invalid IP address format.")

def os_fingerprint():
    """Perform OS fingerprinting on a given IP address or domain."""
    target = input("Enter IP address or domain name: ")
    if is_ip(target):
        try:
            nm = nmap.PortScanner()
            nm.scan(target, arguments='-O')
            print("OS Fingerprinting Result:")
            print(nm[target]['osmatch'])
        except Exception as e:
            print(f"Error: {e}")
    else:
        print("Invalid IP address format.")

def reverse_dns():
    """Perform reverse DNS lookup for a given IP address."""
    ip = input("Enter IP address: ")
    if is_ip(ip):
        try:
            hostname, _, _ = socket.gethostbyaddr(ip)
            print(f"Reverse DNS Result: Hostname for IP {ip} is {hostname}")
        except Exception as e:
            print(f"Error: {e}")
    else:
        print("Invalid IP address format.")

def network_mapping():
    """Map a network to find active hosts."""
    subnet = input("Enter subnet (e.g., 192.168.1.0/24): ")
    try:
        nm = nmap.PortScanner()
        nm.scan(hosts=subnet, arguments='-sP')
        print("Hosts in the subnet:")
        print(nm.all_hosts())
    except Exception as e:
        print(f"Error: {e}")

def address_ranges():
    """List all address ranges within a given subnet."""
    subnet = input("Enter subnet (e.g., 192.168.1.0/24): ")
    try:
        network = ipaddress.ip_network(subnet)
        print("Network address ranges:")
        for ip in network.hosts():
            print(ip)
    except Exception as e:
        print(f"Error: {e}")

def hostnames():
    """Resolve hostnames for IP addresses in a subnet."""
    subnet = input("Enter subnet (e.g., 192.168.1.0/24): ")
    try:
        network = ipaddress.ip_network(subnet)
        for ip in network.hosts():
            try:
                hostname = socket.gethostbyaddr(str(ip))[0]
                print(f"{ip} - Hostname: {hostname}")
            except socket.herror:
                print(f"{ip} - No hostname found")
    except Exception as e:
        print(f"Error: {e}")

def exposed_hosts():
    """Find hosts with exposed ports in a given subnet."""
    subnet = input("Enter subnet (e.g., 192.168.1.0/24): ")
    try:
        nm = nmap.PortScanner()
        nm.scan(hosts=subnet, arguments='-sS')
        exposed_hosts = [host for host in nm.all_hosts() if nm[host].all_tcp()]
        print("Exposed hosts:")
        for host in exposed_hosts:
            print(host)
    except Exception as e:
        print(f"Error: {e}")

def os_version_info():
    """Retrieve service and version information for a given IP address or domain."""
    target = input("Enter IP address or domain name: ")
    if is_ip(target):
        try:
            nm = nmap.PortScanner()
            nm.scan(target, arguments='-sV')
            print("Service and version information:")
            for port in nm[target]['tcp']:
                print(f"Port {port}: {nm[target]['tcp'][port]['name']} {nm[target]['tcp'][port]['version']}")
        except Exception as e:
            print(f"Error: {e}")
    else:
        print("Invalid IP address format.")

def path_state():
    """Ping and perform traceroute for a given IP address."""
    ip = input("Enter IP address: ")
    if is_ip(ip):
        print("Pinging host...")
        try:
            if platform.system() == 'Windows':
                response = subprocess.run(['ping', ip], capture_output=True, text=True)
            else:
                response = subprocess.run(['ping', '-c', '4', ip], capture_output=True, text=True)
            print(response.stdout)
        except Exception as e:
            print(f"Error: {e}")

        print("Traceroute...")
        try:
            if platform.system() == 'Windows':
                response = subprocess.run(['tracert', ip], capture_output=True, text=True)
            else:
                response = subprocess.run(['traceroute', ip], capture_output=True, text=True)
            print(response.stdout)
        except Exception as e:
            print(f"Error: {e}")
    else:
        print("Invalid IP address format.")

def app_backend_structure():
    """Analyze application and backend server structures for a given IP address or domain."""
    target = input("Enter IP address or domain name: ")
    if is_ip(target):
        try:
            nm = nmap.PortScanner()
            nm.scan(target, arguments='-sS -sV')
            print("Backend structure:")
            for port in nm[target]['tcp']:
                print(f"Port {port}: {nm[target]['tcp'][port]['name']}")
        except Exception as e:
            print(f"Error: {e}")
    else:
        print("Invalid IP address format.")
def install_nmap():
    os_type = platform.system().lower()
    if os_type == 'windows':
        print("To install Nmap on Windows:")
        print("1. Download the Nmap installer from https://nmap.org/download.html.")
        print("2. Run the installer and follow the on-screen instructions.")
        print("3. After installation, ensure Nmap is added to your system PATH.")
        print("   - Go to 'Environment Variables' in System Properties.")
        print("   - Edit the 'Path' variable and add the directory where Nmap is installed (e.g., C:\\Program Files (x86)\\Nmap).")
        print("4. Restart your command prompt or terminal.")
    elif os_type == 'linux':
        print("To install Nmap on Linux:")
        print("1. Open your terminal.")
        print("2. Install Nmap using your package manager. For example:")
        print("   - On Debian-based systems (e.g., Ubuntu): sudo apt-get install nmap")
        print("   - On Red Hat-based systems (e.g., Fedora): sudo yum install nmap")
        print("3. Verify the installation by running: nmap --version")
    else:
        print("Unsupported OS. Please manually install Nmap from https://nmap.org/download.html")

def network_menu():
    print("Network Footprinting Tool")
    print("1. IP Address Lookup")
    print("2. Subnet Scanning")
    print("3. Port Scanning")
    print("4. Service Enumeration")
    print("5. OS Fingerprinting")
    print("6. Reverse DNS Lookup")
    print("7. Network Mapping")
    print("8. Network Address Ranges")
    print("9. Hostnames")
    print("10. Exposed Hosts")
    print("11. OS and Application Version Information")
    print("12. Path State of Hosts and Applications")
    print("13. Application and Backend Server Structures")
    print("14. Install Nmap")
    print("15. Exit")

    choice = input("Enter your choice: ")
    if choice == '1':
        ip_lookup()
    elif choice == '2':
        subnet_scan()
    elif choice == '3':
        port_scan()
    elif choice == '4':
        service_enum()
    elif choice == '5':
        os_fingerprint()
    elif choice == '6':
        reverse_dns()
    elif choice == '7':
        network_mapping()
    elif choice == '8':
        address_ranges()
    elif choice == '9':
        hostnames()
    elif choice == '10':
        exposed_hosts()
    elif choice == '11':
        os_version_info()
    elif choice == '12':
        path_state()
    elif choice == '13':
        app_backend_structure()
    elif choice == '14':
        install_nmap()
    elif choice == '15':
        print("Exiting...")
        exit()
    else:
        print("Invalid choice. Please try again.")

if __name__ == "__main__":
    while True:
        network_menu()
