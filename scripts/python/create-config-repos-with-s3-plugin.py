import requests
import config


for i in range(config.FROM,config.LESS_THAN):
    REPO_NAME = f'repo-s3-{i}'
    URL = f"{config.GOCD_HOST_1}go/api/admin/config_repos"
    payload = {
        "id": REPO_NAME,
        "plugin_id": "yaml.config.plugin",
        "material": {
            "type": "git",
            "attributes": {
                "url": f"{config.GIT_HOST_FROM_VAGRANT_1}/{config.USER_NAME}/{REPO_NAME}.git",
                "username": config.USER_NAME,
                "password": config.PASSWORD,
                "branch": "master",
                "auto_update": True
            }
        },
        "configuration": [],
        "rules": [{
            "directive": "allow",
            "action": "refer",
            "type": "*",
            "resource": "*"
        }]
    }
    r = requests.post(url=URL, json=payload, headers=config.GOCD_HEADER_1)
    print(f"create config repo in gocd with buildin material 'repo-{i}': ", r.status_code, r.json())