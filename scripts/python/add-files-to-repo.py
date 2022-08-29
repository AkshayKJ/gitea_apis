import requests
import config
import templates
import base64


for i in range(config.FROM,config.LESS_THAN):
    FILENAME = f'repo-{i}.gocd.yaml'
    PIPELINE = f'pipeline-repo-{i}'
    REPO_NAME = f'repo-{i}'
    URL = f"{config.HOST}/api/v1/repos/{config.USER_NAME}/{REPO_NAME}/contents/{FILENAME}"

    raw_content = templates.get_pipeline_config(
        PIPELINE, REPO_NAME)
    payload = {

        "content": base64.b64encode(raw_content.encode("ascii")).decode("ascii"),

        "message": f"add {FILENAME}",

    }
    r = requests.post(url=URL, json=payload, headers=config.HEADER)
    print(f"added file '{FILENAME}' to repo-{i}: ", r.status_code)
