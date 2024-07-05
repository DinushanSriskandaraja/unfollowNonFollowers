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
        return [], 0
    soup = BeautifulSoup(html_content, 'html.parser')
    usernames = [a_tag.text.strip() for a_tag in soup.find_all('a', href=True)]
    return usernames, len(usernames)

def compare_lists(followers_file, following_file):
    followers_content = read_html_file(followers_file)
    following_content = read_html_file(following_file)

    if followers_content is None or following_content is None:
        return

    followers_usernames, followers_count = extract_usernames(followers_content)
    following_usernames, following_count = extract_usernames(following_content)

    print(f"Followers count: {followers_count}")
    print(f"Following count: {following_count}")

    followers_set = set(followers_usernames)
    following_set = set(following_usernames)
    followers_not_following = followers_set - following_set
    following_not_followers = following_set - followers_set

    print("Followers not following back:")
    count = 0
    for user in followers_not_following:
        print(user)
        count += 1
    print(f"Followers not following back: {count}")

    print("\nFollowing not followers:")
    count = 0
    for user in following_not_followers:
        print(user)
        count += 1
    print(f"Following count: {count}")

if __name__ == "__main__":
    compare_lists('followers_1.html', 'following.html')
