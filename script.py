import requests # import requests library to make HTTP requests
import csv # import csv library to handle CSV file operations
import os # import os library to handle file operations
from dotenv import load_dotenv # import load_dotenv to load environment variables from a .env file

load_dotenv()
TOKEN = os.getenv("GITHUB_TOKEN")
USERNAME = os.getenv("GITHUB_USERNAME")

if not TOKEN or not USERNAME:
    raise ValueError("GITHUB_TOKEN and GITHUB_USERNAME must be set in the .env file.")

headers = {"Authorization": f"token {TOKEN}"}

def get_paginated_users(url):
    users = []
    while url:
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            raise Exception(f"Failed to fetch data: {response.status_code} {response.text}")
        data = response.json()
        users.extend(data)
        url = response.links.get('next', {}).get('url')  # get the next page URL
    return users

def main():

    followers_url = f"https://api.github.com/users/{USERNAME}/followers"
    following_url = f"https://api.github.com/users/{USERNAME}/following"

    print("🔍 Coletando seguidores...")
    followers = set(get_paginated_users(followers_url))

    print("🔍 Coletando usuários que você segue...")
    following = set(get_paginated_users(following_url))

    not_following_back = sorted(following - followers)

    output_file = "dont_follow_me_back.csv"
    with open(output_file, mode="w", newline='', encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Usuários que você segue mas não te seguem de volta"])
        for user in not_following_back:
            writer.writerow([user])

    print(f"\n✅ Resultado salvo em: {output_file}")