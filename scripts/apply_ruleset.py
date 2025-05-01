import json
import os
from pathlib import Path

import requests

# Load the GitHub token from the environment
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
REPO_OWNER = "crsiebler"
REPO_NAME = "pysubstitutor"
BASE_API_URL = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/rulesets"
RULESETS_DIR = Path(".github/rulesets")


# Function to delete existing rulesets
def delete_existing_rulesets():
    headers = {
        "Authorization": f"Bearer {GITHUB_TOKEN}",
        "Accept": "application/vnd.github+json",
    }

    # Get all existing rulesets
    response = requests.get(BASE_API_URL, headers=headers)
    if response.status_code == 200:
        rulesets = response.json()
        for ruleset in rulesets:
            ruleset_id = ruleset["id"]
            delete_response = requests.delete(
                f"{BASE_API_URL}/{ruleset_id}", headers=headers
            )
            if delete_response.status_code == 204:
                print(f"Deleted ruleset with ID: {ruleset_id}")
            else:
                print(
                    f"Failed to delete ruleset with ID: {ruleset_id} - {delete_response.text}"
                )
    else:
        print(
            f"Failed to fetch existing rulesets: {response.status_code} - {response.text}"
        )


# Function to apply a single ruleset
def apply_ruleset(ruleset):
    headers = {
        "Authorization": f"Bearer {GITHUB_TOKEN}",
        "Accept": "application/vnd.github+json",
    }

    # Make the API request
    response = requests.post(BASE_API_URL, headers=headers, json=ruleset)
    if response.status_code == 201:
        print(f"Ruleset '{ruleset['name']}' applied successfully.")
        print(f"Ruleset ID: {response.json().get('id')}")
    elif response.status_code == 403:
        print(
            f"Failed to apply ruleset '{ruleset['name']}': 403 - Permission denied. "
            "Ensure your token has 'Administration' permissions for the repository."
        )
    elif response.status_code == 422:
        print(
            f"Failed to apply ruleset '{ruleset['name']}': 422 - Invalid request. "
            "Check the ruleset JSON file for errors."
        )
        print(f"Error details: {response.json()}")
    else:
        print(
            f"Failed to apply ruleset '{ruleset['name']}': {response.status_code} - {response.text}"
        )


# Function to load all rulesets from the directory
def load_rulesets():
    rulesets = []
    if not RULESETS_DIR.exists():
        print(f"Error: Rulesets directory '{RULESETS_DIR}' does not exist.")
        return rulesets

    for ruleset_file in RULESETS_DIR.glob("*.json"):
        try:
            with open(ruleset_file, "r") as file:
                ruleset = json.load(file)
                rulesets.append(ruleset)
                print(f"Loaded ruleset from '{ruleset_file}'.")
        except json.JSONDecodeError as e:
            print(f"Error: Failed to parse JSON file '{ruleset_file}'. {e}")
    return rulesets


# Run the script
if __name__ == "__main__":
    if not GITHUB_TOKEN:
        print("Error: GITHUB_TOKEN is not set in the environment.")
    else:
        delete_existing_rulesets()
        rulesets = load_rulesets()
        for ruleset in rulesets:
            apply_ruleset(ruleset)
