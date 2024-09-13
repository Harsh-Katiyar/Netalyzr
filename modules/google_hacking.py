import webbrowser


def display_initial_options():
    """Display the initial Google Hacking Module options."""
    print("\nGoogle Hacking Module:")
    print("1. Generate a custom Google dork")
    print("2. Explore Google hacking techniques")
    print("3. Exit")


def display_technique_options():
    """Display the technique options for Google hacking."""
    print("\nGoogle Hacking Techniques:")
    print("1. Create using cheatsheet")
    print("2. Google hacking commands")
    print("3. Google hacking operators")
    print("4. Examples of dorks")
    print("5. Back to main menu")


def get_cheatsheet():
    """Display a Google Hacking cheatsheet."""
    print("\nGoogle Hacking Cheatsheet:")
    print("1. allintext: Searches for occurrences of all the keywords given.")
    print("2. intext: Searches for occurrences of keywords all at once or one at a time.")
    print("3. inurl: Searches for a URL matching one of the keywords.")
    print("4. allinurl: Searches for a URL matching all the keywords in the query.")
    print("5. intitle: Searches for occurrences of keywords in title all or one.")
    print("6. allintitle: Searches for occurrences of keywords all at a time.")
    print("7. site: Specifically searches that particular site.")
    print("8. filetype: Searches for a particular filetype mentioned in the query.")
    print("9. link: Searches for external links to pages.")
    print("10. numrange: Used to locate specific numbers in your searches.")
    print("11. before/after: Used to search within a particular date range.")
    print("12. allinanchor: Shows sites with key terms in links pointing to them.")
    print("13. allinpostauthor: Picks out blog posts by specific individuals.")
    print("14. related: Lists web pages similar to a specified web page.")
    print("15. cache: Shows the version of the web page in Google's cache.")


def get_google_hacking_commands():
    """Display examples of Google hacking commands."""
    print("\nGoogle Hacking Commands:")
    print('Examples of Google hacking commands:')
    print('1. "index of /" - Find directory listings.')
    print('2. "intitle:admin login" - Find admin login pages.')
    print('3. "filetype:pdf inurl:confidential" - Find confidential PDF files.')
    print('4. "site:example.com inurl:admin" - Find admin pages on a specific site.')


def get_google_hacking_operators():
    """Display Google hacking operators."""
    print("\nGoogle Hacking Operators:")
    print("1. \"\" (Quotes): Search for an exact phrase.")
    print("2. OR: Search for either term.")
    print("3. AND: Search for both terms.")
    print("4. - (Minus): Exclude a term.")
    print("5. ~ (Tilde): Include synonyms.")
    print("6. * (Asterisk): Use as a wildcard.")


def get_examples_of_dorks():
    """Display examples of creepy Google dorks."""
    print("\nExamples of Creepy Dorks:")
    print('1. inurl:"view.shtml" "Network Camera" "Camera Live Image" inurl:"guestimage.html" intitle:"webcamXP 5"')
    print('2. "Not for Public Release" + "Confidential" ext:pdf | ext:doc | ext:xlsx')
    print('3. site:.hk & inurl:wp-login')
    print('4. "index of" inurl:ftp secret')
    print('5. filetype:env "DB_PASSWORD" OR "SECRET_KEY"')


