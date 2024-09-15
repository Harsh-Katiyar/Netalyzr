import requests
from bs4 import BeautifulSoup
from googleapiclient.discovery import build
import json

# Google Custom Search API setup
GOOGLE_API_KEY = 'YOUR_GOOGLE_API_KEY'
GOOGLE_SEARCH_ENGINE_ID = 'YOUR_CUSTOM_SEARCH_ENGINE_ID'

# NewsAPI setup
NEWS_API_KEY = 'YOUR_NEWS_API_KEY'

# BuiltWith API setup (replace with actual API endpoint and key)
BUILTWITH_API_KEY = 'YOUR_BUILTWITH_API_KEY'
BUILTWITH_API_URL = 'https://api.builtwith.com/v18/api.json'

# Social Media APIs setup (replace with actual API endpoints and keys)
SOCIAL_MEDIA_API_KEYS = {
    'twitter': 'YOUR_TWITTER_API_KEY',
    'facebook': 'YOUR_FACEBOOK_API_KEY',
    'linkedin': 'YOUR_LINKEDIN_API_KEY'
}


def google_search(query, num_results=10):
    """Perform a Google search using the Custom Search API."""
    service = build("customsearch", "v1", developerKey=GOOGLE_API_KEY)
    response = service.cse().list(
        q=query,
        cx=GOOGLE_SEARCH_ENGINE_ID,
        num=num_results
    ).execute()
    return response.get('items', [])


def fetch_website_data(url):
    """Fetch the title and meta description of a website."""
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        return {
            'title': soup.title.string if soup.title else 'No title',
            'meta_description': soup.find('meta', attrs={'name': 'description'})['content'] if soup.find('meta', attrs={
                'name': 'description'}) else 'No description'
        }
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return {}


def fetch_news_articles(query):
    """Fetch news articles related to the query using NewsAPI."""
    headers = {'Authorization': f'Bearer {NEWS_API_KEY}'}
    response = requests.get(f'https://newsapi.org/v2/everything?q={query}&apiKey={NEWS_API_KEY}', headers=headers)
    return response.json().get('articles', [])


def fetch_social_media_profiles(query):
    """Fetch social media profiles from various platforms."""
    profiles = {}
    for platform, key in SOCIAL_MEDIA_API_KEYS.items():
        if platform == 'twitter':
            response = requests.get(f'https://api.twitter.com/2/users/by/username/{query}',
                                    headers={'Authorization': f'Bearer {key}'})
            profiles['twitter'] = response.json()
        elif platform == 'facebook':
            response = requests.get(f'https://graph.facebook.com/v10.0/{query}?access_token={key}')
            profiles['facebook'] = response.json()
        elif platform == 'linkedin':
            response = requests.get(f'https://api.linkedin.com/v2/people/(id:{query})',
                                    headers={'Authorization': f'Bearer {key}'})
            profiles['linkedin'] = response.json()
    return profiles


def analyze_social_media_posts(query, platform):
    """Analyze recent social media posts on the specified platform."""
    print(f"Analyzing recent posts on {platform} for query: {query}")
    # Placeholder - implement with real API calls
    return []


def analyze_followers_connections(query, platform):
    """Analyze followers and connections on the specified social media platform."""
    print(f"Analyzing followers/connections on {platform} for query: {query}")
    # Placeholder - implement with real API calls
    return []


def search_social_media_mentions(query):
    """Search for social media mentions related to the query."""
    print(f"Searching social media mentions for query: {query}")
    # Placeholder - implement with real API calls
    return []


def analyze_website_traffic(url):
    """Analyze the website traffic for the given URL."""
    print(f"Analyzing website traffic for {url}")
    # Placeholder - implement with real API calls
    return {}


def perform_seo_analysis(url):
    """Perform SEO analysis for the given URL."""
    print(f"Performing SEO analysis for {url}")
    # Placeholder - implement with real API calls
    return {}


def analyze_technology_stack(url):
    """Analyze the technology stack used by the website."""
    headers = {'Authorization': f'Bearer {BUILTWITH_API_KEY}'}
    response = requests.get(f'{BUILTWITH_API_URL}?key={BUILTWITH_API_KEY}&url={url}', headers=headers)
    return response.json()


def fetch_company_financials(query):
    """Fetch company financials or check for data breaches."""
    print(f"Fetching company financials or data breaches for query: {query}")
    response = requests.get(f'https://haveibeenpwned.com/api/v3/breachedaccount/{query}',
                            headers={'User-Agent': 'Mozilla/5.0'})
    return response.json()


