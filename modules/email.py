import re
import smtplib
import dns.resolver
import requests
import json

# Function to validate email format
def validate_email_format(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if re.match(pattern, email):
        return True
    else:
        return False

# Function to resolve MX records for a domain
def check_mx_record(domain):
    try:
        mx_records = dns.resolver.resolve(domain, 'MX')
        return [str(record.exchange) for record in mx_records]
    except dns.resolver.NoAnswer:
        return None
    except Exception as e:
        return str(e)

# Function to check email in breach databases using an API key
def check_data_breach(email, api_key):
    try:
        api_url = f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}"
        headers = {"hibp-api-key": api_key}
        response = requests.get(api_url, headers=headers)
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            return "No breaches found"
        else:
            return f"Error: {response.status_code}"
    except Exception as e:
        return f"Error fetching data breach info: {e}"

# Function to check email in breach databases without an API key
def check_data_breach_without_api(email):
    try:
        api_url = f"https://haveibeenpwned.com/unifiedsearch/{email}"
        response = requests.get(api_url)
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            return "No breaches found"
        else:
            return f"Error: {response.status_code}"
    except Exception as e:
        return f"Error fetching data breach info: {e}"

# Function to verify email existence via SMTP
def check_email_smtp(email, domain):
    try:
        mx_record = check_mx_record(domain)
        if not mx_record:
            return "No MX record found."

        server = smtplib.SMTP(mx_record[0])
        server.set_debuglevel(0)
        server.helo(domain)
        server.mail('test@example.com')
        code, message = server.rcpt(email)
        server.quit()

        if code == 250:
            return "Email exists."
        else:
            return "Email does not exist."
    except Exception as e:
        return str(e)

# Function to display menu
def display_menu():
    print("\nPlease choose an option to proceed with email footprinting:")
    print("1. Validate Email Format")
    print("2. Perform MX Record Lookup")
    print("3. Check if Email is in Data Breach")
    print("4. Verify Email Existence via SMTP")
    print("5. Exit")

# Function to handle the email footprinting process
def email_footprinting_tool():
    print("Welcome to the Advanced Email Footprinting Tool!")

    # Descriptive message for email input
    print("Please enter a valid email address for footprinting.")
    print("Example: user@example.com")
    email = input("Enter the email address: ").strip()

    # Validate email format
    if not validate_email_format(email):
        print(f"Invalid Email Format: {email}")
        return

    domain = email.split('@')[1]
    results = {}

    while True:
        display_menu()
        choice = input("Choose an option (1-5): ").strip()

        if choice == '1':
            # Email Format Validation
            print(f"\nValidating email format for: {email}")
            if validate_email_format(email):
                print(f"Valid Email Format: {email}")
            else:
                print(f"Invalid Email Format: {email}")

        elif choice == '2':
            # MX Record Lookup
            print(f"\nMX Record Lookup for domain: {domain}")
            mx_records = check_mx_record(domain)
            if mx_records:
                results['MX Records'] = mx_records
                print(f"MX Records found: {mx_records}")
            else:
                results['MX Records'] = "No MX records found."
                print(f"No MX Records found for {domain}")

        elif choice == '3':
            # Data Breach Lookup
            print(f"\nChecking if {email} is found in public breaches...")
            print("Choose an option:")
            print("1) Search with Have I Been Pwned API Key")
            print("2) Search without API Key")
            breach_choice = input("Enter your choice (1/2): ").strip()

            if breach_choice == '1':
                print("Please enter your Have I Been Pwned API Key.")
                print("If you don't have an API key, you can get one from https://haveibeenpwned.com/API/Key")
                api_key = input("Enter your API Key: ").strip()
                breaches = check_data_breach(email, api_key)
                results['Breach Info'] = breaches
                print(f"Breach Info: {breaches}")
            elif breach_choice == '2':
                breaches = check_data_breach_without_api(email)
                results['Breach Info'] = breaches
                print(f"Breach Info: {breaches}")
            else:
                print("Invalid choice. Please select 1 or 2.")

        elif choice == '4':
            # Email SMTP Verification
            print(f"\nVerifying email existence via SMTP...")
            smtp_status = check_email_smtp(email, domain)
            results['SMTP Verification'] = smtp_status
            print(f"SMTP Verification: {smtp_status}")

        elif choice == '5':
            # Exit the tool
            print("Exiting the tool. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

        # Ask if user wants to save results after each option
        save_to_file = input("Do you want to save the results to a file (y/n)? ").strip().lower()
        if save_to_file == 'y':
            file_name = input("Enter the filename to save results: ").strip()
            with open(file_name, 'w') as f:
                json.dump(results, f, indent=4)
            print(f"Results saved to {file_name}")
        else:
            print("Results not saved.")

    print("Email Footprinting Completed!")

# Example usage
if __name__ == "__main__":
    email_footprinting_tool()
