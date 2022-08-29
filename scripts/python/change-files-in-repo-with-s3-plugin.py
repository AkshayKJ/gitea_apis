import requests
import config
import templates
import base64
import uuid


for i in range(config.FROM,config.LESS_THAN):
    FILENAME = f'change.txt'
    REPO_NAME = f'repo-s3-{i}'
    URL = f"{config.HOST}/api/v1/repos/{config.USER_NAME}/{REPO_NAME}/contents/{FILENAME}"
    file_response = requests.get(url=URL, headers=config.HEADER)
    if file_response.status_code == 200:
        file_info = file_response.json()
        raw_content = str(uuid.uuid4())
        payload = {
            "content": base64.b64encode(raw_content.encode("ascii")).decode("ascii"),
            "message": f"modify {FILENAME} from api",
            "sha": file_info["sha"]
        }
        r = requests.put(url=URL, json=payload, headers=config.HEADER)
        print(f"modified file '{FILENAME}' in {REPO_NAME}: ", r.status_code)
    else:
        print(f"error getting file response from repo {REPO_NAME} for file {FILENAME}: ", file_response.status_code, file_response.json)
