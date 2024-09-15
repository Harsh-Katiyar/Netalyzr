import requests
import json
import shodan
import os
from getpass import getpass

# Load API keys from environment variables or prompt user
def load_api_keys():
    api_keys = {
        "google_api_key": os.getenv("GOOGLE_API_KEY"),
        "search_engine_id": os.getenv("SEARCH_ENGINE_ID"),
        "bing_api_key": os.getenv("BING_API_KEY"),
        "shodan_api_key": os.getenv("SHODAN_API_KEY"),
        "censys_api_id": os.getenv("CENSYS_API_ID"),
        "censys_api_secret": os.getenv("CENSYS_API_SECRET"),
        "hunter_io_api_key": os.getenv("HUNTER_IO_API_KEY"),
        "yandex_api_key": os.getenv("YANDEX_API_KEY"),
        "baidu_api_key": os.getenv("BAIDU_API_KEY")
    }
    if not all(api_keys.values()):
        print("Some API keys are missing. Please provide them:")
        api_keys["google_api_key"] = input("Enter your Google API Key: ") or api_keys["google_api_key"]
        api_keys["search_engine_id"] = input("Enter your Google Custom Search Engine ID: ") or api_keys["search_engine_id"]
        api_keys["bing_api_key"] = input("Enter your Bing API Key: ") or api_keys["bing_api_key"]
        api_keys["shodan_api_key"] = input("Enter your Shodan API Key: ") or api_keys["shodan_api_key"]
        api_keys["censys_api_id"] = input("Enter your Censys API ID: ") or api_keys["censys_api_id"]
        api_keys["censys_api_secret"] = getpass("Enter your Censys API Secret: ") or api_keys["censys_api_secret"]
        api_keys["hunter_io_api_key"] = input("Enter your Hunter.io API Key: ") or api_keys["hunter_io_api_key"]
        api_keys["yandex_api_key"] = input("Enter your Yandex API Key: ") or api_keys["yandex_api_key"]
        api_keys["baidu_api_key"] = input("Enter your Baidu API Key: ") or api_keys["baidu_api_key"]
    
    return api_keys

# Define search functions with error handling
def search_google(query, api_key, search_engine_id, language=None, geo=None, date_range=None):
    try:
        url = f"https://www.googleapis.com/customsearch/v1?q={query}&key={api_key}&cx={search_engine_id}"
        if language:
            url += f"&lr=lang_{language}"
        if geo:
            url += f"&gl={geo}"
        if date_range:
            start_date, end_date = date_range
            url += f"&dateRestrict={start_date},{end_date}"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error with Google search: {e}")
        return None

def search_bing(query, api_key, count=50, language=None, region=None):
    try:
        headers = {"Ocp-Apim-Subscription-Key": api_key}
        params = {"q": query, "count": count}
        if language:
            params["setLang"] = language
        if region:
            params["setMkt"] = region
        url = "https://api.bing.microsoft.com/v7.0/search"
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error with Bing search: {e}")
        return None

def search_duckduckgo(query, max_results=50):
    try:
        url = f"https://duckduckgo.com/?q={query}&format=json"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error with DuckDuckGo search: {e}")
        return None

def search_shodan(query, api_key):
    try:
        api = shodan.Shodan(api_key)
        results = api.search(query)
        return results
    except shodan.APIError as e:
        print(f"Shodan Error: {e}")
        return None

def search_censys(query, api_id, api_secret):
    try:
        url = f"https://search.censys.io/api/v1/search/certificates?q={query}"
        response = requests.get(url, auth=(api_id, api_secret))
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error with Censys search: {e}")
        return None

def search_hunterio(domain, api_key):
    try:
        url = f"https://api.hunter.io/v2/domain-search?domain={domain}&api_key={api_key}"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error with Hunter.io search: {e}")
        return None

def search_yandex(query, api_key):
    try:
        url = f"https://yandex.com/search/xml?user=your_username&key={api_key}&query={query}"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error with Yandex search: {e}")
        return None

def search_baidu(query, api_key):
    try:
        url = f"https://www.baidu.com/s?wd={query}&api_key={api_key}"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error with Baidu search: {e}")
        return None

