import config

def get_pipeline_config(pipeline_name, repo_name):

    template = f"""format_version: 3
pipelines:
    {pipeline_name}:
        group: 'Default'
        label_template: ${{COUNT}}
        lock_behavior: unlockWhenFinished
        display_order: 1
        environment_variables:
            TMPDIR: /data/tmp
        materials:
            {repo_name}:
                git: {config.GIT_HOST_FROM_VAGRANT_1}/{config.USER_NAME}/{repo_name}.git
                username: {config.USER_NAME}
                shallow_clone: false
                auto_update: true
                branch: master
                destination: {repo_name}
                name: {repo_name}
                encrypted_password: 'AES:rRJ/TnzG58KCNzeu793Xbw==:xkcr7sDN16y6G0tfOsZLag=='
        stages:
            - stagename:
                fetch_materials: true
                keep_artifacts: true
                clean_workspace: false
                approval:
                    type: success
                    allow_only_on_success: false
                jobs:
                    deploy:
                        timeout: 30
                        resources:
                            - Linux
                        artifacts:
                            - build:
                                source: {repo_name}/files/*
                                destination: ""
                        tasks:
                          - exec:
                                arguments:
                                    - -c
                                    - echo "upload artifact to gocd server"
                                command: bash
                                run_if: passed"""
    return template


def get_pipeline_config_s3(pipeline_name, repo_name):

    template = f"""format_version: 3
pipelines:
    {pipeline_name}:
        group: 'Default'
        label_template: ${{COUNT}}
        lock_behavior: unlockWhenFinished
        display_order: 1
        environment_variables:
            TMPDIR: /data/tmp
        materials:
            {repo_name}:
                git: {config.GIT_HOST_FROM_VAGRANT_1}/{config.USER_NAME}/{repo_name}.git
                username: {config.USER_NAME}
                shallow_clone: false
                auto_update: true
                branch: master
                destination: {repo_name}
                name: {repo_name}
                encrypted_password: 'AES:rRJ/TnzG58KCNzeu793Xbw==:xkcr7sDN16y6G0tfOsZLag=='
        stages:
            - stagename:
                fetch_materials: true
                keep_artifacts: true
                clean_workspace: false
                approval:
                    type: success
                    allow_only_on_success: false
                jobs:
                    deploy:
                        timeout: 30
                        resources:
                            - Linux
                        artifacts:
                            - external:
                                id: "s3"
                                store_id: "ArtifactS3"
                                configuration:
                                    options:
                                        Source: {repo_name}/files
                                        Destination: "${{GO_ARTIFACT_LOCATOR}}"
                                        IsFile: false
                        tasks:
                          - exec:
                                arguments:
                                    - -c
                                    - echo "upload artifact to s3"
                                command: bash
                                run_if: passed"""
    return template


