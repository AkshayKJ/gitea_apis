import requests
import config

TEMLPATE_NAME='sample'
header = {
    'Authorization': f'token {config.TOKEN}',
    "Content-Type" : "application/json",
    "accept": "application/json" 
}

for i in range(1,3):
    URL = f"{config.HOST}/api/v1/repos/{config.USER_NAME}/{TEMLPATE_NAME}/generate"
    payload = {
        'name': f'repo-{i}',
        'owner': f'{config.USER_NAME}',
        'default_branch': 'master',
        'description': f'repo created from api - repo{i}',
        'git_content': True,
        'git_hooks': True,
        'labels': True,
        'private': True,
        'topics': True,
        'webhooks': True
    }
    r = requests.post(url = URL, json=payload, headers=header)
    print(f"Status code for repo-{i} creation", r.status_code, r.json(), URL, payload)