def search_haveibeenpwned(email):
    try:
        url = f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error with HaveIBeenPwned: {e}")
        return None

# Display and export results
def display_results(results, engine):
    print(f"\n[Search Results from {engine}]\n")
    if engine == "Google" and 'items' in results:
        for item in results['items']:
            print(f"Title: {item['title']}\nLink: {item['link']}\nSnippet: {item['snippet']}\n")
    elif engine == "Bing" and 'webPages' in results:
        for item in results['webPages']['value']:
            print(f"Title: {item['name']}\nLink: {item['url']}\nSnippet: {item['snippet']}\n")
    elif engine == "DuckDuckGo" and 'RelatedTopics' in results:
        for item in results['RelatedTopics']:
            if 'Text' in item and 'FirstURL' in item:
                print(f"Title: {item['Text']}\nLink: {item['FirstURL']}\n")
    elif engine == "Shodan":
        for result in results['matches']:
            print(f"IP: {result['ip_str']}\nData: {result['data']}\n")
    elif engine == "Censys":
        for result in results['results']:
            print(f"Title: {result['parsed.subject_dn']}\nFingerprint: {result['parsed.fingerprint_sha256']}\n")
    elif engine == "Hunter.io":
        for email in results['data']['emails']:
            print(f"Email: {email['value']}\nType: {email['type']}\n")
    elif engine == "Yandex":
        # Assuming Yandex API returns results in a similar format as Google
        if 'results' in results:
            for item in results['results']:
                print(f"Title: {item['title']}\nLink: {item['link']}\nSnippet: {item['snippet']}\n")
    elif engine == "Baidu":
        # Assuming Baidu API returns results in a similar format as Google
        if 'results' in results:
            for item in results['results']:
                print(f"Title: {item['title']}\nLink: {item['link']}\nSnippet: {item['snippet']}\n")
    elif engine == "HaveIBeenPwned":
        for breach in results:
            print(f"Breach: {breach['Name']}\nDomain: {breach['Domain']}\n")
    else:
        print("No results found or unsupported search engine.")

def export_results(results, engine, file_name):
    with open(file_name, 'w') as file:
        json.dump(results, file, indent=4)
    print(f"Results exported to {file_name}")

def search_engine_module():
    api_keys = load_api_keys()
    
    while True:
        print("\nSearch Engine OSINT Tool")
        print("1. Google")
        print("2. Bing")
        print("3. DuckDuckGo")
        print("4. Shodan")
        print("5. Censys")
        print("6. Hunter.io")
        print("7. Yandex")
        print("8. Baidu")
        print("9. HaveIBeenPwned")
        print("0. Exit")
        
        choice = input("Select an option: ")
        
        if choice == '0':
            break
        
        query = input("Enter search query: ")
        
        if choice in ['1', '2', '3', '7', '8']:
            api_key = api_keys.get("google_api_key") if choice == '1' else api_keys.get("bing_api_key") if choice == '2' else None
            search_engine_id = api_keys.get("search_engine_id") if choice == '1' else None
            if choice == '1':
                results = search_google(query, api_key, search_engine_id)
            elif choice == '2':
                results = search_bing(query, api_key)
            elif choice == '3':
                results = search_duckduckgo(query)
            elif choice == '7':
                results = search_yandex(query, api_keys.get("yandex_api_key"))
            elif choice == '8':
                results = search_baidu(query, api_keys.get("baidu_api_key"))
        elif choice == '4':
            results = search_shodan(query, api_keys.get("shodan_api_key"))
        elif choice == '5':
            results = search_censys(query, api_keys.get("censys_api_id"), api_keys.get("censys_api_secret"))
        elif choice == '6':
            results = search_hunterio(query, api_keys.get("hunter_io_api_key"))
        elif choice == '9':
            results = search_haveibeenpwned(query)
        else:
            print("Invalid choice, please select again.")
            continue
        
        display_results(results, choice)
        
        export = input("Do you want to export results to a file? (yes/no): ").strip().lower()
        if export == 'yes':
            file_name = input("Enter file name: ")
            export_results(results, choice, file_name)

if __name__ == "__main__":
    search_engine_module()
