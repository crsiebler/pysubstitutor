import json
import os

import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# GitHub API details
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
REPO_OWNER = os.getenv("REPO_OWNER", "crsiebler")
REPO_NAME = os.getenv("REPO_NAME", "pysubstitutor")
BASE_API_URL = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/rulesets"


def fetch_rulesets():
    headers = {
        "Authorization": f"Bearer {GITHUB_TOKEN}",
        "Accept": "application/vnd.github+json",
    }

    try:
        response = requests.get(BASE_API_URL, headers=headers)
        if response.status_code == 200:
            rulesets = response.json()
            if rulesets:
                print("Fetched Rulesets:")
                print(json.dumps(rulesets, indent=4))
                return [ruleset["id"] for ruleset in rulesets]
            else:
                print("No rulesets found for this repository.")
                return []
        else:
            print(f"Failed to fetch rulesets: {response.status_code} - {response.text}")
            return []
    except requests.RequestException as e:
        print(f"Error: Failed to fetch rulesets. {e}")
        return []


def fetch_ruleset_by_id(ruleset_id):
    headers = {
        "Authorization": f"Bearer {GITHUB_TOKEN}",
        "Accept": "application/vnd.github+json",
    }

    try:
        response = requests.get(f"{BASE_API_URL}/{ruleset_id}", headers=headers)
        if response.status_code == 200:
            ruleset = response.json()
            print(f"Fetched Ruleset with ID {ruleset_id}:")
            print(json.dumps(ruleset, indent=4))
        elif response.status_code == 404:
            print(f"Ruleset with ID {ruleset_id} not found.")
        else:
            print(f"Failed to fetch ruleset: {response.status_code} - {response.text}")
    except requests.RequestException as e:
        print(f"Error: Failed to fetch ruleset. {e}")


if __name__ == "__main__":
    if not GITHUB_TOKEN:
        print("Error: GITHUB_TOKEN is not set in the environment.")
    else:
        ruleset_ids = fetch_rulesets()
        for ruleset_id in ruleset_ids:
            fetch_ruleset_by_id(ruleset_id)
