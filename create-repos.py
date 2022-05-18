import requests
import config


for i in range(1,50):
    URL = f"{config.HOST}/repos/{config.USER_NAME}/repo-{i}"
    r = requests.post(url = URL)
    print(f"Status code for repo-{i} creation", r.status_code)