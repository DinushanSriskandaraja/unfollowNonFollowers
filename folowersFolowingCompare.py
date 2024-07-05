import webbrowser
from bs4 import BeautifulSoup


def read_html_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except (FileNotFoundError, Exception) as e:
        print(f"Error reading file {file_path}: {e}")
        return None


def extract_usernames(html_content):
    if not html_content:
        return []
    soup = BeautifulSoup(html_content, 'html.parser')
    return [a_tag.text.strip() for a_tag in soup.find_all('a', href=True)]


def get_usernames_set(file_path):
    content = read_html_file(file_path)
    return set(extract_usernames(content)) if content else set()


def identify_non_reciprocal_followers(followers_set, following_set, option):
    if option == "1":
        return followers_set - following_set, "Followers not following back:"
    elif option == "2":
        return following_set - followers_set, "Following not followers:"
    else:
        print("Invalid option selected.")
        return None, None


def display_usernames(result_set, message):
    print(f"{message}\n" + "\n".join(result_set) + f"\nCount: {len(result_set)}")


def open_profiles_in_browser(usernames):
    for user in usernames:
        webbrowser.open(f"https://www.instagram.com/{user}", new=2)


if __name__ == "__main__":
    option = input(
        "Please choose an option:\n1. Identify followers who are not followed back by you.\n2. Identify users you are following who are not following you back.\nEnter your choice (1 or 2): ")

    followers_set = get_usernames_set('followers_1.html')
    following_set = get_usernames_set('following.html')

    result_set, message = identify_non_reciprocal_followers(followers_set, following_set, option)

    if result_set:
        display_usernames(result_set, message)

        if len(result_set) > 20:
            print("\033[1;31mWarning: The list contains more than 20 users. Opening all profiles at once might cause your browser or device to hang.\033[0m")
            if input("Are you sure you want to open all profiles in your browser? (yes/no): ").strip().lower() != "yes":
                print("Profiles will not be opened in the browser.")
                exit()

        if input("Would you like to open these profiles in your browser? (yes/no): ").strip().lower() == "yes":
            open_profiles_in_browser(result_set)