def get_user_input():
    """
    Prompt the user for input to generate Google dorks.

    Description:
    This function collects search criteria from the user to construct a Google dork. Each input field allows
    the user to specify parameters such as URL patterns, title keywords, file types, and more to refine their search.
    The user can leave fields blank if they don't want to use that particular filter.

    Returns:
    dict: A dictionary containing the user's input for generating the Google dork.
    """

    print("\n--- Automated Dork Generator ---")

    # Message to guide: Enter a specific URL pattern or leave blank if not needed.
    print(
        "You can specify the following search parameters. Leave any field blank if you don't want to use that filter.")

    # Message to guide: Enter a specific URL pattern or leave blank if not needed.
    inurl = input(
        "Enter a specific URL pattern to search for (e.g., 'view.shtml' for camera feeds, 'index.html' for directories) (optional, leave blank if none): ").strip()

    # Message to guide: Enter keywords that should be in the title or leave blank if not needed.
    intitle = input(
        "Enter specific title keywords (e.g., 'login' for login pages, 'error' for error pages) (optional, leave blank if none): ").strip()

    # Message to guide: Specify the file type you are interested in, such as PDF or DOC.
    filetype = input(
        "Enter filetype to search for (e.g., 'pdf' for documents, 'doc' for text files) (optional, leave blank if none): ").strip()

    # Message to guide: Restrict your search to a specific site or domain.
    site = input(
        "Enter a specific site to search within (e.g., 'example.com' for results from example.com, 'edu' for educational sites) (optional, leave blank if none): ").strip()

    # Message to guide: Enter keywords that should be present in the page's text.
    intext = input(
        "Enter keywords to search for within the page's text (e.g., 'confidential' for confidential information, 'login' for login-related text) (optional, leave blank if none): ").strip()

    # Message to guide: Exclude results containing certain keywords.
    exclude_terms = input(
        "Enter keywords to exclude from results (e.g., 'password' to avoid results mentioning passwords, 'test' to exclude test results) (optional, leave blank if none): ").strip()

    return {
        "inurl": inurl,
        "intitle": intitle,
        "filetype": filetype,
        "site": site,
        "intext": intext,
        "exclude_terms": exclude_terms
    }


def generate_dork(user_input):
    """Generate a Google dork based on the user input."""
    dork = []

    # Build the dork using user input
    if user_input["inurl"]:
        dork.append(f'inurl:"{user_input["inurl"]}"')
    if user_input["intitle"]:
        dork.append(f'intitle:"{user_input["intitle"]}"')
    if user_input["filetype"]:
        dork.append(f'filetype:{user_input["filetype"]}')
    if user_input["site"]:
        dork.append(f'site:{user_input["site"]}')
    if user_input["intext"]:
        dork.append(f'intext:"{user_input["intext"]}"')
    if user_input["exclude_terms"]:
        dork.append(f'-"{user_input["exclude_terms"]}"')

    # Join the elements into a single search string (dork)
    generated_dork = " ".join(dork)
    return generated_dork


def ask_to_open_in_browser(dork):
    """Ask the user if they want to open the dork in the browser."""
    choice = input("Do you want to open this dork in the browser? (yes/no): ").strip().lower()
    if choice == 'yes':
        google_search_url = f"https://www.google.com/search?q={dork}"
        webbrowser.open(google_search_url)
        print(f"Opening {google_search_url} in your browser...")
    else:
        print("Not opening in browser.")


def main():
    """Main function to run the Google Hacking module."""
    while True:
        display_initial_options()  # Show the initial menu
        try:
            # Prompt user for a choice and validate input
            user_choice = int(input("Enter the number for your choice (1-3): "))

            if user_choice == 3:  # Exit the program
                print("Exiting...")
                break
            elif user_choice == 2:  # Explore Google hacking techniques
                while True:
                    display_technique_options()  # Show technique options
                    try:
                        technique_choice = int(input("Enter the number for your choice (1-5): "))
                        if technique_choice == 5:  # Return to main menu
                            break
                        elif technique_choice == 1:
                            get_cheatsheet()
                        elif technique_choice == 2:
                            get_google_hacking_commands()
                        elif technique_choice == 3:
                            get_google_hacking_operators()
                        elif technique_choice == 4:
                            get_examples_of_dorks()
                        else:
                            print("Invalid option. Please choose a valid number (1-5).")
                    except ValueError:
                        print("Invalid input. Please enter a valid number (1-5).")
            elif user_choice == 1:  # Generate a custom Google dork
                user_input = get_user_input()
                generated_dork = generate_dork(user_input)
                if generated_dork:
                    print(f"\nGenerated Dork: {generated_dork}")
                    ask_to_open_in_browser(generated_dork)
                else:
                    print("\nNo input provided to generate a dork.")
            else:
                print("Invalid option. Please choose a valid number (1-3).")
        except ValueError:
            print("Invalid input. Please enter a valid number (1-3).")


if __name__ == "__main__":
    main()
