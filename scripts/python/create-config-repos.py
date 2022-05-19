import requests
import config


for i in range(2, 51):
    REPO_NAME = f'repo-{i}'
    URL = f"{config.GOCD_HOST}go/api/admin/config_repos"
    payload = {
        "id": REPO_NAME,
        "plugin_id": "yaml.config.plugin",
        "material": {
            "type": "git",
            "attributes": {
                "url": f"http://192.168.56.1:3000/admin123/{REPO_NAME}.git",
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
    r = requests.post(url=URL, json=payload, headers=config.GOCD_HEADER)
    print(f"Status code for Config repo-{i}  create",
          r.status_code)
