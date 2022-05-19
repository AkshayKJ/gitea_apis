import requests
import config


for i in range(1,50):
    URL = f"{config.HOST}/api/v1/repos/{config.USER_NAME}/repo-{i}"
    r = requests.delete(url = URL, headers=config.HEADER)
    print(f"Status code for repo-{i} deletion", r.status_code)