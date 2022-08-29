import requests
import config
from telnetlib import Telnet




for i in range(config.FROM,config.LESS_THAN):
    URL = f"{config.HOST}/api/v1/repos/{config.USER_NAME}/repo-s3-{i}"
    r = requests.delete(url = URL, headers=config.HEADER)
    print(f"delete repo-{i}: ", r.status_code)