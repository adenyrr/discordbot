import os
import requests
from dotenv import load_dotenv
import re

load_dotenv()  # Load GitHub token and Discord webhook URL from .env

GITHUB_TOKEN = os.environ['GITHUB_TOKEN']
DISCORD_WEBHOOK_URL = os.environ['DISCORD_WEBHOOK_URL']

def get_latest_release(repo_owner, repo_name):
    url = f'https://api.github.com/repos/{repo_owner}/{repo_name}/releases/latest'
    response = requests.get(url, headers={'Authorization': f'Bearer {GITHUB_TOKEN}'})
    return response.json()

def send_discord_message(message):
    data = {
        'content': message
    }
    requests.post(DISCORD_WEBHOOK_URL, json=data)

if __name__ == '__main__':
    repo_list = [
        ('immich-app', 'immich'),
        # Add more repos here...
    ]
    
    for owner, name in repo_list:
        latest_release = get_latest_release(owner, name)
        
        # Exemple de format du message Discord
        message = f"🚀 Nouvelle version disponible sur le dépôt {owner}/{name}: **{latest_release['tag_name']}**\n{latest_release['body']}"
        
        send_discord_message(message)