def get_domain_age_expiry(domain):
    """Fetch domain age and expiry information."""
    print(f"Fetching domain age and expiry for domain: {domain}")
    response = requests.get(f'https://whois.iana.org/{domain}')
    soup = BeautifulSoup(response.text, 'html.parser')
    # Parse the WHOIS information for domain age and expiry
    return {
        'age': 'Domain age data',
        'expiry': 'Domain expiry data'
    }


def display_results(results):
    """Display the search results."""
    for idx, result in enumerate(results):
        print(f"\nResult {idx + 1}:")
        print(f"Title: {result.get('title')}")
        print(f"Link: {result.get('link')}")
        print(f"Snippet: {result.get('snippet')}")

        # Fetch website data if URL is available
        if 'link' in result:
            website_data = fetch_website_data(result['link'])
            print(f"Website Title: {website_data.get('title')}")
            print(f"Website Meta Description: {website_data.get('meta_description')}")


def competitive_intelligence_module():
    """Main function for the Competitive Intelligence module."""
    print("\nCompetitive Intelligence OSINT Tool")
    print("1. Google Search")
    print("2. News Articles")
    print("3. Social Media Profiles")
    print("4. Business Data")
    print("5. Website Traffic Analysis")
    print("6. SEO Analysis")
    print("7. Technology Stack Analysis")
    print("8. Company Financials")
    print("9. Domain Age and Expiry")

    print("\nAdvanced Social Media OSINT")
    print("10. Analyze Social Media Posts")
    print("11. Analyze Followers/Connections")
    print("12. Search Social Media Mentions")

    choice = input("Select an option (1-12): ")

    if choice in ['1', '2', '4', '5', '6', '7', '8', '9']:
        query = input("Enter the competitor's name or relevant keywords (e.g., 'Competitor XYZ'): ")

    if choice in ['3', '10', '11', '12']:
        query = input(
            "Enter the keyword or username to search for on social media (e.g., 'username' or 'company name'): ")

    if choice == '1':
        print("Performing Google Search for the given query.")
        search_results = google_search(query)
        display_results(search_results)
    elif choice == '2':
        print("Fetching news articles related to the given query.")
        news_articles = fetch_news_articles(query)
        for article in news_articles:
            print(f"Title: {article.get('title')}")
            print(f"Description: {article.get('description')}")
            print(f"URL: {article.get('url')}")
    elif choice == '3':
        print("Fetching social media profiles for the given query. Supported platforms: Twitter, Facebook, LinkedIn.")
        social_profiles = fetch_social_media_profiles(query)
        print(json.dumps(social_profiles, indent=2))
    elif choice == '4':
        print("Fetching business data for the given query.")
        business_data = fetch_business_data(query)
        for data in business_data:
            print(data)
    elif choice == '5':
        url = input("Enter the website URL to analyze traffic (e.g., 'https://example.com'): ")
        print(f"Analyzing website traffic for {url}.")
        traffic_data = analyze_website_traffic(url)
        print(traffic_data)
    elif choice == '6':
        url = input("Enter the website URL for SEO analysis (e.g., 'https://example.com'): ")
        print(f"Performing SEO analysis for {url}.")
        seo_data = perform_seo_analysis(url)
        print(seo_data)
    elif choice == '7':
        url = input("Enter the website URL to analyze technology stack (e.g., 'https://example.com'): ")
        print(f"Analyzing technology stack for {url}.")
        tech_stack = analyze_technology_stack(url)
        print(json.dumps(tech_stack, indent=2))
    elif choice == '8':
        query = input("Enter the company name or relevant keyword (e.g., 'Company XYZ'): ")
        print(f"Fetching company financials or data breaches for {query}.")
        financials = fetch_company_financials(query)
        print(json.dumps(financials, indent=2))
    elif choice == '9':
        domain = input("Enter the domain (e.g., 'example.com') to fetch domain age and expiry: ")
        print(f"Fetching domain age and expiry information for {domain}.")
        domain_info = get_domain_age_expiry(domain)
        print(json.dumps(domain_info, indent=2))
    elif choice == '10':
        platform = input("Enter the social media platform (twitter, facebook, linkedin) for post analysis: ")
        print(f"Analyzing recent posts on {platform} for the query: {query}.")
        posts_data = analyze_social_media_posts(query, platform)
        print(posts_data)
    elif choice == '11':
        platform = input(
            "Enter the social media platform (twitter, facebook, linkedin) to analyze followers/connections: ")
        print(f"Analyzing followers/connections on {platform} for the query: {query}.")
        followers_data = analyze_followers_connections(query, platform)
        print(followers_data)
    elif choice == '12':
        print(f"Searching for social media mentions for the query: {query}.")
        mentions_data = search_social_media_mentions(query)
        print(mentions_data)
    else:
        print("Invalid choice. Please select a valid option.")

    print("\nSearch completed.")


if __name__ == "__main__":
    competitive_intelligence_module()
