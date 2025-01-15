import requests
GITHUB_API_URL = "https://api.github.com/repos/abhi2k19/Python-for-DevOps/pull"

def get_github_api_response():
    try:
        response = requests.get(GITHUB_API_URL) 
        print(response.status_code)
        if response.status_code != 200:
            print(f"Error : {response.status_code}")
            return
        response.raise_for_status()
        pull_requests = response.json() # Automatically converts JSON to Dictionary....
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