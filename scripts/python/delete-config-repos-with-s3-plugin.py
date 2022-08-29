import requests
import config


for i in range(config.FROM,config.LESS_THAN):
    REPO_NAME = f'repo-s3-{i}'
    URL = f"{config.GOCD_HOST_1}go/api/admin/config_repos/{REPO_NAME}"
    
    r = requests.delete(url=URL, headers=config.GOCD_HEADER_1)
    print(f"delete config repo 'repo-{i}'", r.status_code)
