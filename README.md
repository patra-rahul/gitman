# GITMAN: Github-Activity Tracker #
A lightweight, command-line interface (CLI) tool written in Python that fetches and summarizes a user's recent GitHub activity using the GitHub REST API.

## Features ##
The tool queries GitHub's public data to provide three key insights:

✅ **Push Commits:** Counts the total number of commits pushed by the user (excluding commits to forked repositories).

🔴 **Issues Opened:** Displays whether the user has opened any issues, showing either "No issues opened" or the specific count.

⭐️ **Starred Repositories:** Lists all the repositories the user has starred.

## Prerequisites ##
Before running the script, ensure you have Python 3 installed on your system.
This project uses the built-in urllib and json libraries, so no external dependencies (like requests) are required.

## Installation & Setup ##
1. **Clone the Repository**
```bash
git clone https://github.com/patra-rahul/gitman.git
cd gitman
```
2. **(Optional) Configure a GitHub Token:**
To avoid GitHub API rate limiting, you can set up a personal access token. Once you get the token, create a `.env` file and write:
```bash
GITHUB_TOKEN = Bearer github_{your username}_{token}
```

## Usage ##
Run the script from your terminal using the following command structure:
```bash
python3 gitman.py github-activity "username"
```

## How it works
* The script communicates directly with the GitHub REST API (https://api.github.com).
* It parses the `/users/{username}/events` endpoint to calculate recent push events and opened issues.
* It fetches the `/users/{username}/starred` endpoint to retrieve the list of starred repositories.

This was a very short project to learn about how to use REST APIs. It was a good learning experience for me.
Thank you for checking it out! ❤️

**Project link:** https://roadmap.sh/projects/github-user-activity