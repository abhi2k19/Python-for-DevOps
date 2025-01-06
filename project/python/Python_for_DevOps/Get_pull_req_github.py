import requests

# GitHub API base URL
GITHUB_API_URL = "https://api.github.com/repos/kubernetes/kubernetes/pulls"

# Fetch and display pull request information for the Kubernetes repository.
def fetch_pull_requests():
    try:
         # Make a GET request to the GitHub API
        response = requests.get(GITHUB_API_URL)
         # Raise exception for HTTP errors
        response.raise_for_status() 
         # Parse the JSON response
        pull_requests = response.json()
         # Display pull request information
        print(f"total open pull requests:{len(pull_requests)}\n")
        for pr in pull_requests:
            print(f"Title : {pr['title']}")
            print(f"Author : {pr['user']['login']}")
            print(f"Created at : {pr['created_at']}")
            print(f"State : {pr['state']}")
            print(f"URL : {pr['html_url']}\n")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching pull requests: {e}")
# Call the function
fetch_pull_requests()

