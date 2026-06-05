from dotenv import load_dotenv
import requests
import argparse

HEADERS = {
    "Authorization": f"{load_dotenv()}"
}

def gitman(username):
    url = f"https://api.github.com/users/{username}/repos"
    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200:
        repos = response.json()

        for repo in repos:
            if repo['fork'] == False:
                commits_url = f"https://api.github.com/repos/{username}/{repo['name']}/commits?per_page=100" # pagination
                commits_response = requests.get(commits_url, headers=HEADERS)
                commits = commits_response.json()
                commits_count = len(commits)
                print(f"Pushed {commits_count} commits to {repo['full_name']}")

                issues_url = f"https://api.github.com/repos/{username}/{repo['name']}/issues"
                issues_reponse = requests.get(issues_url, headers=HEADERS)
                issues = issues_reponse.json()
                if len(issues) == 0:
                    print(f"🟢 Opened no issues in {repo['full_name']}\n")
                else:
                    print(f"🔴 Opened {len(issues)} issues in {repo['full_name']}\n")
            else:
                pass

        starred_url = f"https://api.github.com/users/{username}/starred"
        starred_response = requests.get(starred_url, headers=HEADERS)
        starred = starred_response.json()
        for star in starred:
            print(f"⭐️ Starred {star['full_name']}")
    else:
        print("❌ Couldn't find any such user on github...")

    
parser = argparse.ArgumentParser(
    prog='GITMAN- GITHUB USER ACTIVITY TOOL',
)

subparsers = parser.add_subparsers(dest='command', required=True)

user_response = subparsers.add_parser('github-activity', help='Command to enter Github username')
user_response.add_argument('username', type=str)

args = parser.parse_args()

if args.command == 'github-activity':
    gitman(args.username)