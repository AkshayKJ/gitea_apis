import requests
import config

TEMLPATE_NAME='sample-template-repo'

for i in range(config.FROM,config.LESS_THAN):
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
    r = requests.post(url = URL, json=payload, headers=config.HEADER)
    print(f"create repo 'repo-{i}': ", r.status_code)