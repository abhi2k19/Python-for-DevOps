from flask import Flask, request, jsonify
import json
import requests
import base64

app = Flask(__name__)

# GitHub and Jira credentials
GITHUB_SECRET = "your_github_webhook_secret"  # Set this in your webhook
JIRA_API_TOKEN = "your_jira_api_token"
JIRA_EMAIL = "your_email@example.com"
JIRA_DOMAIN = "your_jira_domain"  # e.g., "yourcompany.atlassian.net"
JIRA_PROJECT_KEY = "PROJ"  # Replace with your Jira project key

# Jira headers
JIRA_HEADERS = {
    "Authorization": f"Basic {base64.b64encode(f'{JIRA_EMAIL}:{JIRA_API_TOKEN}'.encode()).decode()}",
    "Content-Type": "application/json"
}

@app.route('/webhook', methods=['POST'])
def github_webhook():
    # Verify GitHub signature (optional, but recommended)
    signature = request.headers.get('X-Hub-Signature-256')
    if not verify_signature(signature, request.data):
        return jsonify({"error": "Invalid signature"}), 401

    # Parse the GitHub webhook payload
    event = request.headers.get('X-GitHub-Event')
    payload = request.json

    if event == "issue_comment":
        handle_issue_comment(payload)

    return jsonify({"status": "success"}), 200


def verify_signature(signature, payload):
    """Verify GitHub webhook signature (optional for security)."""
    import hmac
    import hashlib
    computed_signature = 'sha256=' + hmac.new(GITHUB_SECRET.encode(), payload, hashlib.sha256).hexdigest()
    return hmac.compare_digest(computed_signature, signature)


def handle_issue_comment(payload):
    """Handle GitHub issue comment events."""
    comment_body = payload['comment']['body']
    issue_url = payload['issue']['html_url']
    commenter = payload['comment']['user']['login']

    # Check if the comment contains the trigger phrase "/jira"
    if "/jira" in comment_body.lower():
        # Extract additional context from the GitHub issue/pull request
        issue_title = payload['issue']['title']
        issue_description = f"""
        This Jira issue was automatically created based on a GitHub comment.

        **GitHub Issue URL**: {issue_url}
        **Commenter**: {commenter}

        **Comment**:
        {comment_body}
        """
        create_jira_issue(issue_title, issue_description)


def create_jira_issue(title, description):
    """Create a new issue in Jira."""
    jira_url = f"https://{JIRA_DOMAIN}/rest/api/3/issue"
    issue_data = {
        "fields": {
            "project": {"key": JIRA_PROJECT_KEY},
            "summary": title,
            "description": description,
            "issuetype": {"name": "Task"}  # Use the appropriate issue type
        }
    }

    response = requests.post(jira_url, headers=JIRA_HEADERS, json=issue_data)
    if response.status_code == 201:
        print(f"Jira issue created successfully: {response.json()['key']}")
    else:
        print(f"Failed to create Jira issue: {response.status_code} - {response.text}")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

    