import webbrowser
from bs4 import BeautifulSoup


def read_html_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None


def extract_usernames(html_content):
    if not html_content:
        return []
    soup = BeautifulSoup(html_content, 'html.parser')
    return [a_tag.text.strip() for a_tag in soup.find_all('a', href=True)]


def compare_lists(followers_file, following_file, option):
    followers_content = read_html_file(followers_file)
    following_content = read_html_file(following_file)

    if followers_content is None or following_content is None:
        return

    followers_usernames = extract_usernames(followers_content)
    following_usernames = extract_usernames(following_content)

    followers_set = set(followers_usernames)
    following_set = set(following_usernames)

    if option == "1":
        # Followers not following back
        result_set = followers_set - following_set
        message = "Followers not following back:"
    elif option == "2":
        # Following not followers
        result_set = following_set - followers_set
        message = "Following not followers:"
    else:
        print("Invalid option selected.")
        return

    print(message)
    for user in result_set:
        print(user)
    print(f"Count: {len(result_set)}")

    return list(result_set)


if __name__ == "__main__":
    option = input("Please choose an option:\n1. Identify followers who are not followed by you.\n2. Identify users you are following who are not following you back.\nEnter your choice (1 or 2): ")
    result_set = compare_lists('followers_1.html', 'following.html', option)

    if result_set:
        open_in_browser = input("Would you like to open these profiles in your browser? (yes/no): ").strip().lower()
        if open_in_browser == "yes" or "y":
            for user in result_set:
                webbrowser.open(f"https://www.instagram.com/{user}", new=2)
