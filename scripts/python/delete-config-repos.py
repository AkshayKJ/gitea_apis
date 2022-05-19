import requests
import config


for i in range(2, 51):
    REPO_NAME = f'repo-{i}'
    URL = f"{config.GOCD_HOST}go/api/admin/config_repos/{REPO_NAME}"
    
    r = requests.delete(url=URL, headers=config.GOCD_HEADER)
    print(f"Status code for Config repo-{i}  create",
          r.status_code)
