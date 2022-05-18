import requests
import config
import templates
import base64


for i in range(1, 3):
    FILENAME = f'git-path-material-repo-{i}.gocd.yaml'
    PIPELINE = f'pipeline-repo-{i}'
    REPO_NAME = f'repo-{i}'
    URL = f"{config.HOST}/api/v1/repos/{config.USER_NAME}/{REPO_NAME}/contents/{FILENAME}"

    raw_content = templates.get_pipeline_config_yaml_git_path(
        PIPELINE, REPO_NAME)
    payload = {
        "author": {
            "email": "sanjayshanmu7@gmail.com",
            "name": "Shunmugam"
        },
        "branch": "master",
        "committer": {
            "email": "sanjayshanmu7@gmail.com",
            "name": "Shunmugam"
        },
        "content": "hello",
        "dates": {
            "author": "2022-05-18T10:41:08.929Z",
            "committer": "2022-05-18T10:41:08.929Z"
        },
        "message": "add hello",
        "signoff": True,
    }
    r = requests.post(url=URL, json=payload, headers=config.HEADER)
    print(f"Status code for repo-{i} file create",
          r.status_code, r.json(), URL)
