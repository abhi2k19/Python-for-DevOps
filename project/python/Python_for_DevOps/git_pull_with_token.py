import requests
GITHUB_API_URL = "https://api.github.com/repos/abhi2k19/Python-for-DevOps/pulls"

# Optional: Use a GitHub personal access token for higher rate limits (set in environment or directly here)
#GITHUB_TOKEN = ""


# Headers for authentication (if token is used)
# headers = {}
# if GITHUB_TOKEN:
#     headers["Authorization"] = f"token {GITHUB_TOKEN}"

def get_github_api_response():
    try:
        response = requests.get(GITHUB_API_URL)
        response.raise_for_status()
        pull_requests = response.json()
        print(f"Total Open Pull Requests : {len(pull_requests)}")
        for pr in pull_requests:
            print(f"Pull Request #{pr['number']} : {pr['title']}")
            print(f"Created At : {pr['created_at']}")
            print(f"Updated At : {pr['updated_at']}")
            print(f"URL : {pr['html_url']}")
            print(f"Author : {pr['user']['login']}\n")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from GitHub API : {e}")
get_github_api_response()